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

CSS += """
/* ---------- transcribed page patterns ---------- */
.phead{padding:96px var(--pad) 100px}
.phead .kicker{font-size:13px;font-weight:500;letter-spacing:.12em;line-height:16px;color:var(--color-accent);margin-bottom:26px}
.phead-h1{font-size:60px;font-weight:700;letter-spacing:-.035em;line-height:66px;max-width:1000px}
.phead-lede{font-size:22px;line-height:34px;color:var(--color-ink-muted);max-width:820px;margin-top:26px}
.phead .flag-box{margin-top:26px}
.phead .pill{margin-top:26px}

.twocol{display:flex;gap:80px;align-items:flex-start;flex-wrap:wrap}
.twocol-h{width:320px;flex-shrink:0;font-size:34px;font-weight:700;letter-spacing:-.02em;line-height:42px}
.twocol-body{flex:1;min-width:320px;display:flex;flex-direction:column;gap:26px}
.twocol-p{font-size:22px;line-height:36px}

.chain{display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap}
.chain-box{flex:1 1 190px;min-height:96px;border-radius:12px;background:var(--color-surface);
  border:1px solid var(--color-line);display:flex;flex-direction:column;align-items:center;
  justify-content:center;gap:6px;padding:12px}
.chain-box b{font-size:18px;line-height:22px}
.chain-box span{font-size:13px;line-height:16px;color:var(--color-ink-faint)}
.chain-box.dark{background:var(--color-surface-deep);border-color:var(--color-surface-deep)}
.chain-box.dark b{color:var(--color-surface)}
.chain-box.dark span{color:#EAF1F2B3}
.chain-arrow{font-size:22px;font-style:normal;font-weight:500;color:var(--color-accent);flex-shrink:0}
.chain-rule{height:2px;border-radius:2px;background:var(--color-accent);margin-top:26px}
.chain-cap{margin-top:10px;font-size:15px;font-weight:500;letter-spacing:.06em;line-height:18px;color:var(--color-accent-hover)}

.bcard{border:1px solid var(--color-line);border-radius:16px;padding:34px 32px;display:flex;
  flex-direction:column;gap:14px;background:var(--color-surface)}
.bcard h3{font-size:25px;letter-spacing:-.01em;line-height:32px}
.bcard .kick{font-size:18px;font-weight:500;line-height:27px;color:var(--color-accent-hover)}
.bcard p{font-size:17px;line-height:27px;color:var(--color-ink-muted)}
.bcard .go{font-size:16px;font-weight:500;line-height:20px;color:var(--color-accent-hover);padding-top:6px}
a.bcard:hover{border-color:var(--color-accent)}

.flagbox{background:var(--flag-bg);border:1px dashed #D9B84A;border-radius:16px;padding:32px 32px 30px;
  display:flex;flex-wrap:wrap;gap:24px;justify-content:space-between}
.fstat{flex:1 1 220px}
.fstat b{display:block;font-size:44px;font-weight:700;letter-spacing:-.04em;line-height:48px}
.fstat span{font-size:16px;line-height:24px}
.fstat-note{flex-basis:100%;font-size:14px;line-height:22px;color:var(--flag-ink)}

.darkbar{background:var(--color-surface-deep);display:flex;flex-wrap:wrap;gap:20px;
  justify-content:space-between;padding:34px var(--pad);border-bottom:1px solid #EAF1F229}
.darkbar span{flex:1 1 150px;font-size:14px;line-height:21px;color:#EAF1F2D9}

.closing-dark{text-align:center;padding:96px var(--pad) 100px}
.closing-dark h2{font-size:48px;letter-spacing:-.03em;line-height:58px;color:var(--color-surface);
  max-width:820px;margin:0 auto}
.closing-sub{font-size:20px;line-height:32px;color:#EAF1F2C7;max-width:700px;margin:20px auto 0}
.closing-dark .pill{margin-top:30px}

.formwrap{display:flex;gap:60px;align-items:flex-start;justify-content:space-between;flex-wrap:wrap}
.fld label{display:flex;align-items:center;gap:8px}
"""

