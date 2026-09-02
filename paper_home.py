"""Exact transcription of the 'Impruvon — Homepage prototype' artboard."""
import io, os

NUMBERS = [("1M+", "Medications administered"), ("50K+", "Medication errors eliminated"),
           ("25K+", "Nursing hours saved"), ("75K+", "DSP hours saved"),
           ("75+", "Pharmacy partners")]

PAIN = [
    ("More training on paper.",
     "A paper MAR can't catch an error before it happens."),
    ("Or an eMAR retrofitted from acute care.",
     "It assumes a workforce you don't have, so your DSPs work around it, and the risk moves back onto your best people."),
    ("Either way, the cost compounds quietly.",
     "The failed audit. The citation. The med error that becomes an incident report. The DSP who burns out and walks, taking months of training with them."),
]

PRODUCTS = [
    ("eMAR+", "Simplify every workflow.",
     "Guided smart med pass, in-app barcode scanning, PRN and narcotic tracking, with treatments, vitals and clinical notes in the same record.",
     "See eMAR+", "platform/emar.html"),
    ("MedBox", "Empower every person.",
     "Smart medication storage with precise, individual-level dispensing. Access to only the correct medications, at the correct times.",
     "See MedBox", "platform/medbox.html"),
    ("Integrations", "Connect every touchpoint.",
     "24/7 bidirectional pharmacy integration and your existing EHR. No changes to pharmacy or medication packaging needed.",
     "See integrations", "platform/pharmacy-integration.html"),
    ("HRST Automation", "Ensure audit readiness.",
     "Complete all of your HRST inputs with a single click, pulled from the pharmacy filling your medications.",
     "See HRST automation", "platform/hrst-automation.html"),
]

AUDIENCE = [
    ("I/DD & Residential Providers", "Purpose-built for the demands of group homes, ICFs and HCBS waiver programs.", "who-we-serve/idd-residential.html"),
    ("Behavioral & Mental Health", "Built for the documentation and complexity of psychiatric care.", "who-we-serve/behavioral-mental-health.html"),
    ("Home Health", "Real-time visibility into care delivered outside the facility.", "who-we-serve/home-health.html"),
    ("Foster Care", "Continuity of care for every child, at every placement change.", "who-we-serve/foster-care.html"),
]

REASONS = [
    ("01", "Smart medication storage, not just software.",
     "Smart MedBoxes go beyond basic access control, replacing key cabinets, unsecured closets and paper pass logs with precise, individual-level dispensing."),
    ("02", "Built for community-based care, not adapted from hospital software.",
     "Built from the ground up for the workflow rhythms, staffing and budget constraints, and regulatory requirements of residential and community-based care."),
    ("03", "The safeguard is in the workflow, not in the person.",
     "One workflow makes the safe choice the automatic choice, for every member of your team, from day one."),
    ("04", "Nothing you already run has to change.",
     "Complete visibility and control without changing the pharmacies, packaging or EHR systems you already use."),
]

STAFF = [
    ("Guided smart med pass", "Step-by-step prompts walk any caregiver through every administration."),
    ("In-app barcode scanning", "No external scanners required."),
    ("Role-specific interfaces", "Every team member sees exactly what they need."),
    ("Works on the devices you have", "Android, iOS and web browsers, with automated single sign-on."),
]

FAQ = [
    ("Is Impruvon just an eMAR?",
     "Most eMARs digitize the paper MAR and stop there. eMAR+ pairs guided medication management with the clinical workflows that surround it, and MedBox adds physical medication storage no other platform has."),
    ("Will non-medical staff actually use it?",
     "Easy to learn and use for DSPs and nurses alike. Step-by-step prompts walk any caregiver through every administration, and role-specific interfaces mean every team member sees exactly what they need."),
    ("Do we have to replace our EHR?",
     "No. Impruvon connects with your existing EHR systems, eliminating the duplicate documentation and multi-system logins that burden care teams."),
    ("Do we have to change pharmacies or packaging?",
     "No changes to pharmacy or medication packaging needed."),
]

NOTES = [
    "Transcribed from the Paper artboard “Impruvon — Homepage prototype”. Section numbering (01–10) matches the artboard.",
    "One conversion for the whole site: Book a demo. State-directed traffic gets a second door in section 05.",
    "Yellow blocks are the open questions: the list of states for the FAQ, and the demo length in the closing section.",
]


def write(out, nav, foot, esc, demo):
    b = ""  # homepage sits at the site root

    numbers = "".join(f'<div class="n"><b>{v}</b><span>{esc(l)}</span></div>' for v, l in NUMBERS)
    pain = "".join(f'<div class="pcard"><div class="rule"></div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
                   for t, d in PAIN)
    prods = "".join(
        f'<a class="dcard" href="{b}{href}"><h3>{esc(n)}</h3><div class="kick">{esc(k)}</div>'
        f'<p>{esc(d)}</p><div class="go">{esc(cta)} &rarr;</div></a>'
        for n, k, d, cta, href in PRODUCTS)
    aud = "".join(
        f'<a class="acard" href="{b}{href}"><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
        f'<div class="go">See more &rarr;</div></a>' for t, d, href in AUDIENCE)
    reasons = "".join(f'<div class="ncard"><div class="num">{n}</div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
                      for n, t, d in REASONS)
    staff = "".join(f'<div class="fcard"><div class="ico"></div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
                    for t, d in STAFF)
    faq = "".join(f'<div class="faqrow"><div class="q">{esc(q)}</div><div class="a">{esc(a)}</div></div>'
                  for q, a in FAQ)
    notes = ('<aside class="notes" id="notes"><h4>Prototype notes</h4><ul>' +
             "".join(f"<li>{esc(n)}</li>" for n in NOTES) + "</ul></aside>")

    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Homepage — Impruvon (prototype)</title>
