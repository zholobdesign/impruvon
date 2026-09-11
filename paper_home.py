"""Homepage — built from the client's 'IMPRUVON — Home Page Draft Copy' (Sept 2026).

Ten sections, in the client's order, with their wording. Section comments name the
heading used in their document so the two can be diffed line by line.
"""
import io, os

ASSET_V = ""  # set by build.py from the CSS hash

CHECK_SVG = ('<svg width="22" height="22" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
             '<path d="M4 12.5 L9.5 18 L20 6.5" fill="none" stroke="var(--color-accent)" '
             'stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')

# STAT BAR (below hero)
NUMBERS = [("1M+", "Medications administered"), ("50K+", "Medication errors eliminated"),
           ("25K+", "Nursing hours saved"), ("75K+", "Care hours saved"),
           ("75+", "Pharmacy partners")]

# SECTION: WHO WE SERVE — five cards, each linking to its Who We Serve page
AUDIENCE = [
    ("I/DD & Residential Providers",
     "Purpose-built for the demands of group homes, ICFs, and Home and Community-Based Services waiver programs.",
     "who-we-serve/idd-residential.html"),
    ("Behavioral & Mental Health",
     "Built for the documentation and complexity of psychiatric care.",
     "who-we-serve/behavioral-mental-health.html"),
    ("Home Health",
     "Real-time visibility into care delivered outside the facility.",
     "who-we-serve/home-health.html"),
    ("Foster Care",
     "Continuity of care for every child, at every placement change.",
     "who-we-serve/foster-care.html"),
    ("State-Directed Programs",
     "Prevention infrastructure for state agencies and health plans.",
     "who-we-serve/state-directed.html"),
]

# SECTION: PLATFORM AT A GLANCE — five capability cards, each linking to its Platform page
CAPABILITIES = [
    ("eMAR+",
     "Guided, smart med passes with in-app barcode scanning, PRN and narcotic tracking, treatments (eTAR), "
     "vitals, and 1-click regulatory reporting. Guidance before the error, not documentation after it.",
     "platform/emar.html"),
    ("MedBox",
     "Smart medication storage replacing key cabinets and paper pass logs: right medication, right person, "
     "right time — with support for supervised self-administration.",
     "platform/medbox.html"),
    ("Pharmacy Integration",
     "Continuous, 24/7 bidirectional data sync across 75+ pharmacy partners and your EHR eliminates "
     "double-documentation and accelerates care delivery.",
     "platform/pharmacy-integration.html"),
    ("HRST Automation",
     "The only platform fully integrating with state-mandated HRST requirements — complete inputs in a single "
     "click, with medications, diagnoses, and allergies pulled straight from the pharmacy.",
     "platform/hrst-automation.html"),
    ("EHR Integration",
     "Impruvon integrates directly with your existing EHRs, pharmacy management systems, and telehealth "
     "platforms, creating a single source of truth for your care team.",
     "platform/ehr-integration.html"),
]

# SECTION: RESULTS AT A GLANCE — WHAT OUR CUSTOMERS EXPERIENCE
RESULTS = [
    ("Avg. 48%", "Reduction in Medication Errors"),
    ("39%", "Improvement in Compliance Rates"),
    ("50,000+", "Medication Errors Eliminated to Date"),
]

# SECTION: FOUR COMMITMENTS, ONE PLATFORM
COMMITMENTS = [
    ("Simplify Every Workflow",
     "Medication management should work the way your care teams work, not the other way around."),
    ("Ensure Audit Readiness",
     "Meeting compliance and regulatory requirements should be built into your workflow, not an afterthought."),
    ("Connect Every Touchpoint",
     "Great care doesn't happen in silos. Your platform shouldn't either."),
    ("Empower Every Person",
     "Medication management should build confidence and resilience for individuals and the teams who support them."),
]