CSS += """
.splithero{display:flex;align-items:center;justify-content:space-between;gap:80px;flex-wrap:wrap;
  padding:88px var(--pad) 96px}
.splithero .copy{flex:1 1 520px;max-width:620px;display:flex;flex-direction:column;gap:24px;align-items:flex-start}
.splithero h1{font-size:56px;letter-spacing:-.035em;line-height:62px}
.splithero .sub{font-size:22px;line-height:34px;color:var(--color-ink-muted)}
.photoslot{width:500px;max-width:100%;height:480px;border:1px dashed #D9B84A;border-radius:20px;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;flex-shrink:0;padding:24px}
.photoslot .box{width:230px;height:280px;max-width:100%;border:2px dashed #C4A43A;border-radius:14px}
.photoslot .cap{width:360px;max-width:100%;text-align:center;font-size:12px;font-weight:500;
  letter-spacing:.08em;line-height:20px;color:#8A6B12}

.spectable{border-top:2px solid var(--color-ink)}
.specrow{display:flex;gap:40px;padding:18px 4px;border-bottom:1px solid var(--color-line);flex-wrap:wrap}
.specrow b{width:300px;flex-shrink:0;font-size:17px;font-weight:500;line-height:26px}
.specrow span{flex:1;min-width:240px;font-size:17px;line-height:26px;color:var(--color-ink-muted)}

.duo{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}
.duocard{background:var(--color-surface);border-radius:18px;padding:44px 40px;display:flex;flex-direction:column;gap:18px}
.duocard h3{font-size:30px;letter-spacing:-.02em;line-height:38px}
.duocard p{font-size:18px;line-height:29px;color:var(--color-ink-muted)}
.duocard.dark{background:var(--color-surface-deep)}
.duocard.dark h3{color:var(--color-surface)}
.duocard.dark p{color:#EAF1F2D1}

.steps3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.step{background:var(--color-surface-sunk);border-radius:14px;padding:30px 28px;display:flex;flex-direction:column;gap:12px}
.step .num{font-size:13px;font-weight:500;letter-spacing:.12em;line-height:16px;color:var(--color-accent)}
.step p{font-size:19px;line-height:29px}

.faqcards{display:flex;flex-direction:column;gap:12px}
.faqcard{display:flex;gap:40px;background:var(--color-surface);border-radius:12px;padding:28px 26px;flex-wrap:wrap}
.faqcard .q{width:360px;flex-shrink:0;font-size:19px;font-weight:700;line-height:28px}
.faqcard .a{flex:1;min-width:280px;font-size:17px;line-height:27px;color:var(--color-ink-muted)}

.annot .badge{background:var(--flag-bg);color:var(--flag-ink);border-radius:6px;padding:4px 10px;
  font-size:11px;font-weight:500;letter-spacing:.08em;line-height:14px}
@media (max-width:900px){ .duo,.steps3{grid-template-columns:1fr} .splithero{padding:56px var(--pad)}
  .splithero h1{font-size:34px;line-height:42px} .photoslot{height:360px} .specrow b{width:100%} }
"""

CSS += """
.bigfeat{background:var(--color-accent-soft);border-radius:18px;padding:38px 36px;display:flex;flex-direction:column;gap:20px}
.bigfeat .ico{width:52px;height:52px;border-radius:14px;background:var(--color-accent);opacity:.16}
.bigfeat h3{font-size:26px;line-height:34px}
.bigfeat p{font-size:19px;line-height:30px;color:var(--color-ink-muted)}
.bullets{border-top:1px solid var(--color-line)}
.bullets .b{display:flex;gap:14px;align-items:flex-start;padding:18px 0;border-bottom:1px solid var(--color-line)}
.bullets .b i{width:7px;height:7px;border-radius:999px;background:var(--color-accent);flex-shrink:0;margin-top:9px}
.bullets .b span{font-size:17px;line-height:26px}
.numlist{border-top:2px solid var(--color-ink)}
.numlist .r{display:flex;gap:16px;align-items:flex-start;padding:20px 0;border-bottom:1px solid var(--color-line)}
.numlist .r b{width:26px;flex-shrink:0;font-size:13px;font-weight:500;letter-spacing:.12em;line-height:16px;
  color:var(--color-accent);padding-top:4px}
.numlist .r span{font-size:18px;line-height:27px}
.checks{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
.check{display:flex;gap:16px;align-items:flex-start;background:var(--color-surface);border-radius:14px;padding:26px 28px}
.check svg{flex-shrink:0}
.check span{font-size:17px;line-height:26px}
.statcards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}
.statcard{background:var(--color-surface);border-radius:18px;padding:38px 36px;display:flex;flex-direction:column;gap:16px}
.statcard b{font-size:50px;font-weight:700;letter-spacing:-.04em;line-height:54px;color:var(--color-accent)}
.statcard p{font-size:20px;line-height:30px}
.statcard .src{font-size:13px;line-height:20px;color:var(--color-ink-faint)}
@media (max-width:900px){ .checks,.statcards{grid-template-columns:1fr} }
"""

