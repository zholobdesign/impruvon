"""Pages transcribed section-by-section from the Paper artboards.

Each entry in PAGES is a list of sections using the block vocabulary below;
the vocabulary mirrors the patterns that actually appear on the artboards.
"""
import io, os, html

DEMO = "book-a-demo/index.html"
ASSET_V = ""  # set by build.py from the CSS hash


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
    if b.get("side_dark"):
        parts = []
        for i, (txt, strong) in enumerate(b["side_dark"]):
            if i:
                parts.append('<div class="rule"></div>')
            parts.append(f'<p class="{"strong" if strong else ""}">{esc(txt)}</p>')
        proof = '<div class="sidedark">' + "".join(parts) + "</div>"
        label, target = b.get("cta", ("Book a demo", DEMO))
        return (f'<section class="sec"><div class="sec-inner formwrap">'
                f'<div class="form">{fields}'
                f'<a class="pill pill-lg" style="align-self:flex-start" href="{_link(base, target)}">{esc(label)}</a></div>'
                f'{proof}</div></section>')
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
    rows = ""
    for item in b["items"]:
        cls = "faqcard flag" if len(item) == 3 and item[2] == "flag" else "faqcard"
        rows += f'<div class="{cls}"><div class="q">{esc(item[0])}</div><div class="a">{esc(item[1])}</div></div>'
    extra = ""
    if b.get("after"):
        lbl, tgt = b.get("cta", ("Book a demo", DEMO))
        extra = (f'<div class="smallcta"><h2>{esc(b["after"])}</h2>'
                 f'<a class="pill pill-lg" href="{_link(base, tgt)}">{esc(lbl)}</a></div>')
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    label, target = b.get("cta", ("Book a demo", DEMO))
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner stack-44">{h}'
            f'<div class="faqcards">{rows}</div>'
            + (extra if b.get("after") else
               f'<a class="pill pill-lg" style="align-self:flex-start" href="{_link(base, target)}">{esc(label)}</a>')
            + '</div></section>')



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
    grid = cols if len(b["cols"]) == 1 else f'<div class="grid g2">{cols}</div>'
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'{grid}</div></section>')


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
    flag = f'<div class="flag-box">{esc(b["flag"])}</div>' if b.get("flag") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'<div class="grid g{b.get("cols",2)}">{out}</div>{flag}</div></section>')


def s_ctarow(b, base):
    l, t = b["link"]
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner ctarow">'
            f'<div class="t"><h2>{esc(b["h"])}</h2><p>{esc(b["text"])}</p></div>'
            f'<a class="go" href="{_link(base, t)}">{esc(l)} &rarr;</a></div></section>')



def s_dotcards(b, base):
    out = "".join(f'<div class="dotcard"><i></i><span>{esc(t)}</span></div>' for t in b["items"])
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    cols = b.get("cols", 2)
    grid = f'<div class="grid g{cols}">{out}</div>' if cols > 1 else f'<div class="grid">{out}</div>'
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'{grid}</div></section>')


def s_splitstat(b, base):
    cells = ('<div class="div"></div>').join(
        f'<div class="cell"><b>{esc(v)}</b><span>{esc(l)}</span></div>' for v, l in b["stats"])
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner splitstat">'
            f'<div class="t"><h2>{esc(b["h"])}</h2><p>{esc(b["text"])}</p></div>'
            f'<div class="statbox">{cells}</div></div></section>')


def s_prose(b, base):
    sub = f'<p class="sub">{esc(b["sub"])}</p>' if b.get("sub") else ""
    body = "".join(f'<p class="body">{esc(x)}</p>' for x in b.get("body", []))
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner prose">'
            f'<h2>{esc(b["h"])}</h2>{sub}{body}</div></section>')



def s_nbar(b, base):
    cells = "".join(f'<div class="n"><b>{esc(v)}</b><span>{esc(l)}</span></div>' for v, l in b["items"])
    return f'<section class="nbar {b.get("bg","sec-sunk")}"><div class="sec-inner" style="display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;width:100%">{cells}</div></section>'



def s_pain(b, base):
    out = "".join(f'<div class="pcard"><div class="rule"></div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
                  for t, d in b["items"])
    h = f'<h2 class="h2 h2-wide">{esc(b["h"])}</h2>' if b.get("h") else ""
    line = f'<div class="darkline">{esc(b["line"])}</div>' if b.get("line") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'<div class="grid g{b.get("cols",3)}">{out}</div>{line}</div></section>')


STAR_SVG = '''<svg width="46" height="46" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 3.5 L14.4 9.2 L20.5 9.7 L15.9 13.7 L17.3 19.7 L12 16.5 L6.7 19.7 L8.1 13.7 L3.5 9.7 L9.6 9.2 Z" fill="none" stroke="var(--color-accent)" stroke-width="1.8" stroke-linejoin="round"/></svg>'''


def s_sunkcards(b, base):
    out = ""
    for item in b["items"]:
        kind = item[2] if len(item) == 3 else ""
        if kind == "highlight":
            out += (f'<div class="highlight">{STAR_SVG}<div><h3>{esc(item[0])}</h3>'
                    f'<p>{esc(item[1])}</p></div></div>')
            continue
        cls = "sunkcard wide" if kind == "wide" else "sunkcard"
        out += f'<div class="{cls}"><h3>{esc(item[0])}</h3><p>{esc(item[1])}</p></div>'
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'<div class="grid g2">{out}</div></div></section>')


def s_center(b, base):
    return (f'<section class="sec {b.get("bg","sec-sunk")}" style="padding-top:96px;padding-bottom:96px">'
            f'<div class="sec-inner"><p class="centertext">{esc(b["text"])}</p></div></section>')


def s_scards(b, base):
    out = "".join(f'<div class="scard"><b>{esc(v)}</b><span>{esc(t)}</span></div>' for v, t in b["items"])
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'<div class="g3 statcards3">{out}</div></div></section>')



def s_contrast(b, base):
    left = "".join(f'<p class="{"strong" if strong else ""}">{esc(t)}</p>' for t, strong in b["left"])
    right = "".join(f'<p class="{"big" if big else ""}">{esc(t)}</p>' for t, big in b["right"])
    h = f'<h2 class="h2 h2-wide">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}'
            f'<div class="contrast"><div class="col">{left}</div>'
            f'<div class="col dark">{right}</div></div></div></section>')



def s_flagprose(b, base):
    paras = "".join(f'<p class="{"small" if small else ""}">{esc(t)}</p>' for t, small in b["body"])
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    hh = f'<h2 class="twocol-h">{esc(b["side"])}</h2>' if b.get("side") else ""
    cls = "flagprose dashed" if b.get("dashed") else "flagprose"
    inner = f'<div class="{cls}"><div class="note">{esc(b["note"])}</div>{paras}</div>'
    if b.get("side"):
        return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner twocol">'
                f'{hh}<div class="twocol-body">{inner}</div></div></section>')
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">{h}{inner}</div></section>')



def s_flagtable(b, base):
    head = '<th></th>' + "".join(
        f'<th class="{"us" if i == 0 else ""}">{esc(c)}</th>' for i, c in enumerate(b["cols"]))
    rows = ""
    for label, mark in b["rows"]:
        blanks = "".join("<td></td>" for _ in range(len(b["cols"]) - 1))
        rows += f'<tr><td>{esc(label)}</td><td class="us">{esc(mark)}</td>{blanks}</tr>'
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner stack-44">{h}'
            f'<div class="flagtable"><div class="note">{esc(b["note"])}</div>'
            f'<div class="inner"><table><thead><tr>{head}</tr></thead>'
            f'<tbody>{rows}</tbody></table></div></div></div></section>')



def s_filters(b, base):
    fs = "".join(f'<div class="f"><span class="lbl">{esc(l)}</span>'
                 f'<span class="sel">{esc(v)} <i>&#9662;</i></span></div>' for l, v in b["items"])
    return (f'<section class="sec" style="padding-top:0;padding-bottom:44px"><div class="sec-inner filters">'
            f'{fs}<div class="search">{esc(b.get("search","Search resources"))}</div></div></section>')


def s_rescards(b, base):
    cards = ""
    for c in b["items"]:
        tags = "".join(f'<span class="tag{"" if i == 0 else " alt"}">{esc(t)}</span>'
                       for i, t in enumerate(c["tags"]))
        meta = f'<div class="meta">{esc(c["meta"])}</div>' if c.get("meta") else ""
        cards += (f'<div class="rescard"><div><div class="tags">{tags}</div>'
                  f'<h3>{esc(c["title"])}</h3>{meta}</div>'
                  f'<div class="go">{esc(c["cta"])} &rarr;</div></div>')
    band = ""
    if b.get("band"):
        h, p, l, t = b["band"]
        band = (f'<div class="darkband"><div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>'
                f'<a class="go" href="{_link(base, t)}">{esc(l)} &rarr;</a></div>')
    return (f'<section class="sec" style="padding-top:0;padding-bottom:90px"><div class="sec-inner stack-44">'
            f'<div class="flagtable"><div class="note">{esc(b["note"])}</div>'
            f'<div class="rescards">{cards}</div></div>{band}</div></section>')



