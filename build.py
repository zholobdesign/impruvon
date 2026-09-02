#!/usr/bin/env python3
"""Generates the Impruvon clickable structure prototype (static HTML)."""
import os, shutil, html
from paper_theme import CSS, JS
import paper_home

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "docs")

# ---------------------------------------------------------------- navigation
NAV = [
    ("Platform", "platform/index.html", [
        ("eMAR+", "platform/emar.html"),
        ("MedBox", "platform/medbox.html"),
        ("Pharmacy integration", "platform/pharmacy-integration.html"),
        ("EHR integration", "platform/ehr-integration.html"),
        ("HRST automation", "platform/hrst-automation.html"),
    ]),
    ("Who we serve", "who-we-serve/index.html", [
        ("I/DD & Residential", "who-we-serve/idd-residential.html"),
        ("Behavioral & Mental Health", "who-we-serve/behavioral-mental-health.html"),
        ("Home Health", "who-we-serve/home-health.html"),
        ("Foster Care", "who-we-serve/foster-care.html"),
        ("State-Directed Programs", "who-we-serve/state-directed.html"),
    ]),
    ("Compare", "compare/index.html", []),
    ("Pricing", "pricing/index.html", []),
    ("Trust", "trust/index.html", []),
    ("Resources", "resources/index.html", [
        ("Supporting DSPs", "resources/caregivers/index.html"),
        ("Guides for administrators", "resources/guides/index.html"),
        ("Customer stories", "resources/customers/index.html"),
    ]),
    ("About", "about/index.html", [
        ("Our story", "about/our-story.html"),
        ("Our commitment", "about/our-commitment.html"),
        ("Careers", "about/careers.html"),
        ("Contact", "about/contact.html"),
    ]),
]

DEMO = "book-a-demo/index.html"


# ---------------------------------------------------------------- block types
def esc(s):
    return html.escape(str(s), quote=False)


def rel(base, target):
    return base + target


def b_text(base, b):
    out = ""
    if b.get("h"):
        out += f'<h2>{esc(b["h"])}</h2>'
    for p in b.get("p", []):
        out += f'<p>{esc(p)}</p>'
    return f'<section class="block">{out}</section>'


def b_list(base, b):
    items = "".join(f"<li>{esc(i)}</li>" for i in b["items"])
    h = f'<h2>{esc(b["h"])}</h2>' if b.get("h") else ""
    lead = f'<p>{esc(b["lead"])}</p>' if b.get("lead") else ""
    return f'<section class="block">{h}{lead}<ul class="ticks">{items}</ul></section>'


def b_cards(base, b):
    cards = ""
    for c in b["items"]:
        link = c.get("link")
        title = esc(c["title"])
        text = f'<p>{esc(c["text"])}</p>' if c.get("text") else ""
        if link:
            cards += (f'<a class="card" href="{rel(base, link)}"><h3>{title}</h3>{text}'
                      f'<span class="go">{esc(c.get("cta", "Open page"))} &rarr;</span></a>')
        else:
            cards += f'<div class="card"><h3>{title}</h3>{text}</div>'
    h = f'<h2>{esc(b["h"])}</h2>' if b.get("h") else ""
    lead = f'<p>{esc(b["lead"])}</p>' if b.get("lead") else ""
    cls = "cards cards-" + str(b.get("cols", 3))
    return f'<section class="block">{h}{lead}<div class="{cls}">{cards}</div></section>'


HERO_PANEL = """
<div class="hero-panel">
  <div class="tabs"><span class="tab on">eMAR+</span><span class="tab">MedBox</span>
    <span class="tab">Pharmacy</span><span class="tab">HRST</span></div>
  <div class="appwin">
    <div class="appside">
      <h3 style="font-size:17px;margin-bottom:14px">Evening pass &middot; Maple House</h3>
      <div class="approw"><span class="avat"></span><span style="flex:1">Denise R.</span><span class="pill-ok">GIVEN</span></div>
      <div class="approw"><span class="avat"></span><span style="flex:1">James O.</span><span class="pill-ok">GIVEN</span></div>
      <div class="approw on"><span class="avat"></span><span style="flex:1">Marcus T.</span><span class="pill-now">NOW</span></div>
      <div class="approw"><span class="avat"></span><span style="flex:1">Aisha K.</span><span class="pill-ok" style="background:#EDF0F1;color:#5A6B78">6:15 PM</span></div>
    </div>
    <div class="appmain">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">
        <span class="avat" style="width:42px;height:42px;border-radius:21px"></span>
        <span><b style="display:block;font-size:18px;letter-spacing:-.02em">Marcus T.</b>
        <span style="font-size:14px;color:var(--mut)">Room 2 &middot; MedBox A &middot; 6:00 PM pass</span></span>
        <span class="pill-ok" style="margin-left:auto;background:#EEF7EF;color:#4A6B1F">BARCODE VERIFIED</span>
      </div>
      <div class="medcard">
        <span style="flex:1"><b style="display:block;font-size:22px;letter-spacing:-.03em">Sertraline 50&nbsp;mg</b>
        <span style="font-size:15px;color:var(--mut)">1 tablet &middot; by mouth &middot; with food</span></span>
        <span style="text-align:right"><b style="display:block;font-size:11px;letter-spacing:.1em;color:var(--mut)">DRAWER</b>
        <span style="font-size:18px;font-weight:700;color:var(--accent)">A-3 open</span></span>
      </div>
      <div class="rights">
        <span class="right"><b>PERSON</b><span>Marcus T.</span></span>
        <span class="right"><b>MEDICATION</b><span>Sertraline</span></span>
        <span class="right"><b>DOSE</b><span>50 mg</span></span>
        <span class="right"><b>ROUTE</b><span>By mouth</span></span>
        <span class="right"><b>TIME</b><span>6:04 PM</span></span>
      </div>
      <div class="appbtn">Mark as given</div>
    </div>
  </div>
</div>"""


def b_media(base, b):
    kind = b.get("kind", "image")
    if kind == "hero":
        return '<section class="block">' + HERO_PANEL + '</section>'
    return (f'<section class="block"><div class="ph ph-{kind}">'
            f'<div class="ph-inner"><div class="ph-tag">{esc(kind.upper())}</div>'
            f'<p class="ph-label">{esc(b["label"])}</p></div></div></section>')


def b_stats(base, b):
    cells = "".join(f'<div class="stat"><strong>{esc(s["v"])}</strong><span>{esc(s["l"])}</span></div>'
                    for s in b["items"])
    h = f'<h2>{esc(b["h"])}</h2>' if b.get("h") else ""
    note = f'<p class="src">{esc(b["src"])}</p>' if b.get("src") else ""
    return f'<section class="block">{h}<div class="stats">{cells}</div>{note}</section>'


def b_quote(base, b):
    return (f'<section class="block"><blockquote><p>{esc(b["text"])}</p>'
            f'<cite>{esc(b["by"])}</cite></blockquote></section>')


def b_faq(base, b):
    rows = "".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>'
                   for q, a in b["items"])
    h = f'<h2>{esc(b.get("h","Common questions"))}</h2>'
    return f'<section class="block">{h}{rows}</section>'


def b_table(base, b):
    head = "".join(f"<th>{esc(c)}</th>" for c in b["head"])
    body = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in b["rows"])
    h = f'<h2>{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="block">{h}<div class="tablewrap"><table>'
            f'<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div></section>')


def b_cta(base, b):
    btns = ""
    for i, (label, target) in enumerate(b["buttons"]):
        cls = "btn" if i == 0 else "btn btn-2"
        btns += f'<a class="{cls}" href="{rel(base, target)}">{esc(label)}</a>'
    ht = b.get("h", "Ready to see it?")
    h = f'<h2>{esc(ht)}</h2>' if ht else ""
    p = f'<p>{esc(b["p"])}</p>' if b.get("p") else ""
    return f'<section class="block cta">{h}{p}<div class="btns">{btns}</div></section>'


def b_links(base, b):
    items = "".join(f'<li><a href="{rel(base, t)}">{esc(l)}</a></li>' for l, t in b["items"])
    h = f'<h2>{esc(b["h"])}</h2>' if b.get("h") else ""
    return f'<section class="block"><nav class="linklist">{h}<ul>{items}</ul></nav></section>'