CSS += """
.softcard{background:var(--color-accent-soft);border-radius:16px;padding:32px 30px;display:flex;flex-direction:column;gap:12px}
.softcard h3{font-size:22px;line-height:30px}
.softcard p{font-size:17px;line-height:27px;color:var(--color-ink-muted)}
.ctarow{display:flex;align-items:center;justify-content:space-between;gap:80px;flex-wrap:wrap}
.ctarow .t{max-width:760px;display:flex;flex-direction:column;gap:20px}
.ctarow h2{font-size:38px;letter-spacing:-.03em;line-height:48px}
.ctarow p{font-size:19px;line-height:30px;color:var(--color-ink-muted)}
.ctarow .go{font-size:17px;font-weight:500;line-height:22px;color:var(--color-accent-hover);flex-shrink:0}
.eyebrow-accent{font-size:20px;font-weight:700;letter-spacing:.02em;line-height:28px;color:var(--color-accent)}
"""

CSS += """
.dotcard{display:flex;gap:16px;align-items:flex-start;border:1px solid var(--color-line);border-radius:14px;padding:28px 30px}
.dotcard i{width:8px;height:8px;border-radius:999px;background:var(--color-accent);flex-shrink:0;margin-top:9px}
.dotcard span{font-size:18px;line-height:28px}
.splitstat{display:flex;align-items:center;justify-content:space-between;gap:80px;flex-wrap:wrap}
.splitstat .t{flex:1 1 480px;max-width:640px;display:flex;flex-direction:column;gap:24px}
.splitstat h2{font-size:44px;letter-spacing:-.03em;line-height:54px}
.splitstat p{font-size:20px;line-height:32px;color:var(--color-ink-muted)}
.statbox{display:flex;align-items:center;justify-content:center;gap:24px;background:var(--color-surface);
  border-radius:18px;padding:44px 40px;flex:0 1 440px}
.statbox .cell{display:flex;flex-direction:column;align-items:center;gap:6px}
.statbox .cell b{font-size:52px;font-weight:700;letter-spacing:-.04em;line-height:56px;color:var(--color-accent)}
.statbox .cell span{font-size:15px;line-height:18px;color:var(--color-ink-muted)}
.statbox .div{width:1px;height:80px;background:var(--color-line)}
.prose h2{font-size:44px;letter-spacing:-.03em;line-height:54px;max-width:1000px}
.prose .sub{font-size:22px;line-height:34px;color:var(--color-ink-muted);max-width:860px;margin-top:30px}
.prose .body{font-size:18px;line-height:30px;max-width:900px;margin-top:30px}
"""

CSS += """
.sec-deep .twocol-h{color:var(--color-surface)}
.sec-deep .twocol-p{color:#EAF1F2D1}
.nbar{display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;padding:64px var(--pad)}
.nbar .n{flex:1 1 200px}
.nbar .n b{display:block;font-size:42px;font-weight:700;letter-spacing:-.04em;line-height:46px}
.nbar .n span{font-size:16px;line-height:24px;color:var(--color-ink-muted)}
.closing-light{background:var(--color-surface);text-align:center;padding:100px var(--pad)}
.closing-light h2{font-size:46px;letter-spacing:-.03em;line-height:56px;max-width:900px;margin:0 auto;color:var(--color-ink)}
.closing-light .pill{margin-top:30px}
"""

CSS += """
.darkline{display:inline-flex;background:var(--color-surface-deep);border-radius:12px;padding:20px 28px;
  font-size:20px;font-weight:500;line-height:30px;color:var(--color-surface);max-width:100%}
.sunkcard{background:var(--color-surface-sunk);border-radius:16px;padding:32px 30px;display:flex;flex-direction:column;gap:12px}
.sunkcard h3{font-size:21px;line-height:29px}
.sunkcard p{font-size:17px;line-height:27px;color:var(--color-ink-muted)}
.wide{grid-column:1/-1}
.centertext{max-width:1000px;margin:0 auto;text-align:center;font-size:24px;line-height:40px}
.g3.statcards3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.scard{border:1px solid var(--color-line);border-radius:16px;padding:34px 32px;display:flex;flex-direction:column;gap:14px}
.scard b{font-size:44px;font-weight:700;letter-spacing:-.04em;line-height:50px;color:var(--color-accent)}
.scard span{font-size:18px;line-height:28px}
@media (max-width:900px){ .g3.statcards3{grid-template-columns:1fr} .centertext{font-size:19px;line-height:31px} }
"""

