#!/usr/bin/env python3
"""Builds the program pages (programs/*.html) from the English READMEs in src/readmes
and the download table (assets/downloads.js) from src/releases.json.
Run from the repository root:  python3 tools/build.py"""
import json, re, html, os, markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

PROGS = [  # file, repo, slug, title, tagline
    ("YA-NEC", "YA-NEC", "ya-nec", "YA-NEC", "Yet Another NEC – NEC-2 antenna simulator"),
    ("YA-MS", "YA-MS", "ya-ms", "YA-MS", "Yet Another MS – meteor scatter"),
    ("YAEC", "YAEC", "yaec", "YAEC", "Yet Another EME Calc"),
    ("E-LAYER-ANALYZER", "E-LAYER-ANALYZER", "e-layer-analyzer", "E-LAYER ANALYZER", "VHF propagation via the E layer"),
    ("IP-TRX-CTRL", "IP-TRX-CTRL", "ip-trx-ctrl", "IP-TRX-CTRL", "Remote control of your HF radio"),
    ("LIVETROPOVHF", "LIVETROPOVHF", "livetropovhf", "LIVETROPOVHF", "Live VHF/UHF tropospheric propagation"),
]
TRANSLATED = {"E-LAYER-ANALYZER", "IP-TRX-CTRL"}

def fix_links(md, repo):
    blob = f"https://github.com/ic8tem/{repo}/blob/main/"
    raw = f"https://raw.githubusercontent.com/ic8tem/{repo}/main/"
    def absu(u, img):
        if re.match(r"^(https?:|mailto:|#)", u): return u
        if u.startswith("../../"): return f"https://github.com/ic8tem/{repo}/" + u[6:]
        return (raw if img else blob) + u.lstrip("./")
    md = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", lambda m: f"![{m.group(1)}]({absu(m.group(2), True)})", md)
    md = re.sub(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)", lambda m: f"[{m.group(1)}]({absu(m.group(2), False)})", md)
    md = re.sub(r'src="([^"]+)"', lambda m: f'src="{absu(m.group(1), True)}"', md)
    md = re.sub(r'href="([^"]+)"', lambda m: f'href="{absu(m.group(1), bool(re.search(r"\.(png|jpe?g|gif)$", m.group(1))))}"', md)
    return md

PAGE = open("tools/program.tpl.html", encoding="utf-8").read()

for fname, repo, slug, title, tag in PROGS:
    md = open(f"src/readmes/{fname}.md", encoding="utf-8").read()
    md = re.sub(r"(?m)^\[Italiano\]\(README\.md\).*\n", "", md)       # language switcher of the README
    md = fix_links(md, repo)
    body = markdown.markdown(md, extensions=["tables", "fenced_code", "md_in_html", "sane_lists"])
    note = ("<p class=\"note\">This page is an English translation of the program's README, which on GitHub is in Italian.</p>"
            if fname in TRANSLATED else "<p class=\"note\">This page is the English README of the program on GitHub.</p>")
    out = (PAGE.replace("{{TITLE}}", html.escape(title)).replace("{{TAG}}", html.escape(tag))
               .replace("{{REPO}}", repo).replace("{{SLUG}}", slug).replace("{{NOTE}}", note).replace("{{BODY}}", body))
    open(f"programs/{slug}.html", "w", encoding="utf-8").write(out)
    print("programs/%s.html" % slug, len(out))

