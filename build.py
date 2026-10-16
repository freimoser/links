import html
G=[
("Tiermedizin",[
("Tiermedizin in Zahlen","https://tiermedizin-in-zahlen.org/","Tierärzte, Praxen und Haustiere in Zahlen, jede mit Quelle"),
("GDT Viewer","https://freimoser.github.io/gdt-viewer/","GDT-Dateien im Browser lesen und Testdaten erzeugen"),
]),
("Ratgeber",[
("BierDurst","https://bierdurst.org/","Biersorten, Vergleiche, Rechner und Oktoberfest-Infos"),
("TickSpot – Zecken finden","https://zecken-finden.org/","Zecken mit der Handykamera in Sekunden entdecken"),
("Wasserfasten","https://wasserfasten.fyi/","Ehrlich fasten, sicher bleiben und das Gewicht halten"),
("SolarBalkon Ratgeber","https://freimoser.github.io/balkonkraftwerk-ratgeber/","Balkonkraftwerk kaufen, anmelden und Strom sparen"),
("Balkon bepflanzen","https://freimoser.github.io/balkon-bepflanzen.de/","Die richtigen Pflanzen für Sonne, Schatten und Saison"),
("KlimaCheck","https://klimacheck-kostenrechner.91serdar.workers.dev/","Heizsysteme vergleichen und Kosten berechnen"),
]),
("Apps & Tools",[
("Konfliktlotse","https://konfliktlotse.app/","Konkrete Worte für schwierige Gespräche im Alltag"),
("FamilyTree Free","https://familytree-free.com/de/","Stammbaum kostenlos erstellen, ohne Konto und Cloud"),
("Solvitalk","https://solvitalk.com/","25 Minuten spazieren und reden, per Google Meet"),
("LDT & BDT Viewer","https://freimoser.github.io/ldt-bdt-viewer/","Labor- und Praxisdaten-Exporte im Browser lesen, ohne Upload"),
("E-Rechnung Klartext","https://freimoser.github.io/e-rechnung-klartext/","XRechnung und ZUGFeRD lesbar anzeigen, ohne Upload"),
("DICOM Viewer","https://freimoser.github.io/dicom-viewer/","Röntgen-, CT- und MRT-Bilder und Radiologie-CDs im Browser ansehen, ohne Upload"),
("ICS Editor","https://freimoser.github.io/ics-editor/","Kalenderdateien im Browser bearbeiten, ohne Upload"),
("Easy Photo Editor","https://freimoser.github.io/easy-photo-editor/","Druckfertige Collagen für Fotoabzüge im Browser"),
("Journey Journal","https://freimoser.github.io/journey-journal-web/","Privates Tagebuch für die eigene Transformation"),
("Love the World","https://lovetheworld.app/","Deine Begegnungen als Weltkarte, verschlüsselt auf dem Gerät"),
("10K Burn Challenge","https://10kburn.com/","Rechner und Planer für 10.000 kcal an einem Tag"),
("KinoTom","https://freimoser.github.io/kinotom/","Kuratierte Sammlung frei zugänglicher Filme"),
]),
("Gaming",[
("MyNextGameFinder","https://nextgamefinder.org/","Acht Fragen, danach das passende Spiel für heute Abend"),
("Meta Awards","https://metaawards.org/","Alle Game-of-the-Year-Awards, Jahr für Jahr gezählt"),
]),
("Sonstiges",[
("Cappuccino Schaumorakel","https://schaumorakel.com/","Milchschaum fotografieren und deuten lassen"),
("SEO Helper","https://freimoser.github.io/seo-helper/","Einsteiger-Handbuch für Websites, Backlinks und AdSense"),
("Portfolio freimoser.de","https://freimoser.github.io/freimoser.de/","Über mich, Projekte und Kontakt"),
]),
("Code",[
("VetKompass","https://github.com/freimoser/vetkompass","Marktübersicht digitaler Lösungen für Tierarztpraxen"),
("Alle Repos auf GitHub","https://github.com/freimoser","Mein GitHub-Profil mit allen öffentlichen Projekten"),
]),
]
e=html.escape
sec=[]
for title,items in G:
    t="Code auf GitHub" if title=="Code" else title
    lis="\n".join(f'''      <li><a class="btn" href="{e(u)}" rel="noopener"><span class="t">{e(n)}</span><span class="s">{e(s)}</span><span class="ar" aria-hidden="true">→</span></a></li>''' for n,u,s in items)
    sec.append(f'''  <section aria-labelledby="h-{len(sec)}">
    <h2 id="h-{len(sec)}">{e(t)}</h2>
    <ul>
{lis}
    </ul>
  </section>''')