CSS += """
.contrast{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}
.contrast .col{display:flex;flex-direction:column;gap:22px}
.contrast .col p{font-size:19px;line-height:32px;color:var(--color-ink-muted)}
.contrast .col p.strong{color:var(--color-ink);font-weight:500}
.contrast .dark{background:var(--color-surface-deep);border-radius:18px;padding:36px 34px}
.contrast .dark p{color:#EAF1F2D9}
.contrast .dark p.big{font-size:22px;line-height:34px;font-weight:500;color:var(--color-surface)}
@media (max-width:900px){ .contrast{grid-template-columns:1fr} }
"""

CSS += """
.highlight{display:flex;align-items:center;gap:28px;background:var(--color-accent-soft);
  border:2px solid var(--color-accent);border-radius:16px;padding:38px 36px;grid-column:1/-1}
.highlight svg{flex-shrink:0}
.highlight h3{font-size:23px;line-height:31px;margin-bottom:10px}
.highlight p{font-size:18px;line-height:28px}
"""

CSS += """
.flagprose{background:var(--flag-bg);border:1px solid var(--flag-border);border-radius:14px;padding:26px 28px;
  display:flex;flex-direction:column;gap:14px}
.flagprose.dashed{border-style:dashed;border-color:#D9B84A;padding:34px}
.flagprose .note{font-size:12px;font-weight:500;letter-spacing:.12em;line-height:20px;color:#8A6B12}
.flagprose p{font-size:21px;line-height:34px}
.flagprose p.small{font-size:19px;line-height:30px;font-weight:500}
"""

CSS += """
.sidedark{background:var(--color-surface-deep);border-radius:18px;padding:36px 34px;display:flex;
  flex-direction:column;gap:26px;width:400px;flex-shrink:0}
.sidedark p{font-size:18px;line-height:29px;color:#EAF1F2E0}
.sidedark p.strong{color:var(--color-surface);font-weight:500}
.sidedark .rule{height:1px;background:#EAF1F233}
@media (max-width:900px){ .sidedark{width:100%} }
"""

CSS += """
.flagtable{background:var(--flag-bg);border:1px dashed #D9B84A;border-radius:16px;padding:26px;
  display:flex;flex-direction:column;gap:18px}
.flagtable .note{font-size:12px;font-weight:500;letter-spacing:.12em;line-height:20px;color:var(--flag-ink)}
.flagtable .inner{background:var(--color-surface);border-radius:12px;overflow-x:auto}
.flagtable table{min-width:900px;border-collapse:collapse;width:100%}
.flagtable th,.flagtable td{padding:16px 20px;text-align:left;border-bottom:1px solid var(--color-line);vertical-align:middle}
.flagtable th{font-size:12px;letter-spacing:.1em;font-weight:500;color:var(--color-ink-faint);background:transparent}
.flagtable th.us{font-size:13px;letter-spacing:.04em;font-weight:700;color:var(--color-accent)}
.flagtable td{font-size:16px;line-height:24px}
.flagtable td.us{font-size:16px;font-weight:500;color:var(--color-accent)}
.flagtable tbody tr:last-child td{border-bottom:0}
"""

CSS += """
.faqcard.flag{background:var(--flag-bg);border:1px solid var(--flag-border)}
.faqcard.flag .a{color:#8A6B12}
.smallcta{display:flex;flex-direction:column;align-items:flex-start;gap:24px}
.smallcta h2{font-size:36px;letter-spacing:-.03em;line-height:46px}
"""

