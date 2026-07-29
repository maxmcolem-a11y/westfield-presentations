#!/usr/bin/env python3
import html
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "industrial-design-innovation-portfolio-august-2026"
MODEL = json.loads((SOURCE / "data/portfolio-model.json").read_text())
PROJECTS = {p["name"]: p for p in MODEL["projects"]}
PREFIX = "../industrial-design-innovation-portfolio-august-2026/"

heroes = ["Origami Wagon", "Flow-Motion V2", "Instant Indoor"]
pairs = [
    ("Diamond Daypack", "Spiral Daypack"),
    ("Hawkeye V3", "Suspend Chair"),
    ("Hard Liners", "ComfortCore Hybrid Arms"),
    ("GRAM Chair", "Camp / Field Utility Board"),
    ("Systems Wagon", "Westfield Adventure Pack"),
    ("Westfield Adventure Tote", "Concertina Cooler"),
]
TOTAL_SLIDES = 1 + len(heroes) + len(pairs)

hero_copy = {
    "Origami Wagon": (
        "One sheet. One unforgettable transformation.",
        "A living-hinge body collapses the old wagon equation—tube cage, sewn body, loose complexity—into a structural shell that folds like a piece of engineered magic.",
        "This is platform thinking made visible: construction method, pack-down behavior, retail theater, and brand story all working as one.",
        "The team has already proven full-scale folding. The next unlock is converting that wonder into repeatable load performance, hinge life, and production confidence.",
    ),
    "Flow-Motion V2": (
        "Motion, tuned—not guessed.",
        "Flow V2 turns rocker feel into a deliberate system. Wedge geometry and leaf-spring behavior let the team shape lean-back character, return force, and pinch-gap control instead of accepting whatever one spring rate delivers.",
        "The result is more than movement. It is a repeatable Westfield motion signature that can scale across a furniture family.",
        "Digital validation is complete and the production sample has shipped. The team is now tuning the human experience, not searching for the mechanism.",
    ),
    "Instant Indoor": (
        "Outdoor speed. Indoor polish.",
        "Instant Indoor takes the effortless setup customers expect from Westfield and translates it into a refined furniture proposition—fast transformation without the visual language of temporary gear.",
        "It is a category bridge: the confidence and portability of outdoor engineering, upgraded for apartments, guest rooms, flexible offices, and modern multipurpose living.",
        "The core experience is already tangible. The next move is disciplined refinement around comfort, finish, stability, and the moment of transformation.",
    ),
}

def media(project):
    return PREFIX + project["hero"]

def product_card(name):
    p = PROJECTS[name]
    hook, why = p.get("rallyLine", ""), p.get("whyCool", "")
    return f"""
      <article class="product-card">
        <button class="media-button" data-image="{html.escape(media(p))}" data-alt="{html.escape(p.get('heroAlt', name))}">
          <img src="{html.escape(media(p))}" alt="{html.escape(p.get('heroAlt', name))}" loading="lazy">
          <span class="media-open">EXPAND ↗</span>
        </button>
        <div class="card-copy">
          <div class="card-meta"><span>{html.escape(p['category'])}</span><span>TRL {p['trl']}</span></div>
          <h2>{html.escape(name)}</h2>
          <p class="hook">{html.escape(hook)}</p>
          <p>{html.escape(why)}</p>
          <div class="proof"><b>TEAM PROOF</b><span>{html.escape(p['brief'])}</span></div>
        </div>
      </article>"""

