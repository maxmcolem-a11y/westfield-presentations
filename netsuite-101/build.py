#!/usr/bin/env python3
"""Build script for NetSuite 101 presentation."""

CSS = """
/* ============================================================
   THEME: Westfield Outdoors — Navy Blue Professional
   Light backgrounds, navy/dark-blue accents, black text
   Clean, studious, corporate-training aesthetic
   ============================================================ */
:root {
    --navy:        #1a2b4a;
    --navy-dark:   #0f1b30;
    --navy-mid:    #1e3461;
    --accent:      #2563eb;
    --accent-lt:   #3b82f6;
    --gold:        #b8860b;
    --gold-lt:     #d4a017;
    --white:       #ffffff;
    --off-white:   #f6f8fb;
    --gray-50:     #f9fafb;
    --gray-100:    #f0f2f7;
    --gray-200:    #dde3ef;
    --gray-400:    #8898b0;
    --gray-600:    #475569;
    --black:       #111827;
    --green:       #15803d;
    --red:         #dc2626;
    --orange:      #d97706;

    /* Typography — all clamp() */
    --fs-title:   clamp(1.8rem,  5vw,  3.8rem);
    --fs-h2:      clamp(1.25rem, 3vw,  2.2rem);
    --fs-h3:      clamp(1rem,    2vw,  1.5rem);
    --fs-body:    clamp(0.8rem,  1.4vw, 1.05rem);
    --fs-small:   clamp(0.68rem, 1vw,  0.85rem);
    --fs-label:   clamp(0.6rem,  0.8vw, 0.75rem);
    --fs-big:     clamp(1.4rem,  3.5vw, 2.8rem);
    --fs-mono:    clamp(0.72rem, 1.1vw, 0.9rem);

    /* Spacing — all clamp() */
    --pad-h:      clamp(1.5rem, 4vw,  4.5rem);
    --pad-v:      clamp(0.8rem, 1.8vh, 2rem);
    --gap:        clamp(0.6rem, 1.4vw, 1.4rem);
    --gap-sm:     clamp(0.3rem, 0.7vw, 0.7rem);

    /* Header/footer heights */
    --hdr-h:      clamp(2.6rem, 4.5vh, 3.8rem);
    --ftr-h:      clamp(1.8rem, 3vh,   2.6rem);

    --ease-expo: cubic-bezier(0.16, 1, 0.3, 1);
    --dur: 0.45s;
}

/* ============================================================ RESET */
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

html {
    height: 100%;
    scroll-snap-type: y mandatory;
    scroll-behavior: smooth;
    overflow-x: hidden;
}

body {
    font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
    background: var(--off-white);
    color: var(--black);
    height: 100%;
    overflow-x: hidden;
}

/* ============================================================
   SLIDE BASE — each = exactly 100vh, no overflow ever
   ============================================================ */
.slide {
    width: 100vw;
    height: 100vh;
    height: 100dvh;
    overflow: hidden;
    scroll-snap-align: start;
    display: flex;
    flex-direction: column;
    position: relative;
    background: var(--off-white);
}

/* ---- Chrome bar ---- */
.s-head {
    flex-shrink: 0;
    height: var(--hdr-h);
    background: var(--navy);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 var(--pad-h);
}
.s-head .brand {
    font-size: var(--fs-label);
    font-weight: 700;
    color: rgba(255,255,255,.65);
    letter-spacing: .12em;
    text-transform: uppercase;
}
.s-head .sec-tag {
    font-size: var(--fs-label);
    color: rgba(255,255,255,.42);
    letter-spacing: .08em;
    text-transform: uppercase;
}

/* ---- Body area ---- */
.s-body {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: var(--pad-v) var(--pad-h);
    overflow: hidden;
    gap: var(--gap-sm);
}

/* ---- Footer ---- */
.s-foot {
    flex-shrink: 0;
    height: var(--ftr-h);
    background: var(--gray-100);
    border-top: 1px solid var(--gray-200);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 var(--pad-h);
}
.s-foot span {
    font-size: var(--fs-label);
    color: var(--gray-400);
    letter-spacing: .04em;
}

/* ---- Typography ---- */
h1 { font-size: var(--fs-title); font-weight: 700; line-height: 1.15; }
h2 { font-size: var(--fs-h2); font-weight: 700; color: var(--navy); line-height: 1.2; }
h3 { font-size: var(--fs-h3); font-weight: 600; color: var(--navy-mid); line-height: 1.3; }
p  { font-size: var(--fs-body); line-height: 1.55; color: var(--gray-600); }

.rule {
    width: clamp(2rem, 4vw, 3.5rem);
    height: 3px;
    background: var(--accent);
    border-radius: 2px;
    flex-shrink: 0;
}

/* ---- Bullet lists ---- */
.blist { list-style: none; display: flex; flex-direction: column; gap: var(--gap-sm); }
.blist li {
    font-size: var(--fs-body);
    color: var(--black);
    display: flex;
    align-items: flex-start;
    gap: .5em;
    line-height: 1.4;
}
.blist li::before {
    content: '▸';
    color: var(--accent);
    flex-shrink: 0;
    font-size: .88em;
    margin-top: .08em;
}

/* ---- Cards ---- */
.card {
    background: var(--white);
    border: 1px solid var(--gray-200);
    border-radius: 8px;
    padding: var(--gap);
    display: flex;
    flex-direction: column;
    gap: var(--gap-sm);
    overflow: hidden;
}
.card.navy { background: var(--navy); border-color: var(--navy-dark); }
.card.navy h3 { color: #fff; }
.card.navy p  { color: rgba(255,255,255,.72); }

/* ---- Two-column layout ---- */
.two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--gap);
    flex: 1;
    min-height: 0;
    overflow: hidden;
}

/* ---- Account badge ---- */
.acct {
    display: inline-flex;
    align-items: center;
    gap: .35em;
    font-size: var(--fs-body);
}
.acct-n {
    background: var(--navy);
    color: #fff;
    font-family: 'Consolas','Courier New',monospace;
    font-size: .85em;
    padding: .15em .45em;
    border-radius: 4px;
    flex-shrink: 0;
}
.up   { color: var(--green);  font-weight: 700; }
.down { color: var(--red);    font-weight: 700; }

/* ---- Info badge row ---- */
.ibadge {
    display: inline-flex;
    align-items: center;
    gap: .4em;
    background: var(--gray-100);
    border: 1px solid var(--gray-200);
    border-radius: 6px;
    padding: clamp(.25rem,.6vh,.5rem) clamp(.5rem,1.2vw,.9rem);
    font-size: var(--fs-body);
}
.ibadge .n { font-family: monospace; font-weight: 700; color: var(--navy); }
.ibadge .u { color: var(--green); font-weight: 700; }
.ibadge .d { color: var(--red);   font-weight: 700; }

/* ---- Screenshot placeholder ---- */
.screenshot {
    background: var(--gray-100);
    border: 2px dashed var(--gray-400);
    border-radius: 6px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: .4em;
    flex: 1;
    min-height: clamp(4rem, 10vh, 9rem);
    max-height: clamp(6rem, 20vh, 14rem);
    padding: var(--gap-sm);
}
.screenshot .icon { font-size: clamp(1rem, 2.5vw, 1.8rem); }
.screenshot .lbl  {
    font-size: var(--fs-small);
    color: var(--gray-400);
    font-weight: 600;
    letter-spacing: .04em;
    text-align: center;
}

/* ---- Tables ---- */
.dtable { width: 100%; border-collapse: collapse; font-size: var(--fs-body); }
.dtable th {
    background: var(--navy);
    color: #fff;
    padding: clamp(.35rem,.9vh,.7rem) clamp(.6rem,1.5vw,1.2rem);
    text-align: left;
    font-size: var(--fs-small);
    text-transform: uppercase;
    letter-spacing: .06em;
}
.dtable td {
    padding: clamp(.3rem,.8vh,.6rem) clamp(.6rem,1.5vw,1.2rem);
    border-bottom: 1px solid var(--gray-200);
    color: var(--black);
    vertical-align: top;
}
.dtable tr:last-child td { border-bottom: none; }
.dtable tr:nth-child(even) td { background: var(--gray-50); }

/* ---- SVG diagram wrapper ---- */
.dbox {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 0;
    overflow: hidden;
}
.dbox svg {
    max-width: 100%;
    max-height: clamp(8rem, 28vh, 20rem);
    width: 100%;
}

/* ---- Emphasis / dark body ---- */
.emph-body {
    background: var(--navy-dark);
    color: #fff;
}
.emph-text {
    font-size: var(--fs-big);
    font-weight: 700;
    color: #fff;
    line-height: 1.3;
    text-align: center;
}
.emph-sub {
    font-size: var(--fs-h3);
    color: rgba(255,255,255,.6);
    text-align: center;
    margin-top: var(--gap-sm);
}

/* ---- Section divider slide ---- */
.sec-div {
    background: var(--navy);
    color: #fff;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: var(--pad-h);
    gap: var(--gap-sm);
}
.sec-num {
    font-size: var(--fs-label);
    font-weight: 700;
    letter-spacing: .2em;
    text-transform: uppercase;
    color: var(--accent-lt);
}
.sec-div h2 { color: #fff; font-size: var(--fs-title); text-align: center; }
.sec-div p  { color: rgba(255,255,255,.6); text-align: center; font-size: var(--fs-h3); }

/* ---- Tag pill ---- */
.tag {
    display: inline-block;
    background: var(--accent);
    color: #fff;
    border-radius: 20px;
    padding: .15em .7em;
    font-size: var(--fs-label);
    font-weight: 700;
    letter-spacing: .04em;
}
.tag.warn { background: var(--orange); }
.tag.ok   { background: var(--green); }
.tag.red  { background: var(--red); }
.tag.gray { background: var(--gray-400); }

/* ---- Progress bar (fixed) ---- */
#prog {
    position: fixed;
    top: 0; left: 0;
    height: 3px;
    background: var(--accent);
    z-index: 200;
    transition: width .25s ease;
    pointer-events: none;
}

/* ---- Slide counter (fixed) ---- */
#ctr {
    position: fixed;
    bottom: clamp(.5rem, 1.2vh, 1rem);
    right: clamp(.8rem, 2vw, 1.6rem);
    font-size: var(--fs-label);
    color: var(--gray-400);
    z-index: 200;
    font-family: monospace;
    pointer-events: none;
    letter-spacing: .04em;
}

/* ---- Reveal animations ---- */
.rv {
    opacity: 0;
    transform: translateY(14px);
    transition: opacity var(--dur) var(--ease-expo), transform var(--dur) var(--ease-expo);
}
.slide.vis .rv { opacity: 1; transform: translateY(0); }
.rv:nth-child(1) { transition-delay: .05s; }
.rv:nth-child(2) { transition-delay: .12s; }
.rv:nth-child(3) { transition-delay: .19s; }
.rv:nth-child(4) { transition-delay: .26s; }
.rv:nth-child(5) { transition-delay: .33s; }
.rv:nth-child(6) { transition-delay: .40s; }
.rv:nth-child(7) { transition-delay: .47s; }

/* ---- Highlight box ---- */
.hbox {
    background: var(--gray-100);
    border-left: 4px solid var(--accent);
    border-radius: 0 6px 6px 0;
    padding: var(--gap-sm) var(--gap);
    font-size: var(--fs-body);
}
.hbox.gold  { border-color: var(--gold); }
.hbox.red   { border-color: var(--red); }
.hbox.green { border-color: var(--green); }

/* ---- Financial table ---- */
.ftable {
    border-collapse: collapse;
    font-size: var(--fs-body);
    min-width: clamp(14rem, 30vw, 24rem);
}
.ftable th {
    background: var(--navy);
    color: #fff;
    padding: clamp(.3rem,.8vh,.6rem) clamp(.6rem,1.5vw,1.1rem);
    text-align: left;
    font-size: var(--fs-small);
    text-transform: uppercase;
    letter-spacing: .06em;
}
.ftable td {
    padding: clamp(.28rem,.7vh,.55rem) clamp(.6rem,1.5vw,1.1rem);
    border-bottom: 1px solid var(--gray-200);
}
.ftable td:last-child { text-align: right; font-family: monospace; font-weight: 600; }
.ftable tr.total td   { font-weight: 700; border-top: 2px solid var(--navy); color: var(--green); border-bottom: none; }

/* ---- Step number circle ---- */
.snum {
    flex-shrink: 0;
    width: clamp(1.7rem, 3.5vw, 2.6rem);
    height: clamp(1.7rem, 3.5vw, 2.6rem);
    background: var(--navy);
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: var(--fs-small);
    font-weight: 700;
}

/* ---- Breakpoints ---- */
@media (max-height: 700px) {
    :root {
        --fs-title: clamp(1.5rem, 4.5vw, 3rem);
        --fs-h2:    clamp(1.1rem, 2.8vw, 1.9rem);
        --pad-v:    clamp(.6rem, 1.4vh, 1.4rem);
        --gap:      clamp(.5rem, 1.2vw, 1.1rem);
    }
}
@media (max-height: 600px) {
    :root {
        --fs-title: clamp(1.3rem, 4vw, 2.4rem);
        --fs-h2:    clamp(1rem,  2.5vw, 1.6rem);
        --fs-body:  clamp(.72rem,1.2vw, .9rem);
        --pad-h:    clamp(1rem, 3vw, 3rem);
        --pad-v:    clamp(.5rem, 1.2vh, 1rem);
        --gap:      clamp(.4rem, 1vw, .9rem);
        --gap-sm:   clamp(.25rem,.6vw,.55rem);
    }
    .dtable th, .dtable td { padding: .28rem .5rem; }
}
@media (max-height: 500px) {
    :root {
        --fs-title: clamp(1.1rem, 3.5vw, 2rem);
        --fs-h2:    clamp(.95rem, 2.2vw, 1.4rem);
        --fs-body:  clamp(.65rem, 1.1vw, .82rem);
        --hdr-h:    clamp(2rem, 3.5vh, 2.8rem);
        --ftr-h:    clamp(1.5rem, 2.5vh, 2rem);
    }
    .screenshot { max-height: 7rem; }
}
@media (max-width: 640px) {
    .two-col { grid-template-columns: 1fr; }
    :root { --fs-title: clamp(1.5rem, 7vw, 3rem); }
}
@media (prefers-reduced-motion: reduce) {
    .rv { transition: opacity .2s ease; transform: none; }
    html { scroll-behavior: auto; }
}
"""