# SECTION: WHY IMPRUVON (differentiator strip)
WHY = [
    "Easy to learn and use for Direct Support Professionals and nurses alike — role-specific interfaces mean "
    "every team member sees exactly what they need",
    "Tailored solutions, seamless integrations, regulatory compliance per state",
    "No changes required to your existing pharmacies, medication packaging, or EHRs",
    "SOC2 and HIPAA compliant, ready for immediate deployment",
]

# SECTION: LATEST NEWS — not in the client's draft; added on the agency's instruction
NEWS = [
    ("CASE STUDY", "[Headline]", "[Date]", "resources/case-studies/index.html", "Read the case study"),
    ("BLOG", "[Article title]", "[Date]", "resources/blog/index.html", "Read"),
    ("EVENT", "[Event name]", "[Date] · [City, State]", "resources/events/index.html", "See the event"),
]

NOTES = [
    "Built from the client's “IMPRUVON — Home Page Draft Copy”. All ten sections follow their order and their "
    "wording; section comments in paper_home.py name the heading each block came from.",
    "Resolved in the client review of 8 Sept 2026: the Platform page took its own headline (“I/DD care is complex. Your tools shouldn't be.”) and the home page keeps this one.",
    "“Deployed across more than 50% of U.S. states” means customers in more than half the states, not state contracts — confirmed by the client. The wording still reads as though it meant contracts; “Customers in more than half of U.S. states” would say what they actually mean. “Zero Compromises” and “The only platform fully integrating with state-mandated HRST” are still unsourced.",
    "PENDING: the stat bar reads 25K+ nursing hours and 75K+ care hours. If care hours include nursing hours, "
    "the two figures overlap and should be one number or two clearly different ones.",
    "Resolved 9 Sept 2026: pharmacy and EHR are two pages again, /platform/pharmacy-integration and "
    "/platform/ehr-integration, and the two cards here point to one each.",
    "The Latest news band above the closing CTA is not in the client's draft — it was added so the Resources section has a route from the homepage. Every card in it is a placeholder; the band should not ship until at least three real items exist.",
    "Sections dropped against the previous build, because the client's draft does not include them: the homepage "
    "FAQ, the DSP/staff block, the two case-study cards, and the separate state-conversion band. "
    "State-Directed is now reached through its Who We Serve card.",
]