def s_cases_rows(b, base):
    out = ""
    for c in b["items"]:
        cls = "caserow flag" if c.get("flag") else "caserow"
        tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in c["tags"])
        go = (f'<a class="go" href="{_link(base, c["link"])}">{esc(c["cta"])} &rarr;</a>'
              if c.get("link") else f'<span class="go">{esc(c["cta"])}</span>')
        out += (f'<div class="{cls}"><div class="metric"><b>{esc(c["metric"])}</b>'
                f'<span>{esc(c["metric_label"])}</span></div>'
                f'<div class="body"><div class="tags">{tags}</div><h3>{esc(c["title"])}</h3>'
                f'<p>{esc(c["text"])}</p>{go}</div></div>')
    rule = ""
    if b.get("rule"):
        rule = (f'<div class="ruleblock"><b>{esc(b["rule"][0])}</b>'
                f'<p>{esc(b["rule"][1])}</p></div>')
    return (f'<section class="sec" style="padding-top:0;padding-bottom:90px">'
            f'<div class="sec-inner" style="display:flex;flex-direction:column;gap:24px">{out}{rule}</div></section>')



def s_casehead(b, base):
    crumbs = " / ".join(esc(c) for c in b["crumbs"])
    meta = "".join(f'<div class="m"><b>{esc(k)}</b><span>{esc(v)}</span></div>' for k, v in b["meta"])
    note = f'<div class="notebox">{esc(b["note"])}</div>' if b.get("note") else ""
    return (f'<section class="sec" style="padding-top:80px;padding-bottom:56px"><div class="sec-inner stack-44">'
            f'<div><div class="crumbs">{crumbs}</div>'
            f'<h1 class="phead-h1" style="font-size:52px;line-height:62px;margin-top:20px">{esc(b["h1"])}</h1>'
            f'<p class="phead-lede">{esc(b["lede"])}</p></div>'
            f'<div class="casemeta">{meta}</div>{note}</div></section>')


def s_labelsplit(b, base):
    paras = "".join(f'<p>{esc(t)}</p>' for t in b.get("body", []))
    bullets = ""
    if b.get("bullets"):
        items = "".join(f'<div class="i"><i></i><span>{esc(t)}</span></div>' for t in b["bullets"])
        bullets = f'<div class="coralist">{items}</div>'
    note = f'<div class="notebox">{esc(b["note"])}</div>' if b.get("note") else ""
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner labelsplit">'
            f'<div class="l"><div class="lab">{esc(b["label"])}</div><h2>{esc(b["h"])}</h2></div>'
            f'<div class="r">{paras}{bullets}{note}</div></div></section>')


def s_numsteps(b, base):
    out = "".join(f'<div class="numstep"><div class="n">{i+1}</div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
                  for i, (t, d) in enumerate(b["items"]))
    note = f'<div class="notebox">{esc(b["note"])}</div>' if b.get("note") else ""
    return (f'<section class="sec {b.get("bg","")}"><div class="sec-inner stack-44">'
            f'<div><div class="lab" style="font-size:12px;font-weight:500;letter-spacing:.12em;'
            f'color:var(--color-accent-hover);margin-bottom:16px">{esc(b["label"])}</div>'
            f'<h2 class="h2" style="font-size:36px;line-height:46px">{esc(b["h"])}</h2></div>'
            f'<div class="numsteps">{out}</div>{note}</div></section>')


def s_results(b, base):
    out = ""
    for v, t, flag in b["items"]:
        cls = "rc flag" if flag else "rc"
        out += f'<div class="{cls}"><b>{esc(v)}</b><p>{esc(t)}</p></div>'
    q = ""
    if b.get("quote"):
        text, name, title, warn = b["quote"]
        q = (f'<div class="quoteflag"><div class="q">&ldquo;{esc(text)}&rdquo;</div>'
             f'<div class="by"><b>{esc(name)}</b><span>{esc(title)}</span></div>'
             f'<div class="warn">{esc(warn)}</div></div>')
    return (f'<section class="sec sec-deep"><div class="sec-inner stack-44">'
            f'<div><div style="font-size:12px;font-weight:500;letter-spacing:.12em;color:var(--color-seafoam);'
            f'margin-bottom:16px">{esc(b["label"])}</div>'
            f'<h2 class="h2" style="font-size:36px;line-height:46px">{esc(b["h"])}</h2></div>'
            f'<div class="rescard3">{out}</div>{q}</div></section>')


def s_closing2(b, base):
    btns = "".join(
        f'<a class="pill pill-lg{"" if i == 0 else " pill-ghost"}" href="{_link(base, t)}">{esc(l)}</a>'
        for i, (l, t) in enumerate(b["buttons"]))
    return (f'<section class="closing-light"><div class="sec-inner"><h2>{esc(b["h"])}</h2>'
            f'<div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:28px">{btns}</div>'
            f'</div></section>')



def s_storyflag(b, base):
    paras = "".join(f'<p class="{cls}">{esc(t)}</p>' for t, cls in b["body"])
    return (f'<section class="sec" style="padding-top:0;padding-bottom:100px"><div class="sec-inner">'
            f'<div class="storyflag"><div class="note">{esc(b["note"])}</div>{paras}</div></div></section>')



def s_flagcards(b, base):
    cards = "".join(f'<div class="softcard" style="background:var(--color-surface)">'
                    f'<h3 style="font-size:20px;line-height:28px">{esc(t)}</h3><p>{esc(d)}</p></div>'
                    for t, d in b["items"])
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","sec-deep")}"><div class="sec-inner stack-44">{h}'
            f'<div class="flagtable"><div class="note">{esc(b["note"])}</div>'
            f'<div class="grid g2">{cards}</div></div></div></section>')


def s_pairsplit(b, base):
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner labelsplit">'
            f'<div class="l"><p style="font-size:21px;line-height:34px;color:var(--color-ink-muted)">'
            f'{esc(b["left"])}</p></div>'
            f'<div class="r"><p style="font-size:26px;line-height:40px;font-weight:500;color:var(--color-ink)">'
            f'{esc(b["right"])}</p></div></div></section>')



def s_routes(b, base):
    out = ""
    for c in b["items"]:
        cls = "routecard new" if c.get("new") else "routecard"
        tag = f'<div class="newtag">{esc(c["new"])}</div>' if c.get("new") else ""
        inner = f'{tag}<h3>{esc(c["title"])}</h3><p>{esc(c["text"])}</p>'
        if c.get("link"):
            out += f'<a class="{cls}" href="{_link(base, c["link"])}">{inner}</a>'
        else:
            out += f'<div class="{cls}">{inner}</div>'
    return (f'<section class="sec" style="padding-top:0;padding-bottom:90px">'
            f'<div class="sec-inner"><div class="grid g3">{out}</div></div></section>')


def s_contactform(b, base):
    fields = ""
    for row in b["fields"]:
        cells = "".join(f'<div class="fld"><label>{esc(f)}</label><div class="input"></div></div>' for f in row)
        fields += f'<div class="frow">{cells}</div>'
    fields += ('<div class="fld"><label>Message</label>'
               '<div class="input" style="height:120px"></div></div>')
    rows = "".join(f'<div class="row"><b>{esc(k)}</b><span>{esc(v)}</span></div>' for k, v in b["contacts"])
    side = (f'<div class="contactside"><div class="note">{esc(b["note"])}</div>'
            f'<div><h3>{esc(b["org"])}</h3><p class="addr">{esc(b["address"])}</p></div>'
            f'<div class="rule"></div><div style="display:flex;flex-direction:column;gap:12px">{rows}</div></div>')
    return (f'<section class="sec sec-sunk"><div class="sec-inner formwrap">'
            f'<div class="form" style="background:var(--color-surface);border:0">{fields}'
            f'<span class="pill pill-lg" style="align-self:flex-start">Send</span></div>{side}</div></section>')



def s_joblist(b, base):
    jobs = "".join('<div class="job"><div><b>[Role title]</b>'
                   '<span>[Team] &middot; [Location] &middot; [Type]</span></div><i>&rarr;</i></div>'
                   for _ in range(b.get("count", 3)))
    h = f'<h2 class="h2">{esc(b["h"])}</h2>' if b.get("h") else ""
    return (f'<section class="sec {b.get("bg","sec-sunk")}"><div class="sec-inner stack-44">{h}'
            f'<div class="joblist"><div class="note">{esc(b["note"])}</div>'
            f'<div style="display:flex;flex-direction:column;gap:12px">{jobs}</div></div></div></section>')


def s_stub(b, base):
    return (f'<section class="sec"><div class="sec-inner stack-44">'
            f'<h2 class="h2">{esc(b["h"])}</h2>'
            f'<div class="stub"><b>NO ARTBOARD YET</b><p>{esc(b["text"])}</p></div></div></section>')


BLOCKS = {"head": s_head, "twocol": s_twocol, "chain": s_chain, "cards": s_cards,
          "numbered": s_numbered, "flagstats": s_flagstats, "audience": s_audience,
          "ticks": s_ticks, "quote": s_quote, "cases": s_cases, "faq": s_faq,
          "table": s_table, "darkbar": s_darkbar, "closing": s_closing,
          "form": s_form, "links": s_links, "splithero": s_splithero,
          "spectable": s_spectable, "duo": s_duo, "steps": s_steps, "faqcards": s_faqcards, "bigfeat": s_bigfeat,
          "numlist": s_numlist, "checks": s_checks, "statcards": s_statcards,
          "softcards": s_softcards, "ctarow": s_ctarow, "dotcards": s_dotcards,
          "splitstat": s_splitstat, "prose": s_prose, "nbar": s_nbar,
          "pain": s_pain, "sunkcards": s_sunkcards, "center": s_center, "scards": s_scards,
          "contrast": s_contrast, "flagprose": s_flagprose, "flagtable": s_flagtable,
          "filters": s_filters, "rescards": s_rescards, "caserows": s_cases_rows,
          "casehead": s_casehead, "labelsplit": s_labelsplit, "numsteps": s_numsteps,
          "results": s_results, "closing2": s_closing2, "storyflag": s_storyflag,
          "flagcards": s_flagcards, "pairsplit": s_pairsplit,
          "routes": s_routes, "contactform": s_contactform, "joblist": s_joblist, "stub": s_stub}

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
<link rel="stylesheet" href="{base}assets/style.css?v={ASSET_V}">
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
<script src="{base}assets/proto.js?v={ASSET_V}"></script>
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
        {"title": "Integrations", "text": "24/7 bidirectional pharmacy integration with 75+ partners, plus your existing EHR.", "link": "platform/integrations.html", "cta": "See integrations"},
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
        {"title": "Pharmacy and EHR", "text": "Real-time pharmacy integration and connection to your existing EHR, so nothing is transcribed by hand.", "link": "platform/integrations.html", "cta": "See integrations"},
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