JS = """
(function () {
    const slides = Array.from(document.querySelectorAll('.slide'));
    const total  = slides.length;
    const prog   = document.getElementById('prog');
    const ctr    = document.getElementById('ctr');
    let cur = 0;

    function setSlide(idx) {
        if (idx < 0 || idx >= total) return;
        cur = idx;
        slides[idx].classList.add('vis');
        if (prog) prog.style.width = (total <= 1 ? 100 : (idx / (total - 1)) * 100) + '%';
        if (ctr)  ctr.textContent  = (idx + 1) + ' / ' + total;
    }

    function goTo(idx) {
        if (idx < 0 || idx >= total) return;
        slides[idx].scrollIntoView({ behavior: 'smooth', block: 'start' });
        setSlide(idx);
    }

    /* Keyboard */
    document.addEventListener('keydown', function (e) {
        switch (e.key) {
            case 'ArrowDown': case 'ArrowRight': case ' ': e.preventDefault(); goTo(cur + 1); break;
            case 'ArrowUp':   case 'ArrowLeft':            e.preventDefault(); goTo(cur - 1); break;
            case 'Home':                                   e.preventDefault(); goTo(0);       break;
            case 'End':                                    e.preventDefault(); goTo(total-1); break;
        }
    });

    /* Touch */
    let ty0 = 0, tx0 = 0;
    document.addEventListener('touchstart', e => { ty0 = e.touches[0].clientY; tx0 = e.touches[0].clientX; }, { passive: true });
    document.addEventListener('touchend',   e => {
        const dy = ty0 - e.changedTouches[0].clientY;
        const dx = tx0 - e.changedTouches[0].clientX;
        if (Math.abs(dy) > Math.abs(dx) && Math.abs(dy) > 40) goTo(dy > 0 ? cur + 1 : cur - 1);
    }, { passive: true });

    /* Intersection Observer */
    const obs = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting && entry.intersectionRatio >= 0.5) {
                const i = slides.indexOf(entry.target);
                if (i !== -1) setSlide(i);
            }
        });
    }, { threshold: 0.5 });

    slides.forEach(s => obs.observe(s));
    setSlide(0);
})();
"""

# Helper: standard chrome
def head(section_tag):
    return f'<div class="s-head"><span class="brand">Westfield Outdoors</span><span class="sec-tag">{section_tag}</span></div>'

def foot(label, n):
    return f'<div class="s-foot"><span>{label}</span><span>Slide {n} of 48</span></div>'

# SVG arrow marker defs (reused inline)
def arrow_defs(ids):
    out = "<defs>"
    for aid, color in ids:
        out += f'<marker id="{aid}" markerWidth="8" markerHeight="6" refX="6" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="{color}"/></marker>'
    out += "</defs>"
    return out

slides_html = []