CSS += """
.filters{display:flex;align-items:center;gap:40px;flex-wrap:wrap}
.filters .f{display:flex;align-items:center;gap:12px}
.filters .lbl{font-size:13px;font-weight:500;letter-spacing:.1em;line-height:16px;color:var(--color-ink-faint)}
.filters .sel{display:flex;align-items:center;gap:10px;background:var(--color-surface-sunk);border-radius:8px;padding:10px 16px;font-size:15px}
.filters .sel i{font-style:normal;font-size:13px;color:var(--color-ink-faint)}
.filters .search{width:300px;max-width:100%;border:1px solid var(--color-rule);border-radius:8px;padding:10px 16px;
  font-size:15px;color:var(--color-ink-faint)}
.rescards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.rescard{background:var(--color-surface);border-radius:14px;padding:26px 24px;display:flex;flex-direction:column;
  justify-content:space-between;gap:18px}
.rescard .tags{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px}
.rescard .tag{font-size:11px;font-weight:500;letter-spacing:.08em;line-height:14px;border-radius:5px;padding:4px 10px;
  background:var(--color-accent-soft);color:var(--color-accent-hover)}
.rescard .tag.alt{background:var(--color-surface-sunk);color:var(--color-ink-muted)}
.rescard h3{font-size:20px;line-height:29px}
.rescard .meta{font-size:14px;line-height:18px;color:var(--color-ink-faint);margin-top:14px}
.rescard .go{font-size:14px;font-weight:500;line-height:18px;color:var(--color-accent-hover)}
.darkband{display:flex;align-items:center;justify-content:space-between;gap:40px;flex-wrap:wrap;
  background:var(--color-surface-deep);border-radius:16px;padding:34px 36px}
.darkband h3{font-size:24px;line-height:32px;color:var(--color-surface);margin-bottom:8px}
.darkband p{font-size:17px;line-height:26px;color:#EAF1F2C7}
.darkband .go{font-size:16px;font-weight:500;color:var(--color-seafoam);flex-shrink:0}
@media (max-width:900px){ .rescards{grid-template-columns:1fr} }
"""

CSS += """
.caserow{display:flex;border:1px solid var(--color-line);border-radius:18px;overflow:hidden;background:var(--color-surface);flex-wrap:wrap}
.caserow .metric{width:380px;flex-shrink:0;background:var(--color-accent-soft);padding:52px 36px;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;text-align:center}
.caserow .metric b{font-size:52px;font-weight:700;letter-spacing:-.03em;line-height:64px;color:var(--color-accent-hover)}
.caserow .metric span{font-size:16px;line-height:24px;color:var(--color-ink-muted)}
.caserow .body{flex:1;min-width:320px;padding:48px 44px;display:flex;flex-direction:column;justify-content:center;gap:18px}
.caserow .tags{display:flex;gap:8px;flex-wrap:wrap}
.caserow .tag{font-size:11px;font-weight:500;letter-spacing:.08em;line-height:14px;background:var(--color-surface-sunk);
  color:var(--color-ink-muted);border-radius:5px;padding:5px 11px}
.caserow h3{font-size:30px;letter-spacing:-.02em;line-height:39px}
.caserow p{font-size:17px;line-height:27px;color:var(--color-ink-muted)}
.caserow .go{font-size:16px;font-weight:500;color:var(--color-accent-hover)}
.caserow.flag{background:var(--flag-bg);border:1px dashed #D9B84A}
.caserow.flag .metric{background:#FFFFFF8C}
.caserow.flag .metric b,.caserow.flag .metric span{color:#8A6B12}
.caserow.flag .tag{background:#FFFFFFB3;color:var(--flag-ink)}
.caserow.flag h3{color:var(--flag-ink)}
.caserow.flag p{color:#8A6B12}
.caserow.flag .go{color:#8A6B12}
.ruleblock{background:var(--flag-bg);border:1px dashed #D9B84A;border-radius:12px;padding:22px 26px;
  display:flex;flex-direction:column;gap:8px}
.ruleblock b{font-size:12px;font-weight:500;letter-spacing:.12em;line-height:20px;color:var(--flag-ink)}
.ruleblock p{font-size:15px;line-height:24px;color:var(--flag-ink)}
@media (max-width:900px){ .caserow .metric{width:100%;padding:32px} .caserow .body{padding:28px} }
"""