BLOCKS = {"text": b_text, "list": b_list, "cards": b_cards, "media": b_media,
          "stats": b_stats, "quote": b_quote, "faq": b_faq, "table": b_table,
          "cta": b_cta, "links": b_links}



CHROME_LINKS = [("Platform", "platform/index.html"), ("Who We Serve", "who-we-serve/index.html"),
                ("Pricing", "pricing/index.html"), ("Resources", "resources/index.html"),
                ("Company", "about/index.html")]

FOOT_COLS = [
    ("PLATFORM", [("eMAR+", "platform/emar.html"), ("MedBox", "platform/medbox.html"),
                  ("Integrations", "platform/pharmacy-integration.html"),
                  ("HRST Automation", "platform/hrst-automation.html")]),
    ("WHO WE SERVE", [("I/DD & Residential", "who-we-serve/idd-residential.html"),
                      ("Home Health", "who-we-serve/home-health.html"),
                      ("State-Directed Programs", "who-we-serve/state-directed.html")]),
    ("COMPANY", [("Our Story", "about/our-story.html"), ("Trust & Compliance", "trust/index.html"),
                 ("Careers", "about/careers.html"), ("Contact", "about/contact.html")]),
]


def render_chrome_nav(base, path):
    links = ""
    for label, target in CHROME_LINKS:
        on = " class=\"on\"" if path.startswith(target.split("/")[0]) else ""
        links += f'<a href="{base}{target}"{on}>{esc(label)}</a>'
    return (f'<header class="nav"><a class="brand" href="{base}index.html">'
            f'<span class="mark"></span>Impruvon</a>'
            f'<nav class="links">{links}</nav>'
            f'<div class="right"><a class="login" href="{base}login/index.html">Log in</a>'
            f'<a class="pill" href="{base}{DEMO}">Book a demo</a></div></header>')


def render_chrome_foot(base):
    cols = ""
    for head, items in FOOT_COLS:
        links = "".join(f'<a href="{base}{t}">{esc(l)}</a>' for l, t in items)
        cols += f'<div class="col"><h4>{esc(head)}</h4>{links}</div>'
    return (f'<footer class="foot"><div class="fbrand">'
            f'<div class="row"><span class="mark"></span><b>Impruvon</b></div>'
            f'<p>Medication safety for residential and community-based care.</p></div>{cols}</footer>')


# ---------------------------------------------------------------- page shell
def render_nav(base, active):
    items = ""
    for label, target, kids in NAV:
        cls = ' class="on"' if active and active.startswith(target.split("/")[0]) else ""
        sub = ""
        if kids:
            sub = '<div class="sub">' + "".join(
                f'<a href="{rel(base, t)}">{esc(l)}</a>' for l, t in kids) + '</div>'
        items += f'<div class="navitem"><a href="{rel(base, target)}"{cls}>{esc(label)}</a>{sub}</div>'
    return items


def render_footer(base):
    cols = ""
    for label, target, kids in NAV:
        links = f'<li><a href="{rel(base, target)}">{esc(label)}</a></li>'
        links += "".join(f'<li><a href="{rel(base, t)}">{esc(l)}</a></li>' for l, t in kids)
        cols += f'<div><h4>{esc(label)}</h4><ul>{links}</ul></div>'
    return cols


def page(path, title, h1, kicker="", intro="", blocks=(), notes=(), crumbs=()):
    depth = path.count("/")
    base = "../" * depth
    body = "".join(BLOCKS[b["t"]](base, b) for b in blocks)

    crumb_html = ""
    if crumbs:
        parts = " / ".join(f'<a href="{rel(base, t)}">{esc(l)}</a>' if t else esc(l)
                           for l, t in crumbs)
        crumb_html = f'<div class="crumbs">{parts}</div>'

    notes_html = ""
    if notes:
        notes_html = ('<aside class="notes" id="notes"><h4>Prototype notes</h4><ul>' +
                      "".join(f"<li>{esc(n)}</li>" for n in notes) + "</ul></aside>")

    url = "/" + path.replace("index.html", "")
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{esc(title)} — Impruvon (prototype)</title>
<link rel="stylesheet" href="{base}assets/style.css">
</head><body>
<div class="annot">
  <span class="aurl">PROTOTYPE · {esc(title.upper())} · {esc(url)}</span>
  <span class="aleg"><span class="swatch"></span>Yellow = needs client confirmation before build</span>
  <span class="aleg"><button id="notesToggle" type="button">Show notes</button>
    <a href="{base}sitemap.html">Sitemap</a></span>
</div>
{render_chrome_nav(base, path)}
<main>
  {notes_html}
  <div class="sec"><div class="sec-inner">
    {crumb_html}
    {f'<div class="kicker">{esc(kicker)}</div>' if kicker else ''}
    <h1 class="h2 h2-wide" style="font-size:52px;line-height:60px;margin-bottom:20px">{esc(h1)}</h1>
    {f'<p class="lede" style="max-width:70ch">{esc(intro)}</p>' if intro else ''}
  </div></div>
  {body}