total=sum(len(i) for _,i in G)
urls=[u for _,i in G for _,u,_ in i]
ld='{"@context":"https://schema.org","@type":"ProfilePage","mainEntity":{"@type":"Person","name":"Thomas Freimoser","url":"https://freimoser.github.io/freimoser.de/","sameAs":["https://github.com/freimoser"],"homeLocation":{"@type":"Place","name":"München"}}}'
page=f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Thomas Freimoser – alle Projekte auf einen Blick</title>
<meta name="description" content="Alle Websites, Apps und Tools von Thomas Freimoser auf einer Seite: Tiermedizin, Ratgeber, Apps & Tools, Gaming und Code auf GitHub.">
<meta name="author" content="Thomas Freimoser">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#05070d">
<meta name="google-site-verification" content="6pYvtFCnU7UFcQFajtMSkQ7tYMy3Z_Bt7teKiT5yKNg" />
<meta name="msvalidate.01" content="E1F30DEB311AAF5458907DB431B481AC" />
<link rel="canonical" href="https://freimoser.github.io/links/">
<link rel="icon" type="image/svg+xml" href="/links/favicon.svg">
<meta property="og:type" content="profile">
<meta property="og:locale" content="de_DE">
<meta property="og:title" content="Thomas Freimoser – alle Projekte auf einen Blick">
<meta property="og:description" content="Websites, Apps und Tools aus Tiermedizin, Ratgebern, Gaming und mehr.">
<meta property="og:url" content="https://freimoser.github.io/links/">
<meta property="og:image" content="https://freimoser.github.io/links/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Thomas Freimoser – alle Projekte auf einen Blick">
<meta name="twitter:description" content="Websites, Apps und Tools aus Tiermedizin, Ratgebern, Gaming und mehr.">
<meta name="twitter:image" content="https://freimoser.github.io/links/og.png">
<script type="application/ld+json">{ld}</script>
<style>
:root{{--bg:#05070d;--card:#0e1420;--hover:#1a2438;--border:rgba(148,163,184,.12);--accent:#2dd4bf;--accent2:#5eead4;--violet:#a78bfa;--text:#f1f5f9;--muted:#94a3b8;--dim:#64748b}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{-webkit-text-size-adjust:100%}}
html,body{{overflow-x:hidden;max-width:100%}}
body{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.5;min-height:100vh;
background-image:radial-gradient(ellipse 80% 40% at 50% -10%,rgba(45,212,191,.14),transparent),radial-gradient(ellipse 60% 40% at 100% 0,rgba(167,139,250,.08),transparent)}}
main{{width:100%;max-width:640px;margin:0 auto;padding:48px 16px 32px}}
header{{text-align:center;margin-bottom:32px}}
.av{{width:88px;height:88px;border-radius:24px;margin:0 auto 16px;display:grid;place-items:center;background:var(--card);border:1px solid rgba(45,212,191,.35);box-shadow:0 0 40px rgba(45,212,191,.15);font-weight:800;font-size:40px;
background-clip:padding-box}}
.av span{{background:linear-gradient(135deg,var(--accent),var(--violet));-webkit-background-clip:text;background-clip:text;color:transparent}}
h1{{font-size:clamp(1.6rem,6vw,2rem);font-weight:800;letter-spacing:-.02em}}
.loc{{color:var(--violet);font-size:.95rem;margin-top:4px}}
.bio{{color:var(--muted);font-size:.95rem;margin-top:10px}}
.count{{display:inline-block;margin-top:14px;font-size:.8rem;color:var(--accent2);border:1px solid rgba(45,212,191,.3);border-radius:999px;padding:4px 12px}}
section{{margin-top:28px}}
h2{{font-size:.78rem;text-transform:uppercase;letter-spacing:.12em;color:var(--dim);font-weight:700;margin:0 4px 10px}}
ul{{list-style:none;display:flex;flex-direction:column;gap:10px}}
.btn{{position:relative;display:block;width:100%;padding:14px 44px 14px 18px;border-radius:14px;background:var(--card);border:1px solid var(--border);color:var(--text);text-decoration:none;transition:transform .15s ease,border-color .15s ease,background .15s ease;overflow-wrap:anywhere}}
.btn:hover,.btn:focus-visible{{background:var(--hover);border-color:rgba(45,212,191,.45);transform:translateY(-1px);outline:none}}
.t{{display:block;font-weight:650;font-size:1rem}}
.s{{display:block;color:var(--muted);font-size:.86rem;margin-top:2px}}
.ar{{position:absolute;right:16px;top:50%;transform:translateY(-50%);color:var(--accent);font-size:1.1rem}}
footer{{text-align:center;color:var(--dim);font-size:.82rem;margin-top:40px;padding-bottom:16px}}
footer a{{color:var(--muted)}}
@media (prefers-reduced-motion:reduce){{.btn{{transition:none}}.btn:hover{{transform:none}}}}
</style>
</head>
<body>
<main>
  <header>
    <div class="av" aria-hidden="true"><span>F</span></div>
    <h1>Thomas Freimoser</h1>
    <p class="loc">München / Remote</p>
    <p class="bio">Websites, Apps und Tools, die ein konkretes Problem lösen.</p>
    <p class="count">{total} Links</p>
  </header>
{chr(10).join(sec)}
  <footer>
    <p><a href="https://freimoser.github.io/freimoser.de/impressum/">Impressum</a> · <a href="https://freimoser.github.io/freimoser.de/">freimoser.de</a></p>
  </footer>
</main>
</body>
</html>
'''
open('index.html','w').write(page)
open('urls.txt','w').write("\n".join(urls)+"\n")
for t,i in G: print(t,len(i))
print('total',total)