def hero_slide(name, number):
    p = PROJECTS[name]
    headline, lead, rally, proof = hero_copy[name]
    simulation = ""
    if name == "Origami Wagon":
        simulation = f"""
          <div class="simulation-wrap">
            <iframe title="Origami Wagon interactive folding simulation"
              src="{html.escape(p['simulation'])}" loading="lazy"
              referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
            <a href="{html.escape(p['simulation'])}" target="_blank" rel="noopener">OPEN FULL-SCREEN SIMULATION ↗</a>
          </div>"""
    else:
        simulation = f"""
          <button class="hero-media media-button" data-image="{html.escape(media(p))}" data-alt="{html.escape(p.get('heroAlt', name))}">
            <img src="{html.escape(media(p))}" alt="{html.escape(p.get('heroAlt', name))}">
            <span class="media-open">EXPAND ↗</span>
          </button>"""
    return f"""
  <section class="slide hero-slide" id="{name.lower().replace(' ','-').replace('/','-')}">
    <img class="logo" src="assets/westfield-outdoors-logo.png" alt="Westfield Outdoors">
    <div class="hero-grid">
      <div class="hero-copy">
        <p class="eyebrow">FEATURED PLATFORM · {html.escape(p['code'])}</p>
        <h1>{html.escape(name)}</h1>
        <h3>{html.escape(headline)}</h3>
        <p class="hero-lead">{html.escape(lead)}</p>
        <p>{html.escape(rally)}</p>
        <div class="hero-proof"><span>WHERE THE TEAM HAS IT</span><b>{html.escape(proof)}</b></div>
        <div class="metrics"><span>TRL {p['trl']}</span><span>{html.escape(p['category'])}</span><span>Momentum: high</span></div>
      </div>
      {simulation}
    </div>
    <div class="section-label">INDUSTRIAL DESIGN · HERO PLATFORM</div>
    <div class="slide-number">{number:02d} / {TOTAL_SLIDES:02d}</div>
  </section>"""

slides = [hero_slide(name, i + 2) for i, name in enumerate(heroes)]
for i, pair in enumerate(pairs, start=5):
    slides.append(f"""
  <section class="slide pair-slide" id="showcase-{i}">
    <img class="logo" src="assets/westfield-outdoors-logo.png" alt="Westfield Outdoors">
    <div class="pair-shell">
      <div class="pair-heading">
        <p class="eyebrow">PORTFOLIO MOMENTUM</p>
        <h1>Designed as products.<br><span>Built as leverage.</span></h1>
      </div>
      <div class="pair-grid">{product_card(pair[0])}{product_card(pair[1])}</div>
    </div>
    <div class="section-label">WESTFIELD INDUSTRIAL DESIGN · CATEGORY BUILDERS</div>
    <div class="slide-number">{i:02d} / {TOTAL_SLIDES:02d}</div>
  </section>""")

doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Industrial Design — Built to Move the Category</title>
  <meta name="description" content="Westfield Industrial Design innovation showcase: category-building products, platform thinking, and proof in motion.">
  <link rel="canonical" href="https://maxmcolem-a11y.github.io/westfield-presentations/industrial-design-innovation-showcase-august-2026/">
  <meta property="og:type" content="website"><meta property="og:site_name" content="Westfield Outdoors">
  <meta property="og:title" content="Industrial Design — Built to Move the Category">
  <meta property="og:description" content="The team behind the next Westfield product platforms.">
  <meta property="og:url" content="https://maxmcolem-a11y.github.io/westfield-presentations/industrial-design-innovation-showcase-august-2026/">
  <meta property="og:image" content="https://maxmcolem-a11y.github.io/westfield-presentations/industrial-design-innovation-showcase-august-2026/assets/social-preview.png">
  <meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#d53a30">
  <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
  :root{{--paper:#f5f3ed;--white:#fff;--ink:#111;--muted:#62615d;--line:rgba(17,17,17,.14);--red:#d53a30;--blue:#244f68;--green:#2b6f55}}
  *{{box-sizing:border-box}}html{{scroll-snap-type:y mandatory;scroll-behavior:auto;background:#ddd}}body{{margin:0;font-family:Inter,Arial,sans-serif;color:var(--ink);background:#ddd}}
  .slide{{height:100vh;height:100dvh;scroll-snap-align:start;position:relative;overflow:hidden;background:var(--paper)}}
  .slide::after{{content:"Property of Westfield Outdoors. Confidential and proprietary. Do not reproduce, distribute, or disclose without written permission.";position:absolute;bottom:14px;left:50%;transform:translateX(-50%);font-size:7px;letter-spacing:.04em;color:rgba(17,17,17,.38);white-space:nowrap}}
  .logo{{position:absolute;z-index:4;right:28px;top:22px;width:145px;opacity:.88}}.slide-number{{position:absolute;right:28px;bottom:17px;font-size:10px;font-weight:900;letter-spacing:.12em;color:#777}}.section-label{{position:absolute;left:28px;bottom:17px;font-size:9px;font-weight:800;letter-spacing:.14em;color:#777}}
  .eyebrow{{margin:0;color:var(--red);font-weight:900;font-size:11px;letter-spacing:.17em;text-transform:uppercase}}h1,h2,h3,p{{margin-top:0}}h1{{font-size:clamp(48px,5.2vw,84px);line-height:.93;letter-spacing:-.065em}}h1 span{{color:var(--red)}}
  .cover{{background:#edeae1;display:grid;grid-template-columns:1.05fr .95fr}}.cover-copy{{padding:9vh 5.6vw;display:flex;flex-direction:column;justify-content:center;position:relative;z-index:2}}.cover h1{{max-width:860px;font-size:clamp(62px,7.5vw,112px)}}.cover .dek{{font-size:clamp(18px,1.8vw,28px);line-height:1.35;max-width:700px;color:#3b3a37}}.cover-statement{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:36px}}.cover-statement div{{border-top:3px solid var(--ink);padding-top:11px}}.cover-statement b{{display:block;font-size:24px}}.cover-statement span{{font-size:11px;color:var(--muted);font-weight:700}}.cover-visual{{position:relative;background:#111;overflow:hidden}}.cover-visual img{{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.12);opacity:.75}}.cover-visual::after{{content:"";position:absolute;inset:0;background:linear-gradient(145deg,rgba(213,58,48,.08),rgba(0,0,0,.48))}}.cover-tag{{position:absolute;left:34px;bottom:54px;z-index:2;color:white;font-size:clamp(23px,2.5vw,42px);line-height:1.05;font-weight:900;max-width:430px}}
  .hero-grid{{height:100%;display:grid;grid-template-columns:.84fr 1.16fr}}.hero-copy{{padding:9vh 4.2vw 5vh;display:flex;flex-direction:column;justify-content:center}}.hero-copy h1{{margin:.55rem 0 .35rem}}.hero-copy h3{{font-size:clamp(22px,2vw,34px);margin:0 0 18px;color:var(--blue);letter-spacing:-.035em}}.hero-copy p{{font-size:clamp(13px,1.05vw,17px);line-height:1.48;max-width:680px}}.hero-lead{{font-weight:750;font-size:clamp(15px,1.25vw,20px)!important}}.hero-proof{{border-left:5px solid var(--red);padding:13px 16px;margin:8px 0 15px;background:#fff}}.hero-proof span{{display:block;font-size:9px;letter-spacing:.14em;font-weight:900;color:var(--red);margin-bottom:5px}}.hero-proof b{{font-size:13px;line-height:1.4}}.metrics{{display:flex;gap:8px;flex-wrap:wrap}}.metrics span{{padding:8px 11px;border-radius:999px;background:#111;color:#fff;font-size:9px;font-weight:800;text-transform:uppercase;letter-spacing:.08em}}
  .hero-media,.simulation-wrap{{border:0;padding:0;margin:0;background:#111;position:relative;overflow:hidden}}.hero-media img{{width:100%;height:100%;object-fit:contain;background:#eceae3}}.simulation-wrap iframe{{width:100%;height:100%;border:0;background:#111}}.simulation-wrap a{{position:absolute;right:20px;bottom:24px;background:#fff;color:#111;padding:11px 15px;font-size:10px;font-weight:900;text-decoration:none;border-radius:999px}}
  .pair-shell{{height:100%;padding:7vh 4vw 4.5vh;display:grid;grid-template-rows:auto 1fr;gap:18px}}.pair-heading{{display:flex;justify-content:space-between;align-items:end;padding-right:180px}}.pair-heading h1{{font-size:clamp(34px,3.6vw,58px);margin:0}}.pair-grid{{display:grid;grid-template-columns:1fr 1fr;gap:18px;min-height:0}}.product-card{{background:#fff;border:1px solid var(--line);display:grid;grid-template-columns:.92fr 1.08fr;min-height:0;overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.06)}}.media-button{{cursor:zoom-in;position:relative;border:0;padding:0;background:#e7e5df;overflow:hidden}}.media-button img{{width:100%;height:100%;object-fit:cover;display:block;filter:grayscale(1) contrast(1.06);transition:.35s}}.media-button:hover img{{transform:scale(1.025);filter:grayscale(.15)}}.media-open{{position:absolute;right:10px;bottom:10px;background:#111;color:#fff;padding:6px 8px;font-size:8px;font-weight:900;letter-spacing:.08em}}.card-copy{{padding:22px 20px;display:flex;flex-direction:column;justify-content:center;min-width:0}}.card-meta{{display:flex;justify-content:space-between;font-size:8px;letter-spacing:.11em;text-transform:uppercase;font-weight:900;color:var(--red)}}.card-copy h2{{font-size:clamp(24px,2.1vw,38px);line-height:.96;letter-spacing:-.045em;margin:10px 0}}.card-copy p{{font-size:clamp(10px,.8vw,13px);line-height:1.4;color:#4d4c49}}.card-copy .hook{{font-weight:850;color:#111;font-size:clamp(11px,.95vw,15px)}}.proof{{border-top:1px solid var(--line);padding-top:10px;margin-top:auto;display:grid;gap:4px}}.proof b{{font-size:8px;letter-spacing:.12em;color:var(--green)}}.proof span{{font-size:9px;line-height:1.35;color:#5a5955}}
  .media-open-modal{{position:fixed;inset:0;z-index:50;background:rgba(0,0,0,.92);display:none;align-items:center;justify-content:center;padding:44px}}.media-open-modal.open{{display:flex}}.media-open-modal img{{max-width:94vw;max-height:90vh;object-fit:contain}}.modal-close{{position:absolute;right:24px;top:18px;border:1px solid rgba(255,255,255,.55);background:#111;color:#fff;width:42px;height:42px;border-radius:50%;font-size:22px;cursor:pointer}}
  .nav{{position:fixed;z-index:20;right:12px;top:50%;transform:translateY(-50%);display:grid;gap:7px}}.nav button{{width:7px;height:7px;padding:0;border:0;border-radius:50%;background:rgba(0,0,0,.25);cursor:pointer}}.nav button.active{{background:var(--red);transform:scale(1.45)}}.lang{{position:fixed;z-index:25;left:18px;bottom:34px;border:1px solid #999;background:#fff;color:#555;border-radius:999px;padding:7px 11px;font:800 9px Inter;opacity:.78}}
  @media(max-width:850px){{.slide{{height:auto;min-height:100dvh;overflow:visible}}.cover,.hero-grid{{grid-template-columns:1fr}}.cover-visual{{min-height:38vh}}.cover-copy{{padding:7rem 1.2rem 3rem}}.cover h1{{font-size:52px}}.cover-statement{{grid-template-columns:1fr 1fr 1fr}}.hero-copy{{padding:6rem 1.2rem 2rem}}.hero-media,.simulation-wrap{{min-height:45vh}}.pair-shell{{padding:5.8rem 1rem 3.5rem}}.pair-heading{{padding-right:0}}.pair-heading .eyebrow{{display:none}}.pair-grid{{grid-template-columns:1fr;gap:12px}}.product-card{{min-height:37vh}}.card-copy{{padding:15px}}.nav{{display:none}}.logo{{width:108px}}.section-label{{display:none}}.slide::after{{font-size:5px;max-width:72vw;white-space:normal;text-align:center}}}}
  </style>
</head>
<body>
  <button class="lang" type="button" title="Chinese translation is added after final English approval">中文 · FINAL PASS</button>
  <nav class="nav" aria-label="Slide navigation"></nav>
  <section class="slide cover" id="cover">
    <img class="logo" src="assets/westfield-outdoors-logo.png" alt="Westfield Outdoors">
    <div class="cover-copy">
      <p class="eyebrow">INDUSTRIAL DESIGN · AUGUST 2026</p>
      <h1>Built to move<br><span>the category.</span></h1>
      <p class="dek">A team turning mechanisms, materials, and customer behavior into products people can understand in a second—and remember for years.</p>
      <div class="cover-statement"><div><b>15</b><span>market-facing concepts</span></div><div><b>3</b><span>hero platforms</span></div><div><b>1</b><span>team building the next curve</span></div></div>
    </div>
    <div class="cover-visual"><img src="{media(PROJECTS['Origami Wagon'])}" alt="Origami Wagon"><div class="cover-tag">Not styling.<br>Structural advantage.</div></div>
    <div class="section-label">WESTFIELD OUTDOORS · CONFIDENTIAL</div><div class="slide-number">01 / {TOTAL_SLIDES:02d}</div>
  </section>
  {''.join(slides)}
  <div class="media-open-modal" role="dialog" aria-modal="true" aria-label="Expanded product image"><button class="modal-close" aria-label="Close">×</button><img alt=""></div>
  <script>
  const slides=[...document.querySelectorAll('.slide')],nav=document.querySelector('.nav');
  slides.forEach((s,i)=>{{const b=document.createElement('button');b.ariaLabel=`Go to slide ${{i+1}}`;b.onclick=()=>s.scrollIntoView({{behavior:'smooth'}});nav.appendChild(b)}});
  const dots=[...nav.children];const observer=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{dots.forEach(d=>d.classList.remove('active'));dots[slides.indexOf(e.target)].classList.add('active')}}}}),{{threshold:.55}});slides.forEach(s=>observer.observe(s));
  document.addEventListener('keydown',e=>{{const i=slides.findIndex(s=>Math.abs(s.getBoundingClientRect().top)<innerHeight*.5);if(e.key==='ArrowDown'||e.key==='PageDown')slides[Math.min(i+1,slides.length-1)].scrollIntoView({{behavior:'smooth'}});if(e.key==='ArrowUp'||e.key==='PageUp')slides[Math.max(i-1,0)].scrollIntoView({{behavior:'smooth'}})}});
  const modal=document.querySelector('.media-open-modal'),modalImg=modal.querySelector('img');document.querySelectorAll('.media-button').forEach(b=>b.addEventListener('click',()=>{{modalImg.src=b.dataset.image;modalImg.alt=b.dataset.alt||'';modal.classList.add('open')}}));const close=()=>{{modal.classList.remove('open');modalImg.src=''}};modal.querySelector('.modal-close').onclick=close;modal.onclick=e=>{{if(e.target===modal)close()}};document.addEventListener('keydown',e=>{{if(e.key==='Escape')close()}});
  </script>
</body>
</html>"""

(ROOT / "index.html").write_text(doc)
preview = Image.new("RGB", (1200, 630), "#f1eee5")
hero = Image.open(SOURCE / PROJECTS["Origami Wagon"]["hero"]).convert("RGB")
hero = ImageOps.grayscale(hero).convert("RGB")
hero = ImageEnhance.Contrast(hero).enhance(1.12)
hero = ImageOps.fit(hero, (515, 630), method=Image.Resampling.LANCZOS, centering=(0.5, 0.48))
preview.paste(hero, (685, 0))
draw = ImageDraw.Draw(preview)
font_bold = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
font_regular = "/System/Library/Fonts/Supplemental/Arial.ttf"
eyebrow_font = ImageFont.truetype(font_bold, 19)
title_font = ImageFont.truetype(font_bold, 72)
body_font = ImageFont.truetype(font_regular, 25)
chip_font = ImageFont.truetype(font_bold, 16)
draw.text((58, 55), "WESTFIELD INDUSTRIAL DESIGN", font=eyebrow_font, fill="#d53a30")
draw.multiline_text((58, 112), "Built to move\nthe category.", font=title_font, fill="#111111", spacing=-5)
draw.multiline_text(
    (61, 335),
    "15 market-facing concepts.\n3 hero platforms. One team\nbuilding the next curve.",
    font=body_font,
    fill="#3f3d39",
    spacing=8,
)
for x, label in [(60, "ORIGAMI WAGON"), (243, "FLOW V2"), (365, "INSTANT INDOOR")]:
    width = draw.textbbox((0, 0), label, font=chip_font)[2] + 26
    draw.rounded_rectangle((x, 518, x + width, 553), radius=17, fill="#111111")
    draw.text((x + 13, 527), label, font=chip_font, fill="#ffffff")
draw.rectangle((685, 0, 698, 630), fill="#d53a30")
preview.save(ROOT / "assets/social-preview.png", optimize=True)
print(f"wrote {ROOT / 'index.html'} with {TOTAL_SLIDES} total slides (cover + {TOTAL_SLIDES - 1} content)")
