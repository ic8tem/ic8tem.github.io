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
                     "u": f"https://github.com/ic8tem/{prog}/releases/download/{tag}/{n}"})
unk = [r["f"] for r in rows if r["s"] == ["other"] and r["k"] not in ("src", "mgr")]
if unk: print("UNCLASSIFIED:", unk)
js = ("// generated by tools/build.py from src/releases.json\n"
      f"window.DL_SYS={json.dumps(SYS, ensure_ascii=False)};\n"
      f"window.DL_KIND={json.dumps(KIND, ensure_ascii=False)};\n"
      f"window.DL={json.dumps(rows, ensure_ascii=False)};\n")
open("assets/downloads.js", "w", encoding="utf-8").write(js)
print("assets/downloads.js", len(rows), "files")
