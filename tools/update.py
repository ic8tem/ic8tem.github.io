#!/usr/bin/env python3
"""Aggiornamento automatico dei link del sito (programmi e videocorsi).

Lanciato ogni 3 ore da .github/workflows/aggiorna-link.yml, poi tools/build.py rigenera le pagine.
  1. Programmi: legge l'ultima release di ogni repository (src/auto.json) e aggiorna src/releases.json
     (versione e file da scaricare); copia il README inglese aggiornato in src/readmes.
  2. Videocorsi: conta le lezioni nelle pagine del wiki e aggiorna il numero in tools/i18n/*.json.
  3. Video: legge il feed del canale YouTube e aggiunge i video nuovi a src/videos.json ("auto").
  4. Controlla che i video e le playlist del sito esistano ancora e scrive l'esito in report.md.
Si può lanciare anche a mano:  GITHUB_TOKEN=... python3 tools/update.py"""
import json, os, re, sys, urllib.request, urllib.error, xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
OWNER = "ic8tem"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPORT = os.environ.get("REPORT", "report.md")
changes, problems = [], []


def get(url, api=False):
    h = {"User-Agent": "ic8tem.github.io-updater"}
    if api:
        h["Accept"] = "application/vnd.github+json"
        if TOKEN: h["Authorization"] = f"Bearer {TOKEN}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=30) as r:
        return r.read().decode("utf-8")


def status(url):
    try:
        get(url); return 200
    except urllib.error.HTTPError as e: return e.code
    except Exception: return 0  # rete: non si sa, non è un errore del link


def load(p): return json.load(open(p, encoding="utf-8"))
def save(p, d): open(p, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")


cfg = load("src/auto.json")

# ---------- 1. programmi ----------
MAIN = [r"-win(dows)?-x64-setup\.exe$", r"-x86_64\.AppImage$", r"(apple-silicon|osx-arm64)\.dmg$", r"(mac-intel|osx-x64)\.dmg$"]
rel = load("src/releases.json")
for repo, pc in cfg["programs"].items():
    try:
        r = json.loads(get(f"https://api.github.com/repos/{OWNER}/{repo}/releases/latest", api=True))
        tag, names = r["tag_name"], [a["name"] for a in r.get("assets", [])]
        missing = [p for p in MAIN if not any(re.search(p, n) for n in names)]
        if missing:  # release ancora in caricamento o incompleta: si tiene la precedente
            print(f"{repo} {tag}: mancano i file principali {missing}, resta {rel.get(repo, ['?'])[0]}")
        elif rel.get(repo) != [tag, names]:
            old = rel.get(repo, ["–"])[0]
            rel[repo] = [tag, names]
            changes.append(f"{repo}: {old} → {tag}" if old != tag else f"{repo} {tag}: file della release aggiornati")
    except Exception as e:
        print(f"{repo}: release non letta ({e})")
    if pc.get("readme"):
        try:
            md = get(f"https://raw.githubusercontent.com/{OWNER}/{repo}/HEAD/{pc['readme']}")
            dest = f"src/readmes/{repo}.md"
            if md.strip() and md != open(dest, encoding="utf-8").read():
                open(dest, "w", encoding="utf-8").write(md); changes.append(f"{repo}: README aggiornato")
        except Exception as e:
            print(f"{repo}: README non letto ({e})")
open("src/releases.json", "w", encoding="utf-8").write(json.dumps(rel, ensure_ascii=False))  # stesso formato di prima

# ---------- 2. lezioni dei videocorsi ----------
for c in cfg.get("courses", []):
    try:
        page = get(f"https://raw.githubusercontent.com/wiki/{OWNER}/{c['repo']}/{c['page']}")
    except Exception as e:
        print(f"wiki {c['repo']}/{c['page']}: non letta ({e})"); continue
    n = len(re.findall(c["heading"], page, re.M))
    if not n: continue
    for f in sorted(os.listdir("tools/i18n")):
        p = f"tools/i18n/{f}"; txt = open(p, encoding="utf-8").read(); k = c["i18n_key"]
        # sostituzione nel testo, per non cambiare il formato del file
        nt = re.sub(r'("%s":\s*"[^"\d]*)\d+' % re.escape(k), lambda m: m.group(1) + str(n), txt, count=1)
        if nt != txt:
            open(p, "w", encoding="utf-8").write(nt)
            if f == "it.json": changes.append(f"{c['repo']}: videocorso ora di {n} lezioni")

# ---------- 3. video nuovi dal canale YouTube ----------
NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}
def feed(q):
    root = ET.fromstring(get(f"https://www.youtube.com/feeds/videos.xml?{q}"))
    return [(e.findtext("yt:videoId", namespaces=NS), e.findtext("a:title", namespaces=NS), e.findtext("a:published", namespaces=NS) or "")
            for e in root.findall("a:entry", NS)]