CSS += """
.casemeta{display:flex;flex-wrap:wrap;gap:24px;padding-top:26px;border-top:1px solid var(--color-line)}
.casemeta .m{flex:1 1 200px;display:flex;flex-direction:column;gap:7px}
.casemeta .m b{font-size:12px;font-weight:500;letter-spacing:.1em;line-height:16px;color:var(--color-ink-faint)}
.casemeta .m span{font-size:17px;font-weight:500;line-height:22px}
.notebox{background:var(--flag-bg);border:1px dashed #D9B84A;border-radius:12px;padding:18px 22px;
  font-size:14px;line-height:22px;color:var(--flag-ink)}
.labelsplit{display:flex;gap:80px;align-items:flex-start;flex-wrap:wrap}
.labelsplit .l{width:520px;flex:1 1 380px;display:flex;flex-direction:column;gap:18px}
.labelsplit .lab{font-size:12px;font-weight:500;letter-spacing:.12em;line-height:16px;color:var(--color-accent-hover)}
.labelsplit h2{font-size:36px;letter-spacing:-.025em;line-height:46px}
.labelsplit .r{flex:1 1 420px;display:flex;flex-direction:column;gap:20px}
.labelsplit .r p{font-size:18px;line-height:30px;color:var(--color-ink-muted)}
.coralist{display:flex;flex-direction:column;gap:14px}
.coralist .i{display:flex;gap:14px;align-items:flex-start}
.coralist .i i{width:7px;height:7px;border-radius:999px;background:var(--color-coral);flex-shrink:0;margin-top:10px}
.coralist .i span{font-size:17px;line-height:27px}
.numsteps{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.numstep{border:1px solid var(--color-line);border-radius:16px;padding:32px 28px;display:flex;flex-direction:column;gap:16px}
.numstep .n{width:38px;height:38px;border-radius:999px;background:var(--color-accent-soft);display:flex;
  align-items:center;justify-content:center;font-size:16px;font-weight:700;color:var(--color-accent-hover)}
.numstep h3{font-size:22px;line-height:30px}
.numstep p{font-size:16px;line-height:26px;color:var(--color-ink-muted)}
.rescard3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.rc{border-radius:16px;padding:32px 28px;display:flex;flex-direction:column;gap:12px;background:#FFFFFF12}
.rc b{font-size:44px;font-weight:700;letter-spacing:-.03em;line-height:54px;color:var(--color-seafoam)}
.rc p{font-size:17px;line-height:27px;color:#EAF1F2D1}
.rc.flag{background:var(--flag-bg)}
.rc.flag b{color:#8A6B12}
.rc.flag p{color:var(--flag-ink)}
.quoteflag{background:var(--flag-bg);border:1px dashed #D9B84A;border-radius:16px;padding:38px 40px;
  display:flex;flex-direction:column;gap:24px}
.quoteflag .q{font-size:26px;line-height:40px;color:var(--flag-ink)}
.quoteflag .by b{display:block;font-size:16px;font-weight:500;line-height:20px;color:var(--flag-ink)}
.quoteflag .by span{font-size:15px;line-height:18px;color:#8A6B12}
.quoteflag .warn{font-size:14px;line-height:22px;color:#8A6B12}
@media (max-width:900px){ .numsteps,.rescard3{grid-template-columns:1fr} .labelsplit h2{font-size:28px;line-height:36px} }
"""

CSS += """
.storyflag{background:var(--flag-bg);border:1px dashed #D9B84A;border-radius:20px;padding:52px 56px;
  display:flex;flex-direction:column;gap:26px}
.storyflag .note{font-size:12px;font-weight:500;letter-spacing:.12em;line-height:20px;color:var(--flag-ink)}
.storyflag .lead{font-size:24px;line-height:40px}
.storyflag .body{font-size:20px;line-height:34px}
.storyflag .kicker2{font-size:24px;line-height:36px;font-weight:500}
@media (max-width:900px){ .storyflag{padding:28px 24px} .storyflag .lead{font-size:19px;line-height:31px} }
"""

CSS += """
.routecard{border:1px solid var(--color-line);border-radius:14px;padding:28px 26px;display:flex;
  flex-direction:column;gap:10px}
.routecard h3{font-size:19px;line-height:27px}
.routecard p{font-size:16px;line-height:25px;color:var(--color-ink-muted)}
.routecard.new{background:var(--color-accent-soft);border:2px solid var(--color-accent)}
.routecard .newtag{align-self:flex-start;background:var(--color-accent);color:#fff;border-radius:6px;
  padding:4px 10px;font-size:11px;font-weight:500;letter-spacing:.08em;line-height:14px}
.contactside{width:440px;flex-shrink:0;background:var(--flag-bg);border:1px dashed #D9B84A;border-radius:18px;
  padding:36px 34px;display:flex;flex-direction:column;gap:22px}
.contactside .note{font-size:12px;font-weight:500;letter-spacing:.12em;line-height:20px;color:var(--flag-ink)}
.contactside h3{font-size:19px;line-height:27px}
.contactside .addr{font-size:17px;line-height:27px;color:#8A6B12}
.contactside .rule{height:1px;background:#8A6B124D}
.contactside .row{display:flex;gap:12px}
.contactside .row b{width:80px;flex-shrink:0;font-size:15px;font-weight:500;line-height:18px}
.contactside .row span{font-size:15px;line-height:18px;color:#8A6B12}
@media (max-width:900px){ .contactside{width:100%} }
"""

