"""Pages transcribed section-by-section from the Paper artboards.

Each entry in PAGES is a list of sections using the block vocabulary below;
the vocabulary mirrors the patterns that actually appear on the artboards.
"""
import io, os, html

DEMO = "book-a-demo/index.html"


def esc(s):
    return html.escape(str(s), quote=False)


# ------------------------------------------------------------------ blocks
def _link(base, target):
    return base + target


def s_head(b, base):
    kcls = "eyebrow-accent" if b.get("eyebrow_big") else "kicker"
    kick = f'<div class="{kcls}">{esc(b["kicker"])}</div>' if b.get("kicker") else ""
    lede = f'<p class="phead-lede">{esc(b["lede"])}</p>' if b.get("lede") else ""
    cta = ""
    if b.get("cta"):
        label, target = b["cta"]
        cta = f'<a class="pill pill-lg" href="{_link(base, target)}">{esc(label)}</a>'
    flag = f'<div class="flag-box">{esc(b["flag"])}</div>' if b.get("flag") else ""
    return (f'<section class="sec phead"><div class="sec-inner">{kick}'
            f'<h1 class="phead-h1">{esc(b["h1"])}</h1>{lede}{flag}{cta}</div></section>')


def s_twocol(b, base):
    paras = "".join(f'<p class="twocol-p">{esc(p)}</p>' for p in b["body"])
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner twocol">'
            f'<h2 class="twocol-h">{esc(b["h"])}</h2><div class="twocol-body">{paras}</div>'
            f'</div></section>')


def s_chain(b, base):
    cells = []
    for i, (t, s, dark) in enumerate(b["steps"]):
        cls = "chain-box dark" if dark else "chain-box"
        cells.append(f'<div class="{cls}"><b>{esc(t)}</b><span>{esc(s)}</span></div>')
    joined = '<i class="chain-arrow">&rarr;</i>'.join(cells)
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner">'
            f'<div class="chain">{joined}</div>'
            f'<div class="chain-rule"></div><div class="chain-cap">{esc(b["caption"])}</div>'
            f'</div></section>')


def s_cards(b, base):
    out = ""
    for c in b["items"]:
        go = ""
        if c.get("link"):
            go = f'<div class="go">{esc(c.get("cta","See more"))} &rarr;</div>'
        kick = f'<div class="kick">{esc(c["kick"])}</div>' if c.get("kick") else ""
        body = f'<p>{esc(c["text"])}</p>' if c.get("text") else ""
        tag = "a" if c.get("link") else "div"
        href = f' href="{_link(base, c["link"])}"' if c.get("link") else ""
        out += f'<{tag} class="bcard"{href}><h3>{esc(c["title"])}</h3>{kick}{body}{go}</{tag}>'
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-48">{h}'
            f'<div class="grid g{b.get("cols",2)}">{out}</div></div></section>')


def s_numbered(b, base):
    out = "".join(f'<div class="ncard"><div class="num">{esc(n)}</div><h3>{esc(t)}</h3>'
                  f'<p>{esc(d)}</p></div>' for n, t, d in b["items"])
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner stack-52">{h}'
            f'<div class="grid g2" style="row-gap:44px">{out}</div></div></section>')


def s_flagstats(b, base):
    cells = "".join(f'<div class="fstat"><b>{esc(v)}</b><span>{esc(l)}</span></div>' for v, l in b["items"])
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    note = f'<p class="fstat-note">{esc(b["note"])}</p>' if b.get("note") else ""
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner stack-44">{h}'
            f'<div class="flagbox">{cells}{note}</div></div></section>')


def s_audience(b, base):
    cards = "".join(
        f'<a class="acard" href="{_link(base, href)}"><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
        f'<div class="go">See more &rarr;</div></a>' for t, d, href in b["items"])
    band = ""
    if b.get("band"):
        bh, bp, bl, bt = b["band"]
        band = (f'<div class="stateband"><div><h3>{esc(bh)}</h3><p>{esc(bp)}</p></div>'
                f'<a class="pill" href="{_link(base, bt)}">{esc(bl)}</a></div>')
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner stack-48">{h}'
            f'<div class="grid g4">{cards}</div>{band}</div></section>')