PAGES["platform/integrations.html"] = dict(title="Integrations", notes=[
    "Transcribed from the artboard “Impruvon — Integrations”. The artboard merges pharmacy and EHR into one page at /platform/integrations; the earlier separate URLs now redirect here.",
    "“Integration-friendly” is a wedge against competitors who are seen as closed, so this page exists to be found and linked, not buried as an anchor.",
], sections=[
    {"t": "head", "kicker": "PLATFORM · INTEGRATIONS",
     "h1": "Every hour a prescription sits unsynced is an hour of risk.",
     "lede": "Real-time connectivity closes that window, with no changes to your existing pharmacy relationships.",
     "cta": ("See integrations in a demo", DEMO)},
    {"t": "twocol", "h": "What does Impruvon integrate with?", "body": [
        "24/7 bidirectional integration means new orders, refills and discontinuations flow directly between your pharmacy and your platform in real time. No more manual transcription from paper MARs or TARs, no more wasted time faxing documents, no more disputes over deliveries, and no changes to pharmacy or medication packaging needed."]},
    {"t": "dotcards", "h": "Benefits of pharmacy integration.", "items": [
        "Automated prescription and refill reminders — always have the PRNs you need, no unexpected shortages",
        "Smart order review and approval for medications and treatments",
        "Real-time awareness of all orders and statuses",
        "Streamlined pharmacy communications — new orders, refills, discontinues",
    ]},
    {"t": "splitstat", "h": "Connected with 75+ pharmacy partners nationally.",
     "text": "Trusted by providers, state agencies and pharmacies across 20+ states, a statewide network effect that benefits everyone in it.",
     "stats": [("75+", "pharmacy partners"), ("20+", "states")]},
    {"t": "prose", "h": "When systems don't talk to each other, no one has the full picture.",
     "sub": "Not because anyone missed a step, but because the systems were never connected in the first place.",
     "body": ["Impruvon connects with your existing EHR systems, eliminating the duplicate documentation and multi-system logins that burden care teams. Staff work in one place, and data flows where it needs to go."]},
    {"t": "duo", "items": [
        ("Beyond the EHR.",
         "Telehealth integrations with platforms like StationMD ensure physicians conducting remote evaluations have access to accurate, real-time records, instead of relying on a DSP to report from memory.", False),
        ("HRST is an integration too.",
         "Medications, diagnoses and allergies pulled from the source: the pharmacy filling your medications.", False),
    ]},
    {"t": "faq", "h": "Questions we get about integrations.", "items": [
        ("Does it work with our pharmacy?", "We are connected with 75+ pharmacy partners nationally, across 20+ states. Tell us the name and we will confirm."),
        ("Do we have to change pharmacies or packaging?", "No changes to pharmacy or medication packaging needed, and no changes to your existing pharmacy relationships."),
        ("Do we have to replace our EHR?", "No. Impruvon connects with your existing EHR systems."),
        ("What about telehealth?", "Telehealth integrations with platforms like StationMD give physicians running remote evaluations access to accurate, real-time records."),
    ]},
    {"t": "closing", "h": "See integrations in a demo."},
])


PAGES["who-we-serve/index.html"] = dict(title="Who We Serve", notes=[
    "Transcribed from the artboard “Impruvon — Who We Serve”.",
    "Entry by audience. Each vertical is a standalone page rather than an anchor, so it can rank on long-tail terms like “eMAR for foster care agency” and hold the compliance detail that setting needs.",
    "State-Directed sits in a separate highlighted band because it is a different kind of visitor — a network-scale buyer with a different CTA.",
], sections=[
    {"t": "head", "kicker": "WHO WE SERVE", "h1": "One platform. Many realities.",
     "lede": "Impruvon is a provider platform built for the specific regulatory and staffing realities of several distinct care settings, adaptable to the workflows of every setting we serve.",
     "cta": ("Book a demo", DEMO)},
    {"t": "twocol", "h": "What settings does Impruvon serve?", "body": [
        "Impruvon is used by I/DD and residential providers, behavioral and mental health programs, home health agencies, foster care agencies, and state agencies and Medicaid health plans. What they share: medication is given by a non-clinical workforce, in dispersed settings, under state compliance requirements."]},
    {"t": "audience", "bg": "", "h": "Explore how Impruvon is purpose-built for the setting you work in.", "items": [
        ("I/DD & Residential Providers", "Purpose-built for the demands of group homes, ICFs and HCBS waiver programs.", "who-we-serve/idd-residential.html"),
        ("Behavioral & Mental Health", "Built for the documentation and complexity of psychiatric care.", "who-we-serve/behavioral-mental-health.html"),
        ("Home Health", "Real-time visibility into care delivered outside the facility.", "who-we-serve/home-health.html"),
        ("Foster Care", "Continuity of care for every child, at every placement change.", "who-we-serve/foster-care.html")],
     "band": ("State-Directed Programs",
              "Prevention infrastructure for state agencies and Medicaid health plans.",
              "Request a state briefing", "who-we-serve/state-directed.html")},
    {"t": "twocol", "bg": "sec-deep", "h": "The safeguard goes in the workflow, not in the person.", "body": [
        "Different settings, one problem: medication is given by people who aren't clinicians, in places without a pharmacy down the hall, under rules that demand proof. Impruvon was built from the ground up for those workflow rhythms, staffing and budget constraints, and regulatory requirements."]},
    {"t": "nbar", "items": [
        ("1M+", "Medications administered"), ("50K+", "Medication errors eliminated"),
        ("25K+", "Nursing hours saved"), ("75K+", "DSP hours saved"), ("75+", "Pharmacy partners")]},
    {"t": "closing", "light": True, "h": "See the platform in action."},
])


PAGES["who-we-serve/idd-residential.html"] = dict(title="I/DD & Residential", notes=[
    "Transcribed from the artboard “Impruvon — I/DD & Residential”.",
    "This is the highest-value vertical page: it answers the search “what is the right eMAR for a group home” in the second section, in one paragraph, before any feature list.",
    "The dark statement after the three failure cards is the argument the champion repeats to the executive director: one problem showing up four ways.",
], sections=[
    {"t": "head", "kicker": "WHO WE SERVE · I/DD & RESIDENTIAL",
     "h1": "If your system was built for nurses in a hospital, you've digitized the risk, not removed it.",
     "lede": "Impruvon is purpose-built for group homes, ICFs and HCBS waiver programs, and for the DSPs who actually give the medication.",
     "cta": ("Book a demo", DEMO)},
    {"t": "twocol", "h": "What is the right eMAR for a group home?", "body": [
        "The right eMAR for a group home is one your DSPs will actually use on a busy evening shift. Impruvon guides every med pass step by step, scans the barcode in the app, and keeps treatments, vitals and daily documentation in the same record. Charles Lea Center recorded 23,000+ medications administered with zero errors."]},
    {"t": "pain", "h": "Both of the usual answers leave the same gap.",
     "line": "Clinical, financial, compliance, staffing. That's not four problems. It's one problem showing up four ways.",
     "items": [
        ("More training on the paper process.", "A paper MAR can't catch an error before it happens."),
        ("Or an eMAR retrofitted from acute care.", "It assumes a workforce you don't have, so your DSPs work around it, and the risk moves back onto your best people."),
        ("Either way, the cost compounds quietly.", "The failed audit. The citation on your record. The med error that becomes an incident report, or a hospitalization. The referral source that stops calling. The DSP who burns out and walks, taking months of training with them."),
     ]},
    {"t": "twocol", "bg": "sec-deep", "h": "Designed for the people delivering care.", "body": [
        "At the center is your workforce. DSPs are more than just staff on a schedule. They're the care your residents count on and the business you run. Some bring clinical backgrounds, many don't, and for many English is a second language. When tools assume everyone is a nurse, the burden lands on your best people and the risk lands on everyone.",
        "You can't train, budget, document or hire your way out of that separately. You engineer it out at the source, with a system designed for the people who actually use it."]},
    {"t": "sunkcards", "h": "Built for the way you actually work.", "items": [
        ("Guided med passes", "Barcode scanning, PRN tracking and narcotic counting remove guesswork at every step."),
        ("Real-time pharmacy integration", "Orders, refills and treatment changes flow directly into the platform, eliminating manual entry and transcription errors."),
        ("Smart MedBoxes", "Physical access control. Right medication, right person, right time."),
        ("HRST automation", "Eliminates duplicate data entry and predicts risk instead of reacting to it."),
        ("Real-time analytics dashboard", "Medication administration status across every resident, in every location, at all times. No end-of-shift reconstruction, no blind spots.", "wide"),
    ]},
    {"t": "center", "text": "Representing 2 to 3% of the U.S. population, adults with intellectual and developmental disabilities suffer higher rates and greater severity of polypharmacy-related adverse events than those without I/DD, a risk escalating alongside rising polypharmacy trends in young adults."},
    {"t": "scards", "h": "Proven results.", "items": [
        ("23,000+", "medications administered with zero errors, Charles Lea Center"),
        ("75%", "reduction in medication errors across 18 sites in 6 states, Vista Care"),
        ("20–25 min", "saved per resident, per medication pass"),
    ]},
    {"t": "quote", "light": True,
     "text": "Impruvon is a game changer, it really is as good as it sounds. I can literally administer all of the meds on my shift in less than half the time it used to take.",
     "by": "DSP, I/DD residential / group home, Washington D.C."},
    {"t": "faqcards", "bg": "sec-sunk", "h": "Questions we get from I/DD providers.", "items": [
        ("Will our DSPs use it?", "Step-by-step prompts walk any caregiver through every administration, and role-specific interfaces mean each person sees exactly what they need. Easy to learn and use for DSPs and nurses alike."),
        ("Does it handle narcotic counts and PRNs?", "Yes. Narcotic counting and PRN reason and effectiveness tracking are part of the med pass, not a separate system."),
        ("Do we have to change pharmacies or packaging?", "No changes to your existing pharmacy relationships or medication packaging."),
        ("Do we have to replace our EHR?", "No. Impruvon connects with your existing EHR systems."),
    ]},
])


