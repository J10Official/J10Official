"""Render the profile's self-contained SVGs. Standard library only; no API/token needed."""
import html
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "profile.json").read_text(encoding="utf-8"))
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)


def text(x, y, value, size=18, fill="currentColor", weight=400, extra=""):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-weight="{weight}" {extra}>{html.escape(value)}</text>'


def svg(body, width, height, title, desc, bg, ink):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(desc)}</desc>
<style>text{{font-family:Arial,Helvetica,sans-serif}}.mono{{font-family:Consolas,monospace}}@media(prefers-reduced-motion:reduce){{.motion{{animation:none!important}}}}</style>
<rect width="{width}" height="{height}" rx="18" fill="{bg}"/>
<g color="{ink}">{body}</g></svg>'''


def write(name, content):
    ET.fromstring(content)
    (OUT / name).write_text(content + "\n", encoding="utf-8")


for theme in ("dark", "light"):
    dark = theme == "dark"
    bg = "#111c2d" if dark else "#f1f6f5"
    ink = "#f1f6fc" if dark else "#142b39"
    muted = "#aabacb" if dark else "#4d6573"
    accent = "#63e4c6" if dark else "#087b68"
    amber = "#f3c777" if dark else "#ad6414"
    grid = "#23354a" if dark else "#d4e4e1"
    panel = "#17273a" if dark else "#e5efed"

    dots = ''.join(f'<circle cx="{x}" cy="{y}" r="1" fill="{grid}"/>' for x in range(600, 901, 20) for y in range(20, 260, 20))
    body = f'<path d="M18 1H882" stroke="{accent}" stroke-width="3"/>{dots}'
    body += text(38, 52, "LANGUAGE / MODELS / SYSTEMS", 12, accent, 700, 'letter-spacing="2"')
    body += text(36, 113, DATA["name"], 49, ink, 700)
    body += text(38, 153, DATA["role"], 25, muted)
    body += f'<path d="M38 182H88" stroke="{accent}" stroke-width="3"/>'
    body += text(38, 215, DATA["tagline"], 18, ink, 500)
    # A branching decision motif: models, alternatives, and a return to evidence.
    body += f'<g fill="none" stroke="{grid}" stroke-width="2"><path d="M630 130L715 62L805 130L715 198Z"/><path d="M630 130H805M715 62V198"/></g>'
    body += f'<path d="M630 130L715 62L805 130L715 198Z" fill="none" stroke="{accent}" stroke-opacity=".5" stroke-width="2"/>'
    for x,y,r,color in [(630,130,9,accent),(715,62,9,accent),(805,130,9,amber),(715,198,9,accent)]:
        body += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{bg}" stroke="{color}" stroke-width="2"/>'
    body += f'<rect x="695" y="110" width="40" height="40" rx="10" fill="{panel}" stroke="{accent}"/>'
    body += f'<path d="M705 130l7 7 14-15" fill="none" stroke="{accent}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    write(f"header-{theme}.svg", svg(body, 900, 254, f'{DATA["name"]} | {DATA["role"]}', DATA["tagline"], bg, ink))

    body = ''
    for i, metric in enumerate(DATA["metrics"]):
        x = 30 + 300*i
        if i:
            body += f'<path d="M{i*300} 24V106" stroke="{grid}"/>'
        body += text(x, 50, metric["value"], 33, accent, 700)
        body += text(x, 78, metric["label"], 17, ink, 600)
        body += text(x, 101, metric["context"], 10, muted, 500, 'letter-spacing=".7"')
    write(f"evidence-{theme}.svg", svg(body, 900, 130, "Research at a glance", "; ".join(m["value"] + " " + m["label"] for m in DATA["metrics"]), bg, ink))

    # Intentionally decorative. This board does not read or imitate contribution data.
    board = ''.join(f'<rect x="{x}" y="{y}" width="11" height="11" rx="2" fill="{grid}" opacity=".7"/>' for x in range(330, 870, 15) for y in range(30, 135, 15))
    path = "M350 50H830V110H350Z"
    body = text(30, 47, "AFTER HOURS", 11, accent, 700, 'letter-spacing="2"')
    body += text(30, 83, "Still building.", 25, ink, 700)
    body += text(30, 111, "Sometimes, just for play.", 15, muted)
    body += board
    body += f'''<style>@keyframes crawl{{to{{stroke-dashoffset:-1080}}}}@keyframes blink{{50%{{opacity:.3}}}}.snake{{animation:crawl 18s linear infinite}}.food{{animation:blink 2s ease-in-out infinite}}</style>
<path class="motion snake" d="{path}" pathLength="1080" fill="none" stroke="{accent}" stroke-width="11" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="66 1014"/>
<rect class="motion food" x="695" y="77" width="11" height="11" rx="3" fill="{amber}"/>'''
    write(f"playground-{theme}.svg", svg(body, 900, 160, "After hours", "A decorative pixel snake, independent of GitHub contribution activity.", bg, ink))

print("Rendered and XML-validated 6 SVGs.")
