#!/usr/bin/env python3
"""Render a user flow as a viewable HTML page: a wireflow (low-fi screen
thumbnails in happy-path order) plus the full branching diagram.

Usage:
  python render_flow.py --spec flow.json --out flow.html [--png flow.png]

Spec format (JSON):
{
  "title": "Add item by photo",
  "context": "One line: who, where, what job",
  "platform": "mobile" | "web",
  "screens": [
    {
      "id": "camera",
      "name": "Camera",
      "purpose": "Take a photo of the item",
      "primary": "Shutter",
      "blocks": [                      # top-to-bottom rough layout
        {"type": "header", "label": "Add item"},
        {"type": "image", "label": "Live camera"},
        {"type": "text", "label": "Lay item flat, good light"},
        {"type": "chips", "label": "Top, Bottom, Shoes"},
        {"type": "input", "label": "Name"},
        {"type": "list", "label": "Recent categories"},
        {"type": "button", "label": "Take photo"},      # primary
        {"type": "link", "label": "Choose from Photos"}, # secondary
        {"type": "sheet", "label": "..."},
        {"type": "tabbar", "label": "..."}
      ],
      "states": ["Permission denied", "Low light"]
    }
  ],
  "happy_path": ["camera", "review", "saved"],   # order of the wireflow row
  "edges": [                                      # all transitions, for the diagram
    {"from": "camera", "to": "review", "label": "Takes photo"},
    {"from": "review", "to": "picker", "label": "AI unsure", "unhappy": true}
  ],
  "start": "Taps + in wardrobe",   # optional entry label
  "end": "Back in wardrobe",       # optional exit label

  # Optional: where the work lives in the whole app
  "app_map": {
    "model": "Tab bar (4) + stacks; sheets for quick tasks",
    "areas": [
      {"name": "Wardrobe", "nav": "tab", "items": [
        {"name": "Item grid"},
        {"name": "Add item flow", "status": "new"},      # new | changed
        {"name": "Item detail"}]},
      {"name": "Outfits", "nav": "tab", "items": [{"name": "Today"}]}
    ]
  },
  # Optional: every way people arrive, where they land, what back does
  "entry_points": [
    {"type": "tab", "label": "+ in Wardrobe", "lands_on": "camera", "back": "Wardrobe grid"},
    {"type": "notification", "label": "'Finish adding 3 items'", "lands_on": "review", "back": "Wardrobe grid"},
    {"type": "share sheet", "label": "Share photo to app", "lands_on": "review", "back": "Photos app"}
  ]
}

Everything is plain HTML/CSS/SVG, so the page works offline and in previews.
A Mermaid version of the diagram is also written next to the HTML (.mmd) for
pasting into docs, FigJam or mermaid.live.
"""
import argparse, html, json, re, subprocess, sys
from pathlib import Path

def esc(s): return html.escape(str(s or ""))

def mm_id(s): return re.sub(r"[^A-Za-z0-9_]", "_", s)

def mm_text(s): return str(s or "").replace('"', "'")

BLOCK_CSS_CLASS = {"header","text","image","list","input","button","link","chips","sheet","tabbar"}

def render_screen(sc, n, platform):
    blocks = []
    for b in sc.get("blocks", []):
        t = b.get("type", "text")
        t = t if t in BLOCK_CSS_CLASS else "text"
        blocks.append(f'<div class="b b-{t}"><span>{esc(b.get("label"))}</span></div>')
    states = "".join(f"<li>{esc(s)}</li>" for s in sc.get("states", []))
    frame = "phone" if platform == "mobile" else "browser"
    return f'''
    <figure class="screen" id="s-{esc(sc["id"])}">
      <div class="frame {frame}"><div class="canvas">{"".join(blocks)}</div></div>
      <figcaption>
        <div class="num">{n}</div>
        <h3>{esc(sc.get("name"))}</h3>
        <p>{esc(sc.get("purpose"))}</p>
        <p class="primary"><b>Primary action:</b> {esc(sc.get("primary"))}</p>
        {f'<details><summary>States ({len(sc.get("states", []))})</summary><ul>{states}</ul></details>' if states else ''}
      </figcaption>
    </figure>'''