def write(out, nav, foot, esc, demo):
    b = ""  # homepage sits at the site root

    numbers = "".join(f'<div class="n"><b>{v}</b><span>{esc(l)}</span></div>' for v, l in NUMBERS)

    aud = "".join(
        f'<a class="acard" href="{b}{href}"><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
        f'<div class="go">See more &rarr;</div></a>' for t, d, href in AUDIENCE)

    caps = "".join(
        f'<a class="caprow" href="{b}{href}"><div class="cname">{esc(n)}</div>'
        f'<div class="cbody"><p>{esc(d)}</p><span class="go">See {esc(n)} &rarr;</span></div></a>'
        for n, d, href in CAPABILITIES)

    results = "".join(f'<div class="scard"><b>{esc(v)}</b><span>{esc(t)}</span></div>' for v, t in RESULTS)

    commits = "".join(f'<div class="softcard"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in COMMITMENTS)

    news = "".join(
        f'<a class="newscard" href="{b}{href}"><div><div class="ntag">{esc(tag)}</div>'
        f'<h3>{esc(title)}</h3><div class="nmeta">{esc(meta)}</div></div>'
        f'<div class="go">{esc(cta)} &rarr;</div></a>'
        for tag, title, meta, href, cta in NEWS)

    why = "".join(f'<div class="check">{CHECK_SVG}<span>{esc(t)}</span></div>' for t in WHY)

    notes = ('<aside class="notes" id="notes"><h4>Prototype notes</h4><ul>' +
             "".join(f"<li>{esc(n)}</li>" for n in NOTES) + "</ul></aside>")

    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Homepage — Impruvon (prototype)</title>
<link rel="stylesheet" href="assets/style.css?v={ASSET_V}">
</head><body>
<div class="annot">
  <span class="aurl">PROTOTYPE &middot; HOMEPAGE &middot; /</span>
  <span class="aleg"><span class="swatch"></span>Yellow = needs client confirmation before build</span>
  <span class="aleg"><button id="notesToggle" type="button">Show notes</button>
    <a href="sitemap.html">Sitemap</a></span>
</div>
{nav(b, "index.html")}
<main>
{notes}

<!-- HERO -->
<section class="hero wrap" id="s01">
  <div class="hero-copy">
    <h1>From Medication Management to Clinical Workflow &mdash; Precision You Can Count On.</h1>
    <p class="sub">Impruvon simplifies medication and treatment management for community-based care teams
      &mdash; with guided workflows that enhance compliance, reduce errors, and ensure safer, more efficient care.</p>
    <div class="btns">
      <a class="pill pill-lg" href="{b}{demo}">Book a Demo</a>
      <a class="pill pill-ghost" href="{b}platform/index.html">Explore the Platform</a>
    </div>
  </div>
  <div class="hero-visual">
    <div class="mbox">
      <div class="cap"><b>MEDBOX</b><span class="led"></span></div>
      <div class="slots">
        <div class="srow"><i class="slot"></i><i class="slot"></i><i class="slot on"></i><i class="slot"></i></div>
        <div class="srow"><i class="slot"></i><i class="slot"></i><i class="slot"></i><i class="slot"></i></div>
        <div class="srow"><i class="slot"></i><i class="slot"></i><i class="slot"></i><i class="slot"></i></div>
        <div class="srow"><i class="slot"></i><i class="slot"></i><i class="slot"></i><i class="slot"></i></div>
      </div>
      <div class="reader"><i class="rline"></i><i class="rtag"></i></div>
    </div>
    <div class="emar">
      <div class="top"><b>Morning pass</b><span>8:00 AM</span></div>
      <div class="rows">
        <div class="r"><i class="dot"></i><i class="bar" style="width:150px"></i></div>
        <div class="r"><i class="dot"></i><i class="bar" style="width:186px"></i></div>
        <div class="r"><i class="dot next"></i><i class="bar on" style="width:126px"></i></div>
      </div>
      <div class="scan"><i></i><span>Scan the barcode to confirm</span></div>
    </div>
  </div>
</section>

<!-- STAT BAR (below hero) -->
<section class="numbers wrap" id="s02">{numbers}</section>

<!-- SECTION: THE PROBLEM WE SOLVE -->
<section class="sec" id="s03"><div class="sec-inner stack-44">
  <h2 class="h2 h2-wide">Most platforms tell you what already happened. Impruvon is built to guide what happens next.</h2>
  <p class="lede lede-wide">Medication management is the one operational process that touches every resident,
    every caregiver, every shift, every day. When it runs on paper or on software built for nurses in hospitals,
    your organization absorbs the risk. Impruvon puts the safeguard in the workflow, not in the person, so a
    caregiver's first shift is exactly as safe as their thousandth.</p>
</div></section>

<!-- SECTION: WHO WE SERVE -->
<section class="sec sec-sunk" id="s04"><div class="sec-inner stack-44">
  <div class="sechead">
    <h2 class="h2">One Platform. Many Realities. Zero Compromises.</h2>
    <p class="lede">Purpose-built for residential and community-based care &mdash; not retrofitted from hospitals
      or skilled nursing &mdash; Impruvon makes the safe choice the automatic choice on every shift, for every
      member of your team, from day one. Deployed across more than 50% of U.S. states, purpose-built for the
      regulatory and staffing realities of each care setting we serve.</p>
  </div>
  <div class="grid g5">{aud}</div>
  <div><a class="pill" href="{b}who-we-serve/index.html">See How We Serve Your Organization</a></div>
</div></section>

<!-- SECTION: PLATFORM AT A GLANCE -->
<section class="sec" id="s05"><div class="sec-inner stack-44">
  <div class="sechead">
    <h2 class="h2 h2-wide">Everything Medication Management Touches. One Connected Ecosystem.</h2>
    <p class="lede lede-wide">Impruvon is a fully compliant eMAR platform that transforms medication
      administration from a manual compliance activity into a proactive safety and quality system &mdash; with
      no changes to the pharmacies, packaging, or EHR systems you already use.</p>
  </div>
  <div class="caplist">{caps}</div>
  <div><a class="pill" href="{b}platform/index.html">Explore the Full Platform</a></div>
</div></section>

<!-- SECTION: RESULTS AT A GLANCE — WHAT OUR CUSTOMERS EXPERIENCE -->
<section class="sec sec-sunk" id="s06"><div class="sec-inner stack-44">
  <h2 class="h2">Results at a glance &mdash; what our customers experience.</h2>
  <div class="grid g3 statcards3">{results}</div>
</div></section>

<!-- SECTION: FOUR COMMITMENTS, ONE PLATFORM -->
<section class="sec" id="s07"><div class="sec-inner stack-44">
  <h2 class="h2">Four commitments, one platform.</h2>
  <div class="grid g4">{commits}</div>
</div></section>

<!-- SECTION: PROOF / CASE STUDY CALLOUT -->
<section class="sec sec-sunk" id="s08"><div class="sec-inner stack-44">
  <div class="eyebrow-line">Voice of Customer</div>
  <div class="quote">
    <div class="bar"></div>
    <div><p>&ldquo;Our mission at Vista Care is simple: serve more people, better, while keeping them in our
      hearts and actions at all times. I'm incredibly proud of the partnership we've built with Impruvon and
      the results we've achieved together &hellip; This is what our best care values look like in action:
      pursuing Excellence, embracing Adaptation, strengthening Communication, and keeping the people we support
      at the center of every decision we make. Better systems. Better visibility. Better accountability. Better
      outcomes. Continuous improvement is a responsibility we owe to the people we support, and I'm proud of
      what we've accomplished together.&rdquo;</p>
      <cite>Liz Olive, CEO of Vista Care, Inc.</cite></div>
  </div>
</div></section>

<!-- SECTION: WHY IMPRUVON (differentiator strip) -->
<section class="sec" id="s09"><div class="sec-inner stack-44">
  <h2 class="h2 h2-wide">Built for states, health plans and Home and Community-Based Services providers.</h2>
  <div class="checks">{why}</div>
</div></section>

<!-- SECTION: LATEST NEWS (added by Toggle, not in the client's draft) -->
<section class="sec sec-sunk" id="s10"><div class="sec-inner stack-44">
  <div class="newshead">
    <h2 class="h2">Latest from Impruvon.</h2>
    <a class="go" href="{b}resources/index.html">All resources &rarr;</a>
  </div>
  <div class="newsgrid">{news}</div>
  <div class="newsflag">PLACEHOLDER CARDS &middot; NOT IN THE CLIENT&rsquo;S HOME PAGE DRAFT &middot; DO NOT SHIP THIS BAND UNTIL THERE ARE THREE REAL ITEMS</div>
</div></section>

<!-- CLOSING CTA BAND -->
<section class="sec sec-deep" id="s11"><div class="sec-inner closing closing-ondeep">
  <h2>Eliminate the Guesswork of Medication Management.</h2>
  <div class="line"><span>See how Impruvon makes safe, compliant, connected care achievable for your team
    &mdash; from the first med pass to the next audit.</span></div>
  <div class="btns">
    <a class="pill pill-lg" href="{b}{demo}">Book a Demo</a>
    <a class="pill pill-ghost pill-ondeep" href="{b}about/contact.html">Contact Us</a>
  </div>
</div></section>

</main>
{foot(b)}
<script src="assets/proto.js?v={ASSET_V}"></script>
</body></html>"""

    io.open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(doc)