# ---------- download table ----------
SYS = [  # key, Italian label, English label
    ("win64", "Windows 10/11 a 64 bit", "Windows 10/11 64-bit"),
    ("win32", "Windows 10/11 a 32 bit", "Windows 10/11 32-bit"),
    ("winarm", "Windows su ARM (PC Snapdragon)", "Windows on ARM (Snapdragon PCs)"),
    ("win7_64", "Windows 7 SP1, 8, 8.1 a 64 bit", "Windows 7 SP1, 8, 8.1 64-bit"),
    ("win7_32", "Windows 7 SP1, 8, 8.1 a 32 bit", "Windows 7 SP1, 8, 8.1 32-bit"),
    ("mac_arm", "macOS Apple Silicon (M1-M4)", "macOS Apple Silicon (M1-M4)"),
    ("mac_intel", "macOS Intel", "macOS Intel"),
    ("deb64", "Debian, Ubuntu, Mint (x86_64)", "Debian, Ubuntu, Mint (x86_64)"),
    ("rpm64", "Fedora, openSUSE (x86_64)", "Fedora, openSUSE (x86_64)"),
    ("arch64", "Arch, Manjaro, EndeavourOS (x86_64)", "Arch, Manjaro, EndeavourOS (x86_64)"),
    ("slack64", "Slackware (x86_64)", "Slackware (x86_64)"),
    ("alpine64", "Alpine Linux (x86_64)", "Alpine Linux (x86_64)"),
    ("lin64", "Qualsiasi Linux x86_64 (AppImage, portatile)", "Any Linux x86_64 (AppImage, portable)"),
    ("lin32", "Linux a 32 bit su PC (i686)", "32-bit PC Linux (i686)"),
    ("rpi64", "Raspberry Pi OS a 64 bit", "Raspberry Pi OS 64-bit"),
    ("rpi32", "Raspberry Pi OS a 32 bit", "Raspberry Pi OS 32-bit"),
    ("linarm64", "Qualsiasi Linux ARM64 (AppImage, portatile)", "Any Linux ARM64 (AppImage, portable)"),
    ("rpmarm", "Fedora, openSUSE su ARM", "Fedora, openSUSE on ARM"),
    ("archarm", "Arch Linux ARM", "Arch Linux ARM"),
    ("slackarm", "Slackware ARM64", "Slackware ARM64"),
    ("alpinearm", "Alpine Linux ARM64", "Alpine Linux ARM64"),
    ("armv7", "Schede Linux armv7l (ARM a 32 bit)", "Linux armv7l boards (32-bit ARM)"),
    ("freebsd", "FreeBSD (sperimentale)", "FreeBSD (experimental)"),
    ("openbsd", "OpenBSD (non provato)", "OpenBSD (not tested)"),
    ("other", "Altro (sorgenti, gestori di pacchetti)", "Other (sources, package managers)"),
]
KIND = {"setup": ("installatore", "installer", True), "portable": ("portatile", "portable", True),
        "dmg": ("immagine disco .dmg", ".dmg disk image", True), "app": ("solo l'app (.zip)", "app only (.zip)", True),
        "appimage": ("AppImage", "AppImage", True), "deb": ("pacchetto .deb", ".deb package", False),
        "rpm": ("pacchetto .rpm", ".rpm package", False), "arch": ("pacchetto Arch", "Arch package", False),
        "txz": ("pacchetto Slackware", "Slackware package", False), "zip": ("archivio zip", "zip archive", True),
        "src": ("sorgenti", "sources", False), "mgr": ("manifesti winget/scoop/chocolatey", "winget/scoop/chocolatey manifests", False)}