def s_ticks(b, base):
    items = "".join(f"<li>{esc(i)}</li>" for i in b["items"])
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    lede = f'<p class="lede">{esc(b["lede"])}</p>' if b.get("lede") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}{lede}'
            f'<ul class="ticks">{items}</ul></div></section>')


def s_quote(b, base):
    cls = "quote quote-light" if b.get("light") else "quote"
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner"><div class="{cls}">'
            f'<div class="bar"></div><div><p>&ldquo;{esc(b["text"])}&rdquo;</p>'
            f'<cite>{esc(b["by"])}</cite></div></div></div></section>')


def s_cases(b, base):
    out = ""
    for eyebrow, big, text, href in b["items"]:
        out += (f'<a class="ccard" href="{_link(base, href)}"><div class="eyebrow">{esc(eyebrow)}</div>'
                f'<div class="big">{esc(big)}</div><p>{esc(text)}</p>'
                f'<div class="go">Read the case study &rarr;</div></a>')
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner stack-48">{h}'
            f'<div class="grid g2">{out}</div></div></section>')


def s_faq(b, base):
    rows = ""
    for item in b["items"]:
        if len(item) == 3 and item[2] == "flag":
            rows += f'<div class="faqrow flag"><div class="q">{esc(item[0])}</div><div class="a">{esc(item[1])}</div></div>'
        else:
            rows += f'<div class="faqrow"><div class="q">{esc(item[0])}</div><div class="a">{esc(item[1])}</div></div>'
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'<div class="faq">{rows}</div></div></section>')


def s_table(b, base):
    head = "".join(f"<th>{esc(c)}</th>" for c in b["head"])
    body = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in b["rows"])
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    note = f'<div class="flag-box" style="margin-top:20px">{esc(b["flag"])}</div>' if b.get("flag") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'<div class="tablewrap"><table><thead><tr>{head}</tr></thead>'
            f'<tbody>{body}</tbody></table></div>{note}</div></section>')


def s_darkbar(b, base):
    cells = "".join(f'<span>{esc(t)}</span>' for t in b["items"])
    return f'<section class="darkbar">{cells}</section>'


def s_closing(b, base):
    label, target = b.get("cta", ("Book a demo", DEMO))
    sub = f'<p class="closing-sub">{esc(b["sub"])}</p>' if b.get("sub") else ""
    return (f'<section class="sec sec-deep closing-dark"><div class="sec-inner">'
            f'<h2>{esc(b["h"])}</h2>{sub}'
            f'<a class="pill pill-lg" href="{_link(base, target)}">{esc(label)}</a></div></section>')


def s_form(b, base):
    fields = ""
    for row in b["fields"]:
        cells = ""
        for f in row:
            req = ""
            cls = "input"
            if isinstance(f, tuple):
                f, req_label = f
                req = f'<span class="tag-req">{esc(req_label)}</span>'
                cls = "input req"
            cells += (f'<div class="fld"><label>{esc(f)}{req}</label>'
                      f'<div class="{cls}"></div></div>')
        fields += f'<div class="frow">{cells}</div>'
    proof = ""
    for p in b.get("proof", []):
        if len(p) == 2 and p[0].endswith("+") or (len(p) == 2 and p[0][0].isdigit()):
            proof += f'<div class="p"><b>{esc(p[0])}</b><span>{esc(p[1])}</span></div>'
        else:
            proof += f'<div class="p"><div class="t">{esc(p[0])}</div><span>{esc(p[1])}</span></div>'
    label, target = b.get("cta", ("Book a demo", DEMO))
    return (f'<section class="sec"><div class="sec-inner formwrap">'
            f'<div class="form">{fields}'
            f'<a class="pill pill-lg" style="align-self:flex-start" href="{_link(base, target)}">{esc(label)}</a></div>'
            f'<div class="proofcol">{proof}</div></div></section>')


def s_links(b, base):
    items = "".join(f'<a href="{_link(base, t)}">{esc(l)} &rarr;</a>' for l, t in b["items"])
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'<div class="linklist">{items}</div></div></section>')