def lang(title):
    s = " " + title.lower() + " "
    if re.search(r"[\(\[ ](it|ita|italiano)[\)\] ]", s) or re.search(r" (della|delle|lezione|come|il|per|nel|con) ", s): return "Italiano"
    if re.search(r"[\(\[ ](en|eng|english)[\)\] ]", s) or re.search(r" (the|how|with|lesson|and|of) ", s): return "English"
    if re.search(r"[぀-ヿ]", title): return "日本語"
    if re.search(r" (los|las|cómo|del) ", s): return "Español"
    if re.search(r" (como|dos|das|não) ", s): return "Português"
    return ""

yt = cfg["youtube"]
vid = load("src/videos.json")
if not yt.get("channel_id"):
    try:
        m = re.search(r'"(?:channelId|externalId)":"(UC[\w-]{22})"', get(f"https://www.youtube.com/watch?v={yt['seed_video']}"))
        if m: yt["channel_id"] = m.group(1); save("src/auto.json", cfg); print("canale YouTube:", m.group(1))
    except Exception as e:
        print(f"canale YouTube non trovato ({e})")
in_playlists = set()
for pl in yt.get("playlists", []):
    try: in_playlists |= {v for v, _, _ in feed(f"playlist_id={pl}")}
    except Exception: pass
if yt.get("channel_id"):
    try:
        known = {v["id"] for v in vid["manual"] + vid["auto"]} | set(vid["ignore"]) | in_playlists
        skip = re.compile(yt.get("skip_title_regex") or r"$^")
        for v, title, pub in feed(f"channel_id={yt['channel_id']}"):
            if v in known or skip.search(title or ""): continue
            l = lang(title)
            vid["auto"].append({"id": v, "title": title, "sub": " · ".join(x for x in (l, pub[:10]) if x), "published": pub})
            changes.append(f"nuovo video: {title} ({v})")
        vid["auto"].sort(key=lambda x: x.get("published", ""), reverse=True)
    except Exception as e:
        print(f"feed del canale non letto ({e})")

# ---------- 4. controllo dei link ----------
for v in vid["manual"] + vid["auto"]:
    if v["id"] in vid["ignore"]: continue
    s = status(f"https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v={v['id']}")
    if s in (400, 404): problems.append(f"video non trovato: https://youtu.be/{v['id']} – {v['title']}")
pls = set(yt.get("playlists", []))
for v in vid["manual"]:
    m = re.search(r"list=([\w-]+)", v["url"])
    if m: pls.add(m.group(1))
for src in ("tools/build.py",):
    pls |= set(re.findall(r"list=([\w-]+)", open(src, encoding="utf-8").read()))
for pl in sorted(pls):
    s = status(f"https://www.youtube.com/feeds/videos.xml?playlist_id={pl}")
    if s in (400, 404): problems.append(f"playlist non trovata: https://www.youtube.com/playlist?list={pl}")
save("src/videos.json", vid)

# ---------- esito ----------
out = []
if changes: out += ["### Aggiornamenti", *[f"- {c}" for c in changes]]
if problems: out += ["### Link da controllare", *[f"- {p}" for p in problems]]
open(REPORT, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out) or "nessuna novità")
gh_out = os.environ.get("GITHUB_OUTPUT")
if gh_out:
    with open(gh_out, "a") as f:
        f.write(f"changes={len(changes)}\nproblems={len(problems)}\n")
        f.write("summary=" + "; ".join(changes)[:200].replace("\n", " ") + "\n")