def mermaid_src(spec):
    names = {s["id"]: s.get("name", s["id"]) for s in spec.get("screens", [])}
    lines = ["flowchart LR"]
    if spec.get("start"):
        lines.append(f'  START(["{mm_text(spec["start"])}"])')
    for sid, name in names.items():
        lines.append(f'  {mm_id(sid)}["{mm_text(name)}"]')
    extra = set()
    for e in spec.get("edges", []):
        for k in ("from", "to"):
            v = e[k]
            if v not in names and v not in ("START", "END") and v not in extra:
                extra.add(v); lines.append(f'  {mm_id(v)}("{mm_text(v)}")')
    if spec.get("end"):
        lines.append(f'  END(["{mm_text(spec["end"])}"])')
    hp = spec.get("happy_path", [])
    if spec.get("start") and hp:
        lines.append(f"  START --> {mm_id(hp[0])}")
    unhappy_idx, i = [], 0
    if spec.get("start") and hp: i = 1
    for e in spec.get("edges", []):
        arrow = "-.->" if e.get("unhappy") else "-->"
        lab = f'|"{mm_text(e.get("label"))}"|' if e.get("label") else ""
        lines.append(f'  {mm_id(e["from"])} {arrow}{lab} {mm_id(e["to"])}')
        if e.get("unhappy"): unhappy_idx.append(i)
        i += 1
    if spec.get("end") and hp and not any(e["to"] == "END" for e in spec.get("edges", [])):
        lines.append(f"  {mm_id(hp[-1])} --> END")
    lines.append("  classDef screen fill:#fff,stroke:#1f2937,stroke-width:1.5px,color:#111")
    lines.append("  classDef term fill:#1f2937,stroke:#1f2937,color:#fff")
    if names: lines.append("  class " + ",".join(mm_id(s) for s in names) + " screen")
    terms = [t for t in ("START", "END") if spec.get(t.lower())]
    if terms: lines.append("  class " + ",".join(terms) + " term")
    for k in unhappy_idx:
        lines.append(f"  linkStyle {k} stroke:#c2410c,stroke-dasharray:5 4")
    return "\n".join(lines)


