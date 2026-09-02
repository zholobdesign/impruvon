"""Design language extracted from the Paper file 'Impruvon' / page 'Sitemap'.

Token values, chrome and section patterns are transcribed from the artboards,
not invented here. Keep this file the single source of visual truth.
"""

CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{
  --color-surface:#FFFFFF; --color-surface-sunk:#F1F1F1; --color-surface-deep:#2C3E50;
  --color-line:#DCE3E4; --color-rule:#D7DCDC;
  --color-ink:#2C3E50; --color-ink-muted:#5A6B78; --color-ink-faint:#8E9A9E; --color-ink-ondeep:#EAF1F2;
  --color-accent:#1D899A; --color-accent-hover:#166F7D; --color-accent-soft:#E3F1F3;
  --color-seafoam:#A3D9B1; --color-lime:#87B93C; --color-coral:#FFA87D;
  --flag-bg:#FFF4B8; --flag-border:#E0C24A; --flag-ink:#6B520A;
  --pad:120px; --page:1200px;
}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--color-surface);color:var(--color-ink);
  font:400 17px/1.6 system-ui,sans-serif;-webkit-font-smoothing:antialiased;font-synthesis:none}
a{color:inherit;text-decoration:none}
h1,h2,h3,h4{margin:0;font-weight:700}
p{margin:0}
.wrap{max-width:1440px;margin:0 auto}

/* ---------- annotation strip ---------- */
.annot{position:sticky;top:0;z-index:60;background:var(--color-surface-deep);color:var(--color-ink-ondeep);
  display:flex;align-items:center;justify-content:space-between;gap:16px;padding:12px 40px;flex-wrap:wrap}
.annot .aurl{font-size:12px;font-weight:500;letter-spacing:.12em;line-height:16px}
.annot .aleg{display:flex;align-items:center;gap:10px;font-size:12px;line-height:16px}
.annot .swatch{width:20px;height:12px;border-radius:3px;background:var(--flag-bg);border:1px solid var(--flag-border);flex-shrink:0}
.annot button{font:inherit;font-size:12px;font-weight:600;background:var(--color-ink-ondeep);color:var(--color-surface-deep);
  border:0;border-radius:999px;padding:4px 12px;cursor:pointer}
.annot a{color:var(--color-seafoam);text-decoration:underline}

/* ---------- nav ---------- */
.nav{display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap;
  padding:22px var(--pad);border-bottom:1px solid var(--color-line);background:var(--color-surface)}
.nav .brand{display:flex;align-items:center;gap:10px;font-size:22px;font-weight:700;letter-spacing:-.02em;line-height:28px}
.nav .mark{width:22px;height:22px;border-radius:6px;background:var(--color-accent);flex-shrink:0}
.nav .links{display:flex;align-items:center;gap:30px;flex-wrap:wrap}
.nav .links a{font-size:15px;line-height:18px}
.nav .links a.on{font-weight:700}
.nav .right{display:flex;align-items:center;gap:22px}
.nav .right .login{font-size:15px;color:var(--color-ink-muted)}
.pill{display:inline-flex;align-items:center;background:var(--color-accent);color:#fff;border-radius:999px;
  padding:11px 20px;font-size:15px;font-weight:500;line-height:18px}
.pill-lg{padding:17px 30px;font-size:17px;line-height:22px}
.pill-ghost{background:transparent;color:var(--color-ink);border:1px solid var(--color-rule);padding:16px 28px;
  font-size:17px;font-weight:500;line-height:22px}

/* ---------- sections ---------- */
.sec{padding:110px var(--pad);background:var(--color-surface)}
.sec-sunk{background:var(--color-surface-sunk)}
.sec-deep{background:var(--color-surface-deep);color:var(--color-surface)}
.sec-inner{max-width:var(--page);margin:0 auto}
.h2{font-size:44px;font-weight:700;letter-spacing:-.03em;line-height:52px;max-width:20ch}
.h2-wide{max-width:34ch}
.sec-deep .h2{color:var(--color-surface)}
.lede{font-size:20px;line-height:32px;color:var(--color-ink-muted)}