</main>
{render_chrome_foot(base)}
<script src="{base}assets/proto.js"></script>
</body></html>"""
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(doc)
    return path


# ---------------------------------------------------------------- shared bits
PROOF = {"t": "stats", "h": "Proof", "items": [
    {"v": "1M+", "l": "Medications administered"},
    {"v": "50K+", "l": "Medication errors eliminated"},
    {"v": "75K+", "l": "DSP hours saved"},
    {"v": "25K+", "l": "Nursing hours saved"},
    {"v": "75+", "l": "Pharmacy partners"},
], "src": "Source: Impruvon I/DD elevator pitch, June 2026. PENDING: confirm scope (platform-wide vs I/DD) before publishing."}

DEMO_CTA = {"t": "cta", "h": "See it on a real med pass.",
            "p": "Bring your own workflow — and the questions your auditors ask.",
            "buttons": [("Book a demo", DEMO), ("Talk to sales", "about/contact.html")]}

STATE_CTA = {"t": "cta", "h": "Standardise medication safety across your network.",
             "p": "For state agencies and Medicaid health plans.",
             "buttons": [("Request a state briefing", DEMO), ("Trust & compliance", "trust/index.html")]}


# ---------------------------------------------------------------- pages
def build_pages():
    # ---------- HOME
    page("index.html", "Home", "Fewer medication errors. Even when you're short-staffed.",
         kicker="The state-directed eMAR in Massachusetts",
         intro="Impruvon is the medication-safety platform for residential and community-based care. "
               "Guided software, smart storage and real-time pharmacy integration — in one system.",
         notes=[
             "Every page on this site funnels to one conversion: Book a demo. State-directed traffic gets a second door: Request a state briefing.",
             "Hero must do three jobs (per Stage 5): define the entity in the first 200 words, show MedBox early to break the 'just an eMAR' read, and surface the Massachusetts state-directed proof.",
             "The product visual is a live med-pass record — not a generic dashboard screenshot.",
         ],
         blocks=[
             {"t": "cta", "h": "", "p": "", "buttons": [("Book a demo", DEMO), ("Talk to sales", "about/contact.html")]},
             {"t": "media", "kind": "hero", "label": ""},
             {"t": "text", "h": "Trusted by providers, pharmacies and state agencies",
              "p": ["Logo bar: Charles Lea Center · Vista Care · MA EOHHS · Coastal Autism Academy · StationMD"]},
             PROOF,
             {"t": "text", "h": "Safety shouldn't depend on who's on shift.",
              "p": ["Most safety plans start with “hire better people, train them harder.” We started somewhere else: a caregiver's first shift should be exactly as safe as their thousandth.",
                    "Different experience levels, workforce shortages and complex regimens are the conditions, not the exception. So we put the safeguard in the workflow, not in the person."]},
             {"t": "cards", "h": "Four pillars, one platform", "cols": 4, "items": [
                 {"title": "eMAR+", "text": "Simplify every workflow — guided med passes, barcode scanning, PRN and narcotic counts.", "link": "platform/emar.html", "cta": "Explore eMAR+"},
                 {"title": "HRST automation", "text": "Ensure audit readiness — every input in one click, risk updated in real time.", "link": "platform/hrst-automation.html", "cta": "Explore HRST"},
                 {"title": "Pharmacy & EHR", "text": "Connect every touchpoint — 24/7 bidirectional flow, no change to your systems.", "link": "platform/pharmacy-integration.html", "cta": "Explore integrations"},
                 {"title": "MedBox", "text": "Empower every person — smart storage that opens the right drawer at the right time.", "link": "platform/medbox.html", "cta": "Explore MedBox"},
             ]},
             {"t": "media", "kind": "photo", "label": "Photo: DSP running an evening med pass on a tablet, group-home setting"},
             {"t": "stats", "h": "What changes after you switch", "items": [
                 {"v": "48%", "l": "Fewer medication errors, on average"},
                 {"v": "39%", "l": "Higher compliance rates"},
                 {"v": "69%", "l": "More audit-ready documentation"},
                 {"v": "1,800%", "l": "ROI in the Massachusetts state-directed model"},
             ], "src": "Source: Impruvon I/DD elevator pitch, June 2026. MA model built with the MA Executive Office of Health and Human Services."},
             {"t": "cards", "h": "One platform. Many realities. Zero compromises.", "cols": 3, "items": [
                 {"title": "I/DD & Residential", "text": "Group homes, ICFs and HCBS waiver programs.", "link": "who-we-serve/idd-residential.html"},
                 {"title": "Behavioral & Mental Health", "text": "Complex psychiatric regimens, heaviest documentation load.", "link": "who-we-serve/behavioral-mental-health.html"},
                 {"title": "Home Health", "text": "Every home, every visit — visible in real time.", "link": "who-we-serve/home-health.html"},
                 {"title": "Foster Care", "text": "The record follows the child to every placement.", "link": "who-we-serve/foster-care.html"},
                 {"title": "State-Directed Programs", "text": "Prevention infrastructure for states and Medicaid plans.", "link": "who-we-serve/state-directed.html"},
             ]},
             {"t": "quote", "text": "Impruvon is a game changer, it really is as good as it sounds. I can literally administer all of the meds on my shift in less than half the time it used to take.",
              "by": "Direct Support Professional — I/DD residential group home, Washington D.C."},
             {"t": "cards", "h": "Proof, with names on it", "cols": 3, "items": [
                 {"title": "23,000+ medications, zero errors", "text": "Charles Lea Center", "link": "resources/customers/charles-lea.html", "cta": "Read the case study"},
                 {"title": "75% fewer medication errors", "text": "Vista Care — 18 sites, 6 states", "link": "resources/customers/index.html", "cta": "Read the case study"},
                 {"title": "$371M projected savings", "text": "Massachusetts state-directed model", "link": "who-we-serve/state-directed.html", "cta": "See the state model"},
             ]},
             {"t": "faq", "items": [
                 ("What is an eMAR — and how is eMAR+ different?",
                  "An eMAR is the digital version of the paper MAR. eMAR+ goes further: it guides each administration step by step, adds treatments, vitals and clinical notes, and pulls orders straight from your pharmacy."),
                 ("Which providers is Impruvon built for?",
                  "Residential and community-based care: I/DD providers, group homes, ICFs and HCBS waiver programs; behavioral and mental health; home health; foster care; and state-directed programs."),
                 ("Is there a medication dispensing device for group homes?",
                  "Yes — MedBox. Double-locking narcotic drawers, a controlled drawer for topicals and injectables, cellular and Wi-Fi, backup battery. Up to 64 blister cards or 36 strip packs."),
                 ("Will it work with our pharmacy and EHR?",
                  "Yes. 75+ pharmacy partners nationally, orders and refills flowing both ways 24/7, plus EHR integration. No change to your pharmacy relationships or packaging."),
             ]},
             DEMO_CTA,
         ], crumbs=[])

    # ---------- PLATFORM
    page("platform/index.html", "Platform", "From medication management to clinical workflow.",
         kicker="Platform",
         intro="Most platforms tell you what already happened. Impruvon is built to guide what happens next.",
         crumbs=[("Home", "index.html"), ("Platform", None)],
         notes=["Hub page. Its job is routing: send the visitor to the one product page that answers their question, then to Book a demo.",
                "Each product below is a standalone page (team decision, Stage 5) — not an anchor on this page, so it can rank and hold depth."],
         blocks=[
             PROOF,
             {"t": "cards", "h": "Four pillars, one platform", "cols": 3, "items": [
                 {"title": "eMAR+", "text": "Guided med passes, barcode scanning, PRN tracking, narcotic counting, clinical documentation and vitals.", "link": "platform/emar.html"},
                 {"title": "MedBox", "text": "Smart medication storage with physical access control and supervised self-administration.", "link": "platform/medbox.html"},
                 {"title": "Pharmacy integration", "text": "24/7 bidirectional orders, refills and discontinuations with 75+ pharmacy partners.", "link": "platform/pharmacy-integration.html"},
                 {"title": "EHR integration", "text": "One place to work. Data flows where it needs to go — including telehealth partners.", "link": "platform/ehr-integration.html"},
                 {"title": "HRST automation", "text": "The only platform that fully integrates state-mandated HRST requirements.", "link": "platform/hrst-automation.html"},
             ]},
             {"t": "media", "kind": "product", "label": "Platform overview visual: the four pillars as one connected record"},
             DEMO_CTA,
         ])

    prod = [
        ("platform/emar.html", "eMAR+", "Beyond an eMAR. Care reimagined.",
         "A digital record of an error is still an error. Impruvon eMAR+ guides the right action before it happens.",
         ["Guided, smart med pass — step-by-step prompts walk any caregiver through every administration",
          "In-app barcode scanning — no external scanners required",
          "Guided self-administration — supervised independence with safety guardrails",
          "PRN reason and effectiveness tracking · narcotic counting · smart reminders and alerts",
          "Role-specific interfaces — every team member sees exactly what they need",
          "Treatments (eTAR), vitals, daily documentation, clinical notes and incident reporting",
          "1-click regulatory reporting and smart dashboards"],
         "Product UI: guided med pass, step 2 of 3, barcode verified, five rights checked",
         ["23,000+ medications administered with zero errors — Charles Lea Center",
          "20–25 minutes saved per resident, per medication pass"]),
        ("platform/medbox.html", "MedBox", "Right meds. Right people. Right time. Every time.",
         "Locking meds away keeps them secure. MedBox keeps them accurate.",
         ["Medication packaging agnostic — up to 64 blister cards or 36 strip packs",
          "Double-locking drawers for narcotic storage",
          "Controlled drawer for topicals, injectables and more",
          "Cellular and Wi-Fi connectivity",
          "Backup battery and emergency access key",
          "Compact footprint: 11.5\" H × 11\" W × 14\" D",
          "Supports supervised self-administration — dignity and independence, with oversight kept",
          "Emergency Kit (E-Kit): centralised, real-time tracked emergency medication storage with automated restocking"],
         "Photo: MedBox mounted in a group-home med room, drawer open",
         ["The only medication-safety platform with hardware — no competitor has this."]),
        ("platform/pharmacy-integration.html", "Pharmacy integration", "Every hour a prescription sits unsynced is an hour of risk.",
         "Real-time pharmacy connectivity — with no changes to your existing pharmacy relationships.",
         ["Automated prescription and refill reminders — no unexpected shortages",
          "Smart order review and approval for medications and treatments",
          "Real-time awareness of all orders and statuses",
          "Streamlined pharmacy communications: new orders, refills, discontinues",
          "Connected with 75+ pharmacy partners nationally",
          "Trusted by providers, state agencies and pharmacies across 20+ states"],
         "Product UI: live order queue — synced, refill, discontinue awaiting review",
         ["No changes to pharmacy or medication packaging needed."]),
        ("platform/ehr-integration.html", "EHR integration", "When systems don't talk to each other, no one has the full picture.",
         "Impruvon connects with your existing EHR, eliminating duplicate documentation and multi-system logins.",
         ["Staff work in one place, data flows where it needs to go",
          "No duplicate documentation, no multiple logins",
          "Telehealth integrations — e.g. StationMD — so remote physicians see accurate, real-time records instead of relying on a DSP to report from memory"],
         "Product UI: connected systems map — pharmacy, EHR, telehealth, HRST",
         []),
        ("platform/hrst-automation.html", "HRST automation", "Predict. Prevent. Protect.",
         "A screening tool filled out days late can only describe risk that's already changed.",
         ["Save time — complete all HRST inputs with a single click",
          "Automated accuracy — medications, diagnoses and allergies pulled from the pharmacy filling them",
          "Ensure compliance — submissions completed accurately and on time",
          "Eliminate stress — no manual entry of complex medication, diagnosis or allergy information"],
         "Product UI: HRST sync — inputs completed automatically, risk score updated",
         ["The only platform that fully integrates with state-mandated HRST requirements."]),
    ]
    for path, name, h1, intro, feats, media, proof in prod:
        blocks = [
            {"t": "media", "kind": "product" if "Photo" not in media else "photo", "label": media},
            {"t": "list", "h": "What it does", "items": feats},
        ]
        if proof:
            blocks.append({"t": "list", "h": "Proven results", "items": proof})
        blocks += [
            {"t": "links", "h": "Related", "items": [
                ("Compare Impruvon with other platforms", "compare/index.html"),
                ("Trust, security & compliance", "trust/index.html"),
                ("Who we serve", "who-we-serve/index.html")]},
            {"t": "cta", "h": f"See {name} in a demo.", "p": "Fifteen minutes, your workflow, your questions.",
             "buttons": [("Book a demo", DEMO), ("Back to platform", "platform/index.html")]},
        ]
        page(path, name, h1, kicker="Platform", intro=intro, blocks=blocks,
             crumbs=[("Home", "index.html"), ("Platform", "platform/index.html"), (name, None)],
             notes=["Standalone product page so it can rank on buyer terms and hold depth (Stage 5 decision).",
                    "One CTA per page: Book a demo. Cross-links go to Compare and Trust — the two pages that close the remaining objections."])

    # ---------- WHO WE SERVE
    page("who-we-serve/index.html", "Who we serve", "One platform. Many realities. Zero compromises.",
         kicker="Who we serve",
         intro="Built for the specific regulatory and staffing realities of each care setting — and adaptable to the workflows of every setting we serve. Deployed across more than 50% of U.S. states.",
         crumbs=[("Home", "index.html"), ("Who we serve", None)],
         notes=["Entry by audience ('who are you?'), Platform is entry by capability ('what does it do?'). Standard B2B pattern, matches how competitors are structured.",
                "Each vertical is a standalone page, not a jump anchor (changed from the client's original proposal): anchors can't rank for 'eMAR for foster care' and can't hold depth."],
         blocks=[
             {"t": "cards", "h": "Explore how Impruvon is purpose-built for your setting", "cols": 3, "items": [
                 {"title": "I/DD & Residential Providers", "text": "Purpose-built for the demands of group homes, ICFs and HCBS waiver programs.", "link": "who-we-serve/idd-residential.html"},
                 {"title": "Behavioral & Mental Health", "text": "Built for the documentation and complexity of psychiatric care.", "link": "who-we-serve/behavioral-mental-health.html"},
                 {"title": "Home Health", "text": "Real-time visibility into care delivered outside the facility.", "link": "who-we-serve/home-health.html"},
                 {"title": "Foster Care", "text": "Continuity of care for every child, at every placement change.", "link": "who-we-serve/foster-care.html"},
                 {"title": "State-Directed Programs", "text": "Prevention infrastructure for state agencies and Medicaid health plans.", "link": "who-we-serve/state-directed.html"},
             ]},
             DEMO_CTA,
         ])

    verticals = [
        ("who-we-serve/idd-residential.html", "I/DD & Residential",
         "“Doing nothing” isn't just paper MARs. It's also the wrong eMAR.",
         "If your system was built for nurses in a hospital, you've digitised the risk — not removed it.",
         ["A paper MAR can't catch an error before it happens; an eMAR designed for clinicians assumes a workforce you don't have.",
          "The cost of the status quo compounds quietly: the failed audit, the citation, the incident report, the DSP who burns out and walks.",
          "Clinical, financial, compliance, staffing — that's one problem showing up four ways."],
         ["Guided med passes, barcode scanning, PRN tracking and narcotic counting",
          "Real-time pharmacy integration — orders, refills and changes flow straight in",
          "Smart MedBoxes enforce physical access control",
          "The only platform with automated HRST integration",
          "Real-time analytics across every resident, in every location"],
         [("23,000+ medications administered with zero errors — Charles Lea Center", "resources/customers/charles-lea.html"),
          ("75% reduction in medication errors across 18 sites in 6 states — Vista Care", "resources/customers/index.html")],
         "Photo: DSP and resident in a group home, tablet in hand"),
        ("who-we-serve/behavioral-mental-health.html", "Behavioral & Mental Health",
         "Passing your audit and being defensible aren't the same thing.",
         "One is a scheduled event you prepare for. The other is a standard you either live in — or don't.",
         ["Real scrutiny doesn't arrive on schedule. It arrives with an adverse event, a licensing review, a lawsuit.",
          "If you stay ready, you never have to get ready. Audit readiness should be the byproduct of how documentation happens every shift."],
         ["eMAR, clinical tasks and vitals in one platform — no gaps between systems",
          "Guided med passes for complex psychiatric regimens",
          "Role-based interfaces reduce training burden for a high-turnover workforce",
          "SOC 2 and HIPAA compliant, ready for immediate deployment",
          "Supervised self-administration where clinically appropriate"],
         [("48% reduction in medication errors", None),
          ("39% improvement in compliance rates", None),
          ("69% improvement in audit-ready documentation", None)],
         "Photo: clinical supervisor reviewing a dashboard"),
        ("who-we-serve/home-health.html", "Home Health",
         "Distance isn't the reason you have less visibility. Technology is.",
         "If care happens in a hundred different homes, your records shouldn't live in a hundred different places.",
         ["A paper log in one home. A note texted at the end of a shift. A med change that reaches one location but not the next.",
          "Stop asking “can we get better reports at the end of the week?” Start asking “why can't we see every person served, in every home, right now?”"],
         ["Real-time analytics dashboard across every person served, in every location",
          "Guided, step-by-step workflows support every caregiver in the moment",
          "One centralised record per person, syncing instantly at the point of care",
          "24/7 pharmacy connectivity wherever care is delivered",
          "Smart medication storage adapted for home settings"],
         [("Deployed across more than 50% of U.S. states", None)],
         "Photo: caregiver arriving at a private residence"),
        ("who-we-serve/foster-care.html", "Foster Care",
         "A child's medication history shouldn't depend on a caseworker's memory.",
         "Every placement change is a handoff. Right now, it's also a gamble.",
         ["Information loss at placement transitions isn't bad luck — it's a design flaw. A predictable moment of risk can be engineered for.",
          "A child's medication history shouldn't be the most fragile thing they carry between homes."],
         ["Records that follow the child across placements",
          "Guided, simple workflows — foster parents aren't clinicians and shouldn't have to be",
          "Real-time visibility for the agency, without waiting on paper logs",
          "Documentation ready for state child welfare reporting and audits",
          "Supervised self-administration for youth building toward independence"],
         [],
         "Photo: foster parent and teenager at a kitchen table"),
        ("who-we-serve/state-directed.html", "State-Directed Programs",
         "Your most at-risk populations carry your most preventable costs.",
         "Every medication error avoided is a hospitalization, an ER visit and a claim that never happens.",
         ["Oversight is a rear-view mirror. By the time a violation is caught, the adverse drug event has already happened.",
          "Medication errors injure an estimated 1.5 million Americans each year; roughly 800,000 preventable drug-related injuries occur annually in long-term care settings alone.",
          "In partnership with the Massachusetts Executive Office of Health and Human Services, Impruvon's model projected $371M in savings over four years for approximately 25,000 individuals — roughly 1,800% ROI."],
         ["Enable every provider in your network with guided workflows",
          "Real-time, centralised oversight — enterprise dashboards and automated audit tooling",
          "Reduce fraud, waste and abuse exposure with a verifiable record of every administration",
          "Lower avoidable utilization — fewer hospitalizations, ER visits and transport costs",
          "Statewide deployment support: provider and pharmacy outreach, enrollment, training, legacy integration"],
         [("Impruvon currently serves as the state-directed eMAR in Massachusetts", None)],
         "Photo: state agency team reviewing network-level data"),
    ]
    for path, name, h1, intro, story, feats, proof, media in verticals:
        is_state = "state-directed" in path
        proof_block = []
        if proof:
            items = []
            for text, link in proof:
                items.append({"title": text, "text": "", "link": link} if link else {"title": text})
            proof_block = [{"t": "cards", "h": "Proven results", "cols": 3, "items": items}]
        page(path, name, h1, kicker="Who we serve", intro=intro,
             crumbs=[("Home", "index.html"), ("Who we serve", "who-we-serve/index.html"), (name, None)],
             notes=["Vertical page = the strongest conversion surface: long-tail search intent plus the compliance context specific to this setting.",
                    "Structure per Stage 5: answer-first opening, the cost of the status quo, what the platform does here, proof with a source, one CTA."],
             blocks=[
                 {"t": "text", "h": "Why the status quo costs more than it looks", "p": story},
                 {"t": "media", "kind": "photo", "label": media},
                 {"t": "list", "h": "Built for the way you actually work", "items": feats},
             ] + proof_block + [
                 {"t": "links", "h": "Related", "items": [
                     ("eMAR+", "platform/emar.html"), ("MedBox", "platform/medbox.html"),
                     ("Compare platforms", "compare/index.html"), ("Trust & compliance", "trust/index.html")]},
                 STATE_CTA if is_state else DEMO_CTA,
             ])

    # ---------- COMPARE / PRICING / TRUST
    page("compare/index.html", "Compare", "Not another everything-platform. The medication-safety specialist.",
         kicker="Compare",
         intro="All-in-one EHRs treat medication as one module and stay software-only. Impruvon is purpose-built for I/DD residential care, specialises completely in medication safety, and is the only platform with hardware.",
         crumbs=[("Home", "index.html"), ("Compare", None)],
         notes=["Team decision: ONE comparison page with a table of all competitors, plus teaser blocks on product and vertical pages — not a page per competitor.",
                "Highest-intent traffic in the funnel ('Therap alternatives'). It has to be honest to be credible: state where competitors are genuinely strong."],
         blocks=[
             {"t": "table", "h": "How Impruvon compares", "head": ["", "Impruvon", "Therap", "iCareManager", "eVero", "ECP"],
              "rows": [
                  ["Purpose-built for I/DD residential", "Yes", "Partly", "Partly", "Partly", "No"],
                  ["Medication safety as the specialty", "Yes", "One module", "One module", "One module", "One module"],
                  ["Smart medication hardware", "MedBox", "None", "None", "None", "None"],
                  ["Guided med pass for non-clinical staff", "Yes", "Limited", "Limited", "Limited", "Limited"],
                  ["Automated HRST integration", "Yes", "No", "No", "No", "No"],
                  ["Pharmacy partners", "75+", "—", "—", "—", "—"],
                  ["State-directed deployment", "Massachusetts", "—", "—", "—", "—"],
              ]},
             {"t": "text", "h": "Where the difference actually shows up",
              "p": ["Competitors are everything-platforms: medication is one module among many. That is a reasonable choice if your problem is 'we need one system for everything'.",
                    "It is the wrong choice if your problem is 'a med error can seriously harm someone who can't advocate for themselves, and my staff are non-clinical and stretched thin'.",
                    "PENDING: legal review of competitor claims before publishing. Every cell needs a dated source."]},
             DEMO_CTA,
         ])

    page("pricing/index.html", "Pricing", "What Impruvon costs, and what it replaces.",
         kicker="Pricing",
         intro="A pricing page without numbers: how the model works, what drives it, and what you should have ready for a quote.",
         crumbs=[("Home", "index.html"), ("Pricing", None)],
         notes=["⚠️ TO CONFIRM WITH CLIENT: the client's original structure had no pricing page. Our recommendation is to keep this page but publish no numbers.",
                "Reason: buyers search 'eMAR pricing'. With no page you lose that traffic to competitors and to review sites. With a no-numbers page you capture it and route it to Book a demo.",
                "If the client says no, delete this page and redirect /pricing to Book a demo."],
         blocks=[
             {"t": "list", "h": "How pricing works", "items": [
                 "Priced per individual served, per month — not per staff seat, so turnover doesn't change your bill",
                 "MedBox hardware priced separately, per home",
                 "Implementation, onboarding and training included with a named partner",
                 "Pharmacy and EHR integrations included — no charge per connection",
                 "State-directed programs: low or no cost to the provider (PENDING: confirm)"]},
             {"t": "list", "h": "What to have ready for an accurate quote", "items": [
                 "Number of individuals served and number of homes/sites",
                 "Which states you operate in",
                 "Your current pharmacy partner(s) and EHR",
                 "Whether you want MedBox in all homes or a subset"]},
             {"t": "faq", "h": "Pricing questions", "items": [
                 ("Why aren't prices listed?", "Because the honest number depends on your size, states and how much hardware you deploy. We'd rather give you a real figure in fifteen minutes than a misleading one here."),
                 ("Is there a setup fee?", "PENDING — confirm with client."),
                 ("What contract length?", "PENDING — confirm with client.")]},
             DEMO_CTA,
         ])

    page("trust/index.html", "Trust & compliance", "Built to pass the procurement review.",
         kicker="Trust",
         intro="The questions your IT, compliance and legal teams ask — answered before they ask them.",
         crumbs=[("Home", "index.html"), ("Trust", None)],
         notes=["Added page — it was missing from the client's original structure. Competitors flood their sites with SOC 2 / HIPAA / HITRUST badges and state contracts; without this page Impruvon reads small.",
                "This closes the Stage 3 proof gap and is the page a state administrator or an ED's IT lead will actually open."],
         blocks=[
             {"t": "cards", "h": "Security & compliance", "cols": 2, "items": [
                 {"title": "SOC 2", "text": "Compliant and ready for immediate deployment. PENDING: confirm Type I vs Type II and attach the report request flow."},
                 {"title": "HIPAA", "text": "PHI handled under HIPAA. PENDING: confirm BAA process."},
                 {"title": "Single sign-on", "text": "Automated SSO, role-based permissions and real-time access requests."},
                 {"title": "Data residency & retention", "text": "PENDING: confirm hosting, region and retention policy."},
             ]},
             {"t": "list", "h": "Regulatory standing", "items": [
                 "State-directed eMAR in Massachusetts",
                 "Deployed across more than 50% of U.S. states",
                 "Meets service-provider-specific regulatory requirements, including state-mandated HRST",
                 "Trusted by providers, state agencies and pharmacies across 20+ states"]},
             {"t": "list", "h": "Implementation & support", "items": [
                 "Named implementation partner for onboarding and training",
                 "Provider and pharmacy outreach and enrollment",
                 "Legacy system migration",
                 "In-person and virtual customer support"]},
             DEMO_CTA,
         ])

    # ---------- RESOURCES
    page("resources/index.html", "Resource Center", "Resource Center",
         kicker="Resources",
         intro="Three tracks, three different readers. Caregivers get how-to help and stories. Administrators get audit and compliance guides. Buyers get customer results.",
         crumbs=[("Home", "index.html"), ("Resources", None)],
         notes=["This replaces a generic 'Blog'. Same articles — organised by who is reading, not by publication date.",
                "Why it matters: a caregiver looking up 'what do I do when a resident refuses a med' and a DoN looking up 'medication audit checklist' are different people with different next steps. One blog feed serves neither well."],
         blocks=[
             {"t": "cards", "h": "Three tracks", "cols": 3, "items": [
                 {"title": "Supporting DSPs", "text": "How-to guides, short videos and real stories for the people giving the meds — DSPs, foster parents and home health aides.", "link": "resources/caregivers/index.html", "cta": "Open the track"},
                 {"title": "Guides for administrators", "text": "Audit preparation, compliance by state, staffing and the cost of medication errors — for DoNs, QIDPs and executive directors.", "link": "resources/guides/index.html", "cta": "Open the track"},
                 {"title": "Customer stories", "text": "What changed at real organisations, with numbers and names.", "link": "resources/customers/index.html", "cta": "Open the track"},
             ]},
             {"t": "text", "h": "Also planned", "p": [
                 "Glossary (eMAR, HRST, MedBox, HCBS, five rights) — Wave 2. Reports and webinars — Wave 2. Events — Wave 3."]},
             DEMO_CTA,
         ])

    page("resources/caregivers/index.html", "Supporting DSPs", "Supporting DSPs and caregivers",
         kicker="Resources",
         intro="Straight answers for the people who actually give the medications. No jargon, no login, no cost.",
         crumbs=[("Home", "index.html"), ("Resources", "resources/index.html"), ("Supporting DSPs", None)],
         notes=["This hub replaces the blog for caregiver-facing content. The URL folder is /caregivers/ because foster parents and home health aides are not DSPs — but the H1 speaks to DSPs, who are the primary audience.",
                "Strategic double duty (Stage 2): a DSP is not a buyer, but this hub is proof to the decision-maker that Impruvon helps their staff succeed — which answers the biggest hidden objection, 'will non-medical staff actually use it?'",
                "Primary CTA here is NOT 'Book a demo' — a DSP can't buy. It's 'Send this to your administrator' plus a subscribe option. The demo CTA stays in the footer only.",
                "⚠️ Stories about people served involve a vulnerable population: written consent, first names or pseudonyms, separate photo release, HIPAA review before publishing."],
         blocks=[
             {"t": "cards", "h": "How-to guides", "cols": 3, "items": [
                 {"title": "What are the five rights of medication administration?", "text": "The check behind every safe pass.", "link": "resources/caregivers/five-rights.html", "cta": "Read"},
                 {"title": "A resident refused their medication — what now?", "text": "What to do, and what to document."},
                 {"title": "How to count narcotics at shift change", "text": "The count, the discrepancy, the escalation."},
                 {"title": "Documenting a PRN and whether it worked", "text": "Reason, dose, effect — and why the effect matters."},
                 {"title": "Your first med pass: what to expect", "text": "For new hires, start to finish."},
                 {"title": "Preparing for a medication audit, shift by shift", "text": "What an auditor looks at, in plain terms."},
             ]},
             {"t": "cards", "h": "User stories", "cols": 3, "items": [
                 {"title": "“My first week on the floor”", "text": "A new DSP on learning the pass without a clinical background."},
                 {"title": "“I take my own meds now”", "text": "A person served who moved to supervised self-administration."},
                 {"title": "“We stopped keeping a binder”", "text": "One house's move from paper MAR to a live record."},
             ]},
             {"t": "media", "kind": "video", "label": "Short video tutorials (60–90s) — each with an on-page transcript so AI search can cite it"},
             {"t": "cta", "h": "Working somewhere that still runs on paper?",
              "p": "Send this to whoever decides. It takes one link.",
              "buttons": [("Send this to your administrator", "about/contact.html"), ("Get new guides by email", "about/contact.html")]},
         ])

    page("resources/caregivers/five-rights.html", "Five rights", "What are the five rights of medication administration?",
         kicker="Guide for caregivers",
         intro="Right person, right medication, right dose, right route, right time. Check all five, every single pass — and here is what each one actually means when you are standing in front of someone.",
         crumbs=[("Home", "index.html"), ("Resources", "resources/index.html"),
                 ("Supporting DSPs", "resources/caregivers/index.html"), ("Five rights", None)],
         notes=["Article template. Structure per Stage 5: answer-first opening, H2s written as questions, a real FAQ in HTML, 3–5 internal links, one CTA, an updated date and JSON-LD.",
                "This article targets the TOFU term 'five rights of medication administration' from the semantic core."],
         blocks=[
             {"t": "text", "h": "Right person", "p": ["Confirm who you are giving it to before anything else. A photo in the record, a wristband or a barcode is safer than recognition — especially on a first shift or in a house you are covering."]},
             {"t": "text", "h": "Right medication", "p": ["Read the label against the record, not against memory. Look-alike and sound-alike names are the most common source of the wrong drug reaching the right person."]},
             {"t": "text", "h": "Right dose", "p": ["Check the number and the unit. Half a tablet and one tablet are different doses; 50 mg and 500 mg are different medications in practice."]},
             {"t": "text", "h": "Right route", "p": ["By mouth, topical, injection, inhaled — the route is part of the order. If the person cannot take it the ordered way, that is a call to the nurse, not a decision to make on your own."]},
             {"t": "text", "h": "Right time", "p": ["Inside the window the order allows. Early is not safer than late; both are documented, and both matter for medications where timing drives effectiveness."]},
             {"t": "text", "h": "What happens when the system checks with you", "p": ["A guided med pass walks these five in order and will not let the record close until each one is confirmed. With MedBox, only the correct drawer opens at the correct time, so the check happens physically as well as on screen."]},
             {"t": "faq", "items": [
                 ("What if I realise afterwards that one of the five was wrong?", "Report it immediately, follow your agency's incident procedure and document what happened. A reported error is a fixable error."),
                 ("Are there more than five rights?", "Many agencies teach additional checks — right documentation, right reason, right response. The five are the core; follow your own agency's policy."),
             ]},
             {"t": "links", "h": "Related", "items": [
                 ("A resident refused their medication — what now?", "resources/caregivers/index.html"),
                 ("How eMAR+ guides each pass", "platform/emar.html"),
                 ("How MedBox enforces the check physically", "platform/medbox.html"),
                 ("All caregiver guides", "resources/caregivers/index.html")]},
             {"t": "cta", "h": "Still running this on paper?",
              "p": "Send this guide to whoever decides at your agency.",
              "buttons": [("Send to your administrator", "about/contact.html"), ("How Impruvon works", "platform/index.html")]},
         ])

    page("resources/guides/index.html", "Guides for administrators", "Guides for administrators",
         kicker="Resources",
         intro="Audit preparation, compliance, staffing and cost — for the people who answer to the state and to the board.",
         crumbs=[("Home", "index.html"), ("Resources", "resources/index.html"), ("Guides", None)],
         notes=["This is the half of the old blog that a DSP hub cannot absorb: these articles target the champion (DoN, QIDP) and the executive director.",
                "Primary CTA here IS Book a demo — this reader can start a purchase."],
         blocks=[
             {"t": "cards", "h": "Guides", "cols": 3, "items": [
                 {"title": "Medication audit checklist", "text": "What auditors ask for, and how to have it ready.", "link": "resources/guides/medication-audit-checklist.html", "cta": "Read"},
                 {"title": "Paper MAR vs eMAR", "text": "What each can and cannot prove."},
                 {"title": "How to reduce medication errors in group homes", "text": "The interventions that actually move the number."},
                 {"title": "What DSP turnover really costs", "text": "Training, agency cover, risk — in dollars."},
                 {"title": "Barcode medication administration, explained", "text": "How it works and where it fails."},
                 {"title": "Choosing an eMAR for I/DD providers", "text": "The questions to ask every vendor."},
             ]},
             DEMO_CTA,
         ])

    page("resources/guides/medication-audit-checklist.html", "Medication audit checklist",
         "How do you prepare for a medication audit?",
         kicker="Guide for administrators",
         intro="Stop preparing. Stay ready. Here is what an auditor asks for, what a paper MAR can and cannot prove, and how to have every answer without reconstructing weeks of records.",
         crumbs=[("Home", "index.html"), ("Resources", "resources/index.html"),
                 ("Guides", "resources/guides/index.html"), ("Audit checklist", None)],
         notes=["Article template for the administrator track — same structure as the caregiver article, different reader and different CTA."],
         blocks=[
             {"t": "list", "h": "What an auditor will ask for", "items": [
                 "Proof that each ordered dose was given, refused or held — with a time",
                 "Who administered it, and that they were authorised to",
                 "Narcotic counts and any discrepancies, with resolution",
                 "PRN administrations with a documented reason and effect",
                 "Current orders matching what the pharmacy actually dispensed",
                 "Incident reports and the corrective action that followed"]},
             {"t": "text", "h": "Why paper cannot answer some of these",
              "p": ["Initials in a box prove someone wrote in the box. They do not prove when, or that the five rights were checked, or that the order on file matched the pharmacy's.",
                    "A gap in a paper MAR is discovered at the audit — weeks after the moment when it could have been fixed."]},
             {"t": "list", "h": "The shift-level habits that make audits boring", "items": [
                 "Document at the point of care, never at the end of the shift",
                 "Escalate a discrepancy the same shift it appears",
                 "Reconcile pharmacy orders weekly, not monthly",
                 "Run your own mock audit quarterly, on a random week"]},
             {"t": "faq", "items": [
                 ("How far back will an audit look?", "It varies by state and programme. Assume the current certification period and keep the full period retrievable."),
                 ("What is the most common citation?", "Documentation gaps — a dose with no record — rather than a wrong drug reaching a person.")]},
             {"t": "links", "h": "Related", "items": [
                 ("How eMAR+ produces 1-click regulatory reports", "platform/emar.html"),
                 ("HRST automation", "platform/hrst-automation.html"),
                 ("Trust & compliance", "trust/index.html"),
                 ("All administrator guides", "resources/guides/index.html")]},
             DEMO_CTA,
         ])

    page("resources/customers/index.html", "Customer stories", "Customer stories",
         kicker="Resources",
         intro="What changed at real organisations — with numbers, names and a source.",
         crumbs=[("Home", "index.html"), ("Resources", "resources/index.html"), ("Customer stories", None)],
         notes=["Organisation-level proof for buyers. Distinct from 'user stories' in the caregiver hub, which are person-level and human.",
                "Case studies also serve as proof blocks on vertical pages — write them once, surface them in several places."],
         blocks=[
             {"t": "cards", "h": "Stories", "cols": 3, "items": [
                 {"title": "Charles Lea Center", "text": "23,000+ medications administered with zero errors.", "link": "resources/customers/charles-lea.html", "cta": "Read the story"},
                 {"title": "Vista Care", "text": "75% reduction in medication errors across 18 sites in 6 states."},
                 {"title": "Coastal Autism Academy", "text": "Documentation and medication errors down after implementation."},
                 {"title": "Massachusetts EOHHS", "text": "$371M projected four-year savings; ~1,800% ROI in the state model.", "link": "who-we-serve/state-directed.html", "cta": "See the state model"},
             ]},
             DEMO_CTA,
         ])

    page("resources/customers/charles-lea.html", "Charles Lea Center", "23,000+ medications administered. Zero errors.",
         kicker="Customer story",
         intro="How the Charles Lea Center moved from paper to a live medication record — and what it changed for the people they support.",
         crumbs=[("Home", "index.html"), ("Resources", "resources/index.html"),
                 ("Customer stories", "resources/customers/index.html"), ("Charles Lea Center", None)],
         notes=["Case study template: situation, what changed, results with a source, quote, and the CTA.",
                "⚠️ PENDING: the Shannon Childress quote has no published source link. Confirm clearance for external use before publishing, or replace with the Coastal Autism Academy quote, which is sourced."],
         blocks=[
             {"t": "stats", "h": "Results", "items": [
                 {"v": "23,000+", "l": "Medications administered"},
                 {"v": "0", "l": "Errors"},
                 {"v": "20–25 min", "l": "Saved per resident, per pass"},
             ], "src": "Source: impruvon.com/products — Charles Lea Center case study."},
             {"t": "media", "kind": "photo", "label": "Photo: Charles Lea Center team member with a person they support"},
             {"t": "text", "h": "The situation", "p": ["PENDING: full narrative from the client — organisation size, states, what they ran before, what the audit and staffing picture looked like."]},
             {"t": "text", "h": "What changed", "p": ["Guided med passes replaced paper MAR binders. MedBox took the five rights out of memory and into hardware. Pharmacy orders arrived in the platform instead of on a fax."]},
             {"t": "quote", "text": "Reliance on medication administration shouldn't keep someone from living by themselves. Impruvon was really eye-opening; if someone could manage meds independently, it was a no-brainer.",
              "by": "Shannon Childress — Chief Program Officer, Charles Lea Center (⚠ clearance pending)"},
             {"t": "links", "h": "Related", "items": [
                 ("I/DD & Residential", "who-we-serve/idd-residential.html"),
                 ("MedBox", "platform/medbox.html"),
                 ("All customer stories", "resources/customers/index.html")]},
             DEMO_CTA,
         ])

    # ---------- ABOUT
    page("about/index.html", "About", "About Impruvon",
         kicker="About", intro="Who we are, what we committed to, and how to reach us.",
         crumbs=[("Home", "index.html"), ("About", None)],
         notes=["Mission → solutions is a deliberate bridge: 'Our commitment' links straight into Who we serve.",
                "Contact is kept separate from Book a demo so the conversion path stays clean."],
         blocks=[{"t": "cards", "h": "", "cols": 2, "items": [
             {"title": "Our story", "text": "Why Impruvon exists.", "link": "about/our-story.html"},
             {"title": "Our commitment", "text": "Four commitments, one platform.", "link": "about/our-commitment.html"},
             {"title": "Careers", "text": "Open roles and how we work.", "link": "about/careers.html"},
             {"title": "Contact", "text": "Support, press, partnerships and general enquiries.", "link": "about/contact.html"},
         ]}, DEMO_CTA])

    page("about/our-story.html", "Our story", "Every preventable error started with a system that wasn't built to prevent it.",
         kicker="About", intro="PENDING: founder narrative awaiting CEO approval. Placeholder copy only.",
         crumbs=[("Home", "index.html"), ("About", "about/index.html"), ("Our story", None)],
         notes=["⚠️ The founder's personal story is flagged PENDING in the copy draft. Nothing personal is published here until the client clears it.",
                "Stage 5 asks this page to name real people with LinkedIn profiles and the legal entity — that is what makes a smaller vendor credible to a risk-averse buyer."],
         blocks=[
             {"t": "text", "h": "", "p": ["PENDING: approved founder narrative.",
                                          "PENDING: leadership team — names, roles, photos, LinkedIn.",
                                          "PENDING: legal entity name, founded 2020, US-based, headcount."]},
             {"t": "media", "kind": "photo", "label": "Photo: leadership team — real people, named"},
             DEMO_CTA])

    page("about/our-commitment.html", "Our commitment", "From medication management to clinical workflow — precision you can count on.",
         kicker="About",
         intro="A caregiver's first shift should be exactly as safe as their thousandth. Impruvon was designed for exactly that: putting the safeguard in the workflow, not in the person.",
         crumbs=[("Home", "index.html"), ("About", "about/index.html"), ("Our commitment", None)],
         notes=["This page is the bridge from mission to product. It ends by routing to Who we serve."],
         blocks=[
             {"t": "list", "h": "Four commitments, one platform", "items": [
                 "Simplify every step — medication management should work the way your care teams work",
                 "Gain audit peace-of-mind — compliance built into the workflow, not bolted on",
                 "Connect every touchpoint — great care doesn't happen in silos, and your platform shouldn't either",
                 "Empower every person — build confidence and resilience for individuals and the teams who support them"]},
             {"t": "stats", "h": "Results at a glance", "items": [
                 {"v": "48%", "l": "Reduction in medication errors"},
                 {"v": "39%", "l": "Improvement in compliance rates"},
                 {"v": "50,000+", "l": "Medication errors eliminated to date"},
                 {"v": "1,800%", "l": "ROI in the MA state-directed model"},
             ], "src": "⚠ PENDING: figures are sourced to an I/DD-specific elevator pitch. Confirm scope and external-use clearance before publishing."},
             {"t": "cta", "h": "See how we serve your organisation.", "p": "",
              "buttons": [("Who we serve", "who-we-serve/index.html"), ("Book a demo", DEMO)]}])

    page("about/careers.html", "Careers", "You can do more than provide care. You can redesign how it's delivered.",
         kicker="About",
         intro="Every workflow we build protects thousands of people who will never know our names.",
         crumbs=[("Home", "index.html"), ("About", "about/index.html"), ("Careers", None)],
         notes=["⚠️ PENDING: no employee testimonials, benefits or culture content existed in the source materials. Recommend a short session with HR before this goes live. Values still to be added."],
         blocks=[
             {"t": "list", "h": "How we work", "items": [
                 "We simplify every workflow — including our own",
                 "We ensure audit readiness — “good enough” isn't a standard we build to",
                 "We connect every touchpoint — across teams, not just across the product",
                 "We empower every person — our co-workers included"]},
             {"t": "media", "kind": "feed", "label": "Dynamic careers / ATS feed goes here"},
             {"t": "cta", "h": "Open roles", "p": "", "buttons": [("View open positions", "about/careers.html")]}])

    page("about/contact.html", "Contact", "Let's talk.",
         kicker="About", intro="Tell us what you need, and we'll get you to the right team.",
         crumbs=[("Home", "index.html"), ("About", "about/index.html"), ("Contact", None)],
         notes=["Four routes so the form can be routed to the right inbox and so Book a demo stays a separate, clean conversion.",
                "⚠️ PENDING: physical address, phone number and dedicated support/press email addresses are required before this page can go live."],
         blocks=[
             {"t": "cards", "h": "Where should this go?", "cols": 2, "items": [
                 {"title": "Book a demo", "text": "See the platform in action.", "link": DEMO},
                 {"title": "Customer support", "text": "Get help with your Impruvon account."},
                 {"title": "Press & media", "text": "Media enquiries and press resources."},
                 {"title": "General enquiry", "text": "Everything else."},
             ]},
             {"t": "list", "h": "Contact form fields", "items": [
                 "Name", "Organisation", "Role", "State / region", "Enquiry type", "Message"]},
             {"t": "text", "h": "Details", "p": ["PENDING: address · phone · support@ · press@"]}])

    # ---------- CONVERSION + UTILITY
    page(DEMO, "Book a demo", "See it on a real med pass.",
         kicker="Book a demo",
         intro="Bring your own workflow — and the questions your auditors ask. Fifteen minutes with someone who knows residential care.",
         crumbs=[("Home", "index.html"), ("Book a demo", None)],
         notes=["The single conversion point of the whole site. Every page links here.",
                "Form fields exist to qualify and to route: organisation type and states decide whether this is a provider deal or a state-directed conversation.",
                "State-directed traffic can land here too — the 'Request a state briefing' CTA points to this page with a pre-selected enquiry type."],
         blocks=[
             {"t": "list", "h": "Form fields", "items": [
                 "Name · work email · phone",
                 "Organisation and role",
                 "Type: provider / state agency or MCO / pharmacy / other",
                 "Setting: I/DD & residential · behavioral & mental health · home health · foster care · state-directed",
                 "Number of individuals served · number of homes or sites",
                 "States you operate in",
                 "Current system: paper MAR / another eMAR (which one) / none",
                 "What you'd like to see"]},
             {"t": "list", "h": "What happens next", "items": [
                 "You get a calendar link immediately after submitting",
                 "A 15-minute call walking your own workflow, not a generic tour",
                 "A written follow-up with the answers to anything we couldn't confirm live"]},
             {"t": "links", "h": "Not ready yet?", "items": [
                 ("Compare Impruvon with what you have", "compare/index.html"),
                 ("Read Trust & compliance", "trust/index.html"),
                 ("Browse guides for administrators", "resources/guides/index.html")]}])

    page("login/index.html", "Log in", "Log in",
         kicker="Utility", intro="Existing customers sign in to the Impruvon application.",
         crumbs=[("Home", "index.html"), ("Log in", None)],
         notes=["Utility link only — points to the product application, not part of the marketing site. Shown here so the client can see where it sits in the header."],
         blocks=[{"t": "text", "h": "", "p": ["Redirects to the Impruvon application. Not designed as part of the marketing site."]}])

    # ---------- SITEMAP
    rows = []
    for label, target, kids in NAV:
        rows.append([label, "/" + target.replace("index.html", ""), "Hub" if kids else "Page"])
        for l, t in kids:
            rows.append(["— " + l, "/" + t.replace("index.html", ""), "Page"])
    rows.append(["Book a demo", "/book-a-demo/", "Conversion"])
    rows.append(["Log in", "/login/", "Utility"])
    page("sitemap.html", "Sitemap", "Sitemap and page logic",
         kicker="Prototype",
         intro="Every page in this prototype, what it is for, and where it sends the visitor next.",
         notes=["Wave 1 (release): Home · eMAR+ · MedBox · Integrations · 5 verticals · Compare · Pricing · Trust · About/Contact · Resources · Book a demo.",
                "Wave 2 (month 1): glossary, HTML case studies, per-tool integration pages, use-case pages, first caregiver and administrator articles.",
                "Wave 3: geo pages, medication-error cost calculator, original research, changelog.",
                "Final URLs lock after Google Search Console review, so current ranking pages are protected during the migration."],
         blocks=[
             {"t": "table", "h": "All pages", "head": ["Page", "URL", "Type"], "rows": rows},
             {"t": "text", "h": "Conversion logic", "p": [
                 "One primary conversion for the whole site: Book a demo. Every product, vertical, compare, pricing and trust page ends with it.",
                 "State agencies get a second door: Request a state briefing, which routes to the same form with a different enquiry type.",
                 "Caregiver pages deliberately do not push the demo — that reader cannot buy. They push 'Send this to your administrator' instead.",
                 "Contact is separate from Book a demo so support and press traffic never pollutes the sales pipeline."]},
             {"t": "text", "h": "What still needs the client", "p": [
                 "Pricing page: keep it (no numbers) or drop it — decision needed.",
                 "SOC 2 type, HIPAA BAA process, data residency and retention.",
                 "Clearance for the Shannon Childress quote, and for the Results-at-a-Glance figures.",
                 "Founder story and leadership names for About.",
                 "Address, phone and support/press email addresses.",
                 "Whether Missouri can be claimed alongside Massachusetts for state-directed."]},
         ])


README = """# Impruvon — website structure prototype