def svg_diagram(spec):
    """Layered left-to-right diagram drawn as inline SVG (works offline)."""
    names = {s["id"]: s.get("name", s["id"]) for s in spec.get("screens", [])}
    hp = spec.get("happy_path", [])
    edges = [dict(e) for e in spec.get("edges", [])]
    nodes = []
    def add(n):
        if n not in nodes: nodes.append(n)
    if spec.get("start") and hp:
        add("START"); edges.insert(0, {"from": "START", "to": hp[0]})
    for n in hp: add(n)
    for n in names: add(n)
    for e in edges: add(e["from"]); add(e["to"])
    if spec.get("end") and hp and not any(e["to"] == "END" for e in edges):
        edges.append({"from": hp[-1], "to": "END"})
    if spec.get("end"): add("END")
    label = {n: names.get(n, n) for n in nodes}
    if "START" in nodes: label["START"] = spec["start"]
    if "END" in nodes: label["END"] = spec["end"]
    # rank = BFS distance from first node; happy path gets consecutive ranks
    rank = {}
    base = 1 if "START" in nodes else 0
    if "START" in nodes: rank["START"] = 0
    for i, n in enumerate(hp): rank[n] = base + i
    changed = True
    while changed:
        changed = False
        for e in edges:
            a, b = e["from"], e["to"]
            if a in rank and b not in rank:
                rank[b] = rank[a] + 1; changed = True
    mx = max(rank.values(), default=0)
    for n in nodes:
        if n not in rank: rank[n] = mx + 1
    if "END" in nodes: rank["END"] = max(v for k, v in rank.items() if k != "END") + 1
    # rows: happy path + terminals on row 0, others stacked below per column
    row, used = {}, {}
    for n in nodes:
        if n in hp or n in ("START", "END"): row[n] = 0
    for n in nodes:
        if n in row: continue
        r = 1
        while (rank[n], r) in used: r += 1
        row[n] = r; used[(rank[n], r)] = n
    W, H, GX, GY, PAD = 168, 54, 104, 96, 30
    X = lambda n: PAD + rank[n] * (W + GX)
    Y = lambda n: PAD + 60 + row[n] * (H + GY)
    maxr = max(row.values(), default=0)
    width = PAD * 2 + (max(rank.values(), default=0) + 1) * (W + GX) - GX
    height = PAD * 2 + 60 + (maxr + 1) * (H + GY) - GY + 20
    out = [f'<svg viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="Flow diagram" xmlns="http://www.w3.org/2000/svg">',
           '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#4b5563"/></marker>'
           '<marker id="ahw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#c2410c"/></marker></defs>']
    labels = []
    for i, e in enumerate(edges):
        a, b = e["from"], e["to"]
        un = e.get("unhappy")
        col, mk, dash = ("#c2410c", "ahw", ' stroke-dasharray="6 5"') if un else ("#4b5563", "ah", "")
        if rank[b] > rank[a]:
            x1, y1 = X(a) + W, Y(a) + H / 2; x2, y2 = X(b), Y(b) + H / 2
            if row[b] != row[a]:
                k = GX * (0.6 if rank[b] == rank[a] + 1 else 1.0)
                d = f"M{x1},{y1} C{x1+k},{y1} {x2-k},{y2} {x2},{y2}"
                lx, ly = x2 - 12 - 3.2 * len(str(e.get("label", ""))), y2 - 14
            else:
                d = f"M{x1},{y1} L{x2},{y2}"
                lx, ly = (x1 + x2) / 2, (y1 + y2) / 2 - 8
        elif rank[b] == rank[a]:
            x1, y1 = X(a) + W / 2, Y(a) + (H if row[b] > row[a] else 0)
            x2, y2 = X(b) + W / 2, Y(b) + (0 if row[b] > row[a] else H)
            d = f"M{x1},{y1} L{x2},{y2}"; lx, ly = x1 + 6, (y1 + y2) / 2
        elif row[a] > row[b]:  # back edge from a lower row: go up into the target's bottom
            x1, y1 = X(a) + W / 2, Y(a)
            x2, y2 = X(b) + W / 2 + 20, Y(b) + H
            d = f"M{x1},{y1} C{x1},{y1-GY*0.7} {x2},{y2+GY*0.7} {x2},{y2}"
            lx, ly = (x1 + x2) / 2, (y1 + y2) / 2
        else:  # back edge on the same row: loop underneath
            x1, y1 = X(a) + W / 2 + 14, Y(a)
            x2, y2 = X(b) + W / 2 - 14, Y(b)
            dip = min(y1, y2) - 46 - 12 * (i % 3)
            d = f"M{x1},{y1} C{x1},{dip} {x2},{dip} {x2},{y2}"
            lx, ly = (x1 + x2) / 2, dip + 14
        out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="1.6"{dash} marker-end="url(#{mk})"/>')
        if e.get("label"):
            t = esc(e["label"]); w = 6.4 * len(e["label"]) + 10
            labels.append(f'<rect x="{lx-w/2}" y="{ly-11}" width="{w}" height="18" rx="4" fill="#f7f7f5"/>'
                          f'<text x="{lx}" y="{ly+2}" text-anchor="middle" font-size="11.5" fill="{col}">{t}</text>')
    for n in nodes:
        x, y = X(n), Y(n)
        term = n in ("START", "END"); extra = n not in names and not term
        fill, stroke, tc, rx = ("#111827", "#111827", "#fff", H / 2) if term else ("#fff", "#9ca3af" if extra else "#111827", "#111827", 10)
        dash = ' stroke-dasharray="4 3"' if extra else ""
        out.append(f'<rect x="{x}" y="{y}" width="{W}" height="{H}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"{dash}/>')
        words, lines, cur = str(label[n]).split(), [], ""
        for w_ in words:
            if len(cur) + len(w_) + 1 > 22 and cur: lines.append(cur); cur = w_
            else: cur = (cur + " " + w_).strip()
        lines.append(cur); lines = lines[:2]
        for k, ln in enumerate(lines):
            ty = y + H / 2 + 4 + (k - (len(lines) - 1) / 2) * 15
            out.append(f'<text x="{x+W/2}" y="{ty}" text-anchor="middle" font-size="13" font-weight="{600 if not extra else 400}" fill="{tc}">{esc(ln)}</text>')
    out += labels + ["</svg>"]
    return "\n".join(out)

TYPE_COLOURS = {"tab": "#1f2937", "menu": "#1f2937", "home card": "#0f766e", "search": "#0f766e",
                "notification": "#7c3aed", "email": "#7c3aed", "deep link": "#7c3aed", "shared link": "#7c3aed",
                "widget": "#b45309", "share sheet": "#b45309", "shortcut": "#b45309",
                "cross-link": "#2563eb", "empty state": "#2563eb", "onboarding": "#2563eb", "resume": "#6b7280"}