def classify(n):
    s = n.lower()
    if "sorgenti" in s or s.endswith("-source.zip"): return ["other"], "src"
    if "gestori" in s: return ["other"], "mgr"
    kind = ("setup" if s.endswith("setup.exe") else "dmg" if s.endswith(".dmg") else "app" if s.endswith("-app.zip")
            else "appimage" if s.endswith(".appimage") else "deb" if s.endswith(".deb") else "rpm" if s.endswith(".rpm")
            else "arch" if s.endswith(".pkg.tar.zst") else "txz" if s.endswith(".txz")
            else "portable" if ("portatile" in s or "raspberry-pi" in s or re.search(r"-(linux|alpine|freebsd|openbsd)-[\w]+\.tar\.gz$", s)) else "zip")
    if re.search(r"-win(dows)?7-x64", s): return ["win7_64"], kind
    if re.search(r"-win(dows)?7-x86", s): return ["win7_32"], kind
    if re.search(r"-win(dows)?-x64", s): return ["win64"], kind
    if re.search(r"-win(dows)?-x86", s): return ["win32"], kind
    if re.search(r"-win(dows)?-arm64", s): return ["winarm"], kind
    if "apple-silicon" in s or "osx-arm64" in s: return ["mac_arm"], kind
    if "mac-intel" in s or "osx-x64" in s: return ["mac_intel"], kind
    if s.endswith("_amd64.deb"): return ["deb64"], kind
    if s.endswith("_arm64.deb"): return ["rpi64"], kind
    if s.endswith("_armhf.deb"): return ["rpi32", "armv7"], kind
    if s.endswith(".x86_64.rpm"): return ["rpm64"], kind
    if s.endswith(".aarch64.rpm") or s.endswith(".armv7hl.rpm"): return (["rpmarm", "armv7"] if "armv7" in s else ["rpmarm"]), kind
    if kind == "arch": return (["archarm"] if "aarch64" in s else ["arch64"]), kind
    if kind == "txz": return (["slackarm"] if "aarch64" in s else ["slack64"]), kind
    if kind == "appimage": return (["linarm64"] if "aarch64" in s else ["lin64"]), kind
    if "alpine-x64" in s or "musl-x64" in s: return ["alpine64"], kind
    if "alpine-arm64" in s or "musl-arm64" in s: return ["alpinearm"], kind
    if "raspberry-pi-64bit" in s: return ["rpi64"], kind
    if "raspberry-pi-32bit" in s: return ["rpi32"], kind
    if "freebsd" in s: return ["freebsd"], kind
    if "openbsd" in s: return ["openbsd"], kind
    if "linux-armv7l" in s: return ["armv7"], kind
    if "linux-arm64" in s: return ["linarm64", "rpi64", "slackarm"], kind
    if "linux-arm" in s: return ["rpi32", "armv7"], kind
    if "linux-x64" in s: return ["lin64"], kind
    if "linux-x86" in s: return ["lin32"], kind
    return ["other"], kind

rel = json.load(open("src/releases.json", encoding="utf-8"))
rows = []
for prog, (tag, names) in rel.items():
    for n in names:
        systems, kind = classify(n)
        rows.append({"p": prog.replace("E-LAYER-ANALYZER", "E-LAYER ANALYZER"), "v": tag.lstrip("v"), "s": systems, "k": kind, "f": n,
                     "e": " ".join(dict((x[0], x[2] + " " + x[1]) for x in SYS)[k] for k in systems),
                     "u": f"https://github.com/ic8tem/{prog}/releases/download/{tag}/{n}"})
unk = [r["f"] for r in rows if r["s"] == ["other"] and r["k"] not in ("src", "mgr")]
if unk: print("UNCLASSIFIED:", unk)
js = ("// generated by tools/build.py from src/releases.json\n"
      f"window.DL_AUTO={json.dumps({k: v[2] for k, v in KIND.items()})};\n"
      f"window.DL={json.dumps(rows, ensure_ascii=False)};\n")
open("assets/downloads.js", "w", encoding="utf-8").write(js)
print("assets/downloads.js", len(rows), "files")

# ---------- home page in every language ----------
LANGS = ["it", "en", "fr", "de", "es", "pt", "hi", "ja", "zh", "id"]
I = {l: json.load(open(f"tools/i18n/{l}.json", encoding="utf-8")) for l in LANGS}
ver = {p.replace("E-LAYER-ANALYZER", "E-LAYER ANALYZER"): t.lstrip("v") for p, (t, _) in rel.items()}
def main_files(repo):
    tag, names = rel[repo]
    pick = lambda pat: next(n for n in names if re.search(pat, n))
    return [("Windows", pick(r"-win(dows)?-x64-setup\.exe$")), ("Linux", pick(r"-x86_64\.AppImage$")),
            ("macOS Apple Silicon", pick(r"(apple-silicon|osx-arm64)\.dmg$")), ("macOS Intel", pick(r"(mac-intel|osx-x64)\.dmg$"))], tag