PAGES["who-we-serve/home-health.html"] = dict(title="Home Health", notes=[
    "Transcribed from the artboard “Impruvon — Home Health”.",
    "The argument is reframing, not features: the visibility gap is treated as a technology problem, not a geography problem. The dark card carries that turn.",
], sections=[
    {"t": "head", "kicker": "WHO WE SERVE · HOME HEALTH",
     "h1": "Distance isn't the reason you have less visibility. Technology is.",
     "lede": "If care happens in a hundred different homes, your records shouldn't live in a hundred different places.",
     "cta": ("Book a demo", DEMO)},
    {"t": "twocol", "h": "How does an eMAR work for home health?", "body": [
        "In home health the medication record travels with the caregiver. Impruvon runs on the phone or tablet they already carry, guides each med pass step by step, and syncs at the point of care, so the office sees medication administration status across every person served, in every location, as it happens."]},
    {"t": "contrast", "h": "A quiet tradeoff most providers have accepted.",
     "left": [("Care delivered in the home means less oversight than care delivered in a facility. A caregiver supporting multiple people across multiple locations does their best, but the documentation trails behind them. A paper log in one home. A note texted at the end of a shift. A med change that reaches one location but not the next.", False),
              ("By the time information gets back to the office, it's already history.", True)],
     "right": [("The visibility gap isn't a geography problem. It's a technology problem, and it's solvable.", False),
               ("Stop asking for better reports at the end of the week. Start asking why you can't see every person served, in every home, right now.", True)]},
    {"t": "sunkcards", "bg": "sec-sunk", "h": "Every home. Every person. One view.", "items": [
        ("Real-time analytics dashboard", "Medication administration status across every person served, in every location, at all times. No end-of-shift reconstruction, no blind spots between visits."),
        ("Guided, step-by-step workflows", "Support every caregiver in the moment, clinical background or not, so the safe choice is the automatic choice in every home, on every visit."),
        ("One centralized record per person", "Documentation happens at the point of care and syncs instantly, so a caregiver walking into their third home of the day has the current picture, not last week's."),
        ("24/7 pharmacy connectivity", "Orders, refills and treatment changes flow into the platform in real time, wherever care is delivered."),
        ("Smart medication storage adapted for home settings", "Right medication, right person, right time, even without staff on site.", "wide"),
    ]},
    {"t": "nbar", "items": [
        ("1M+", "Medications administered"), ("50K+", "Medication errors eliminated"),
        ("25K+", "Nursing hours saved"), ("75K+", "DSP hours saved"), ("75+", "Pharmacy partners")]},
    {"t": "faq", "h": "Questions we get from home health agencies.", "items": [
        ("Does it work on a phone?", "Yes. Android, iOS and web browsers, with automated single sign-on."),
        ("Does the record update between visits?", "Documentation happens at the point of care and syncs instantly, so the next caregiver has the current picture."),
        ("Do we have to change pharmacies?", "No changes to your existing pharmacy relationships or medication packaging."),
    ]},
    {"t": "closing", "light": True, "h": "See the platform in action."},
])


PAGES["who-we-serve/behavioral-mental-health.html"] = dict(title="Behavioral & Mental Health", notes=[
    "Transcribed from the artboard “Impruvon — Behavioral & Mental Health”.",
    "The whole page argues one distinction: passing an audit is an event, being defensible is a standard. That is why the proof block is flagged — those figures come from the I/DD elevator pitch and are being reused on a behavioural health page.",
], sections=[
    {"t": "head", "kicker": "WHO WE SERVE · BEHAVIORAL & MENTAL HEALTH",
     "h1": "Passing your audit and being defensible aren't the same thing.",
     "lede": "One is a scheduled event you prepare for. The other is a standard you either live in, or don't.",
     "cta": ("Book a demo", DEMO)},
    {"t": "twocol", "h": "What does medication management look like in behavioral health?", "body": [
        "Behavioral and mental health providers manage some of the most complex psychiatric medication regimens in community-based care, under some of the heaviest documentation requirements, with a budget and workforce in constant flux. Impruvon keeps the eMAR, clinical tasks and vitals in one platform, so the record is current and defensible at any moment, not just before a review."]},
    {"t": "twocol", "bg": "", "h": "Compliance treated as an event.", "body": [
        "Most behavioral health providers treat compliance like an event: the audit is coming, so the team scrambles, pulling records from the eMAR, pharmacy records, the vitals log, the paper binder, reconstructing a defensible story from systems that were never designed to tell one together.",
        "Real scrutiny doesn't arrive on schedule. It arrives with an adverse event, a licensing review, a lawsuit. Exactly the moments when the gaps between your systems stop being invisible and start being liability."]},
    {"t": "twocol", "bg": "sec-deep", "h": "If you stay ready, you never have to get ready.", "body": [
        "Audit readiness shouldn't be a fire drill. It should be the byproduct of how documentation happens every shift, on every med pass, automatically."]},
    {"t": "sunkcards", "h": "Compliance built in, not bolted on.", "items": [
        ("One platform", "eMAR, clinical tasks and vitals together. No documentation gaps between systems, no reconstruction before a review."),
        ("Guided med passes", "PRN tracking and narcotic counting remove guesswork from complex psychiatric regimens. The safe choice is the automatic choice, whoever is on shift."),
        ("Always current, always defensible", "Real-time digital documentation and an analytics dashboard replace error-prone paper processes."),
        ("Role-based interfaces", "Reduce training burden for a high-turnover workforce. New staff are safe and productive from day one."),
        ("SOC 2 and HIPAA compliant", "Ready for immediate deployment."),
        ("Supervised self-administration", "Helps clients build toward managing their own psychiatric medications where clinically appropriate. Independence with oversight."),
    ]},
    {"t": "flagstats", "h": "Proven results.", "items": [
        ("48%", "reduction in medication errors"), ("39%", "improvement in compliance rates"),
        ("69%", "improvement in audit-ready documentation")],
     "note": "Sourced from the I/DD elevator pitch, used here on a behavioural health page. Keep, or drop and lead with the quote."},
    {"t": "quote", "bg": "sec-sunk",
     "text": "The overall system, reduction in documentation errors and medication errors are the biggest outcomes. They're the outcomes that we needed to see, and we've seen that since implementing Impruvon.",
     "by": "Chelsea Curran, Executive Director, Coastal Autism Academy"},
    {"t": "faq", "h": "Questions we get from behavioral health providers.", "items": [
        ("Are you SOC 2 and HIPAA compliant?", "Yes. SOC 2 and HIPAA compliant, ready for immediate deployment."),
        ("Does it handle complex psychiatric regimens?", "Guided med passes, PRN reason and effectiveness tracking, and narcotic counting are built into the med pass."),
        ("How does it help with a high-turnover workforce?", "Role-based interfaces reduce training burden. New staff are safe and productive from day one."),
        ("Can clients self-administer?", "Where clinically appropriate, supervised self-administration lets clients build toward managing their own medications, with oversight retained."),
    ]},
    {"t": "closing", "light": True, "h": "See the platform in action."},
])