def render_nav(spec):
    names = {s["id"]: s.get("name", s["id"]) for s in spec.get("screens", [])}
    am = spec.get("app_map")
    eps = spec.get("entry_points", [])
    if not am and not eps: return ""
    out = ['<h2>Where it lives in the app</h2>']
    if am:
        if am.get("model"): out.append(f'<p class="navmodel"><b>Navigation model:</b> {esc(am["model"])}</p>')
        cols = []
        for a in am.get("areas", []):
            items = []
            for it in a.get("items", []):
                it = it if isinstance(it, dict) else {"name": it}
                st = it.get("status", "")
                badge = f'<span class="st st-{esc(st)}">{esc(st)}</span>' if st else ""
                items.append(f'<li class="{"hl" if st else ""}">{esc(it.get("name"))}{badge}</li>')
            cols.append(f'<div class="area"><div class="area-h"><span>{esc(a.get("name"))}</span><em>{esc(a.get("nav",""))}</em></div><ul>{"".join(items)}</ul></div>')
        out.append(f'<div class="appmap">{"".join(cols)}</div>')
    if eps:
        rows = []
        for e in eps:
            t = str(e.get("type", "")).lower(); c = TYPE_COLOURS.get(t, "#374151")
            land = names.get(e.get("lands_on"), e.get("lands_on", ""))
            rows.append(f'<tr><td><span class="ep" style="--c:{c}">{esc(t)}</span></td><td>{esc(e.get("label"))}</td><td>{esc(land)}</td><td>{esc(e.get("back"))}</td></tr>')
        out.append('<h2>Ways in</h2><div class="tablewrap"><table class="eps"><thead><tr><th>Type</th><th>Entry point</th><th>Lands on</th><th>Back goes to</th></tr></thead><tbody>' + "".join(rows) + '</tbody></table></div>')
    return "\n".join(out)

PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>__TITLE__ · flow</title>
<style>
:root{--ink:#111827;--muted:#6b7280;--line:#d1d5db;--bg:#f7f7f5;--card:#fff;--accent:#2563eb;--warn:#c2410c}
*{box-sizing:border-box}body{margin:0;font:15px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg)}
header{padding:28px 24px 8px;max-width:1400px;margin:auto}h1{margin:0 0 4px;font-size:26px}header p{margin:0;color:var(--muted)}
section{max-width:1400px;margin:auto;padding:16px 24px 32px}h2{font-size:15px;margin:24px 0 12px;color:var(--muted);font-weight:600}
.row{display:flex;gap:0;overflow-x:auto;padding:8px 4px 16px;align-items:flex-start}
.screen{margin:0;flex:0 0 220px;display:flex;flex-direction:column;gap:10px}
.screen.alt{margin-right:28px}.screen.alt .frame{height:auto;min-height:220px}
.arrow{flex:0 0 44px;align-self:center;margin-top:-120px;text-align:center;color:var(--muted);font-size:22px}
.frame{background:var(--card);border:1.5px solid var(--ink);border-radius:26px;padding:10px;height:400px}
.frame.browser{border-radius:10px;height:280px;flex-basis:320px}
.canvas{height:100%;display:flex;flex-direction:column;gap:6px;overflow:hidden;border-radius:16px}
.b{border-radius:6px;font-size:10.5px;line-height:1.25;color:#374151;display:flex;align-items:center;padding:6px 8px}
.b-header{font-weight:700;font-size:12px;padding:4px 2px}
.b-text{background:transparent;padding:2px}
.b-image{background:repeating-linear-gradient(45deg,#eef0f3 0 8px,#e5e7eb 8px 16px);flex:1 1 90px;justify-content:center;min-height:70px}
.b-list{background:#f3f4f6;min-height:54px;align-items:flex-start}
.b-input{border:1px solid var(--line);background:#fff}
.b-chips span{border:1px solid var(--line);border-radius:99px;padding:2px 8px}
.b-button{background:var(--accent);color:#fff;font-weight:600;justify-content:center;min-height:36px;border-radius:10px}
.b-link{color:var(--accent);justify-content:center}
.b-sheet{background:#f3f4f6;border-top:2px solid var(--line);min-height:60px;align-items:flex-start;margin-top:auto}
.b-tabbar{border-top:1px solid var(--line);justify-content:space-around;margin-top:auto;color:var(--muted)}
figcaption{position:relative;padding-left:30px}
.num{position:absolute;left:0;top:2px;width:22px;height:22px;border-radius:50%;background:var(--ink);color:#fff;font-size:12px;display:grid;place-items:center}
figcaption h3{margin:0;font-size:14px}figcaption p{margin:2px 0;color:var(--muted);font-size:12.5px}
.primary{color:var(--ink)!important}details{font-size:12.5px;margin-top:4px}summary{cursor:pointer;color:var(--warn)}
ul{margin:4px 0 0;padding-left:18px}
.navmodel{margin:0 0 10px;font-size:13.5px}
.appmap{display:flex;gap:12px;overflow-x:auto;padding-bottom:6px}
.area{flex:0 0 190px;background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.area-h{display:flex;justify-content:space-between;align-items:baseline;padding:10px 12px;background:#111827;color:#fff;font-weight:600;font-size:13.5px}
.area-h em{font-style:normal;font-weight:400;font-size:11.5px;opacity:.75}
.area ul{list-style:none;margin:0;padding:6px 0}.area li{padding:6px 12px;font-size:13px;display:flex;justify-content:space-between;gap:6px}
.area li.hl{background:#eff6ff;font-weight:600}
.st{font-size:10.5px;border-radius:99px;padding:1px 7px;align-self:center;font-weight:600}.st-new{background:#2563eb;color:#fff}.st-changed{background:#f59e0b;color:#111}
.tablewrap{overflow-x:auto}.eps{border-collapse:collapse;width:100%;background:var(--card);border:1px solid var(--line);border-radius:12px;font-size:13.5px}
.eps th,.eps td{text-align:left;padding:8px 12px;border-bottom:1px solid var(--line)}.eps th{font-size:12px;color:var(--muted);font-weight:600}
.ep{display:inline-block;border:1.5px solid var(--c);color:var(--c);border-radius:99px;padding:1px 8px;font-size:11.5px;font-weight:600;white-space:nowrap}
.diagram svg{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;max-width:none}
.diagram{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;overflow-x:auto}
.legend{font-size:12.5px;color:var(--muted);margin-top:8px}.legend b{color:var(--warn)}
details.src{margin-top:10px}pre{white-space:pre-wrap;font-size:12px;background:#f3f4f6;padding:12px;border-radius:8px}
</style></head><body>
<header><h1>__TITLE__</h1><p>__CONTEXT__</p></header>
<section><h2>Happy path (wireflow)</h2><div class="row">__ROW__</div>
__OTHERS__
__NAV__
<h2>Full flow, including unhappy paths</h2>
<div class="diagram">__SVG__</div>
<p class="legend">Solid arrows: main path. <b>Dashed orange</b>: errors, recovery and alternative paths.</p>
<details class="src"><summary>Mermaid source (paste into docs, FigJam or mermaid.live)</summary><pre>__MERMAID_ESC__</pre></details>
</section>
</body></html>"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--png", help="optional: also save a screenshot (needs Playwright)")
    a = ap.parse_args()
    spec = json.loads(Path(a.spec).read_text())
    platform = spec.get("platform", "mobile")
    by_id = {s["id"]: s for s in spec.get("screens", [])}
    hp = [x for x in spec.get("happy_path", []) if x in by_id]
    parts = []
    for n, sid in enumerate(hp, 1):
        if n > 1: parts.append('<div class="arrow" aria-hidden="true">→</div>')
        parts.append(render_screen(by_id[sid], n, platform))
    others = [s for s in spec.get("screens", []) if s["id"] not in hp]
    others_html = ""
    if others:
        cards = "".join(render_screen(s, "↳", platform).replace('class="screen"', 'class="screen alt"') for s in others)
        others_html = f'<h2>Other screens (recovery, alternatives)</h2><div class="row">{cards}</div>'
    src = mermaid_src(spec)
    out = (PAGE.replace("__TITLE__", esc(spec.get("title", "User flow")))
               .replace("__CONTEXT__", esc(spec.get("context", "")))
               .replace("__ROW__", "".join(parts)).replace("__OTHERS__", others_html).replace("__NAV__", render_nav(spec))
               .replace("__MERMAID_ESC__", esc(src)).replace("__SVG__", svg_diagram(spec)))
    Path(a.out).write_text(out)
    Path(a.out).with_suffix(".mmd").write_text(src)
    print(f"Wrote {a.out} and {Path(a.out).with_suffix('.mmd')}")
    if a.png:
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1400, "height": 900})
                pg.goto(Path(a.out).resolve().as_uri()); pg.wait_for_timeout(2500)
                pg.screenshot(path=a.png, full_page=True); b.close()
            print(f"Wrote {a.png}")
        except Exception as e:
            print(f"PNG skipped: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