A clickable, link-complete prototype of the Impruvon website. **Wireframe only — no visual
design.** Its job is to let the client walk the whole site, see every page, and understand
where each button leads and why.

- Every page is real and linked. Nothing is a dead end.
- The **Show notes** button in the top bar reveals the reasoning behind each page:
  what it is for, who reads it, and what still needs a decision from the client.
- **Sitemap** in the top bar lists every page, the conversion logic, and the open questions.
- Items marked PENDING are waiting on the client (sources, clearances, contact details).

## Structure

Home · Platform (eMAR+, MedBox, Pharmacy, EHR, HRST) · Who we serve (5 verticals) ·
Compare · Pricing · Trust · Resource Center (Supporting DSPs, Guides, Customer stories) ·
About (Story, Commitment, Careers, Contact) · Book a demo · Log in · Sitemap

## Build

```bash
python3 build.py      # regenerates ./docs (served by GitHub Pages)
```

Content is sourced from the Impruvon Discovery Dossier (Stages 1–5) and the
Website Copy v1 draft. Prepared by Toggle.
"""


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    with open(os.path.join(OUT, "assets", "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS)
    with open(os.path.join(OUT, "assets", "proto.js"), "w", encoding="utf-8") as f:
        f.write(JS)
    with open(os.path.join(OUT, ".nojekyll"), "w") as f:
        f.write("")
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nDisallow: /\n")
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
        f.write(README)
    build_pages()
    paper_home.write(OUT, render_chrome_nav, render_chrome_foot, esc, DEMO)
    n = sum(len([x for x in fs if x.endswith(".html")]) for _, _, fs in os.walk(OUT))
    print(f"built {n} pages -> {OUT}")


if __name__ == "__main__":
    main()