CSS += """
.joblist{background:var(--flag-bg);border:1px dashed #D9B84A;border-radius:16px;padding:40px 36px;
  display:flex;flex-direction:column;gap:20px}
.joblist .note{font-size:12px;font-weight:500;letter-spacing:.12em;line-height:20px;color:var(--flag-ink)}
.job{display:flex;align-items:center;justify-content:space-between;gap:20px;background:var(--color-surface);
  border-radius:12px;padding:24px 26px}
.job b{display:block;font-size:19px;line-height:24px;color:var(--color-ink-faint)}
.job span{font-size:15px;line-height:18px;color:var(--color-ink-faint)}
.job i{font-style:normal;font-size:16px;color:var(--color-ink-faint)}
.stub{background:var(--flag-bg);border:1px dashed #D9B84A;border-radius:16px;padding:32px 34px;
  display:flex;flex-direction:column;gap:12px}
.stub b{font-size:12px;font-weight:500;letter-spacing:.12em;color:var(--flag-ink)}
.stub p{font-size:17px;line-height:27px;color:var(--flag-ink)}
"""

CSS += """
/* ---------- nav dropdowns ---------- */
.nav .links{gap:0}
.navitem{position:relative}
.navitem > a.top{display:inline-flex;align-items:center;gap:7px;font-size:15px;line-height:18px;
  color:var(--color-ink);padding:12px 15px;border-radius:8px}
.navitem > a.top.on{font-weight:700}
.navitem > a.top:hover{background:var(--color-surface-sunk)}
.caret{width:7px;height:7px;border-right:1.6px solid var(--color-ink-faint);
  border-bottom:1.6px solid var(--color-ink-faint);transform:rotate(45deg) translate(-1px,-1px);
  transition:transform .12s ease}
.navitem.has-sub:hover .caret,.navitem.has-sub:focus-within .caret{
  transform:rotate(225deg) translate(-2px,-2px);border-color:var(--color-accent)}
.sub{position:absolute;top:100%;left:50%;transform:translateX(-50%);z-index:70;padding-top:10px;
  opacity:0;visibility:hidden;transition:opacity .12s ease}
.navitem.has-sub:hover .sub,.navitem.has-sub:focus-within .sub{opacity:1;visibility:visible}
.subinner{background:var(--color-surface);border:1px solid var(--color-line);border-radius:14px;padding:8px;
  min-width:268px;box-shadow:0 18px 40px rgba(44,62,80,.16);display:flex;flex-direction:column}
.subinner a{display:block;padding:11px 14px;border-radius:9px;font-size:15px;line-height:20px;color:var(--color-ink)}
.subinner a:hover{background:var(--color-accent-soft);color:var(--color-accent-hover)}
@media (max-width:900px){
  .nav .links{gap:2px 10px}
  .navitem > a.top{padding:8px 8px;font-size:14px}
  .caret,.sub{display:none}
}
"""

CSS += """
.tracks{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.track{display:flex;flex-direction:column;justify-content:space-between;gap:22px;border:1px solid var(--color-line);
  border-radius:18px;padding:34px 32px;background:var(--color-surface)}
.track .who{font-size:12px;font-weight:500;letter-spacing:.1em;line-height:16px;color:var(--color-accent-hover)}
.track h3{font-size:25px;letter-spacing:-.01em;line-height:32px;margin-top:12px}
.track p{font-size:17px;line-height:27px;color:var(--color-ink-muted);margin-top:12px}
.track .go{font-size:16px;font-weight:500;color:var(--color-accent-hover)}
a.track:hover{border-color:var(--color-accent)}
.artmeta{display:flex;gap:24px;flex-wrap:wrap;font-size:15px;line-height:22px;color:var(--color-ink-faint)}
@media (max-width:900px){ .tracks{grid-template-columns:1fr} }
"""
