# E-LAYER ANALYZER

**E-LAYER ANALYZER** – analysis of the VHF propagation modes that involve the E layer: sporadic-E (also multi-hop and intercontinental), FAI, meteor scatter (with the YA-MS program built in) and radio aurora.
By Costantino Cerrotta IC8TEM. .NET 8 + Avalonia, same look as YA-MS.
No data in AppData: everything stays in the `data` folder next to the program.

## Distributions and updates

| System | Package (Releases page) | Automatic update |
|---|---|---|
| Windows 10 and 11: 64 bit, 32 bit, ARM64 (Snapdragon) | `-win-x64-setup.exe`, `-win-x86-`, `-win-arm64-` or the portable zips | yes |
| Windows 7 SP1, 8 and 8.1 (64 and 32 bit, .NET 6) | `-win7-x64-setup.exe`, `-win7-x86-` or the portable zips `-win7-...` | yes |
| Mac Apple Silicon and Intel | `-osx-arm64.dmg`, `-osx-x64.dmg` or `-app.zip` | yes |
| Any Linux x86_64 and aarch64 | `.AppImage` or `-linux-x64-portatile.tar.gz`, `-linux-arm64-portatile.tar.gz` | yes |
| Raspberry Pi OS 64 and 32 bit, Linux armv7l | `-linux-arm64-`, `-linux-arm-`, `-linux-armv7l-portatile.tar.gz` | yes |
| Alpine Linux (musl) x86_64 and aarch64 | `-alpine-x64-portatile.tar.gz`, `-alpine-arm64-portatile.tar.gz` | yes |
| Debian, Ubuntu, Mint, Raspberry Pi OS | `_amd64.deb`, `_arm64.deb`, `_armhf.deb` | **no**: install the new `.deb` |
| Fedora, openSUSE | `.x86_64.rpm`, `.aarch64.rpm`, `.armv7hl.rpm` | **no**: install the new `.rpm` |
| Arch, Manjaro, EndeavourOS, Arch Linux ARM | `-x86_64.pkg.tar.zst`, `-aarch64.pkg.tar.zst` | **no**: install the new package |
| Slackware x86_64 and ARM64 | `-x86_64-1_ic8tem.txz`, `-aarch64-1_ic8tem.txz` | **no**: `upgradepkg` with the new package |
| FreeBSD amd64 | `-freebsd-amd64-sperimentale.tar.gz` (**experimental, not tested**) | yes, if the program starts |

Automatic, silent updates work with every package **except the system package managers' ones** (`.deb`, `.rpm`, Arch, Slackware): there the program announces the new version, which you install with the new package, as the first time.
There are no versions for Linux i686 (32-bit PCs) and OpenBSD, because .NET doesn't exist for those systems.

[![Ko-fi](https://img.shields.io/badge/Ko--fi-ic8tem-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/ic8tem)

| Tab | Contents |
|---|---|
| SPORADIC-E | azimuthal map (single hop or maximum distance) or rectangular, spots with the first hops of both stations, Es clouds on the Maidenhead squares, IK3XTV's hop table, the 144 MHz rule |
| BENCHMARK Es | a whole ADIF log (also of other stations): QSOs by day and hour, skip by sector, foEs, multi-hop check, cloud movement |
| IONOSONDES | foEs, foF2 and MUF(D) live from the GIRO ionosondes (every 15 minutes), 24-hour chart, sporadic-E MUF at 1000-2400 km with the bands that open, comparison with the foEs derived from the spots |
| Es CLOUDS OVER TIME | Es clouds step by step (5-15 minutes) on 1-4° cells, minimum foEs and NmE with Chartier's 2022 method, from session spots, ADIF log or CSV spots |
| FAI | scatter trail of the scatter points for a pair of stations and iso-reflection curves (IGRF-14) |
| METEOR SCATTER | the complete YA-MS (latest version) |
| AURORA | OVATION oval, Kp, solar wind (NOAA SWPC), auroral scatter trail and iso-reflection, <AU>/<AUR> spots with the calculation |
| DATA COLLECTION | 3 telnet sessions (cluster of your choice, RBN, DM4X cluster with PSKReporter), PSKReporter MQTT, WSJT-X UDP, collected spots, CALL3 archive |
| SETTINGS | general options (station, language, colours, font, continent, time, updates) and sorting of the spots among the tabs, with the filters and a one-line test |
| ADIF LOG | worked and confirmed squares, band by band from 28 MHz up |
| SOURCES | sources cited by the program |
| SUMMARY OF CALCULATION CHOICES / USER MANUAL / TECHNICAL REPORT | formulas and calculation choices, in-depth user manual, technical report on the choices (exportable to Word) |

Main sources: G. Cerrotta IC8FAX, C. Cerrotta IC8TEM, "IL F.A.I., quello strano fenomeno del dopo E-sporadico" (FAI, that strange phenomenon after sporadic-E, 2011);
https://qsl.net/ic8fax/page4.html; Es hop table by F. Egano IK3XTV.

## Building
The installers are produced by GitHub Actions (`.github/workflows/build.yml`) whenever the `release` branch is updated (version from the `VERSION` file). On every push to `main`: check build on Linux, log on the `ci-log` branch and screenshots of the tabs on the `ci-screenshots` branch.
Locally: `dotnet publish E-LAYER-ANALYZER.csproj -c Release -r win-x64|win-x86|win-arm64|linux-x64|linux-arm64|linux-arm|linux-musl-x64|linux-musl-arm64|osx-arm64|osx-x64 --self-contained true`; Linux packages with `installer/make-deb.sh`, `make-rpm.sh`, `make-arch.sh`, `make-txz.sh`, `make-appimage.sh`.
Word documents: `python3 tools/txt2docx.py data/ela_documento_tecnico.txt data/ela_documento_tecnico.docx`.

## License
E-LAYER ANALYZER is free software: you can redistribute and modify it under the terms of the GNU General Public License version 3 ([COPYING](COPYING)), the same as YA-MS, which the program contains. It is distributed without any warranty. The data of external sources belong to their respective bodies, with their own conditions (for example the GIRO ionosonde data, CC BY-NC-SA 4.0, non-commercial use only); the list is in the SOURCES tab.

## Support the project
E-LAYER ANALYZER is free. If you find it useful, you can buy me a coffee on **[Ko-fi](https://ko-fi.com/ic8tem)**.