def s_splithero(b, base):
    kick = f'<div class="kicker">{esc(b["kicker"])}</div>' if b.get("kicker") else ""
    label, target = b.get("cta", ("Book a demo", DEMO))
    return (f'<section class="splithero"><div class="copy">{kick}'
            f'<h1>{esc(b["h1"])}</h1><p class="sub">{esc(b["lede"])}</p>'
            f'<a class="pill pill-lg" href="{_link(base, target)}">{esc(label)}</a></div>'
            f'<div class="photoslot"><div class="box"></div>'
            f'<div class="cap">{esc(b["photo"])}</div></div></section>')


def s_spectable(b, base):
    rows = "".join(f'<div class="specrow"><b>{esc(k)}</b><span>{esc(v)}</span></div>' for k, v in b["rows"])
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'<div class="spectable">{rows}</div></div></section>')


def s_duo(b, base):
    out = ""
    for t, d, dark in b["items"]:
        cls = "duocard dark" if dark else "duocard"
        out += f'<div class="{cls}"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
    return f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner duo">{out}</div></section>'


def s_steps(b, base):
    out = "".join(f'<div class="step"><div class="num">{esc(n)}</div><p>{esc(t)}</p></div>'
                  for n, t in b["items"])
    h = f'<h2 class="h2 h2-wide">{esc(b["h"])}</h2>' if b.get("h") else ""
    go = ""
    if b.get("link"):
        l, t = b["link"]
        go = f'<a class="bcard-go" href="{_link(base, t)}" style="color:var(--color-accent-hover);font-weight:500">{esc(l)} &rarr;</a>'
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'<div class="steps3">{out}</div>{go}</div></section>')


def s_faqcards(b, base):
    rows = "".join(f'<div class="faqcard"><div class="q">{esc(q)}</div><div class="a">{esc(a)}</div></div>'
                   for q, a in b["items"])
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    label, target = b.get("cta", ("Book a demo", DEMO))
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner stack-44">{h}'
            f'<div class="faqcards">{rows}</div>'
            f'<a class="pill pill-lg" style="align-self:flex-start" href="{_link(base, target)}">{esc(label)}</a>'
            f'</div></section>')



CHECK_SVG = ('<svg width="22" height="22" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
             '<path d="M4 12.5 L9.5 18 L20 6.5" fill="none" stroke="var(--color-accent)" '
             'stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def s_bigfeat(b, base):
    out = "".join(f'<div class="bigfeat"><div class="ico"></div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
                  for t, d in b["items"])
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    extra = ""
    if b.get("bullets"):
        cols = ""
        for col in b["bullets"]:
            rows = "".join(f'<div class="b"><i></i><span>{esc(x)}</span></div>' for x in col)
            cols += f'<div class="bullets">{rows}</div>'
        extra = f'<div class="grid g2">{cols}</div>'
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'<div class="grid g2">{out}</div>{extra}</div></section>')


def s_numlist(b, base):
    cols = ""
    for col in b["cols"]:
        rows = "".join(f'<div class="r"><b>{esc(n)}</b><span>{esc(t)}</span></div>' for n, t in col)
        cols += f'<div class="numlist">{rows}</div>'
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'<div class="grid g2">{cols}</div></div></section>')


def s_checks(b, base):
    out = "".join(f'<div class="check">{CHECK_SVG}<span>{esc(t)}</span></div>' for t in b["items"])
    h = f'<h2 class="h2 h2-wide">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner stack-44">{h}'
            f'<div class="checks">{out}</div></div></section>')


def s_statcards(b, base):
    out = ""
    for v, t, src in b["items"]:
        srch = f'<div class="src">{esc(src)}</div>' if src else ""
        out += f'<div class="statcard"><b>{esc(v)}</b><p>{esc(t)}</p>{srch}</div>'
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner stack-44">{h}'
            f'<div class="statcards">{out}</div></div></section>')



def s_softcards(b, base):
    out = "".join(f'<div class="softcard"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in b["items"])
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'<div class="grid g2">{out}</div></div></section>')


def s_ctarow(b, base):
    l, t = b["link"]
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner ctarow">'
            f'<div class="t"><h2>{esc(b["h"])}</h2><p>{esc(b["text"])}</p></div>'
            f'<a class="go" href="{_link(base, t)}">{esc(l)} &rarr;</a></div></section>')