PAGES["who-we-serve/foster-care.html"] = dict(title="Foster Care", notes=[
    "Transcribed from the artboard “Impruvon — Foster Care”.",
    "The distinct risk here is the move: every placement change is a handoff, so the page argues that a predictable moment of risk can be engineered for rather than absorbed.",
], sections=[
    {"t": "head", "kicker": "WHO WE SERVE · FOSTER CARE",
     "h1": "A child's medication history shouldn't depend on a caseworker's memory.",
     "lede": "Every placement change is a handoff. Right now, it's also a gamble.",
     "cta": ("Book a demo", DEMO)},
    {"t": "twocol", "h": "What makes medication management different in foster care?", "body": [
        "Foster care agencies manage the same medication challenges as any I/DD or behavioral health provider: complex regimens, psychiatric medications, med errors, paper MARs, state compliance requirements. But they carry one risk those providers don't. The child moves. And every time they do, the medication record has to survive the move too."]},
    {"t": "contrast", "h": "What arrives with the child, and what doesn't.",
     "left": [("Most agencies treat what happens next as an unavoidable side effect of the system: a paper folder that arrives incomplete, a caseworker recalling doses from memory, a foster parent with no clinical training starting over with whatever information made the trip. Details fall through the cracks, and everyone does their best.", False)],
     "right": [("Information loss at placement transitions isn't bad luck. It's a design flaw. Every placement change is a predictable moment of risk, and a predictable moment can be engineered for.", False),
               ("A child's medication history shouldn't be the most fragile thing they carry between homes.", True)]},
    {"t": "sunkcards", "bg": "sec-sunk", "h": "The record follows the child, not the paperwork.", "items": [
        ("Records that follow the child across placements", "The receiving caregiver starts with the complete, current picture on day one, not a partial paper file."),
        ("Guided, simple workflows", "Foster parents aren't clinicians, and they shouldn't have to be. Step-by-step med passes make the safe choice the automatic choice in every home."),
        ("Real-time visibility for the agency", "Caseworkers and administrators see medication administration status across every child in care, without waiting on paper logs or phone calls."),
        ("Documentation ready for state child welfare reporting and audits", "Compliance is the byproduct of every med pass, not a scramble before a review."),
        ("Support for youth building toward self-sufficiency", "Supervised self-administration helps older youth learn to manage their own medications before they age out, not after.", "highlight"),
    ]},
    {"t": "nbar", "items": [
        ("1M+", "Medications administered"), ("50K+", "Medication errors eliminated"),
        ("25K+", "Nursing hours saved"), ("75K+", "DSP hours saved"), ("75+", "Pharmacy partners")]},
    {"t": "faq", "h": "Questions we get from foster care agencies.", "items": [
        ("Do foster parents need clinical training?", "No. Step-by-step med passes guide any caregiver through every administration. Foster parents aren't clinicians and don't need to be."),
        ("What happens to the record when a child changes placement?", "The record is centralized and portable. The receiving caregiver starts with the complete, current picture on day one, not a partial paper file."),
        ("Can older youth manage their own medication?", "Supervised self-administration helps older youth learn to manage their own medications before they age out."),
    ]},
    {"t": "closing", "light": True, "h": "See the platform in action."},
])


BRIEF = "request-a-state-briefing/index.html"

PAGES["who-we-serve/state-directed.html"] = dict(title="State-Directed Programs", notes=[
    "Transcribed from the artboard “Impruvon — State-Directed Programs”.",
    "This is the highest-value page on the site: it is the network-scale entry point, and it converts to a state briefing rather than a product demo.",
    "Three yellow blocks mark the three things that must be settled before publishing: which states can be claimed, citations for the national statistics, and consistent use of the word “projected” on the $371M figure.",
], sections=[
    {"t": "head", "kicker": "WHO WE SERVE · STATE-DIRECTED PROGRAMS",
     "h1": "Your most at-risk populations carry your most preventable costs.",
     "lede": "Every medication error avoided is a hospitalization, an ER visit and a claim that never happens.",
     "cta": ("Request a state briefing", BRIEF)},
    {"t": "flagprose", "side": "What is a state-directed eMAR?",
     "note": "MASSACHUSETTS ONLY, OR MASSACHUSETTS AND MISSOURI · CONFIRM",
     "body": [("A state-directed eMAR is one medication platform adopted across a state's provider network, so documentation, oversight and reporting follow a single standard. Impruvon currently serves as the state-directed eMAR in Massachusetts, in partnership with the Massachusetts Executive Office of Health and Human Services.", False)]},
    {"t": "twocol", "bg": "", "h": "Oversight is a rear-view mirror.", "body": [
        "Every state agency knows the playbook: more oversight, more reporting requirements, more audits. But by the time a violation is caught, the adverse drug event has already happened. The ER visit billed, the hospitalization underway, the incident report filed.",
        "And no amount of enforcement fixes the underlying reality: a community-based workforce that is non-clinical, high-turnover, and stretched across thousands of homes your auditors will never see."]},
    {"t": "flagstats", "h": "The scale of the problem is national.", "items": [
        ("1.5 million", "Americans injured by medication errors each year"),
        ("~800,000", "preventable drug-related injuries annually in long-term care settings alone"),
        ("~$21 billion", "in direct medical costs across all care settings annually")],
     "note": "Three external statistics with no attribution. State agencies and MCOs check sources — the sources are public, only the citations are missing."},
    {"t": "twocol", "bg": "sec-deep", "h": "Prevention isn't softer than enforcement.", "body": [
        "Every adverse drug event prevented is a hospitalization, an ER visit and a transport cost that never has to be recovered, and a fraudulent or erroneous claim that never gets filed. Prevention is cheaper, faster, and it protects the individual before the harm, not after."]},
    {"t": "flagprose", "h": "Massachusetts.", "dashed": True, "bg": "",
     "note": "THE WORD “PROJECTED” IS MANDATORY EVERYWHERE THIS FIGURE APPEARS · THE SAME NUMBER ALSO SITS ON OUR COMMITMENT AS AN ACHIEVED RESULT, NEXT TO “ROI > 1500%” · PICK ONE EDITION",
     "body": [("In partnership with the Massachusetts Executive Office of Health and Human Services, Impruvon's financial model projected $371M in savings over four years for approximately 25,000 individuals with I/DD, mental health and co-occurring conditions, a projected return of roughly 1,800%, driven primarily by fewer emergency visits and adverse drug events.", False),
              ("Impruvon currently serves as the state-directed eMAR in Massachusetts.", True)]},
    {"t": "sunkcards", "bg": "sec-sunk", "h": "One platform. Statewide visibility.", "items": [
        ("Enable every provider in your network", "Guided workflows make safe administration the default for a non-clinical workforce, so quality doesn't depend on which agency an individual happens to be served by."),
        ("Real-time, centralized oversight", "Enterprise dashboards and automated audit tooling replace after-the-fact record requests with live, statewide visibility into medication administration."),
        ("Reduce fraud, waste and abuse exposure", "Real-time digital documentation, physical access controls and narcotic counting create a verifiable record of every administration, closing the gaps where diversion and billing irregularities hide."),
        ("Lower avoidable utilization", "Preventing adverse drug events reduces hospitalizations, ER utilization and transport costs."),
        ("Statewide deployment support", "Provider and pharmacy outreach, enrollment, training, reporting and audit optimization, and legacy system integration.", "wide"),
    ]},
    {"t": "faq", "h": "Questions we get from state agencies and health plans.", "items": [
        ("Will providers adopt it?", "Guided workflows make safe administration the default for a non-clinical workforce. Role-based interfaces reduce training burden, and new staff are safe and productive from day one."),
        ("What does statewide deployment involve?", "Provider and pharmacy outreach, enrollment, training, reporting and audit optimization, and legacy system integration."),
        ("How does it work with providers who already have an EHR?", "Impruvon connects with existing EHR systems rather than replacing them."),
        ("Where is Impruvon already state-directed?", "Massachusetts, in partnership with the Executive Office of Health and Human Services, covering approximately 25,000 individuals."),
    ]},
    {"t": "closing", "light": True, "h": "Request a state briefing.",
     "sub": "A working session for state and MCO teams, not a product demo.",
     "cta": ("Request a state briefing", BRIEF)},
])


PAGES[BRIEF] = dict(title="Request a State Briefing",
    badge="CONVERSION FOUND IN THE COPY, NEVER DISCUSSED ON A CALL · CONFIRM IT EXISTS AND WHO HANDLES IT",
    notes=[
    "Transcribed from the artboard “Impruvon — Request a State Briefing”.",
    "A second conversion, separate from Book a demo, because a state administrator is not buying a product — they are evaluating infrastructure. The form asks different questions and routes to a different team.",
    "Flagged: this CTA appears in the copy but was never discussed on a call. Confirm it exists and who handles it before the site goes live.",
], sections=[
    {"t": "head", "h1": "Request a state briefing.",
     "lede": "A working session for state agencies and Medicaid health plans. Not a product demo."},
    {"t": "dotcards", "bg": "sec-sunk", "cols": 1, "h": "What we cover.", "items": [
        "How the Massachusetts state-directed program is structured",
        "What real-time, centralized oversight looks like at network scale",
        "What statewide deployment involves: provider and pharmacy outreach, enrollment, training, reporting and audit optimization, legacy system integration",
        "Security and compliance questions",
    ]},
    {"t": "form", "cta": ("Request a state briefing", BRIEF), "fields": [
        ["Name", "Work email"],
        ["Agency or health plan", "Role"],
        ["State", "Approximate individuals served"],
     ], "side_dark": [
        ("In partnership with the Massachusetts Executive Office of Health and Human Services, covering approximately 25,000 individuals with I/DD, mental health and co-occurring conditions.", False),
        ("SOC 2 and HIPAA compliant, ready for immediate deployment.", True),
     ]},
])


PAGES[DEMO] = dict(title="Book a Demo", notes=[
    "Transcribed from the artboard “Impruvon — Book a Demo”.",
    "The single conversion point for the whole site. State field is marked required because it drives lead routing — the answer decides whether this is a provider deal or a state conversation.",
    "Flagged: demo length is not stated anywhere in the source material. If the client names a number it goes into the subheading.",
], sections=[
    {"t": "head", "h1": "See the platform in action.",
     "lede": "We'll walk through a med pass the way your team would run it, and answer the compliance questions for your setting.",
     "flag": "Demo length not stated anywhere. If the client names a number, it goes into this subheading."},
    {"t": "form", "fields": [
        ["Name", "Work email"],
        ["Organization", "Role"],
        [("State", "REQUIRED · LEAD ROUTING"), "Homes or individuals served"],
        ["What you use today"],
     ], "proof": [
        ("1M+", "medications administered"),
        ("50K+", "medication errors eliminated"),
        ("23,000+", "medications with zero errors at Charles Lea Center"),
        ("SOC 2 and HIPAA compliant", "Ready for immediate deployment."),
     ]},
    {"t": "faq", "bg": "sec-sunk", "h": "Before the call.", "items": [
        ("Who should join the call?", "Usually whoever owns medication compliance, plus the person who signs. Both get their questions answered in the same session."),
        ("Do we need to prepare anything?", "No."),
        ("Is this a sales pitch?", "No. It's a walkthrough of the product on your kind of setup."),
    ]},
])