CARDS = [  # repo, slug, name, tag key or fixed tag, description key, extra links
    ("YA-NEC", "ya-nec", "YA-NEC", "Yet Another NEC", "d_yanec", [("https://github.com/ic8tem/YA-NEC/wiki/Videocorso", "course_link_it"), ("https://github.com/ic8tem/YA-NEC/wiki/Videocorso-en", "course_link_en")]),
    ("YA-MS", "ya-ms", "YA-MS", "Yet Another MS", "d_yams", []),
    ("YAEC", "yaec", "YAEC", "Yet Another EME Calc", "d_yaec", [("https://github.com/ic8tem/YAEC/wiki/Manuals", "yaec_manuals")]),
    ("E-LAYER-ANALYZER", "e-layer-analyzer", "E-LAYER ANALYZER", "@tag_ela", "d_ela", []),
    ("IP-TRX-CTRL", "ip-trx-ctrl", "IP-TRX-CTRL", "@tag_ip", "d_ip", []),
    ("LIVETROPOVHF", "livetropovhf", "LIVETROPOVHF", "Live VHF/UHF tropo", "d_ltv", [("https://www.youtube.com/playlist?list=PLbNitGQIwVXQ", "ltv_course")]),
]
VIDS = [("https://youtu.be/FShpUCHlcSo", "FShpUCHlcSo", "LIVETROPOVHF – {v_ltv_fc}", "Italiano · 2:36"),
        ("https://youtu.be/fDde0aklgI4", "fDde0aklgI4", "LIVETROPOVHF – {v_ltv_fc}", "English · 2:36"),
        ("https://youtu.be/9z9CxBhOyMw", "9z9CxBhOyMw", "LIVETROPOVHF – {v_ltv_call3}", "Italiano · 2:13"),
        ("https://youtu.be/NbunEoC6FBY", "NbunEoC6FBY", "LIVETROPOVHF – {v_ltv_call3}", "English · 2:13"),
        ("https://www.youtube.com/playlist?list=PLdpN-XKt6Gxw", "93MJEVt-Fps", "YA-NEC – {v_course_it}", "{v_lessons} · playlist"),
        ("https://www.youtube.com/playlist?list=PLFfXLoSkjiJE", "Vp_egV0WrZ8", "YA-NEC – {v_course_en}", "{v_lessons} · playlist"),
        ("https://www.youtube.com/playlist?list=PLYCyA6fFaT-U", "Bk_fE5unliE", "YA-MS – Yet Another MS", "10 video · playlist"),
        ("https://youtu.be/NCjFPjtd2Lw", "NCjFPjtd2Lw", "YA-MS – {ngm_jp} {v_gem}", "English · 1:55"),
        ("https://youtu.be/ZoZTmHIqV_0", "ZoZTmHIqV_0", "YA-MS – {ngm_jp} {v_gem}", "日本語 · 1:47"),
        ("https://youtu.be/nVS-yigZmJ4", "nVS-yigZmJ4", "YA-MS – {ngm_au} {v_gem}", "English · 1:51"),
        ("https://youtu.be/QoyncqAoNy0", "QoyncqAoNy0", "YA-MS – {ngm_sa} {v_gem}", "English · 1:54"),
        ("https://youtu.be/MmRJ0epbVNo", "MmRJ0epbVNo", "YA-MS – {ngm_sa} {v_gem}", "Español · 2:07"),
        ("https://youtu.be/TqofNfmDh9w", "TqofNfmDh9w", "YA-MS – {ngm_sa} {v_gem}", "Português · 2:06"),
        ("https://youtu.be/Yop2bzGTiI0", "Yop2bzGTiI0", "YA-MS – RA1WU ↔ IW2EQR {v_gem}", "Italiano · 1:30"),
        ("https://youtu.be/LNopcQcj68E", "LNopcQcj68E", "YA-MS – RA1WU ↔ IW2EQR {v_gem}", "English · 1:30"),
        ("https://youtu.be/Bk_fE5unliE", "Bk_fE5unliE", "YA-MS – {v_pres}", "Italiano"),
        ("https://youtu.be/VsdnUz_-e-U", "VsdnUz_-e-U", "YA-MS – {v_pres}", "English"),
        ("https://youtu.be/uvewuHTyw3k", "uvewuHTyw3k", "YAEC – {v_pres}", "Italiano"),
        ("https://youtu.be/n9ag5MjpoEU", "n9ag5MjpoEU", "YAEC – {v_pres}", "English"),
        ("https://youtu.be/1mjVjKD4O9w", "1mjVjKD4O9w", "YAEC – {v_start}", "Italiano"),
        ("https://youtu.be/tTEs9VY3sEA", "tTEs9VY3sEA", "YAEC – {v_howto}", "English")]