BLOCKS = {"head": s_head, "twocol": s_twocol, "chain": s_chain, "cards": s_cards,
          "numbered": s_numbered, "flagstats": s_flagstats, "audience": s_audience,
          "ticks": s_ticks, "quote": s_quote, "cases": s_cases, "faq": s_faq,
          "table": s_table, "darkbar": s_darkbar, "closing": s_closing,
          "form": s_form, "links": s_links, "splithero": s_splithero,
          "spectable": s_spectable, "duo": s_duo, "steps": s_steps, "faqcards": s_faqcards, "bigfeat": s_bigfeat,
          "numlist": s_numlist, "checks": s_checks, "statcards": s_statcards,
          "softcards": s_softcards, "ctarow": s_ctarow}

PROOF_BAR = {"t": "darkbar", "items": [
    "SOC 2 and HIPAA compliant, ready for immediate deployment",
    "1M+ medications administered",
    "50K+ medication errors eliminated",
    "75+ pharmacy partners across 20+ states",
    "25K+ nursing hours saved",
    "75K+ DSP hours saved"]}


def render(path, title, sections, notes, nav, foot, badge=""):
    depth = path.count("/")
    base = "../" * depth
    url = "/" + path.replace("index.html", "")
    body = "".join(BLOCKS[s["t"]](s, base) for s in sections)
    notes_html = ""
    if notes:
        notes_html = ('<aside class="notes"><h4>Prototype notes</h4><ul>' +
                      "".join(f"<li>{esc(n)}</li>" for n in notes) + "</ul></aside>")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{esc(title)} — Impruvon (prototype)</title>
<link rel="stylesheet" href="{base}assets/style.css">
</head><body>
<div class="annot">
  <span class="aurl">PROTOTYPE &middot; {esc(title.upper())} &middot; {esc(url)}</span>{f'<span class="badge">{esc(badge)}</span>' if badge else ""}
  <span class="aleg"><span class="swatch"></span>Yellow = needs client confirmation before build</span>
  <span class="aleg"><button id="notesToggle" type="button">Show notes</button>
    <a href="{base}sitemap.html">Sitemap</a></span>