# ─────────────────────────────────────────────────────────
# SLIDE 1 — Title
# ─────────────────────────────────────────────────────────
slides_html.append("""
<section class="slide" id="s1" style="background:var(--navy-dark);">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 70% 30%,rgba(37,99,235,.18) 0%,transparent 55%),radial-gradient(ellipse at 20% 80%,rgba(184,134,11,.1) 0%,transparent 50%);pointer-events:none;"></div>
  <div class="s-body" style="position:relative;z-index:1;justify-content:center;gap:var(--gap);">
    <p class="rv" style="font-size:var(--fs-label);font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--accent-lt);">Westfield Outdoors Training</p>
    <h1 class="rv" style="color:#fff;max-width:16ch;">NetSuite 101 –<br>Accounting Basics</h1>
    <div class="rule rv"></div>
    <p class="rv" style="color:rgba(255,255,255,.6);font-size:var(--fs-h3);max-width:36ch;">A foundational guide to how NetSuite records data, tracks transactions, and drives financial reporting.</p>
  </div>
  <div style="flex-shrink:0;height:var(--ftr-h);background:rgba(255,255,255,.05);border-top:1px solid rgba(255,255,255,.1);display:flex;align-items:center;justify-content:space-between;padding:0 var(--pad-h);">
    <span style="font-size:var(--fs-label);color:rgba(255,255,255,.45);letter-spacing:.12em;text-transform:uppercase;font-weight:600;">Westfield Outdoors</span>
    <span style="font-size:var(--fs-label);color:rgba(255,255,255,.45);letter-spacing:.12em;text-transform:uppercase;font-weight:600;">NetSuite 101</span>
  </div>
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 2 — Income Statement vs Balance Sheet
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s2">
  {head("Section 1 — Accounting Basics")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Income Statement vs. Balance Sheet</h2>
    <div class="rule rv"></div>
    <div class="two-col rv" style="margin-top:var(--gap-sm);">
      <div class="card navy" style="gap:var(--gap-sm);">
        <div style="display:flex;align-items:center;gap:.5em;"><span style="font-size:1.3em;">📊</span><h3>Income Statement</h3></div>
        <p style="color:rgba(255,255,255,.75);font-size:var(--fs-body);">Measures <strong style="color:#fff;">performance</strong> over a period of time.</p>
        <ul class="blist" style="--c:#93c5fd;">
          <li style="color:rgba(255,255,255,.9);">Sales</li>
          <li style="color:rgba(255,255,255,.9);">Expenses</li>
          <li style="color:rgba(255,255,255,.9);">Profit</li>
        </ul>
        <div style="margin-top:auto;padding-top:var(--gap-sm);border-top:1px solid rgba(255,255,255,.15);"><span class="tag">"How we perform"</span></div>
      </div>
      <div class="card" style="gap:var(--gap-sm);">
        <div style="display:flex;align-items:center;gap:.5em;"><span style="font-size:1.3em;">🏦</span><h3>Balance Sheet</h3></div>
        <p style="font-size:var(--fs-body);">Captures <strong>position</strong> at a point in time.</p>
        <ul class="blist">
          <li>Assets</li>
          <li>Liabilities</li>
          <li>Equity</li>
        </ul>
        <div style="margin-top:auto;padding-top:var(--gap-sm);border-top:1px solid var(--gray-200);"><span class="tag">"What we have"</span></div>
      </div>
    </div>
  </div>
  {foot("Accounting Basics", 2)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 3 — How Westfield Uses the Income Statement
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s3">
  {head("Section 1 — Accounting Basics")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">How Westfield Uses the Income Statement</h2>
    <div class="rule rv"></div>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card">
        <h3>Sales Reporting Dimensions</h3>
        <ul class="blist" style="margin-top:var(--gap-sm);">
          <li>By <strong>Department</strong> — which channel / customer segment</li>
          <li>By <strong>Brand</strong> (Class) — e.g., Timber Ridge, GCI Outdoor</li>
          <li>By <strong>Item Category</strong> — product type, e.g., Furniture → Folding</li>
        </ul>
      </div>
      <div class="card">
        <h3>Key Account Numbers</h3>
        <div style="display:flex;gap:var(--gap);flex-wrap:wrap;margin-top:var(--gap-sm);">
          <div class="ibadge"><span class="n">4105</span><span>Gross Sales</span><span class="u">↑</span></div>
          <div class="ibadge"><span class="n">5105</span><span>Product (COGS)</span><span class="u">↑</span></div>
        </div>
      </div>
    </div>
  </div>
  {foot("Accounting Basics", 3)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 4 — Balance Sheet Concept
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s4">
  {head("Section 1 — Accounting Basics")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Balance Sheet Concept</h2>
    <div class="rule rv"></div>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:4px solid var(--accent);">
        <div style="display:flex;align-items:center;gap:.6em;"><span style="font-size:1.4em;">🗂️</span><h3>Acts like a holding account</h3></div>
        <p style="margin-top:var(--gap-sm);">Balance sheet accounts hold values — they represent what the business <em>owns</em> or <em>owes</em> at a given point in time, not how it performed.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--red);">
        <div style="display:flex;align-items:center;gap:.6em;"><span style="font-size:1.4em;">🚫</span><h3 style="color:var(--red);">Does NOT measure performance</h3></div>
        <p style="margin-top:var(--gap-sm);">Transactions that only touch balance sheet accounts produce <strong>no income statement impact</strong> — no revenue, no expense. Value moves, it doesn't disappear.</p>
      </div>
    </div>
  </div>
  {foot("Accounting Basics", 4)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 5 — Balanced Transactions
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s5">
  {head("Section 2 — Balanced Entries")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Balanced Transactions</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">Every transaction in NetSuite must balance — equal debits and credits. The system enforces this automatically.</p>
    <div class="dbox rv">
      <svg viewBox="0 0 600 155" xmlns="http://www.w3.org/2000/svg">
        <rect x="20" y="35" width="195" height="80" rx="8" fill="#1a2b4a"/>
        <text x="117" y="67" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="13" font-weight="700">Income</text>
        <text x="117" y="86" text-anchor="middle" fill="#93c5fd" font-family="monospace" font-size="12">4105 Gross Sales</text>
        <text x="117" y="103" text-anchor="middle" fill="#86efac" font-family="system-ui" font-size="12" font-weight="700">↑ Credit</text>
        <path d="M215 75 L265 75" stroke="#2563eb" stroke-width="2.5" marker-end="url(#a1)"/>
        <text x="290" y="80" text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="22" font-weight="700">⇌</text>
        <path d="M315 75 L365 75" stroke="#2563eb" stroke-width="2.5" marker-end="url(#a1)"/>
        <rect x="365" y="35" width="215" height="80" rx="8" fill="#f0f2f7" stroke="#dde3ef" stroke-width="1.5"/>
        <text x="472" y="67" text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="13" font-weight="700">Offset</text>
        <text x="472" y="86" text-anchor="middle" fill="#1a2b4a" font-family="monospace" font-size="12">1110 Accts Receivable</text>
        <text x="472" y="103" text-anchor="middle" fill="#dc2626" font-family="system-ui" font-size="12" font-weight="700">↑ Debit</text>
        <text x="300" y="140" text-anchor="middle" fill="#8898b0" font-family="system-ui" font-size="11">Every transaction posts both sides simultaneously</text>
        {arrow_defs([("a1","#2563eb")])}
      </svg>
    </div>
    <div class="hbox rv"><p><strong>Rule:</strong> For every debit there is an equal and opposite credit. NetSuite will not let you post an unbalanced entry.</p></div>
  </div>
  {foot("Balanced Entries", 5)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 6 — Simple Balance Example
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s6">
  {head("Section 2 — Balanced Entries")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Simple Balance Example</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">A sale creates two simultaneous entries — one on the income statement, one on the balance sheet.</p>
    <div class="dbox rv">
      <svg viewBox="0 0 620 185" xmlns="http://www.w3.org/2000/svg">
        <rect x="20" y="20" width="220" height="130" rx="10" fill="#1a2b4a"/>
        <text x="130" y="50" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="11" font-weight="700" letter-spacing="1">INCOME STATEMENT</text>
        <line x1="40" y1="60" x2="220" y2="60" stroke="rgba(255,255,255,.15)" stroke-width="1"/>
        <text x="130" y="85"  text-anchor="middle" fill="#93c5fd" font-family="monospace" font-size="13">4105 Gross Sales</text>
        <text x="130" y="108" text-anchor="middle" fill="#86efac" font-family="system-ui" font-size="14" font-weight="700">↑ Revenue</text>
        <text x="130" y="136" text-anchor="middle" fill="rgba(255,255,255,.45)" font-family="system-ui" font-size="11">Posted when invoice is saved</text>
        <path d="M240 85 L285 85" stroke="#2563eb" stroke-width="2.5" marker-end="url(#a2)" marker-start="url(#a2s)"/>
        <text x="262" y="77" text-anchor="middle" fill="#2563eb" font-family="system-ui" font-size="11" font-weight="700">=</text>
        <rect x="285" y="20" width="220" height="130" rx="10" fill="#fff" stroke="#dde3ef" stroke-width="1.5"/>
        <text x="395" y="50" text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="11" font-weight="700" letter-spacing="1">BALANCE SHEET</text>
        <line x1="305" y1="60" x2="485" y2="60" stroke="#dde3ef" stroke-width="1"/>
        <text x="395" y="85"  text-anchor="middle" fill="#1a2b4a" font-family="monospace" font-size="13">1110 Accts Receivable</text>
        <text x="395" y="108" text-anchor="middle" fill="#dc2626" font-family="system-ui" font-size="14" font-weight="700">↑ Asset</text>
        <text x="395" y="136" text-anchor="middle" fill="#8898b0" font-family="system-ui" font-size="11">Customer owes us money</text>
        <rect x="20" y="165" width="485" height="18" rx="4" fill="#f0f2f7"/>
        <text x="262" y="178" text-anchor="middle" fill="#475569" font-family="system-ui" font-size="11">NetSuite creates both entries automatically — you only enter one transaction</text>
        {arrow_defs([("a2","#2563eb"),("a2s","#2563eb")])}
      </svg>
    </div>
  </div>
  {foot("Balanced Entries", 6)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 7 — Records vs Transactions
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s7">
  {head("Section 3 — Records vs Transactions")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Records vs. Transactions</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">NetSuite separates permanent setup data (records) from business activity (transactions). Records don't create financial impact — transactions do.</p>
    <div class="rv" style="flex:1;min-height:0;overflow:hidden;margin-top:var(--gap-sm);">
      <table class="dtable">
        <thead><tr><th>📁 Records — Permanent Data</th><th>⚡ Transactions — Actions</th></tr></thead>
        <tbody>
          <tr><td><strong>Customer</strong> — who you sell to</td><td><strong>Sales Order</strong> — commitment to sell</td></tr>
          <tr><td><strong>Item</strong> — what you sell or buy</td><td><strong>Invoice</strong> — billing record, posts revenue</td></tr>
          <tr><td><strong>Vendor</strong> — who you buy from</td><td><strong>Purchase Order</strong> — commitment to buy</td></tr>
          <tr><td><strong>Employee</strong> — internal users</td><td><strong>Item Receipt</strong> — goods received, posts inventory</td></tr>
        </tbody>
      </table>
    </div>
    <div class="hbox gold rv"><p><strong>Key concept:</strong> Records are setup data. Transactions are the events that move money and inventory.</p></div>
  </div>
  {foot("Records vs Transactions", 7)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 8 — Section divider: Transaction Flows
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s8">
  {head("Section 4")}
  <div class="sec-div">
    <p class="sec-num rv">Section 4</p>
    <h2 class="rv">Transaction Flows</h2>
    <p class="rv">How money and inventory move through NetSuite — from purchasing through fulfillment to invoicing.</p>
  </div>
  {foot("Transaction Flows", 8)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 9 — Purchasing Overview
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s9">
  {head("Section 4 — Transaction Flows")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Purchasing Overview</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">The purchasing flow begins with a commitment (PO) and ends when goods are physically received and entered into inventory.</p>
    <div class="dbox rv">
      <svg viewBox="0 0 560 130" xmlns="http://www.w3.org/2000/svg">
        <rect x="20" y="25" width="200" height="75" rx="10" fill="#1a2b4a"/>
        <text x="120" y="57"  text-anchor="middle" fill="#fff"    font-family="system-ui" font-size="14" font-weight="700">Purchase Order</text>
        <text x="120" y="75"  text-anchor="middle" fill="#fbbf24" font-family="system-ui" font-size="11">No financial impact</text>
        <text x="120" y="91"  text-anchor="middle" fill="rgba(255,255,255,.45)" font-family="system-ui" font-size="10">Commitment only</text>
        <path d="M220 63 L308 63" stroke="#2563eb" stroke-width="2.5" marker-end="url(#a3)"/>
        <text x="264" y="55" text-anchor="middle" fill="#8898b0" font-family="system-ui" font-size="10">goods arrive</text>
        <rect x="308" y="25" width="225" height="75" rx="10" fill="#f0f2f7" stroke="#2563eb" stroke-width="2"/>
        <text x="420" y="57"  text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="14" font-weight="700">Item Receipt</text>
        <text x="420" y="75"  text-anchor="middle" fill="#15803d" font-family="system-ui" font-size="11" font-weight="600">💰 Financial Impact</text>
        <text x="420" y="91"  text-anchor="middle" fill="#475569" font-family="system-ui" font-size="10">1210 Inv ↑ · 2010 AP ↑</text>
        <text x="280" y="120" text-anchor="middle" fill="#8898b0" font-family="system-ui" font-size="11">Inventory enters the system at the Item Receipt</text>
        {arrow_defs([("a3","#2563eb")])}
      </svg>
    </div>
  </div>
  {foot("Transaction Flows — Purchasing", 9)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 10 — Purchase Order
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s10">
  {head("Section 4 — Transaction Flows")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Purchase Order</h2>
    <div class="rule rv"></div>
    <div class="two-col rv">
      <div style="display:flex;flex-direction:column;gap:var(--gap-sm);">
        <div class="card" style="border-left:4px solid var(--gold);">
          <h3>No Financial Impact</h3>
          <p style="margin-top:var(--gap-sm);">A PO is a <em>commitment</em> to purchase. It does not move money or inventory in the accounting system — it is not posted to the general ledger.</p>
        </div>
        <div class="card">
          <h3>Required Fields</h3>
          <ul class="blist" style="margin-top:var(--gap-sm);">
            <li><strong>Vendor</strong> — who you're buying from</li>
            <li><strong>Item</strong> — what you're ordering</li>
          </ul>
        </div>
      </div>
      <div class="screenshot">
        <span class="icon">🔲</span>
        <span class="lbl">[INSERT NETSUITE SCREENSHOT HERE]<br>Purchase Order form</span>
      </div>
    </div>
  </div>
  {foot("Transaction Flows — Purchasing", 10)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 11 — Item Receipt
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s11">
  {head("Section 4 — Transaction Flows")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Item Receipt</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">When goods physically arrive and are received in NetSuite, two accounts are affected simultaneously.</p>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:4px solid var(--green);">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:var(--gap-sm);">
          <div class="ibadge"><span class="n">1210</span><span>Inventory Asset</span></div>
          <span style="font-size:var(--fs-h2);color:var(--green);font-weight:700;">↑ Increases</span>
        </div>
        <p style="margin-top:var(--gap-sm);">Inventory value on the balance sheet rises — we now own the goods.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--orange);">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:var(--gap-sm);">
          <div class="ibadge"><span class="n">2010</span><span>Accounts Payable</span></div>
          <span style="font-size:var(--fs-h2);color:var(--orange);font-weight:700;">↑ Increases</span>
        </div>
        <p style="margin-top:var(--gap-sm);">A liability is created — we owe the vendor for these goods.</p>
      </div>
    </div>
  </div>
  {foot("Transaction Flows — Purchasing", 11)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 12 — Landed Cost Concept
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s12">
  {head("Section 4 — Transaction Flows")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Landed Cost Concept</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">True inventory cost is more than the PO price. Landed cost captures everything needed to get goods to your warehouse.</p>
    <div class="dbox rv">
      <svg viewBox="0 0 580 120" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="15" width="150" height="65" rx="8" fill="#1a2b4a"/>
        <text x="85" y="46" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="12" font-weight="700">Product Cost</text>
        <text x="85" y="65" text-anchor="middle" fill="#93c5fd" font-family="system-ui" font-size="11">PO price from vendor</text>
        <text x="172" y="52" text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="22" font-weight="700">+</text>
        <rect x="190" y="15" width="150" height="65" rx="8" fill="#1e3461"/>
        <text x="265" y="46" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="12" font-weight="700">Freight</text>
        <text x="265" y="65" text-anchor="middle" fill="#93c5fd" font-family="system-ui" font-size="11">Shipping to warehouse</text>
        <text x="352" y="52" text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="22" font-weight="700">+</text>
        <rect x="370" y="15" width="200" height="65" rx="8" fill="#243856"/>
        <text x="470" y="46" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="12" font-weight="700">Duties / Tariffs</text>
        <text x="470" y="65" text-anchor="middle" fill="#93c5fd" font-family="system-ui" font-size="11">Import fees &amp; charges</text>
        <text x="290" y="108" text-anchor="middle" fill="#8898b0" font-family="system-ui" font-size="11">= Total Landed Cost → allocated to Account 1210 Inventory</text>
      </svg>
    </div>
    <div class="hbox gold rv"><p>Landed cost flows into COGS only when the item is eventually sold (at Item Fulfillment).</p></div>
  </div>
  {foot("Transaction Flows — Purchasing", 12)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 13 — Important Rule (emphasis)
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s13">
  {head("Section 4 — Transaction Flows")}
  <div class="s-body emph-body" style="align-items:center;justify-content:center;gap:var(--gap);text-align:center;">
    <span class="rv" style="font-size:clamp(2rem,5vw,3.5rem);">⚠️</span>
    <p class="rv" style="font-size:var(--fs-label);letter-spacing:.18em;text-transform:uppercase;color:var(--accent-lt);font-weight:700;">Important Rule</p>
    <p class="emph-text rv">"No purchasing activity<br>should hit the<br>income statement"</p>
    <p class="emph-sub rv">Purchasing touches the balance sheet only (Inventory ↑ and AP ↑).<br>If a purchasing transaction appears on the P&amp;L, something is wrong.</p>
  </div>
  {foot("Transaction Flows — Purchasing", 13)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 14 — Returns Overview
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s14">
  {head("Section 4 — Transaction Flows")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Returns Overview</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">Returns reverse both sides of the original sale — revenue and COGS are both reduced.</p>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:4px solid var(--red);">
        <h3>What Gets Reversed</h3>
        <div style="display:flex;gap:var(--gap);flex-wrap:wrap;margin-top:var(--gap-sm);">
          <div class="ibadge"><span class="n">4105</span><span>Gross Sales</span><span class="d">↓</span></div>
          <div class="ibadge"><span class="n">5105</span><span>Product (COGS)</span><span class="d">↓</span></div>
          <div class="ibadge"><span class="n">1210</span><span>Inventory</span><span class="u">↑</span></div>
        </div>
      </div>
      <div class="card">
        <h3>Transaction Types</h3>
        <ul class="blist" style="margin-top:var(--gap-sm);">
          <li><strong>Return Authorization</strong> — customer requests to return goods</li>
          <li><strong>Credit Memo</strong> — financial reversal of the original invoice</li>
          <li><strong>Item Receipt (return)</strong> — goods physically back in stock</li>
        </ul>
      </div>
    </div>
  </div>
  {foot("Transaction Flows", 14)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 15 — Transfer Orders
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s15">
  {head("Section 4 — Transaction Flows")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Transfer Orders</h2>
    <div class="rule rv"></div>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3>What They Do</h3>
        <p style="margin-top:var(--gap-sm);">Transfer orders move inventory between locations — warehouse to warehouse, or warehouse to a virtual/consignment location. No vendor or customer is involved.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--red);">
        <div style="display:flex;align-items:center;gap:.6em;"><span style="font-size:1.2em;">🚫</span><h3 style="color:var(--red);">Critical Rule</h3></div>
        <p style="margin-top:var(--gap-sm);">Transfers should <strong>NOT</strong> impact the income statement. A transfer is not a sale — no revenue should be recognized. The <strong>transfer cost must match average cost</strong> to prevent phantom P&amp;L entries.</p>
      </div>
    </div>
  </div>
  {foot("Transaction Flows", 15)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 16 — Inventory Adjustments
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s16">
  {head("Section 4 — Transaction Flows")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Inventory Adjustments</h2>
    <div class="rule rv"></div>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3>When to Use</h3>
        <ul class="blist" style="margin-top:var(--gap-sm);">
          <li>Only for <strong>cycle counts</strong> — physical count vs. system discrepancies</li>
          <li><strong>Warehouse team responsibility</strong> — not a general-purpose fix</li>
          <li>Do not use to move inventory between locations (use Transfer Order)</li>
        </ul>
      </div>
      <div class="card" style="border-left:4px solid var(--orange);">
        <h3>Account Impact</h3>
        <div style="display:flex;gap:var(--gap);flex-wrap:wrap;margin-top:var(--gap-sm);align-items:center;">
          <div class="ibadge"><span class="n">6820</span><span>Inventory Adjustment</span></div>
          <span style="font-size:var(--fs-body);">Department = <strong>Warehouse</strong></span>
        </div>
        <p style="margin-top:var(--gap-sm);">This account hits the income statement — it is an expense when inventory is adjusted down (shrinkage, damage, miscounts).</p>
      </div>
    </div>
  </div>
  {foot("Transaction Flows", 16)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 17 — Sales Overview
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s17">
  {head("Section 4 — Transaction Flows")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Sales Overview</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">The sales flow has three steps. Two create financial impact — COGS at fulfillment, revenue at invoice.</p>
    <div class="dbox rv">
      <svg viewBox="0 0 700 138" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="22" width="170" height="82" rx="10" fill="#1a2b4a"/>
        <text x="95" y="53"  text-anchor="middle" fill="#fff" font-family="system-ui" font-size="13" font-weight="700">Sales Order</text>
        <text x="95" y="71"  text-anchor="middle" fill="#fbbf24" font-family="system-ui" font-size="11">$0 — No impact</text>
        <text x="95" y="90"  text-anchor="middle" fill="rgba(255,255,255,.45)" font-family="system-ui" font-size="10">Commitment only</text>
        <path d="M180 63 L235 63" stroke="#2563eb" stroke-width="2.5" marker-end="url(#a4)"/>
        <rect x="235" y="22" width="195" height="82" rx="10" fill="#1e3461"/>
        <text x="332" y="53"  text-anchor="middle" fill="#fff" font-family="system-ui" font-size="13" font-weight="700">Item Fulfillment</text>
        <text x="332" y="71"  text-anchor="middle" fill="#86efac" font-family="system-ui" font-size="11" font-weight="600">💰 COGS entry</text>
        <text x="332" y="90"  text-anchor="middle" fill="rgba(255,255,255,.6)" font-family="system-ui" font-size="10">1210 ↓ · 5105 ↑</text>
        <path d="M430 63 L490 63" stroke="#2563eb" stroke-width="2.5" marker-end="url(#a4)"/>
        <rect x="490" y="22" width="200" height="82" rx="10" fill="#f0f2f7" stroke="#2563eb" stroke-width="2"/>
        <text x="590" y="53"  text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="13" font-weight="700">Invoice</text>
        <text x="590" y="71"  text-anchor="middle" fill="#15803d" font-family="system-ui" font-size="11" font-weight="600">💰 Revenue entry</text>
        <text x="590" y="90"  text-anchor="middle" fill="#475569" font-family="system-ui" font-size="10">4105 ↑ · 1110 ↑</text>
        <text x="350" y="125" text-anchor="middle" fill="#8898b0" font-family="system-ui" font-size="11">Two financial events: COGS at shipment, Revenue at billing</text>
        {arrow_defs([("a4","#2563eb")])}
      </svg>
    </div>
  </div>
  {foot("Transaction Flows — Sales", 17)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 18 — Sales Order
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s18">
  {head("Section 4 — Transaction Flows")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Sales Order</h2>
    <div class="rule rv"></div>
    <div class="two-col rv">
      <div style="display:flex;flex-direction:column;gap:var(--gap-sm);">
        <div class="card" style="border-left:4px solid var(--gold);">
          <h3>No Financial Impact</h3>
          <p style="margin-top:var(--gap-sm);">A Sales Order reserves inventory and locks in the commitment — no journal entries are created until fulfillment.</p>
        </div>
        <div class="card">
          <h3>Header vs. Line</h3>
          <ul class="blist" style="margin-top:var(--gap-sm);">
            <li><strong>Header</strong> — Customer, Department, Date, Terms</li>
            <li><strong>Line</strong> — Item, Qty, Price, Location</li>
          </ul>
          <p style="margin-top:var(--gap-sm);font-size:var(--fs-small);color:var(--gray-400);">Department auto-populates from the customer record.</p>
        </div>
      </div>
      <div class="screenshot">
        <span class="icon">🔲</span>
        <span class="lbl">[INSERT NETSUITE SCREENSHOT HERE]<br>Sales Order form</span>
      </div>
    </div>
  </div>
  {foot("Transaction Flows — Sales", 18)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 19 — Item Fulfillment
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s19">
  {head("Section 4 — Transaction Flows")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Item Fulfillment</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">When inventory ships, NetSuite records COGS and reduces inventory — even before the customer is billed.</p>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:4px solid var(--red);">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:var(--gap-sm);">
          <div class="ibadge"><span class="n">1210</span><span>Inventory Asset</span></div>
          <span style="font-size:var(--fs-h2);color:var(--red);font-weight:700;">↓ Decreases</span>
        </div>
        <p style="margin-top:var(--gap-sm);">Units leave the warehouse — asset value reduced by (qty × average cost).</p>
      </div>
      <div class="card" style="border-left:4px solid var(--orange);">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:var(--gap-sm);">
          <div class="ibadge"><span class="n">5105</span><span>Product (COGS)</span></div>
          <span style="font-size:var(--fs-h2);color:var(--orange);font-weight:700;">↑ Increases</span>
        </div>
        <p style="margin-top:var(--gap-sm);">Cost of Goods Sold recognized — the cost of the item hits the income statement.</p>
      </div>
    </div>
  </div>
  {foot("Transaction Flows — Sales", 19)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 20 — Invoice
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s20">
  {head("Section 4 — Transaction Flows")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Invoice</h2>
    <div class="rule rv"></div>
    <div class="two-col rv">
      <div style="display:flex;flex-direction:column;gap:var(--gap-sm);">
        <div class="card" style="border-left:4px solid var(--green);">
          <div style="display:flex;align-items:center;justify-content:space-between;gap:var(--gap-sm);">
            <div class="ibadge"><span class="n">4105</span><span>Gross Sales</span></div>
            <span style="color:var(--green);font-weight:700;font-size:var(--fs-h3);">↑</span>
          </div>
          <p style="margin-top:var(--gap-sm);font-size:var(--fs-small);">Revenue recognized — sale posted to the income statement.</p>
        </div>
        <div class="card" style="border-left:4px solid var(--accent);">
          <div style="display:flex;align-items:center;justify-content:space-between;gap:var(--gap-sm);">
            <div class="ibadge"><span class="n">1110</span><span>Accounts Receivable</span></div>
            <span style="color:var(--accent);font-weight:700;font-size:var(--fs-h3);">↑</span>
          </div>
          <p style="margin-top:var(--gap-sm);font-size:var(--fs-small);">Customer owes us — receivable created on the balance sheet.</p>
        </div>
      </div>
      <div class="screenshot">
        <span class="icon">🔲</span>
        <span class="lbl">[INSERT NETSUITE SCREENSHOT HERE]<br>Invoice form</span>
      </div>
    </div>
  </div>
  {foot("Transaction Flows — Sales", 20)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 21 — Vendor Bills
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s21">
  {head("Section 4 — Transaction Flows")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Vendor Bills</h2>
    <div class="rule rv"></div>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3>Purpose</h3>
        <p style="margin-top:var(--gap-sm);">Vendor bills are used to record and pay obligations to vendors — for goods received or services rendered.</p>
      </div>
      <div class="card">
        <h3>Two Types of Impact</h3>
        <ul class="blist" style="margin-top:var(--gap-sm);">
          <li><strong>Direct expense bills</strong> — hit the income statement immediately (freight, utilities, services)</li>
          <li><strong>Accrual-clearing bills</strong> — linked to a PO/receipt; they clear the 2010 AP balance, not create a new expense</li>
        </ul>
      </div>
      <div class="hbox rv"><p style="font-size:var(--fs-small);"><strong>Note:</strong> Vendor bills linked to Item Receipts clear the AP accrual — they do NOT create a duplicate expense.</p></div>
    </div>
  </div>
  {foot("Transaction Flows", 21)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 22 — Item Record Overview
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s22">
  {head("Section 5 — Item Records")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Item Record Overview</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">The Item record is the central source of truth for all product data. Cost, pricing, brand, category — everything flows from it.</p>
    <div class="two-col rv" style="margin-top:var(--gap-sm);">
      <div class="card" style="border-left:4px solid var(--navy);">
        <h3>What It Drives</h3>
        <ul class="blist" style="margin-top:var(--gap-sm);">
          <li>Purchasing — PO &amp; Item Receipt</li>
          <li>Sales — SO, Fulfillment &amp; Invoice</li>
          <li>Reporting — Brand, Category dimensions</li>
          <li>Inventory valuation — Average Cost</li>
        </ul>
      </div>
      <div class="screenshot">
        <span class="icon">🔲</span>
        <span class="lbl">[INSERT NETSUITE SCREENSHOT HERE]<br>Item Record form</span>
      </div>
    </div>
  </div>
  {foot("Item Records", 22)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 23 — Required Fields
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s23">
  {head("Section 5 — Item Records")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Required Fields — Item Record</h2>
    <div class="rule rv"></div>
    <div class="rv" style="display:grid;grid-template-columns:1fr 1fr;gap:var(--gap);">
      <div class="card" style="border-top:3px solid var(--accent);">
        <div style="display:flex;align-items:center;gap:.5em;"><span class="tag">Required</span><h3>SKU</h3></div>
        <p style="margin-top:var(--gap-sm);">Unique identifier. Used across all transactions and reports.</p>
      </div>
      <div class="card" style="border-top:3px solid var(--accent);">
        <div style="display:flex;align-items:center;gap:.5em;"><span class="tag">Required</span><h3>Description</h3></div>
        <p style="margin-top:var(--gap-sm);"><strong>Brand first</strong> — e.g., "Timber Ridge XL Folding Chair". Appears on customer documents.</p>
      </div>
      <div class="card" style="border-top:3px solid var(--gold);">
        <div style="display:flex;align-items:center;gap:.5em;"><span class="tag warn">Reporting</span><h3>Class (Brand)</h3></div>
        <p style="margin-top:var(--gap-sm);">Drives brand-level P&amp;L reporting. Cannot be changed retroactively on posted transactions.</p>
      </div>
      <div class="card" style="border-top:3px solid var(--gold);">
        <div style="display:flex;align-items:center;gap:.5em;"><span class="tag warn">Reporting</span><h3>Item Category</h3></div>
        <p style="margin-top:var(--gap-sm);">Product type classification (e.g., Furniture → Folding). Used for category analysis.</p>
      </div>
    </div>
  </div>
  {foot("Item Records", 23)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 24 — Cost Concept
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s24">
  {head("Section 5 — Item Records")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Cost Concept</h2>
    <div class="rule rv"></div>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3>Initial Cost</h3>
        <p style="margin-top:var(--gap-sm);">Set at item creation — equals the <strong>PO price</strong> from the vendor. Used for the very first receipt if no other cost history exists.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--green);">
        <h3>Average Cost</h3>
        <p style="margin-top:var(--gap-sm);">Automatically recalculated by NetSuite with each new receipt. Represents the <strong>blended cost</strong> of all units currently on hand.</p>
        <div style="margin-top:var(--gap-sm);background:var(--gray-100);padding:var(--gap-sm) var(--gap);border-radius:6px;font-size:var(--fs-small);font-family:monospace;">
          (On-hand qty × current avg cost + new qty × new cost) ÷ total qty
        </div>
      </div>
    </div>
  </div>
  {foot("Item Records", 24)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 25 — Transfer Cost (CRITICAL)
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s25">
  {head("Section 5 — Item Records")}
  <div class="s-body emph-body" style="align-items:center;justify-content:center;gap:var(--gap);text-align:center;">
    <p class="rv" style="font-size:var(--fs-label);letter-spacing:.18em;text-transform:uppercase;color:var(--accent-lt);font-weight:700;">Critical — Item Records</p>
    <p class="emph-text rv">"Transfer cost must<br>match average cost"</p>
    <p class="emph-sub rv">If the transfer cost differs from average cost, NetSuite posts a variance directly to the income statement — creating a phantom gain or loss.</p>
    <div class="rv" style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:8px;padding:var(--gap-sm) var(--gap);">
      <p style="color:rgba(255,255,255,.8);font-size:var(--fs-body);">Always verify transfer cost = average cost before processing transfer orders.</p>
    </div>
  </div>
  {foot("Item Records", 25)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 26 — Cost Flow Visual
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s26">
  {head("Section 5 — Item Records")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Cost Flow Visual</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">Cost flows through these four stages — each step either sets, updates, or consumes the item's cost.</p>
    <div class="dbox rv">
      <svg viewBox="0 0 700 145" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="30" width="140" height="68" rx="8" fill="#1a2b4a"/>
        <text x="80" y="58"  text-anchor="middle" fill="#fff" font-family="system-ui" font-size="12" font-weight="700">Purchase Order</text>
        <text x="80" y="77"  text-anchor="middle" fill="#93c5fd" font-family="system-ui" font-size="10">Sets initial cost</text>
        <text x="80" y="92"  text-anchor="middle" fill="rgba(255,255,255,.4)" font-family="system-ui" font-size="9">PO price</text>
        <path d="M150 64 L188 64" stroke="#2563eb" stroke-width="2" marker-end="url(#a5)"/>
        <rect x="188" y="30" width="148" height="68" rx="8" fill="#1e3461"/>
        <text x="262" y="58"  text-anchor="middle" fill="#fff" font-family="system-ui" font-size="12" font-weight="700">Item Receipt</text>
        <text x="262" y="77"  text-anchor="middle" fill="#86efac" font-family="system-ui" font-size="10">Updates avg cost</text>
        <text x="262" y="92"  text-anchor="middle" fill="rgba(255,255,255,.4)" font-family="system-ui" font-size="9">1210 Inventory ↑</text>
        <path d="M336 64 L374 64" stroke="#2563eb" stroke-width="2" marker-end="url(#a5)"/>
        <rect x="374" y="30" width="155" height="68" rx="8" fill="#b8860b" fill-opacity=".15" stroke="#b8860b" stroke-width="2"/>
        <text x="451" y="58"  text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="12" font-weight="700">Average Cost</text>
        <text x="451" y="77"  text-anchor="middle" fill="#92400e" font-family="system-ui" font-size="10">Blended unit cost</text>
        <text x="451" y="92"  text-anchor="middle" fill="#8898b0" font-family="system-ui" font-size="9">auto-calculated</text>
        <path d="M529 64 L568 64" stroke="#2563eb" stroke-width="2" marker-end="url(#a5)"/>
        <rect x="568" y="30" width="122" height="68" rx="8" fill="#f0f2f7" stroke="#dde3ef" stroke-width="1.5"/>
        <text x="629" y="56"  text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="12" font-weight="700">Fulfillment</text>
        <text x="629" y="75"  text-anchor="middle" fill="#dc2626" font-family="system-ui" font-size="10">Uses avg cost</text>
        <text x="629" y="90"  text-anchor="middle" fill="#475569" font-family="system-ui" font-size="9">5105 COGS ↑</text>
        <text x="350" y="130" text-anchor="middle" fill="#8898b0" font-family="system-ui" font-size="11">Average cost bridges purchasing and cost of goods sold</text>
        {arrow_defs([("a5","#2563eb")])}
      </svg>
    </div>
  </div>
  {foot("Item Records", 26)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 27 — Customer Record Overview
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s27">
  {head("Section 6 — Customer Records")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Customer Record Overview</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">The Customer record is the source of all sales-side reporting dimensions. Correct setup here flows through every transaction.</p>
    <div class="two-col rv" style="margin-top:var(--gap-sm);">
      <div class="card" style="border-left:4px solid var(--navy);">
        <h3>What It Drives</h3>
        <ul class="blist" style="margin-top:var(--gap-sm);">
          <li>Department on every SO and Invoice</li>
          <li>Sales Rep assignment</li>
          <li>Payment terms and pricing tier</li>
        </ul>
      </div>
      <div class="screenshot">
        <span class="icon">🔲</span>
        <span class="lbl">[INSERT NETSUITE SCREENSHOT HERE]<br>Customer Record form</span>
      </div>
    </div>
  </div>
  {foot("Customer Records", 27)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 28 — Required Fields
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s28">
  {head("Section 6 — Customer Records")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Required Fields — Customer Record</h2>
    <div class="rule rv"></div>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:5px solid var(--red);">
        <div style="display:flex;align-items:center;gap:.5em;"><span class="tag red">REQUIRED</span><h3>Department</h3></div>
        <p style="margin-top:var(--gap-sm);">The most critical field. Every sales transaction inherits the department from the customer. Wrong department = wrong reporting — and it cannot be easily fixed retroactively.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <div style="display:flex;align-items:center;gap:.5em;"><span class="tag">Required</span><h3>Sales Rep</h3></div>
        <p style="margin-top:var(--gap-sm);">Internal employee assigned to manage the account. Used for commission tracking and reporting.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--gray-400);">
        <div style="display:flex;align-items:center;gap:.5em;"><span class="tag gray">Optional</span><h3>Partner</h3></div>
        <p style="margin-top:var(--gap-sm);">External sales organization (rep firm or agency) that manages the account relationship on Westfield's behalf.</p>
      </div>
    </div>
  </div>
  {foot("Customer Records", 28)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 29 — Parent vs Child
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s29">
  {head("Section 6 — Customer Records")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Parent vs. Child Accounts</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">Large retailers are structured as a parent (corporate HQ) with multiple child accounts (individual stores or DCs).</p>
    <div class="dbox rv">
      <svg viewBox="0 0 560 170" xmlns="http://www.w3.org/2000/svg">
        <rect x="180" y="8" width="200" height="52" rx="8" fill="#1a2b4a"/>
        <text x="280" y="30"  text-anchor="middle" fill="#fff" font-family="system-ui" font-size="13" font-weight="700">Parent Account</text>
        <text x="280" y="50"  text-anchor="middle" fill="#93c5fd" font-family="system-ui" font-size="11">e.g., Bass Pro Shops Corp.</text>
        <line x1="280" y1="60" x2="280" y2="82" stroke="#2563eb" stroke-width="1.5"/>
        <line x1="80" y1="82" x2="480" y2="82" stroke="#2563eb" stroke-width="1.5"/>
        <line x1="80"  y1="82" x2="80"  y2="100" stroke="#2563eb" stroke-width="1.5"/>
        <line x1="280" y1="82" x2="280" y2="100" stroke="#2563eb" stroke-width="1.5"/>
        <line x1="480" y1="82" x2="480" y2="100" stroke="#2563eb" stroke-width="1.5"/>
        <rect x="10"  y="100" width="140" height="48" rx="6" fill="#f0f2f7" stroke="#2563eb" stroke-width="1.5"/>
        <text x="80"  y="121" text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="11" font-weight="600">Child Location</text>
        <text x="80"  y="138" text-anchor="middle" fill="#475569" font-family="system-ui" font-size="10">Store #1 – Indianapolis</text>
        <rect x="210" y="100" width="140" height="48" rx="6" fill="#f0f2f7" stroke="#2563eb" stroke-width="1.5"/>
        <text x="280" y="121" text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="11" font-weight="600">Child Location</text>
        <text x="280" y="138" text-anchor="middle" fill="#475569" font-family="system-ui" font-size="10">DC – Memphis</text>
        <rect x="410" y="100" width="140" height="48" rx="6" fill="#f0f2f7" stroke="#2563eb" stroke-width="1.5"/>
        <text x="480" y="121" text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="11" font-weight="600">Child Location</text>
        <text x="480" y="138" text-anchor="middle" fill="#475569" font-family="system-ui" font-size="10">Store #2 – Nashville</text>
        <text x="280" y="162" text-anchor="middle" fill="#8898b0" font-family="system-ui" font-size="10">Children inherit department, terms, and pricing from the parent</text>
      </svg>
    </div>
  </div>
  {foot("Customer Records", 29)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 30 — What NOT to Include
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s30">
  {head("Section 6 — Customer Records")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">What NOT to Include on Customer Records</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">These fields belong on the <strong>Item Record</strong> — not the Customer Record. Putting them on customers creates reporting confusion.</p>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:5px solid var(--red);">
        <div style="display:flex;align-items:center;gap:.6em;"><span style="font-size:1.3em;">🚫</span><h3 style="color:var(--red);">No Brand (Class)</h3></div>
        <p style="margin-top:var(--gap-sm);">Brand is a product attribute. A customer buys multiple brands — they don't <em>have</em> a brand. Class belongs on the <strong>Item record</strong>.</p>
      </div>
      <div class="card" style="border-left:5px solid var(--red);">
        <div style="display:flex;align-items:center;gap:.6em;"><span style="font-size:1.3em;">🚫</span><h3 style="color:var(--red);">No Item Category</h3></div>
        <p style="margin-top:var(--gap-sm);">Item Category describes the product type (Furniture, Accessories, etc.). This is also an <strong>Item-level</strong> attribute — customers don't have product categories.</p>
      </div>
    </div>
  </div>
  {foot("Customer Records", 30)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 31 — Auto-Population
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s31">
  {head("Section 6 — Customer Records")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Auto-Population</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">When a customer is selected on a transaction, these fields populate automatically from the customer record.</p>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap-sm);">
      <div class="card" style="border-left:4px solid var(--green);">
        <div style="display:flex;align-items:center;gap:.6em;"><span class="tag ok">Auto</span><h3>Department</h3></div>
        <p style="margin-top:var(--gap-sm);">Flows from customer to the transaction header. This is how every transaction gets classified for P&amp;L reporting.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--green);">
        <div style="display:flex;align-items:center;gap:.6em;"><span class="tag ok">Auto</span><h3>Terms</h3></div>
        <p style="margin-top:var(--gap-sm);">Payment terms (Net 30, Net 60, etc.) default from the customer but can be overridden on the transaction.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--green);">
        <div style="display:flex;align-items:center;gap:.6em;"><span class="tag ok">Auto</span><h3>Pricing</h3></div>
        <p style="margin-top:var(--gap-sm);">Price level or customer-specific pricing populates on line items based on the customer's assigned price tier.</p>
      </div>
    </div>
  </div>
  {foot("Customer Records", 31)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 32 — Vendor Records
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s32">
  {head("Section 7 — Supporting Records")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Vendor Records</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">Vendor records represent the companies Westfield purchases goods and services from.</p>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3>Used For Purchasing</h3>
        <ul class="blist" style="margin-top:var(--gap-sm);">
          <li>Required on all <strong>Purchase Orders</strong></li>
          <li>Required on all <strong>Vendor Bills</strong></li>
          <li>Stores payment terms, currency, and remit-to address</li>
        </ul>
      </div>
      <div class="card">
        <h3>Key Vendor Types at Westfield</h3>
        <ul class="blist" style="margin-top:var(--gap-sm);">
          <li><strong>Suppliers</strong> — factories and manufacturers (e.g., HFDT in China)</li>
          <li><strong>Freight vendors</strong> — shipping and logistics providers</li>
          <li><strong>Service vendors</strong> — contractors, utilities, subscriptions</li>
        </ul>
      </div>
    </div>
  </div>
  {foot("Supporting Records", 32)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 33 — Employee Records
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s33">
  {head("Section 7 — Supporting Records")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Employee Records</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">Employee records represent internal NetSuite users — primarily used for assignment, approvals, and tracking.</p>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card">
        <h3>Core Fields</h3>
        <ul class="blist" style="margin-top:var(--gap-sm);">
          <li><strong>Name</strong> — used in Sales Rep assignments and approvals</li>
          <li><strong>Email</strong> — tied to NetSuite login credentials</li>
        </ul>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3>Where Employee Records Are Used</h3>
        <ul class="blist" style="margin-top:var(--gap-sm);">
          <li>Sales Rep field on Customer Record and Sales Orders</li>
          <li>Approval workflows (POs, expenses)</li>
          <li>NetSuite user access and role assignments</li>
        </ul>
      </div>
    </div>
  </div>
  {foot("Supporting Records", 33)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 34 — Partner Records
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s34">
  {head("Section 7 — Supporting Records")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Partner Records</h2>
    <div class="rule rv"></div>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:4px solid var(--gold);">
        <h3>What is a Partner?</h3>
        <p style="margin-top:var(--gap-sm);">A <strong>Partner</strong> represents an <em>external sales organization</em> — typically a manufacturer's rep firm or independent sales agency that manages customer relationships on Westfield's behalf.</p>
      </div>
      <div class="card">
        <h3>Dual Nature</h3>
        <ul class="blist" style="margin-top:var(--gap-sm);">
          <li>Appears on <strong>Customer records</strong> to associate an account with a rep firm</li>
          <li>Is <strong>also a Vendor</strong> in NetSuite — commissions are paid via vendor bills</li>
        </ul>
      </div>
    </div>
  </div>
  {foot("Supporting Records", 34)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 35 — Departments
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s35">
  {head("Section 8 — System Structure")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Departments</h2>
    <div class="rule rv"></div>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3>Where It Comes From</h3>
        <p style="margin-top:var(--gap-sm);">Department flows from the <strong>Customer record</strong> to every Sales Order, Invoice, and Item Fulfillment. It is not manually set on each transaction.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--green);">
        <h3>What It Drives</h3>
        <ul class="blist" style="margin-top:var(--gap-sm);">
          <li>P&amp;L reporting segmented by sales channel</li>
          <li>Budget vs. actual comparisons by department</li>
          <li>Commission calculations for sales reps</li>
          <li>Expense assignment (e.g., Warehouse = Dept on inventory adjustments)</li>
        </ul>
      </div>
    </div>
  </div>
  {foot("System Structure", 35)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 36 — Classes (Brands)
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s36">
  {head("Section 8 — System Structure")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Classes (Brands)</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">In NetSuite, <strong>Class = Brand</strong>. Set on the Item record. Used for brand-level financial reporting.</p>
    <div class="dbox rv">
      <svg viewBox="0 0 600 148" xmlns="http://www.w3.org/2000/svg">
        <rect x="220" y="5" width="160" height="42" rx="8" fill="#1a2b4a"/>
        <text x="300" y="24" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="12" font-weight="700">Brand Classes</text>
        <text x="300" y="40" text-anchor="middle" fill="#93c5fd" font-family="system-ui" font-size="10">(NetSuite Class field on Item)</text>
        <line x1="300" y1="47" x2="300" y2="65" stroke="#2563eb" stroke-width="1.5"/>
        <line x1="90"  y1="65" x2="510" y2="65" stroke="#2563eb" stroke-width="1.5"/>
        <line x1="90"  y1="65" x2="90"  y2="82" stroke="#2563eb" stroke-width="1.5"/>
        <line x1="300" y1="65" x2="300" y2="82" stroke="#2563eb" stroke-width="1.5"/>
        <line x1="510" y1="65" x2="510" y2="82" stroke="#2563eb" stroke-width="1.5"/>
        <rect x="16" y="82" width="148" height="46" rx="6" fill="#1e3461"/>
        <text x="90" y="104" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="11" font-weight="700">Strategic</text>
        <text x="90" y="120" text-anchor="middle" fill="#93c5fd" font-family="system-ui" font-size="10">e.g., Timber Ridge</text>
        <rect x="226" y="82" width="148" height="46" rx="6" fill="#1e3461"/>
        <text x="300" y="104" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="11" font-weight="700">Partner Brand</text>
        <text x="300" y="120" text-anchor="middle" fill="#93c5fd" font-family="system-ui" font-size="10">e.g., GCI Outdoor</text>
        <rect x="436" y="82" width="148" height="46" rx="6" fill="#243856"/>
        <text x="510" y="104" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="11" font-weight="700">Private Label</text>
        <text x="510" y="120" text-anchor="middle" fill="#93c5fd" font-family="system-ui" font-size="10">e.g., Westfield Brand</text>
        <text x="300" y="142" text-anchor="middle" fill="#8898b0" font-family="system-ui" font-size="10">Class is set on the Item record — it never appears on the Customer record</text>
      </svg>
    </div>
  </div>
  {foot("System Structure", 36)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 37 — Item Categories
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s37">
  {head("Section 8 — System Structure")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Item Categories</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">Item Categories classify products by type, enabling category-level analysis alongside brand-level (Class) reporting.</p>
    <div class="dbox rv">
      <svg viewBox="0 0 580 150" xmlns="http://www.w3.org/2000/svg">
        <rect x="200" y="5" width="180" height="42" rx="8" fill="#1a2b4a"/>
        <text x="290" y="23" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="12" font-weight="700">Item Category</text>
        <text x="290" y="39" text-anchor="middle" fill="#93c5fd" font-family="system-ui" font-size="10">Set on the Item record</text>
        <line x1="290" y1="47" x2="290" y2="65" stroke="#2563eb" stroke-width="1.5"/>
        <line x1="140" y1="65" x2="450" y2="65" stroke="#2563eb" stroke-width="1.5"/>
        <line x1="140" y1="65" x2="140" y2="82" stroke="#2563eb" stroke-width="1.5"/>
        <line x1="450" y1="65" x2="450" y2="82" stroke="#2563eb" stroke-width="1.5"/>
        <rect x="55"  y="82" width="170" height="46" rx="6" fill="#f0f2f7" stroke="#2563eb" stroke-width="1.5"/>
        <text x="140" y="104" text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="12" font-weight="700">Furniture</text>
        <text x="140" y="120" text-anchor="middle" fill="#475569" font-family="system-ui" font-size="10">Folding, Rocking, Tables</text>
        <rect x="365" y="82" width="170" height="46" rx="6" fill="#f0f2f7" stroke="#2563eb" stroke-width="1.5"/>
        <text x="450" y="104" text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="12" font-weight="700">Accessories</text>
        <text x="450" y="120" text-anchor="middle" fill="#475569" font-family="system-ui" font-size="10">Storage, Bags, Parts</text>
        <text x="290" y="143" text-anchor="middle" fill="#8898b0" font-family="system-ui" font-size="10">Example: Timber Ridge Chair → Class=Timber Ridge | Category=Furniture → Folding</text>
      </svg>
    </div>
  </div>
  {foot("System Structure", 37)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 38 — Locations
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s38">
  {head("Section 8 — System Structure")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Locations</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">Locations track where inventory is physically present — or virtually assigned for reporting purposes.</p>
    <div class="two-col rv" style="margin-top:var(--gap-sm);">
      <div class="card" style="border-left:4px solid var(--accent);">
        <div style="display:flex;align-items:center;gap:.5em;margin-bottom:var(--gap-sm);"><span style="font-size:1.3em;">🏭</span><h3>Physical Locations</h3></div>
        <ul class="blist">
          <li>Warehouses and distribution centers</li>
          <li>Goods are physically present here</li>
          <li>Cycle counts are performed at this level</li>
        </ul>
      </div>
      <div class="card" style="border-left:4px solid var(--gold);">
        <div style="display:flex;align-items:center;gap:.5em;margin-bottom:var(--gap-sm);"><span style="font-size:1.3em;">🗂️</span><h3>Virtual Locations</h3></div>
        <ul class="blist">
          <li>Consignment, in-transit, or display stock</li>
          <li>Inventory exists on paper — not in a warehouse</li>
          <li>Used for allocation and reporting only</li>
        </ul>
      </div>
    </div>
  </div>
  {foot("System Structure", 38)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 39 — How It All Connects
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s39">
  {head("Section 8 — System Structure")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">How It All Connects</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">Every record feeds a reporting dimension. Correct setup cascades through every transaction automatically.</p>
    <div class="dbox rv">
      <svg viewBox="0 0 640 185" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="155" height="52" rx="8" fill="#1a2b4a"/>
        <text x="87" y="32" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="12" font-weight="700">Customer</text>
        <text x="87" y="50" text-anchor="middle" fill="#93c5fd" font-family="system-ui" font-size="10">Record</text>
        <path d="M165 36 L225 36" stroke="#2563eb" stroke-width="2" marker-end="url(#a6)"/>
        <rect x="225" y="10" width="145" height="52" rx="8" fill="#f0f2f7" stroke="#2563eb" stroke-width="2"/>
        <text x="297" y="32" text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="12" font-weight="700">Department</text>
        <text x="297" y="50" text-anchor="middle" fill="#475569" font-family="system-ui" font-size="10">→ P&amp;L by channel</text>
        <rect x="10" y="85" width="155" height="52" rx="8" fill="#1a2b4a"/>
        <text x="87" y="107" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="12" font-weight="700">Item</text>
        <text x="87" y="125" text-anchor="middle" fill="#93c5fd" font-family="system-ui" font-size="10">Record</text>
        <path d="M165 100 L225 90" stroke="#b8860b" stroke-width="2" marker-end="url(#a6g)"/>
        <path d="M165 108 L225 128" stroke="#b8860b" stroke-width="2" marker-end="url(#a6g)"/>
        <rect x="225" y="72" width="145" height="43" rx="7" fill="#fffbea" stroke="#b8860b" stroke-width="1.5"/>
        <text x="297" y="91" text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="11" font-weight="700">Brand (Class)</text>
        <text x="297" y="107" text-anchor="middle" fill="#92400e" font-family="system-ui" font-size="10">→ P&amp;L by brand</text>
        <rect x="225" y="120" width="145" height="43" rx="7" fill="#fffbea" stroke="#b8860b" stroke-width="1.5"/>
        <text x="297" y="139" text-anchor="middle" fill="#1a2b4a" font-family="system-ui" font-size="11" font-weight="700">Item Category</text>
        <text x="297" y="155" text-anchor="middle" fill="#92400e" font-family="system-ui" font-size="10">→ P&amp;L by type</text>
        <rect x="10" y="155" width="155" height="22" rx="6" fill="#1e3461"/>
        <text x="87" y="170" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="10" font-weight="700">Location → Inventory reporting</text>
        <path d="M370 36 L430 90" stroke="#8898b0" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#a6g)"/>
        <path d="M370 94 L430 100" stroke="#8898b0" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#a6g)"/>
        <path d="M370 142 L430 110" stroke="#8898b0" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#a6g)"/>
        <rect x="430" y="60" width="200" height="68" rx="8" fill="#15803d" fill-opacity=".1" stroke="#15803d" stroke-width="2"/>
        <text x="530" y="87"  text-anchor="middle" fill="#14532d" font-family="system-ui" font-size="13" font-weight="700">Financial Reports</text>
        <text x="530" y="106" text-anchor="middle" fill="#166534" font-family="system-ui" font-size="10">P&amp;L by Dept × Brand</text>
        <text x="530" y="120" text-anchor="middle" fill="#166534" font-family="system-ui" font-size="10">× Category × Location</text>
        {arrow_defs([("a6","#2563eb"),("a6g","#8898b0")])}
      </svg>
    </div>
  </div>
  {foot("System Structure", 39)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 40 — Scenario Setup
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s40">
  {head("Section 9 — Final Walkthrough")}
  <div class="s-body" style="gap:var(--gap);">
    <h2 class="rv">Scenario Setup</h2>
    <div class="rule rv"></div>
    <p class="rv" style="font-size:var(--fs-body);">Let's walk through a complete transaction end-to-end using a concrete Westfield example.</p>
    <div class="rv" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:var(--gap);margin-top:var(--gap-sm);">
      <div class="card" style="border-top:3px solid var(--accent);text-align:center;">
        <span style="font-size:clamp(1.4rem,3.5vw,2.2rem);">🏬</span>
        <h3 style="margin-top:var(--gap-sm);">Customer</h3>
        <p style="color:var(--navy);font-weight:700;font-size:var(--fs-h3);margin-top:var(--gap-sm);">Bass Pro Shops</p>
      </div>
      <div class="card" style="border-top:3px solid var(--gold);text-align:center;">
        <span style="font-size:clamp(1.4rem,3.5vw,2.2rem);">📊</span>
        <h3 style="margin-top:var(--gap-sm);">Department</h3>
        <p style="color:var(--navy);font-weight:700;font-size:var(--fs-h3);margin-top:var(--gap-sm);">SD2</p>
        <p style="font-size:var(--fs-small);color:var(--gray-400);">From customer record</p>
      </div>
      <div class="card" style="border-top:3px solid var(--green);text-align:center;">
        <span style="font-size:clamp(1.4rem,3.5vw,2.2rem);">🪑</span>
        <h3 style="margin-top:var(--gap-sm);">Item</h3>
        <p style="color:var(--navy);font-weight:700;font-size:var(--fs-h3);margin-top:var(--gap-sm);">Timber Ridge Chair</p>
        <p style="font-size:var(--fs-small);color:var(--gray-400);">Class = Timber Ridge</p>
      </div>
    </div>
    <div class="hbox rv" style="margin-top:var(--gap-sm);"><p>We'll trace this order from Sales Order → Fulfillment → Invoice and watch the financial impact at each step.</p></div>
  </div>
  {foot("Final Walkthrough", 40)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 41 — Sales Order Step
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s41">
  {head("Section 9 — Final Walkthrough")}
  <div class="s-body" style="gap:var(--gap);">
    <div class="rv" style="display:flex;align-items:center;gap:var(--gap);">
      <div class="snum">1</div>
      <h2 style="margin-bottom:0;">Sales Order</h2>
    </div>
    <div class="rule rv"></div>
    <div class="rv" style="display:flex;flex-direction:column;gap:var(--gap);">
      <div class="card" style="border-left:4px solid var(--gold);">
        <h3>Financial Impact: <span style="color:var(--gold);">$0</span></h3>
        <p style="margin-top:var(--gap-sm);">No accounting entries are created. The Sales Order reserves inventory and locks in the commitment, but nothing posts to the general ledger.</p>
      </div>
      <div class="card">
        <h3>What Gets Set on the SO</h3>
        <ul class="blist" style="margin-top:var(--gap-sm);">
          <li>Customer = Bass Pro Shops</li>
          <li>Department = SD2 <em>(auto from customer)</em></li>
          <li>Item = Timber Ridge Chair, Qty = 100</li>
          <li>Price = per customer price level</li>
        </ul>
      </div>
    </div>
  </div>
  {foot("Final Walkthrough — Step 1 of 3", 41)}
</section>
""")

# ─────────────────────────────────────────────────────────
# SLIDE 42 — Fulfillment Step
# ─────────────────────────────────────────────────────────
slides_html.append(f"""
<section class="slide" id="s42">
  {head("Section 9 — Final Walkthrough")}
  <div class="s-