/* ---------- hero ---------- */
.hero{display:flex;align-items:center;justify-content:space-between;gap:80px;flex-wrap:wrap;
  padding:96px var(--pad) 104px}
.hero-copy{display:flex;flex-direction:column;gap:26px;max-width:640px;flex:1 1 520px}
.hero h1{font-size:62px;letter-spacing:-.035em;line-height:66px}
.hero .sub{font-size:20px;line-height:32px;color:var(--color-ink-muted);max-width:560px}
.hero .btns{display:flex;gap:14px;flex-wrap:wrap;padding-top:6px}
.hero .microrow{display:flex;gap:34px;flex-wrap:wrap;padding-top:12px}
.hero .microrow span{font-size:13px;line-height:19px;color:var(--color-ink-muted)}
.hero-visual{position:relative;width:480px;height:500px;border-radius:24px;background:var(--color-surface-sunk);flex-shrink:0}

/* MedBox mock */
.mbox{position:absolute;left:22px;top:46px;width:300px;background:#2C3E50;border-radius:20px;padding:22px 20px;
  display:flex;flex-direction:column;gap:16px}
.mbox .cap{display:flex;align-items:center;justify-content:space-between}
.mbox .cap b{font-size:12px;font-weight:500;letter-spacing:.12em;line-height:16px;color:#EAF1F2A6}
.mbox .led{width:8px;height:8px;border-radius:999px;background:var(--color-seafoam)}
.mbox .slots{display:flex;flex-direction:column;gap:10px;background:#EAF1F212;border-radius:12px;padding:16px 14px}
.mbox .srow{display:flex;gap:9px}
.mbox .slot{width:53px;height:26px;border-radius:4px;background:#EAF1F238}
.mbox .slot.on{background:var(--color-accent)}
.mbox .reader{display:flex;align-items:center;justify-content:space-between;background:#EAF1F21F;border-radius:10px;padding:14px 16px}
.mbox .rline{width:64px;height:8px;border-radius:999px;background:#EAF1F259}
.mbox .rtag{width:26px;height:18px;border-radius:3px;border:1px solid #EAF1F273}

/* eMAR mock */
.emar{position:absolute;left:192px;top:288px;width:262px;background:var(--color-surface);border:1px solid var(--color-line);
  border-radius:16px;padding:18px 18px 16px;display:flex;flex-direction:column;gap:14px;
  box-shadow:0 18px 40px #2C3E5029}
.emar .top{display:flex;align-items:center;justify-content:space-between}
.emar .top b{font-size:14px;line-height:18px}
.emar .top span{font-size:12px;line-height:16px;color:var(--color-ink-faint)}
.emar .rows{display:flex;flex-direction:column;gap:10px}
.emar .r{display:flex;align-items:center;gap:10px}
.emar .dot{width:18px;height:18px;border-radius:999px;background:var(--color-seafoam);flex-shrink:0}
.emar .dot.next{background:transparent;border:2px solid var(--color-accent)}
.emar .bar{height:8px;border-radius:999px;background:var(--color-surface-sunk)}
.emar .bar.on{background:var(--color-accent-soft)}
.emar .scan{display:flex;align-items:center;gap:9px;background:var(--color-accent-soft);border-radius:999px;padding:9px 12px}
.emar .scan i{width:7px;height:7px;border-radius:999px;background:var(--color-accent);flex-shrink:0}
.emar .scan span{font-size:12px;font-weight:500;line-height:16px;color:var(--color-accent-hover)}

/* ---------- numbers bar ---------- */
.numbers{display:flex;gap:24px;flex-wrap:wrap;justify-content:space-between;
  padding:44px var(--pad);border-top:1px solid var(--color-line);border-bottom:1px solid var(--color-line);
  background:var(--color-surface)}
.numbers .n{min-width:180px;flex:1}
.numbers .n b{display:block;font-size:34px;font-weight:700;letter-spacing:-.03em;line-height:40px;color:var(--color-accent)}
.numbers .n span{font-size:15px;line-height:22px;color:var(--color-ink-muted)}

/* ---------- generic grids ---------- */
.grid{display:grid;gap:24px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.g4{grid-template-columns:repeat(4,minmax(0,1fr))}
.stack-48{display:flex;flex-direction:column;gap:48px}
.stack-52{display:flex;flex-direction:column;gap:52px}
.stack-44{display:flex;flex-direction:column;gap:44px}

/* pain cards */
.pcard{border:1px solid var(--color-line);border-radius:16px;padding:34px 32px;display:flex;flex-direction:column;gap:14px}
.pcard .rule{width:32px;height:4px;border-radius:999px;background:var(--color-coral)}
.pcard h3{font-size:22px;letter-spacing:-.01em;line-height:29px;padding-top:8px}
.pcard p{font-size:17px;line-height:27px;color:var(--color-ink-muted)}

/* dark product cards */
.dcard{background:#EAF1F212;border-radius:16px;padding:34px 34px 30px;display:flex;flex-direction:column;gap:12px}
.dcard h3{font-size:25px;letter-spacing:-.01em;line-height:32px;color:var(--color-surface)}
.dcard .kick{font-size:18px;font-weight:500;line-height:27px;color:var(--color-seafoam)}
.dcard p{font-size:16px;line-height:26px;color:#EAF1F2B8}
.dcard .go{font-size:16px;font-weight:500;line-height:20px;color:var(--color-ink-ondeep);padding-top:8px}

/* audience cards */
.acard{border:1px solid var(--color-line);border-radius:16px;padding:28px 26px;display:flex;flex-direction:column;
  justify-content:space-between;gap:16px}
.acard h3{font-size:19px;letter-spacing:-.01em;line-height:26px}
.acard p{font-size:15px;line-height:24px;color:var(--color-ink-muted)}
.acard .go{font-size:15px;font-weight:500;line-height:18px;color:var(--color-accent-hover)}

/* state band */
.stateband{display:flex;align-items:center;justify-content:space-between;gap:40px;flex-wrap:wrap;
  background:var(--color-accent-soft);border:2px solid var(--color-accent);border-radius:16px;padding:36px 38px}
.stateband h3{font-size:24px;letter-spacing:-.01em;line-height:32px}
.stateband p{font-size:17px;line-height:27px;color:var(--color-ink-muted)}

/* numbered reasons */
.ncard{border-top:2px solid var(--color-accent);padding-top:26px;display:flex;flex-direction:column;gap:14px}
.ncard .num{font-size:13px;font-weight:500;letter-spacing:.12em;line-height:16px;color:var(--color-accent)}
.ncard h3{font-size:25px;letter-spacing:-.01em;line-height:33px}
.ncard p{font-size:17px;line-height:28px;color:var(--color-ink-muted)}

/* feature mini cards */
.fcard{display:flex;flex-direction:column;gap:10px}
.fcard .ico{width:34px;height:34px;border-radius:9px;background:var(--color-accent-soft)}
.fcard h3{font-size:18px;letter-spacing:-.01em;line-height:25px}
.fcard p{font-size:15px;line-height:24px;color:var(--color-ink-muted)}

/* quotes */
.quote{display:flex;gap:26px;align-items:flex-start;border-radius:18px;padding:46px 44px;background:var(--color-surface-deep)}
.quote .bar{width:4px;border-radius:2px;background:var(--color-seafoam);align-self:stretch;flex-shrink:0}
.quote p{font-size:27px;line-height:42px;color:var(--color-surface)}
.quote cite{display:block;margin-top:22px;font-style:normal;font-size:16px;font-weight:500;line-height:24px;color:#EAF1F2C7}
.quote-light{background:var(--color-surface-sunk)}
.quote-light p{color:var(--color-ink);font-size:24px;line-height:38px}
.quote-light .bar{background:var(--color-accent)}
.quote-light cite{color:var(--color-ink-muted)}

/* case cards */
.ccard{background:var(--color-surface);border-radius:18px;padding:40px 38px;display:flex;flex-direction:column;gap:18px}
.ccard .eyebrow{font-size:12px;font-weight:500;letter-spacing:.12em;line-height:16px;color:var(--color-ink-faint)}
.ccard .big{font-size:52px;font-weight:700;letter-spacing:-.04em;line-height:56px;color:var(--color-accent)}
.ccard p{font-size:20px;line-height:30px}
.ccard .go{font-size:16px;font-weight:500;line-height:20px;color:var(--color-accent-hover);padding-top:8px}

/* faq rows */
.faq{display:flex;flex-direction:column;max-width:var(--page)}
.faqrow{display:flex;gap:40px;align-items:flex-start;padding:30px 0;border-top:1px solid var(--color-line);flex-wrap:wrap}
.faqrow:last-child{border-bottom:1px solid var(--color-line)}
.faqrow .q{width:360px;flex-shrink:0;font-size:20px;font-weight:700;line-height:29px}
.faqrow .a{flex:1;min-width:320px;font-size:17px;line-height:28px;color:var(--color-ink-muted)}
.faqrow.flag{background:var(--flag-bg);border:1px solid var(--flag-border);border-radius:12px;padding:30px 24px;margin-top:24px}
.faqrow.flag:last-child{border-bottom:1px solid var(--flag-border)}
.faqrow.flag .a{color:var(--color-ink)}
.faqrow .go{display:block;margin-top:14px;font-size:16px;font-weight:500;color:var(--color-accent-hover)}

/* flags */
.flag-box{display:inline-flex;align-items:center;gap:10px;background:var(--flag-bg);border:1px solid var(--flag-border);
  border-radius:8px;padding:8px 14px;font-size:14px;font-weight:500;line-height:18px;color:var(--flag-ink)}

/* closing */
.closing{display:flex;flex-direction:column;gap:24px;align-items:flex-start}
.closing h2{font-size:56px;letter-spacing:-.035em;line-height:64px;max-width:900px}
.closing .line{font-size:22px;line-height:34px;color:var(--color-ink-muted);display:flex;gap:8px;align-items:center;flex-wrap:wrap}

/* forms */
.form{border:1px solid var(--color-line);border-radius:20px;padding:44px 42px;display:flex;flex-direction:column;gap:22px;
  flex:1 1 620px;max-width:740px}
.frow{display:flex;gap:20px;flex-wrap:wrap}
.fld{display:flex;flex-direction:column;gap:8px;flex:1 1 260px}
.fld label{font-size:14px;font-weight:500;line-height:18px}
.fld .input{height:50px;border-radius:10px;background:var(--color-surface-sunk)}
.fld .input.req{border:1px solid var(--color-accent)}
.tag-req{background:var(--color-accent-soft);color:var(--color-accent-hover);border-radius:5px;padding:3px 8px;
  font-size:11px;font-weight:500;letter-spacing:.06em;line-height:14px}
.proofcol{width:400px;flex-shrink:0;padding-top:12px}
.proofcol .p{padding:24px 0;border-bottom:1px solid var(--color-line);display:flex;flex-direction:column;gap:8px}
.proofcol .p:last-child{border-bottom:0}
.proofcol .p b{font-size:34px;font-weight:700;letter-spacing:-.03em;line-height:40px;color:var(--color-accent)}
.proofcol .p .t{font-size:18px;font-weight:700;line-height:26px}
.proofcol .p span{font-size:16px;line-height:24px;color:var(--color-ink-muted)}

/* tables */
.tablewrap{overflow-x:auto;border:1px solid var(--color-line);border-radius:16px}
table{border-collapse:collapse;width:100%;font-size:16px;min-width:720px}
th,td{border-bottom:1px solid var(--color-line);padding:16px 20px;text-align:left;vertical-align:top}
th{background:var(--color-surface-sunk);font-size:12px;letter-spacing:.12em;font-weight:500;color:var(--color-ink-muted)}
tbody tr:last-child td{border-bottom:0}

/* lists */
.ticks{margin:0;padding:0;list-style:none;max-width:74ch}
.ticks li{position:relative;padding:14px 0 14px 30px;border-bottom:1px solid var(--color-line);font-size:17px;line-height:27px}
.ticks li::before{content:"";position:absolute;left:0;top:22px;width:14px;height:2px;border-radius:2px;background:var(--color-accent)}

/* link list */
.linklist{display:flex;flex-direction:column;max-width:var(--page)}
.linklist a{padding:16px 0;border-bottom:1px solid var(--color-line);font-size:17px;font-weight:500}
.linklist a:hover{color:var(--color-accent-hover)}

/* notes */
.notes{display:none;background:var(--flag-bg);border:1px solid var(--flag-border);border-radius:12px;
  padding:24px 26px;margin:28px auto 0;max-width:var(--page)}
.notes h4{font-size:12px;letter-spacing:.12em;color:var(--flag-ink);margin-bottom:12px}
.notes ul{margin:0;padding-left:20px}
.notes li{font-size:15px;line-height:24px;color:var(--flag-ink);margin-bottom:8px}
body.shownotes .notes{display:block}

/* footer */
.foot{background:var(--color-surface-deep);border-top:1px solid #EAF1F229;padding:56px var(--pad) 64px;
  display:flex;gap:60px;justify-content:space-between;flex-wrap:wrap;align-items:flex-start}
.foot .fbrand{width:300px;display:flex;flex-direction:column;gap:14px}
.foot .fbrand .row{display:flex;align-items:center;gap:10px}
.foot .fbrand .mark{width:20px;height:20px;border-radius:6px;background:var(--color-accent)}
.foot .fbrand b{font-size:20px;font-weight:700;letter-spacing:-.02em;line-height:24px;color:#fff}
.foot .fbrand p{font-size:14px;line-height:22px;color:#EAF1F29E}
.foot .col{display:flex;flex-direction:column;gap:12px}
.foot .col h4{font-size:12px;font-weight:500;letter-spacing:.12em;line-height:16px;color:#EAF1F280}
.foot .col a{font-size:15px;line-height:18px;color:#EAF1F2D9}
.foot .col a:hover{color:#fff}

@media (max-width:1240px){ :root{--pad:56px} .hero h1{font-size:48px;line-height:54px} .h2,.closing h2{font-size:34px;line-height:42px} }
@media (max-width:900px){
  :root{--pad:20px}
  .sec{padding:64px var(--pad)}
  .hero{padding:56px var(--pad) 64px;gap:40px}
  .hero h1{font-size:36px;line-height:42px}
  .hero-visual{width:100%;max-width:480px;height:460px}
  .g2,.g3,.g4{grid-template-columns:1fr}
  .faqrow .q{width:100%}
  .proofcol{width:100%}
  .quote p{font-size:20px;line-height:32px}
  .ccard .big{font-size:40px;line-height:44px}
  .nav .links{gap:16px;order:3;width:100%}
}
:focus-visible{outline:2px solid var(--color-accent);outline-offset:3px}
"""

JS = """
(function(){
  var KEY='impruvon-proto-notes';
  var btn=document.getElementById('notesToggle');
  function apply(on){
    document.body.classList.toggle('shownotes',on);
    if(btn) btn.textContent = on ? 'Hide notes' : 'Show notes';
  }
  var on=false;
  try{ on = localStorage.getItem(KEY)==='1'; }catch(e){}
  apply(on);
  if(btn) btn.addEventListener('click',function(){
    on=!on; apply(on);
    try{ localStorage.setItem(KEY,on?'1':'0'); }catch(e){}
  });
})();
"""