TPL = open("tools/index.tpl.html", encoding="utf-8").read()
for l in LANGS:
    t = I[l]; root = "" if l == "it" else "../"; path = "" if l == "it" else f"{l}/"
    e = lambda k: html.escape(t[k], quote=False)
    cards = []
    for repo, slug, name, tag, dk, extra in CARDS:
        files, rtag = main_files(repo)
        tg = e(tag[1:]) if tag.startswith("@") else tag
        dl = "".join(f'<a href="https://github.com/ic8tem/{repo}/releases/download/{rtag}/{f}">⬇️ {lab}</a>' for lab, f in files)
        allsys = e("ela_bsd") if repo == "E-LAYER-ANALYZER" else e("all_sys")
        links = (f'<a href="{root}programs/{slug}.html">{e("full_desc")}</a><a href="?p={repo}#download">{e("all_files")}</a><a href="https://github.com/ic8tem/{repo}">GitHub</a>'
                 + "".join(f'<a href="{u}">{e(k)}</a>' for u, k in extra))
        cards.append(f'    <div class="card">\n      <h3>{name} <span class="ver">{rtag.lstrip("v")}</span></h3>\n      <div class="tag">{tg}</div>\n'
                     f'      <p>{e(dk)}</p>\n      <div class="dl">{dl}<a class="all" href="?p={repo}#download">{allsys}</a></div>\n      <div class="links">{links}</div>\n    </div>')
    vids = "\n".join(f'    <a class="vid" href="{u}"><img loading="lazy" src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt=""><div>{html.escape(a.format(**t))}<small>{html.escape(b.format(**t))}</small></div></a>' for u, vid, a, b in VIDS)
    opts = "".join(f'<option value="{x}"{" selected" if x == l else ""}>{I[x]["name"]}</option>' for x in LANGS)
    alts = "\n".join(f'<link rel="alternate" hreflang="{x}" href="https://ic8tem.github.io/{"" if x == "it" else x + "/"}">' for x in LANGS)
    jsT = json.dumps({"js": t["js"], "sys": t["sys"], "kind": t["kind"]}, ensure_ascii=False)
    out = TPL
    rep = {"lang": l, "root": root, "path": path, "cards": "\n".join(cards), "videos": vids, "langopts": opts, "alternates": alts, "jsT": jsT}
    for k, v in rep.items(): out = out.replace("{{" + k + "}}", v)
    def sub(m):
        k = m.group(1)
        if k not in t: raise KeyError(f"{l}: {k}")
        return e(k)
    out = re.sub(r"\{\{(\w+)\}\}", sub, out)
    dest = "index.html" if l == "it" else f"{l}/index.html"
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    open(dest, "w", encoding="utf-8").write(out)
    print(dest, len(out))