</div>
{nav(base, path)}
<main>{notes_html}{body}</main>
{foot(base)}
<script src="{base}assets/proto.js"></script>
</body></html>"""


# ------------------------------------------------------------------ pages
PAGES = {}

PAGES["platform/index.html"] = dict(title="Platform", notes=[
    "Transcribed from the artboard “Impruvon — Platform”.",
    "Hub page: its job is routing. Each pillar is a standalone page so it can rank on buyer terms and hold depth.",
    "The yellow Results block is flagged because the figures are sourced to an I/DD-specific elevator pitch — scope and external-use clearance needed before publishing.",
], sections=[
    {"t": "head", "kicker": "PLATFORM", "h1": "From medication management to clinical workflow.",
     "lede": "Most platforms tell you what already happened. Impruvon is built to guide what happens next.",
     "cta": ("Book a demo", DEMO)},
    {"t": "twocol", "h": "What is Impruvon?", "body": [
        "Impruvon is a fully compliant eMAR platform, purpose-built for residential and community-based care, that transforms medication administration from a manual compliance activity into a proactive safety and quality system: real-time visibility, automated compliance oversight, standardized workflows, early risk detection, and audit-ready documentation, all in one connected ecosystem.",
        "Our integrated software-hardware platform connects guided workflows, smart medication storage and real-time pharmacy integration, giving providers complete visibility and control without changing the pharmacies, packaging or EHR systems they already use."]},
    {"t": "chain", "caption": "EVERY STEP LANDS IN ONE RECORD", "steps": [
        ("Pharmacy", "75+ partners", False), ("MedBox", "hardware", True),
        ("eMAR+", "software", True), ("EHR / HRST", "your systems", False)]},
    {"t": "cards", "h": "Four pillars, one platform.", "cols": 2, "items": [
        {"title": "eMAR+", "text": "Guided smart med pass, in-app barcode scanning, PRN reason and effectiveness tracking, narcotic counting, with treatments, vitals and daily documentation in the same record.", "link": "platform/emar.html", "cta": "See eMAR+"},
        {"title": "MedBox", "text": "Smart medication storage with precise, individual-level dispensing, whether staff are administering or individuals are self-administering with supervision.", "link": "platform/medbox.html", "cta": "See MedBox"},
        {"title": "Integrations", "text": "24/7 bidirectional pharmacy integration with 75+ partners, plus your existing EHR.", "link": "platform/pharmacy-integration.html", "cta": "See integrations"},
        {"title": "HRST Automation", "text": "Complete all of your HRST inputs with a single click.", "link": "platform/hrst-automation.html", "cta": "See HRST automation"},
    ]},
    {"t": "flagstats", "h": "Results at a glance.", "items": [
        ("48%", "Reduction in medication errors"), ("39%", "Improvement in compliance rates"),
        ("69%", "Better audit-ready documentation"), ("50,000+", "Medication errors eliminated to date")],
     "note": "Figures are sourced to an I/DD-specific elevator pitch. Confirm scope and external-use clearance before publishing."},
    {"t": "audience", "h": "Built for the setting you work in.", "items": [
        ("I/DD & Residential Providers", "Purpose-built for the demands of group homes, ICFs and HCBS waiver programs.", "who-we-serve/idd-residential.html"),
        ("Behavioral & Mental Health", "Built for the documentation and complexity of psychiatric care.", "who-we-serve/behavioral-mental-health.html"),
        ("Home Health", "Real-time visibility into care delivered outside the facility.", "who-we-serve/home-health.html"),
        ("Foster Care", "Continuity of care for every child, at every placement change.", "who-we-serve/foster-care.html")],
     "band": ("State-Directed Programs",
              "Prevention infrastructure for state agencies and Medicaid health plans.",
              "Request a state briefing", "who-we-serve/state-directed.html")},
    PROOF_BAR,
    {"t": "closing", "h": "See the platform in action."},
])


def write_all(out, nav, foot):
    written = []
    for path, spec in PAGES.items():
        doc = render(path, spec["title"], spec["sections"], spec.get("notes", []), nav, foot, spec.get("badge",""))
        full = os.path.join(out, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        io.open(full, "w", encoding="utf-8").write(doc)
        written.append(path)
    return written


PAGES["platform/medbox.html"] = dict(title="MedBox", badge="SEPARATE PAGE TO BE CONFIRMED · SOURCE TEXT TRUNCATED IN THE CLIENT FILE", notes=[
    "Transcribed from the artboard “Impruvon — MedBox”.",
    "MedBox is the one thing no competitor has, so it gets a standalone page rather than an anchor on the Platform page.",
    "The device image must be a real photo in a home, not a render on white — a render reads as a concept, a photo reads as a product that exists.",
], sections=[
    {"t": "splithero", "kicker": "PLATFORM · MEDBOX",
     "h1": "Right meds. Right people. Right time. Every time.",
     "lede": "Locking meds away keeps them secure. MedBox keeps them accurate.",
     "cta": ("See MedBox in a demo", DEMO),
     "photo": "REAL PHOTO OF THE DEVICE IN A HOME, NOT A RENDER ON WHITE"},
    {"t": "twocol", "h": "Beyond basic access control.", "body": [
        "Smart MedBoxes replace key cabinets, unsecured closets and paper pass logs with precise, individual-level dispensing, providing access to only the correct medications, at the correct times, whether staff are administering or individuals are self-administering with supervision."]},
    {"t": "cards", "h": "MedBox key features.", "cols": 3, "bg": "sec-sunk", "items": [
        {"title": "Packaging agnostic", "text": "Up to 64 blister cards or 36 strip packs. Capacity may vary by packaging."},
        {"title": "Double-locking drawers", "text": "For narcotic storage."},
        {"title": "Controlled drawer", "text": "For topicals, injectables and more."},
        {"title": "Cellular and Wi-Fi connectivity"},
        {"title": "Backup battery and emergency access key"},
        {"title": "Compact footprint", "text": "11.5\" H × 11\" W × 14\" D"},
    ]},
    {"t": "spectable", "h": "Specifications.", "rows": [
        ("Capacity", "Up to 64 blister cards or 36 strip packs, varies by packaging"),
        ("Dimensions", "11.5\" H × 11\" W × 14\" D"),
        ("Connectivity", "Cellular and Wi-Fi"),
        ("Power", "Backup battery"),
        ("Emergency access", "Physical access key"),
        ("Narcotic storage", "Double-locking drawers"),
        ("Additional storage", "Controlled drawer for topicals and injectables"),
        ("Packaging", "Agnostic"),
    ]},
    {"t": "duo", "items": [
        ("Emergency Kit (E-Kit).",
         "Centralized, real-time tracked emergency medication storage with automated restocking. No pharmacy delays when minutes matter.", False),
        ("Empowerment built in.",
         "MedBox supports supervised self-administration, giving individuals dignity and independence while care teams retain the oversight needed to keep them safe.", True),
    ]},
    {"t": "steps", "h": "MedBox is part of the platform, not a separate product.",
     "link": ("See eMAR+", "platform/emar.html"), "items": [
        ("01", "The app tells MedBox what is due."),
        ("02", "MedBox gives access to only those medications."),
        ("03", "Every dispense is recorded in the same eMAR+ record an auditor reads."),
     ]},
    {"t": "faqcards", "h": "Questions we get about MedBox.", "cta": ("See MedBox in a demo", DEMO), "items": [
        ("Is there a medication dispensing device for group homes?",
         "Yes. Smart MedBoxes replace key cabinets, unsecured closets and paper pass logs with precise, individual-level dispensing, giving access to only the correct medications at the correct times."),
        ("How is this different from a locked cabinet?",
         "A cabinet controls who gets in. MedBox goes beyond basic access control to individual-level dispensing, and every dispense is recorded."),
        ("Do we have to change our pharmacy or packaging?",
         "No. MedBox is medication packaging agnostic and holds up to 64 blister cards or 36 strip packs."),
        ("What happens during a power outage?",
         "MedBox has a backup battery, plus a physical emergency access key."),
    ]},
])


PAGES["platform/emar.html"] = dict(title="eMAR+", notes=[
    "Transcribed from the artboard “Impruvon — eMAR+”.",
    "The page has to break the “just an eMAR” read in the first screen — that is why the hero leads with “Beyond an eMAR” and the second section answers “Why not just any eMAR?” directly.",
    "Clinical workflow items are numbered 01–09 because that list is the answer to “what else is in the record besides medications”.",
], sections=[
    {"t": "head", "kicker": "PLATFORM · eMAR+", "h1": "Beyond an eMAR. Care reimagined.",
     "lede": "A digital record of an error is still an error. Impruvon eMAR+ guides the right action before it happens.",
     "cta": ("See eMAR+ in a demo", DEMO)},
    {"t": "twocol", "h": "Why not just any eMAR?", "body": [
        "Most eMARs digitize the paper MAR and stop there. The Impruvon eMAR+ is your partner in proactive resident and operational excellence, pairing guided medication management with the clinical workflows that surround it, so the safe choice is the automatic choice on every shift."]},
    {"t": "bigfeat", "h": "Medication management.", "items": [
        ("Guided smart med pass", "Step-by-step prompts walk any caregiver through every administration."),
        ("In-app barcode scanning", "No external scanners required."),
    ], "bullets": [
        ["Guided self-administration, supervised independence with safety guardrails",
         "PRN reason and effectiveness tracking", "Narcotic counting", "Smart reminders and alerts"],
        ["Role-specific interfaces, every team member sees exactly what they need",
         "Real-time pharmacy integration", "HRST automation"],
    ]},
    {"t": "numlist", "h": "Clinical workflow optimization.", "cols": [
        [("01", "Treatments (eTAR), vitals and bowel movement tracking"),
         ("02", "Automated treatment order processing"),
         ("03", "Daily documentation, clinical notes and incident reporting"),
         ("04", "Activities of daily living and mood tracking"),
         ("05", "Assessments and self-assessments")],
        [("06", "Goal and independence enablement"),
         ("07", "Medical equipment management"),
         ("08", "Role-based permissions and real-time requests"),
         ("09", "1-click regulatory reporting and smart dashboards")],
    ]},
    {"t": "checks", "h": "Built for community-based care, not retrofitted from hospitals or skilled nursing.", "items": [
        "Easy to learn and use for DSPs and nurses alike",
        "Reminds, guides and tracks medications, treatments and vitals in one system",
        "Meets service-provider-specific regulatory requirements",
        "Works on Android, iOS and web browsers, with automated single sign-on",
        "Tracks inventory, narcotic counts and PRNs, and simplifies refill requests",
        "In-person and virtual customer support",
    ]},
    {"t": "cards", "h": "eMAR+ doesn't work alone.", "cols": 2, "items": [
        {"title": "MedBox", "text": "Optional double-locking smart MedBoxes give access to only the correct medications, at the correct times. Every dispense lands in the same record.", "link": "platform/medbox.html", "cta": "See MedBox"},
        {"title": "Pharmacy and EHR", "text": "Real-time pharmacy integration and connection to your existing EHR, so nothing is transcribed by hand.", "link": "platform/pharmacy-integration.html", "cta": "See integrations"},
    ]},
    {"t": "statcards", "h": "Proven results.", "items": [
        ("23,000+", "medications administered with zero errors, Charles Lea Center",
         "Source: impruvon.com/products, Charles Lea Center case study"),
        ("20–25 min", "saved per resident, per medication pass",
         "Source: impruvonhealth.com, customer testimonial"),
    ]},
    {"t": "quote", "bg": "sec-sunk", "light": True,
     "text": "Impruvon is a game changer, it really is as good as it sounds. I can literally administer all of the meds on my shift in less than half the time it used to take.",
     "by": "DSP, I/DD residential / group home, Washington D.C."},
    {"t": "faq", "h": "Questions we get about eMAR+.", "items": [
        ("What is an eMAR?", "An eMAR is an electronic medication administration record: a digital, time-stamped record of every dose given, replacing the paper MAR binder."),
        ("Paper MAR vs eMAR: what changes?", "A paper MAR can't catch an error before it happens. eMAR+ guides the right action before it happens, and every administration is recorded as it occurs."),
        ("Will staff who aren't clinicians use it?", "Step-by-step prompts walk any caregiver through every administration, and role-specific interfaces mean each person sees exactly what they need. Easy to learn and use for DSPs and nurses alike."),
        ("What devices does it run on?", "Android, iOS and web browsers, with automated single sign-on."),
        ("Do we have to replace our EHR or change pharmacies?", "No. Impruvon connects with your existing EHR systems, and integration requires no changes to pharmacy or medication packaging."),
    ]},
    {"t": "closing", "h": "See eMAR+ in a demo.", "cta": ("Book a demo", DEMO)},
])


PAGES["platform/hrst-automation.html"] = dict(title="HRST Automation", notes=[
    "Transcribed from the artboard “Impruvon — HRST Automation”.",
    "This is the narrowest page on the site and that is deliberate: HRST is an I/DD-specific requirement, so the page ends by handing the reader to the I/DD vertical rather than to a generic overview.",
], sections=[
    {"t": "head", "kicker": "Predict. Prevent. Protect.", "eyebrow_big": True,
     "h1": "Health risk screening, kept current automatically.",
     "lede": "A screening tool filled out days late can only describe risk that's already changed.",
     "cta": ("See HRST automation in a demo", DEMO)},
    {"t": "twocol", "h": "What is HRST automation?", "body": [
        "Impruvon integrates with state-mandated HRST medication and diagnosis requirements, ensuring compliance with automated data syncing, real-time risk updates and streamlined workflows. HRST Automation saves time, reduces manual effort, and transforms health risks into actionable insights."]},
    {"t": "softcards", "h": "Benefits of HRST automation.", "items": [
        ("Save time", "Complete all of your HRST inputs with a single click."),
        ("Automated accuracy", "Medications, diagnoses and allergies pulled from the source: the pharmacy filling your medications."),
        ("Ensure compliance", "HRST submissions completed accurately and on time."),
        ("Eliminate stress", "No more manually entering complex medication, diagnosis or allergy information for every resident."),
    ]},
    {"t": "ctarow", "h": "Built for I/DD providers.",
     "text": "HRST requirements come with I/DD services. If you run group homes, ICFs or HCBS waiver programs, this is the screening your team completes again and again.",
     "link": ("See I/DD & Residential", "who-we-serve/idd-residential.html")},
    {"t": "closing", "h": "See HRST automation in a demo."},
])