PAGES["compare/index.html"] = dict(title="Compare",
    badge="OUTSIDE HEADER AND FOOTER · NO COMPETITOR NAMES", notes=[
    "Transcribed from the artboard “Impruvon — Compare”.",
    "One comparison page for all competitors, not a page per competitor (team decision).",
    "The competitor columns are deliberately empty. The rule on the artboard: if a row cannot be proven with a citation, the cell stays empty. An empty cell is honest; an unsupported “no” is a legal risk and a gift to a competitor.",
    "The page ends by naming who Impruvon is wrong for. That is what makes the rest of it credible.",
], sections=[
    {"t": "head", "h1": "How to choose an eMAR for residential care.",
     "lede": "A buyer's guide, not a sales page. Eight questions worth asking any vendor, including us."},
    {"t": "twocol", "h": "What should you actually compare?", "body": [
        "Most platforms in this space are all-in-one systems where medication is one module among dozens. A medication specialist goes deeper on the med pass itself. Neither is automatically right for you. The questions below tell you which one fits how your homes actually run."]},
    {"t": "numlist", "h": "Eight questions to ask any vendor.", "cols": [
        [("01", "Who gives the medication in your homes, and was the product designed for them?"),
         ("02", "What happens physically to the medication between the pharmacy and the person?"),
         ("03", "How long does it take to pull a month of records for a state reviewer?"),
         ("04", "Does the record include treatments, vitals and daily documentation, or only doses?")],
        [("05", "How many of your pharmacies are already connected, and does data flow both ways?"),
         ("06", "Can you keep your current EHR?"),
         ("07", "What happens when your state changes its documentation requirements?"),
         ("08", "How long until your least tech-confident staff member can run a med pass alone?")],
    ]},
    {"t": "flagtable", "h": "How the options compare.",
     "note": "Competitor columns are deliberately empty. Rule: if a row cannot be proven with a citation, the cell stays empty. An empty cell is honest; an unsupported “no” is a legal risk and a gift to a competitor.",
     "cols": ["IMPRUVON", "VENDOR A", "VENDOR B", "OTHER PLATFORMS"], "rows": [
        ("Purpose-built for residential and community-based care", "Yes"),
        ("Medication is the whole product, not one module", "Yes"),
        ("Smart medication storage hardware", "Yes"),
        ("Guided med pass designed for non-clinical staff", "Yes"),
        ("Treatments, vitals and documentation in the medication record", "Yes"),
        ("Two-way pharmacy integration", "Yes"),
        ("Works with your existing EHR", "Yes"),
        ("No change to medication packaging", "Yes"),
     ]},
    {"t": "head", "h1": "When we're not the right fit.",
     "lede": "If you need one system for billing, EVV, case management and medication together, an all-in-one platform will serve you better. We do one thing.",
     "cta": ("Book a demo", DEMO)},
])


PAGES["pricing/index.html"] = dict(title="Pricing", notes=[
    "Transcribed from the artboard “Impruvon — Pricing”.",
    "A pricing page with no numbers. It exists because buyers search for eMAR pricing — with no page that traffic goes to competitors and review sites; with this page it converts.",
    "Every line describing the model is a draft. Four questions settle the whole page: how the subscription is counted, whether MedBox is sold or leased, whether implementation is one-time, and whether support is included.",
], sections=[
    {"t": "head", "h1": "How Impruvon is priced.",
     "lede": "There are no numbers on this page, because a six-home provider and a statewide network pay very differently. What we can tell you is exactly what the price is built from, so nothing on the call is a surprise."},
    {"t": "sunkcards", "bg": "sec-sunk", "h": "What you pay for.", "items": [
        ("Software subscription", "An annual subscription to eMAR+, priced by the number of individuals you serve. Everything in the platform is included: guided med passes, clinical workflows, reporting and dashboards."),
        ("MedBox hardware", "Smart medication storage is optional and priced separately, per unit. You choose how many homes to equip, and when."),
        ("Implementation", "A one-time setup covering configuration, pharmacy connection, EHR integration and staff training."),
        ("Support", "In-person and virtual customer support, included with your subscription."),
    ]},
    {"t": "flagprose", "bg": "sec-sunk", "dashed": True,
     "note": "EVERY LINE ABOVE IS A DRAFT · FOUR QUESTIONS, ONE TEN-MINUTE CALL",
     "body": [("1 · Is the subscription counted per resident, per home, per user or another way   2 · Is MedBox sold or leased   3 · Is implementation one-time or part of the subscription   4 · Is support included or separate", True)]},
    {"t": "softcards", "cols": 3, "h": "What doesn't cost extra.",
     "flag": "Confirm there is no separate charge for connecting a pharmacy.", "items": [
        ("Barcode scanning", "In-app barcode scanning. No external scanners required."),
        ("Pharmacy integration", "No changes to your pharmacy relationships or medication packaging."),
        ("Platform updates", "Included."),
    ]},
    {"t": "faqcards", "bg": "sec-sunk", "h": "Questions about pricing.",
     "after": "Get a price for your setup.", "items": [
        ("Why aren't there prices on this page?", "Because a six-home provider and a statewide network pay very differently, and a single number here would be wrong for both."),
        ("Is there a minimum?", "[___]", "flag"),
        ("Is there a contract term?", "[___]", "flag"),
        ("Do state-directed programs cost the provider anything?", "[___] · Asked on the State-Directed page too, where we promise a single network standard.", "flag"),
    ]},
])


CASES = "resources/case-studies/index.html"

PAGES["resources/index.html"] = dict(title="Resources",
    badge="URL MUST CHANGE ON FILTERING, OTHERWISE CRAWLERS SEE ONE PAGE", notes=[
    "Transcribed from the artboard “Impruvon — Resources”.",
    "One hub with filters by setting and by role, replacing a dated blog feed. Filtering must change the URL, otherwise search engines only ever see one page.",
    "No real materials exist yet. The cards are the content plan, not published work. Launch condition on the artboard: at least three real items, otherwise publish only case studies and keep this hub dark.",
], sections=[
    {"t": "head", "h1": "Medication safety, explained.",
     "lede": "Reports, articles, webinars and events for the people responsible for medication in community-based care."},
    {"t": "filters", "items": [("SETTING", "All settings"), ("ROLE", "All roles")]},
    {"t": "rescards",
     "note": "No real materials exist yet. The cards below are the content plan, not published work. Condition for launch: at least three real items, otherwise publish only case studies and keep this hub dark.",
     "band": ("Case studies live on their own page.",
              "23,000+ medications with zero errors at Charles Lea Center, and more.",
              "See case studies", CASES),
     "items": [
        {"tags": ["REPORT", "COMPLIANCE"], "title": "[Annual medication safety report, community-based care]", "cta": "Download"},
        {"tags": ["BLOG", "COMPLIANCE"], "title": "How to prepare for a medication audit", "cta": "Read"},
        {"tags": ["BLOG", "I/DD"], "title": "Paper MAR vs eMAR: what actually changes", "cta": "Read"},
        {"tags": ["WEBINAR", "LEADERSHIP"], "title": "[Webinar title]", "meta": "[Date] · [Duration] · On demand", "cta": "Watch"},
        {"tags": ["EVENT", "STATE-DIRECTED"], "title": "[Conference or booth, name]", "meta": "[Date] · [City, State]", "cta": "Meet us there"},
        {"tags": ["BLOG", "DIRECT SUPPORT"], "title": "The five rights of medication administration, in practice", "cta": "Read"},
        {"tags": ["BLOG", "LEADERSHIP"], "title": "What to look for in an eMAR for group homes", "cta": "Read"},
        {"tags": ["BLOG", "COMPLIANCE"], "title": "How to reduce medication errors in residential care", "cta": "Read"},
        {"tags": ["REPORT", "STATE-DIRECTED"], "title": "[State briefing summary, Massachusetts]", "cta": "Download"},
     ]},
    {"t": "closing", "light": True, "h": "See how it works on your setup."},
])


PAGES[CASES] = dict(title="Case Studies", notes=[
    "Transcribed from the artboard “Impruvon — Case Studies”.",
    "Two cards, and only one of them is real. Vista Care is named as a customer everywhere else on the site, but there is no story, no numbers and no approved quote — so the card is shown with the link disabled rather than filled with invented content.",
    "Publishing rule from the artboard: every case study needs written customer sign-off on the name, the numbers and the quote. Without sign-off the provider is described generically and no logo is shown.",
], sections=[
    {"t": "head", "h1": "Proof, from providers like yours.",
     "lede": "What changed after the switch — in error rates, audit results and staff hours."},
    {"t": "caserows", "rule": ("PUBLISHING RULE",
        "Every case study needs a written customer sign-off on the name, the numbers and the quote. Without sign-off the provider is described generically — “a South Carolina I/DD provider” — and the logo is not shown."),
     "items": [
        {"metric": "23,000+", "metric_label": "medications administered with zero errors",
         "tags": ["I/DD & RESIDENTIAL", "SOUTH CAROLINA"],
         "title": "Charles Lea Center replaced paper MARs across every residential site",
         "text": "A provider supporting adults with I/DD moved from paper to eMAR+ and MedBox, and rebuilt how errors are caught before they reach a person.",
         "cta": "Read the case study", "link": "resources/case-studies/charles-lea.html"},
        {"metric": "[metric]", "metric_label": "headline result to be supplied by the client",
         "tags": ["MULTI-STATE PROVIDER", "PAGE NOT BUILT"], "flag": True,
         "title": "Vista Care",
         "text": "Named as a customer, but there is no story, no numbers and no approved quote yet. Card is shown here so the layout holds two cases; the link stays disabled until the client sends the material and signs off on publishing the name.",
         "cta": "Link disabled"},
     ]},
    {"t": "closing", "light": True, "h": "See what the numbers look like on your caseload."},
])