<link rel="stylesheet" href="assets/style.css">
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

<section class="hero wrap" id="s01">
  <div class="hero-copy">
    <h1>Fewer medication errors, short-staffed or not.</h1>
    <p class="sub">Impruvon connects guided workflows, smart medication storage and real-time pharmacy
      integration, giving you complete visibility and control without changing the pharmacies, packaging
      or EHR you already use.</p>
    <div class="btns">
      <a class="pill pill-lg" href="{b}{demo}">Book a demo</a>
      <a class="pill pill-ghost" href="{b}platform/index.html">About platform</a>
    </div>
    <div class="microrow">
      <span>1M+ medications administered</span>
      <span>SOC 2 and HIPAA compliant</span>
      <span>State-directed eMAR in Massachusetts</span>
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

<section class="numbers wrap" id="s02">{numbers}</section>

<section class="sec" id="s03"><div class="sec-inner stack-48">
  <h2 class="h2 h2-wide">If your system was built for nurses in a hospital, you've digitized the risk, not removed it.</h2>
  <div class="grid g3">{pain}</div>
</div></section>

<section class="sec sec-deep" id="s04"><div class="sec-inner stack-52">
  <h2 class="h2 h2-wide">Most platforms tell you what already happened. Impruvon guides what happens next.</h2>
  <div class="grid g2">{prods}</div>
</div></section>

<section class="sec" id="s05"><div class="sec-inner stack-48">
  <h2 class="h2">One platform. Many realities.</h2>
  <div class="grid g4">{aud}</div>
  <div class="stateband">
    <div><h3>State-Directed Programs</h3>
      <p>Prevention infrastructure for state agencies and Medicaid health plans.</p></div>
    <a class="pill" href="{b}who-we-serve/state-directed.html">Request a state briefing</a>
  </div>
</div></section>

<section class="sec sec-sunk" id="s06"><div class="sec-inner stack-52">
  <h2 class="h2">What an all-in-one platform can't do.</h2>
  <div class="grid g2" style="row-gap:44px">{reasons}</div>
</div></section>

<section class="sec" id="s07"><div class="sec-inner stack-48">
  <div>
    <h2 class="h2 h2-wide">A caregiver's first shift should be exactly as safe as their thousandth.</h2>
    <p class="lede" style="margin-top:18px;max-width:860px">DSPs are more than just staff on a schedule.
      They're the care your residents count on and the business you run. Some bring clinical backgrounds,
      many don't, and for many English is a second language.</p>
  </div>
  <div class="grid g4">{staff}</div>
  <div class="quote quote-light">
    <div class="bar"></div>
    <div><p>&ldquo;Impruvon is a game changer, it really is as good as it sounds. I can literally administer
      all of the meds on my shift in less than half the time it used to take.&rdquo;</p>
      <cite>DSP, I/DD residential / group home, Washington D.C.</cite></div>
  </div>
  <p class="lede">Care teams save 20 to 25 minutes per resident, per medication pass.</p>
</div></section>

<section class="sec sec-sunk" id="s08"><div class="sec-inner stack-48">
  <h2 class="h2">Proven results.</h2>
  <div class="grid g2">
    <a class="ccard" href="{b}resources/customers/charles-lea.html">
      <div class="eyebrow">CHARLES LEA CENTER</div>
      <div class="big">23,000+</div>
      <p>medications administered with zero errors.</p>
      <div class="go">Read the case study &rarr;</div></a>
    <a class="ccard" href="{b}resources/customers/index.html">
      <div class="eyebrow">VISTA CARE</div>
      <div class="big">75%</div>
      <p>reduction in medication errors across 18 sites in 6 states.</p>
      <div class="go">Read the case study &rarr;</div></a>
  </div>
  <div class="quote">
    <div class="bar"></div>
    <div><p>&ldquo;The overall system, reduction in documentation errors and medication errors are the biggest
      outcomes. They're the outcomes that we needed to see, and we've seen that since implementing Impruvon.&rdquo;</p>
      <cite>Chelsea Curran, Executive Director, Coastal Autism Academy</cite></div>
  </div>
</div></section>

<section class="sec" id="s09"><div class="sec-inner stack-44">
  <h2 class="h2">Questions we get before every demo.</h2>
  <div class="faq">{faq}
    <div class="faqrow flag">
      <div class="q">Is it approved in our state?</div>
      <div class="a">Impruvon is the state-directed eMAR in Massachusetts and operates in [___].
        <a class="go" href="{b}about/contact.html">Talk to us about your state &rarr;</a></div>
    </div>
  </div>
</div></section>

<section class="sec sec-sunk" id="s10"><div class="sec-inner closing">
  <h2>See the platform in action.</h2>
  <div class="line"><span class="flag-box">[15 minutes]</span>
    <span>, on your setup, with straight answers about your state.</span></div>
  <a class="pill pill-lg" href="{b}{demo}">Book a demo</a>
</div></section>

</main>
{foot(b)}
<script src="assets/proto.js"></script>
</body></html>"""

    io.open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(doc)