PAGES["resources/case-studies/charles-lea.html"] = dict(title="Case Study Template", notes=[
    "Transcribed from the artboard “Impruvon — Case: Charles Lea Center”. This doubles as the template every future case study follows.",
    "Only the 23,000+ figure is client-supplied. The challenge bullets are a plausible reconstruction, the second and third result metrics are placeholders, and the quote is not approved. All three are marked yellow rather than invented silently.",
    "The 23,000+ figure cannot be published without the time period it covers.",
], sections=[
    {"t": "casehead", "crumbs": ["Resources", "Case studies", "Charles Lea Center"],
     "h1": "23,000+ medications administered. Zero errors.",
     "lede": "How Charles Lea Center moved every residential site off paper MARs — and what it changed for the people they support.",
     "meta": [("ORGANIZATION", "Charles Lea Center"), ("SETTING", "I/DD, residential"),
              ("STATE", "South Carolina"), ("USING", "eMAR+ and MedBox")],
     "note": "Confirm with the client: number of sites, number of people supported, number of staff using the system, and the time period the 23,000+ figure covers. Without a period the number cannot be published."},
    {"t": "labelsplit", "label": "THE CHALLENGE", "h": "Paper MARs hid the errors until the audit found them.",
     "body": ["Every site kept its own binder. A missed dose looked identical to a dose that was given but not initialled, and nobody knew which one it was until a nurse drove out to check."],
     "bullets": [
        "No way to see, from the office, whether a medication pass had actually happened.",
        "Errors surfaced weeks later, in a chart review, when nothing could be done about them.",
        "New DSPs learned the medication process from whoever was on shift, not from a system.",
        "Audit prep meant collecting binders from every site and re-reading them by hand."],
     "note": "These four points are a plausible reconstruction, not client-supplied. Replace with what the Charles Lea team actually said in the interview."},
    {"t": "numsteps", "label": "WHAT THEY DID", "h": "Three moves, in order.",
     "note": "Confirm the rollout sequence and how long it took. If eMAR+ and MedBox went in together rather than in stages, this section becomes two steps, not three.",
     "items": [
        ("Replaced the binders with eMAR+", "Every pass now records who administered what, when, and against which order — visible from the office in real time."),
        ("Put MedBox in the homes", "The right compartment opens for the right person at the right time, so the wrong medication is hard to reach in the first place."),
        ("Moved audit prep into the system", "The record a surveyor asks for is exported, not assembled — the same data the team uses day to day."),
     ]},
    {"t": "results", "label": "RESULTS", "h": "What changed.", "items": [
        ("23,000+", "medications administered with zero errors", False),
        ("[X%]", "second metric — audit result, or time saved on documentation. Client to supply.", True),
        ("[X hrs]", "third metric — nurse or DSP hours returned per week. Client to supply.", True),
     ], "quote": ("Quote from the Charles Lea team about what changed for staff and for the people they support.",
                  "Shannon Childress", "Title to confirm · Charles Lea Center",
                  "The name appeared in the client material without a source, a title or an approved quote. Do not publish until the person has seen the exact wording and agreed to it in writing.")},
    {"t": "closing2", "h": "Run the same numbers on your programs.",
     "buttons": [("Book a demo", DEMO), ("See all case studies", CASES)]},
])


PAGES["about/our-story.html"] = dict(title="Our Story", badge="WAITING ON CEO SIGN-OFF", notes=[
    "Transcribed from the artboard “Impruvon — Our Story”.",
    "The founder's account discloses a personal loss in his family. The client flagged this section themselves. The wording is reproduced exactly as supplied and must not be edited by us — not by a single word — until the CEO and leadership confirm the exact text and the level of detail.",
], sections=[
    {"t": "head", "h1": "Every preventable error started with a system that wasn't built to prevent it.",
     "lede": "Impruvon exists because one family learned that lesson the hardest way possible."},
    {"t": "storyflag",
     "note": "THE CLIENT FLAGGED THIS SECTION THEMSELVES · IT DISCLOSES A PERSONAL LOSS IN THE FOUNDER'S FAMILY · EXACT WORDING AND LEVEL OF DETAIL TO BE CONFIRMED WITH THE CEO AND LEADERSHIP · NOT TO BE EDITED BY US, NOT BY A SINGLE WORD",
     "body": [
        ("Founder Justin Amoyal lost his brother Ben from a preventable overdose while living in a supported residential setting. Not because anyone failed to care, but because the systems around him were never engineered to catch it in time.", "lead"),
        ("That loss became a question that stayed with us. Hospitals had spent decades building infrastructure to stop medication errors before they reach a patient. Why hadn't community-based care been given the same tools?", "body"),
        ("The answer became a company.", "kicker2"),
     ]},
    {"t": "twocol", "bg": "sec-deep", "h": "From loss to mission.", "body": [
        "Impruvon was built on a simple, unwavering belief: medication errors in residential and community-based care aren't inevitable. They're the predictable result of asking non-clinical caregivers to do clinical-grade work with paper-era tools. And predictable problems can be engineered away."]},
    {"t": "twocol", "bg": "", "h": "What we exist to do.", "body": [
        "We exist to set the standard for medication management by creating a seamless, safe and connected ecosystem where every care team is equipped and every individual's needs are supported.",
        "We envision a world where medication errors are eliminated, compliance is effortless, and where underserved individuals who cannot advocate for themselves receive the best possible care."]},
    {"t": "nbar", "items": [
        ("1M+", "medications administered"), ("50K+", "medication errors eliminated"),
        ("75+", "pharmacy partners across 20+ states"), ("MA", "state-directed eMAR in Massachusetts")]},
    {"t": "closing", "light": True, "h": "See what we stand for.",
     "cta": ("Our commitment", "about/our-commitment.html")},
])


PAGES["about/our-commitment.html"] = dict(title="Our Commitment", notes=[
    "Transcribed from the artboard “Impruvon — Our Commitment”.",
    "The four pillars exist in three different editions across the client's files. Recommendation on the artboard: treat the Product Overview wording as canonical, and keep the Careers variant as a deliberate first-person restatement.",
    "The word “projected” on the 1,800% figure was added by us and must stay — the same number appears elsewhere as an achieved result and as “ROI > 1500%”.",
], sections=[
    {"t": "head", "h1": "A caregiver's first shift should be exactly as safe as their thousandth.",
     "lede": "Most safety plans start with “hire better people, train them harder.” We started somewhere else."},
    {"t": "pairsplit",
     "left": "Different clinical experience levels among staff, workforce shortages, and individuals with complex needs like polypharmacy and long-term medication use are just a few of the realities that challenge that promise.",
     "right": "Impruvon was designed for exactly this: putting the safeguard in the workflow, not in the person."},
    {"t": "twocol", "bg": "", "h": "What sets us apart.", "body": [
        "Impruvon was built from the ground up for the workflow rhythms, staffing and budget constraints, and regulatory requirements of residential and community-based care.",
        "Our integrated software-hardware platform connects guided workflows, smart medication storage and real-time pharmacy integration, giving providers complete visibility and control without changing the pharmacies, packaging or EHR systems they already use."]},
    {"t": "flagcards", "h": "Four commitments, one platform.",
     "note": "These four pillars exist in three editions in the client file. Here “Simplify every step” and “Gain audit peace of mind”; on Product Overview “Simplify every workflow” and “Ensure audit readiness”; on Careers a first-person variant. Recommendation: Product Overview as canonical, Careers kept as a deliberate restatement.",
     "items": [
        ("Simplify every step", "Medication management should work the way your care teams work, not the other way around."),
        ("Gain audit peace of mind", "Meeting compliance and regulatory requirements should be built into your workflow, not an afterthought."),
        ("Connect every touchpoint", "Great care doesn't happen in silos. Your platform shouldn't either."),
        ("Empower every person", "Medication management should build confidence and resilience for individuals and the teams who support them."),
     ]},
    {"t": "flagstats", "bg": "", "h": "Results at a glance.", "items": [
        ("48%", "Reduction in medication errors"), ("39%", "Improvement in compliance rates"),
        ("50,000+", "Medication errors eliminated to date"),
        ("1,800%", "Projected ROI in the Massachusetts state-directed model")],
     "note": "Flagged by the client. Figures come from an I/DD-specific deck and need confirmation of scope and permission for external use. The word “projected” was added by us and must stay: the same figure appears elsewhere as an achieved result and as “ROI > 1500%”."},
    {"t": "closing", "light": True, "h": "See how we serve your organization.",
     "cta": ("Who we serve", "who-we-serve/index.html")},
])


PAGES["about/contact.html"] = dict(title="Contact", badge="BLOCKS THE RELEASE OF THE WHOLE SITE", notes=[
    "Transcribed from the artboard “Impruvon — Contact”.",
    "None of the contact details exist in any client material. On a B2B site selling compliance to state agencies, a contact page without an address or a phone number damages trust more than anything else on the site. This is the item that blocks release.",
    "Pharmacy partnership is a fifth enquiry type added during design: 75+ pharmacies are a stated asset, but there was no route for a pharmacy to reach out.",
], sections=[
    {"t": "head", "h1": "Let's talk.", "lede": "Tell us what you need, and we'll get you to the right team."},
    {"t": "routes", "items": [
        {"title": "Book a demo", "text": "See the platform in action.", "link": DEMO},
        {"title": "Customer support", "text": "Get help with your Impruvon account."},
        {"title": "Pharmacy partnership", "text": "Connect your pharmacy to the Impruvon network.", "new": "NEW · FIFTH TYPE"},
        {"title": "Press and media", "text": "Media inquiries and press resources."},
        {"title": "General inquiry", "text": "Everything else."},
    ]},
    {"t": "contactform",
     "fields": [["Name", "Organization"], ["Role", "State or region"], ["Inquiry type"]],
     "note": "NONE OF THESE DETAILS EXIST IN ANY CLIENT MATERIAL · A CONTACT PAGE WITHOUT AN ADDRESS OR A PHONE NUMBER, ON A B2B SITE SELLING COMPLIANCE TO STATE AGENCIES, DAMAGES TRUST MORE THAN ANYTHING ELSE ON THE SITE",
     "org": "Impruvon Health", "address": "[Street address] · [City, State ZIP]",
     "contacts": [("General", "[hello@impruvon.com]"), ("Support", "[support@impruvon.com]"),
                  ("Press", "[press@impruvon.com]"), ("Phone", "[(000) 000-0000]")]},
])


PAGES["about/careers.html"] = dict(title="Careers", notes=[
    "Transcribed from the artboard “Impruvon — Careers”.",
    "The four principles here are the first-person restatement of the four commitments — kept deliberately, not treated as a duplicate.",
    "An ATS feed is required. If there is no feed or zero open roles, do not publish this page: an empty careers page hurts more than no careers page.",
], sections=[
    {"t": "head", "h1": "You can do more than provide care. You can redesign how it's delivered."},
    {"t": "pairsplit",
     "left": "Most people in this field are told their impact stops at the bedside, the group home, the med pass. We think that undersells what's possible.",
     "right": "Every workflow we build, every safeguard we design, protects thousands of people who will never know our names. If you want work that scales compassion instead of just performing it, you're in the right place."},
    {"t": "numlist", "h": "How we work.", "cols": [[
        ("01", "We simplify every workflow, including our own internal ones."),
        ("02", "We ensure audit readiness, because “good enough” isn't a standard we build to."),
        ("03", "We connect every touchpoint, across teams, not just across the product."),
        ("04", "We empower every person, our co-workers included."),
    ]]},
    {"t": "joblist", "h": "Open roles.",
     "note": "ATS FEED REQUIRED · IF THERE IS NO FEED OR ZERO OPEN ROLES, DO NOT PUBLISH THIS PAGE · AN EMPTY CAREERS PAGE HURTS MORE THAN NO CAREERS PAGE"},
])


PAGES["trust/index.html"] = dict(title="Trust & Compliance", notes=[
    "Linked from the footer on every artboard, but not designed yet — there is no artboard for it in the Paper file.",
    "Recommended before release: SOC 2 type and report request flow, HIPAA BAA process, data residency and retention, SSO and role-based access, and the state approvals that can be named.",
], sections=[
    {"t": "head", "h1": "Trust and compliance.",
     "lede": "Security, certifications and the answers procurement asks for."},
    {"t": "stub", "h": "Not designed yet.",
     "text": "Every footer on the site links here, so the page has to exist before release. Content needed from the client: SOC 2 type, HIPAA BAA process, data residency and retention, SSO and role-based access, and which state approvals can be named."},
    {"t": "closing", "light": True, "h": "See the platform in action."},
])


PAGES["about/index.html"] = dict(title="Company", notes=[
    "The header's Company link needs a destination. There is no Company hub artboard, so this page routes onward until the client decides whether Company should be a hub or a direct link to Our Story.",
], sections=[
    {"t": "head", "h1": "Company.", "lede": "Who we are, what we stand for, and how to reach us."},
    {"t": "routes", "items": [
        {"title": "Our story", "text": "Why Impruvon exists.", "link": "about/our-story.html"},
        {"title": "Our commitment", "text": "Four commitments, one platform.", "link": "about/our-commitment.html"},
        {"title": "Trust & compliance", "text": "Security and certifications.", "link": "trust/index.html"},
        {"title": "Careers", "text": "Open roles and how we work.", "link": "about/careers.html"},
        {"title": "Contact", "text": "Support, press, partnerships and general enquiries.", "link": "about/contact.html"},
    ]},
])


PAGES["login/index.html"] = dict(title="Log in", notes=[
    "Utility link in the header. Points to the product application, not part of the marketing site.",
], sections=[
    {"t": "head", "h1": "Log in.", "lede": "Existing customers sign in to the Impruvon application."},
    {"t": "stub", "h": "Application, not marketing.",
     "text": "This link leaves the marketing site and opens the Impruvon product. Shown here so the client can see where it sits in the header."},
])


SITEMAP_GROUPS = [
    ("Home", [("Homepage", "index.html")]),
    ("Platform", [("Platform", "platform/index.html"), ("eMAR+", "platform/emar.html"),
                  ("MedBox", "platform/medbox.html"), ("Integrations", "platform/integrations.html"),
                  ("HRST Automation", "platform/hrst-automation.html")]),
    ("Who We Serve", [("Who We Serve", "who-we-serve/index.html"),
                      ("I/DD & Residential", "who-we-serve/idd-residential.html"),
                      ("Behavioral & Mental Health", "who-we-serve/behavioral-mental-health.html"),
                      ("Home Health", "who-we-serve/home-health.html"),
                      ("Foster Care", "who-we-serve/foster-care.html"),
                      ("State-Directed Programs", "who-we-serve/state-directed.html")]),
    ("Decide", [("Compare", "compare/index.html"), ("Pricing", "pricing/index.html"),
                ("Trust & Compliance", "trust/index.html")]),
    ("Resources", [("Resources", "resources/index.html"),
                   ("Case Studies", CASES),
                   ("Case study template", "resources/case-studies/charles-lea.html")]),
    ("Company", [("Company", "about/index.html"), ("Our Story", "about/our-story.html"),
                 ("Our Commitment", "about/our-commitment.html"), ("Careers", "about/careers.html"),
                 ("Contact", "about/contact.html")]),
    ("Convert", [("Book a Demo", DEMO), ("Request a State Briefing", BRIEF), ("Log in", "login/index.html")]),
]

BLOCKERS = [
    "Contact details — address, phone, support and press email. Blocks release of the whole site.",
    "Our Story — the founder's account of a personal loss needs CEO and leadership sign-off, word for word.",
    "States — Massachusetts only, or Massachusetts and Missouri.",
    "Results figures — 48/39/69% come from an I/DD deck; confirm scope and permission for external use.",
    "The $371M / 1,800% figure — “projected” must stay everywhere, and the “ROI > 1500%” edition must go.",
    "Charles Lea — the period the 23,000+ covers, plus a written sign-off on the name, numbers and quote.",
    "Vista Care — named everywhere but has no story, numbers or approved quote.",
    "Pricing — how the subscription is counted, MedBox sold or leased, implementation, support.",
    "Careers — an ATS feed, or the page does not ship.",
    "Resources — at least three real materials, or publish only case studies.",
    "State briefing — confirm the conversion exists and who handles it.",
]


def write_sitemap(out, nav, foot):
    groups = ""
    for title, items in SITEMAP_GROUPS:
        links = "".join(f'<a href="{l[1]}">{esc(l[0])} &rarr;</a>' for l in items)
        groups += (f'<div class="col"><h4 style="color:var(--color-ink-faint)">{esc(title)}</h4>'
                   f'<div class="linklist">{links}</div></div>')
    blockers = "".join(f"<li>{esc(x)}</li>" for x in BLOCKERS)
    body = (f'<section class="sec"><div class="sec-inner stack-44">'
            f'<h2 class="h2">Every page in the prototype.</h2>'
            f'<div class="grid g3">{groups}</div></div></section>'
            f'<section class="sec sec-sunk"><div class="sec-inner stack-44">'
            f'<h2 class="h2">What the client still has to decide.</h2>'
            f'<div class="storyflag"><div class="note">OPEN ITEMS</div>'
            f'<ul style="margin:0;padding-left:20px;display:flex;flex-direction:column;gap:10px">'
            f'{blockers}</ul></div></div></section>')
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Sitemap — Impruvon (prototype)</title>
<link rel="stylesheet" href="assets/style.css?v={ASSET_V}">
</head><body>
<div class="annot">
  <span class="aurl">PROTOTYPE &middot; SITEMAP</span>
  <span class="aleg"><span class="swatch"></span>Yellow = needs client confirmation before build</span>
  <span class="aleg"><button id="notesToggle" type="button">Show notes</button>
    <a href="index.html">Home</a></span>
</div>
{nav("", "sitemap.html")}
<main>
  <section class="sec phead"><div class="sec-inner">
    <div class="kicker">PROTOTYPE</div>
    <h1 class="phead-h1">Sitemap.</h1>
    <p class="phead-lede">Every page transcribed from the Paper file, and everything still waiting on the client.</p>
  </div></section>
  {body}
</main>
{foot("")}
<script src="assets/proto.js?v={ASSET_V}"></script>
</body></html>"""
    io.open(os.path.join(out, "sitemap.html"), "w", encoding="utf-8").write(doc)
