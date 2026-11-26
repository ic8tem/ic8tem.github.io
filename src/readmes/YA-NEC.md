[Italiano](README.md) · **English** · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Português](README.pt.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

# YA-NEC

**NEC-2 wire antenna simulator** for Windows, Linux and macOS (C#, .NET 8, Avalonia).
By Costantino Cerrotta **IC8TEM**.

> *The story of this program will be written by you: with your projects, your ideas, your ingenuity, your discoveries and your certainties.*

The engine is a C# translation of **nec2c** (the NEC-2 of Lawrence Livermore National Laboratory), checked at every release against nec2c and EZNEC. It opens **NEC (.nec)**, **MMANA (.maa)**, **AutoEZ (.weq)**, **EZNEC (.ez)**, **K6STI YO/AO (.yag, .ant)** models and its own **.yanec** format.

Features: impedance, SWR, gain, 2D and 3D patterns, frequency sweep and Smith chart; Leeson correction for telescopic (stepped-diameter) tubing, as in EZNEC; grounds (perfect, reflection coefficient, Sommerfeld, radial screen); variables, formulas and optimizer; more than 40 calculators (DL6WU long Yagi, Quagi, LPDA, Moxon, hexbeam, multiband dipoles and Yagis, four-square, verticals, dishes and feeds, element brackets and more); receiving antennas and RDF; noise, G/T and stacking; coax chart, matching lines and baluns; input data checks. Every calculation choice and every checkbox is explained in the [manual](doc/Manuale_d_uso.pdf), also available inside the program (Manual tab). More in the [Wiki](https://github.com/ic8tem/YA-NEC/wiki).

**Language:** the interface is available in 37 languages (Language menu, top right); the Wiki too. The manual is in Italian.

## Screenshots

<table><tr><td width="50%" align="center"><a href="docs/screenshots/struttura-3d.png"><img src="docs/screenshots/struttura-3d.png" alt="3D structure with currents and lobe"></a><br><sub>3D structure with currents and lobe</sub></td><td width="50%" align="center"><a href="docs/screenshots/terreno-reale.png"><img src="docs/screenshots/terreno-reale.png" alt="HFTA-style real terrain on the DEM profile"></a><br><sub>HFTA-style real terrain on the DEM profile</sub></td></tr><tr><td width="50%" align="center"><a href="docs/screenshots/ricezione-rdf.png"><img src="docs/screenshots/ricezione-rdf.png" alt="Reception: RDF, DMF and noise"></a><br><sub>Reception: RDF, DMF and noise</sub></td><td width="50%" align="center"><a href="docs/screenshots/tolleranze.png"><img src="docs/screenshots/tolleranze.png" alt="Build tolerances (Monte Carlo)"></a><br><sub>Build tolerances (Monte Carlo)</sub></td></tr><tr><td width="50%" align="center"><a href="docs/screenshots/cavo-balun.png"><img src="docs/screenshots/cavo-balun.png" alt="Cable and balun: common-mode current"></a><br><sub>Cable and balun: common-mode current</sub></td><td width="50%" align="center"><a href="docs/screenshots/yagi-incrociate.png"><img src="docs/screenshots/yagi-incrociate.png" alt="Crossed Yagis: RHCP, LHCP, axial ratio"></a><br><sub>Crossed Yagis: RHCP, LHCP, axial ratio</sub></td></tr><tr><td width="50%" align="center"><a href="docs/screenshots/vento.png"><img src="docs/screenshots/vento.png" alt="Mechanical calculations: wind (NTC 2018)"></a><br><sub>Mechanical calculations: wind (NTC 2018)</sub></td><td width="50%" align="center"><a href="docs/screenshots/divisori.png"><img src="docs/screenshots/divisori.png" alt="Power dividers and phasing lines"></a><br><sub>Power dividers and phasing lines</sub></td></tr><tr><td width="50%" align="center"><a href="docs/screenshots/carichi-hf.png"><img src="docs/screenshots/carichi-hf.png" alt="HF loads: traps and coils"></a><br><sub>HF loads: traps and coils</sub></td><td width="50%" align="center"><a href="docs/screenshots/smith.png"><img src="docs/screenshots/smith.png" alt="Smith chart"></a><br><sub>Smith chart</sub></td></tr></table>

## What's new in 1.7

- **New calculators**: 2-3 element HF Yagi with tuning guide, interlaced dual-band Yagi, trap multiband vertical, inverted L / T for 160 m, half-sloper on the tower, broadband dipole, relay multiband dipole, linear loading, wire resonant on harmonics, gamma match and stub matching with the Smith chart.
- **Multiband quad** with the lines of the unfed bands and decoupling lines; **magnetic loop** rectangular, with turns in parallel, with transformer and L network; **Wire antennas** with wire material and FT-82-43.
- **Stack** with the effective area; **SWR** showing on which side R lies; **Real terrain** with take-off angles toward a locator; efficiency in calculators with coils and traps; new **Tips** tab.
- **1.7.1**: clickable heights in the 3D structure; in Patterns the spacing of a stack changes live.
- **1.7.2 (security)**: the automatic update installs only packages signed by YA-NEC; files prepared on purpose no longer close the program.

What's new in earlier versions (1.1 to 1.6) is in the [release notes](https://github.com/ic8tem/YA-NEC/releases), in the [Wiki](https://github.com/ic8tem/YA-NEC/wiki) and in the manual.

## Download

From the **[Releases](https://github.com/ic8tem/YA-NEC/releases)** page download the zip for your platform, extract it to a **writable folder** (for example `C:\YA-NEC` or `~/YA-NEC`) and run `YA-NEC.exe` (Linux and macOS: `YA-NEC`). No .NET installation is needed. Settings and data stay in the `data` folder next to the program: no AppData, no registry.

| System | Package |
|---|---|
| Windows 10/11 64-bit | `YA-NEC-<version>-windows-x64-portatile.zip` |
| Windows 10/11 32-bit | `YA-NEC-<version>-windows-x86-portatile.zip` |
| Windows on ARM (Snapdragon) | `YA-NEC-<version>-windows-arm64-portatile.zip` |
| Windows 7 SP1, 8, 8.1 (.NET 6) | `YA-NEC-<version>-windows7-x64-portatile.zip`, `-windows7-x86-portatile.zip` (updates KB2533623 and KB2999226 required) |
| Linux x86_64 | `YA-NEC-<version>-linux-x64.tar.gz` |
| Linux ARM64 (Raspberry Pi OS 64-bit, other aarch64) | `YA-NEC-<version>-linux-arm64.tar.gz` |
| Linux ARM 32-bit (Raspberry Pi OS 32-bit, armv7l) | `YA-NEC-<version>-linux-armv7l.tar.gz` |
| Alpine and other musl Linux | `YA-NEC-<version>-alpine-x64.tar.gz`, `-alpine-arm64.tar.gz` |
| macOS Apple Silicon (M1-M4) | `YA-NEC-<version>-mac-apple-silicon-app.zip` |
| macOS Intel | `YA-NEC-<version>-mac-intel-app.zip` |

Each zip comes with its `.sha256` checksum.

- **Linux**: after extracting, `chmod +x YA-NEC` if needed; `libfontconfig1` and `libicu` are required (already present on desktop distributions).
- **macOS**: the program is not signed by Apple. After extracting, in Terminal: `xattr -dr com.apple.quarantine ~/YA-NEC` (the extracted folder), then `~/YA-NEC/YA-NEC`.

## Automatic update

The program checks 10 seconds after start-up and then every 3 minutes for a new version here. If there is one, it downloads it and verifies its SHA-256 checksum and, from 1.7.2, the **YA-NEC signature** (ECDSA P-256): without a signature, or with a wrong one, nothing is installed. The new version starts at the restart, which the program does by itself, reopening the model; the previous one is kept in `data/aggiornamenti/precedente-<version>`, settings and models are not touched. It can be turned off in **Settings > Update**.

**Exception: Debian/Ubuntu (.deb) and Fedora/openSUSE (.rpm) packages.** When available, they will install into system folders with administrator rights, so the program cannot (and must not) change itself: they will be updated with the package manager. In those packages automatic update is off, and Settings says so.

## Building from source

.NET 8 SDK required. Windows: `compila.bat` (program in `build\win-x64`), `compila.bat /distribuzione` for the self-contained version, `compila_win7.bat` for Windows 7. Linux and macOS: `./compila.sh`. Details in [LEGGIMI.txt](LEGGIMI.txt) (Italian).

## Credits and license

**GPL-3.0-or-later** ([LICENSE](LICENSE), [THIRD-PARTY-NOTICES.txt](THIRD-PARTY-NOTICES.txt)), like nec2c and xnec2c from which the engine derives. YA-NEC exists thanks to the work of fellow radio amateurs and researchers: the full list is in [CREDITI.txt](CREDITI.txt) and in the **Credits** tab. Thanks to Luis IV3PRK for the free publications on his website.

## Contacts

ic8tem@gmail.com · [QRZ](https://www.qrz.com/db/ic8tem) · [Facebook group](https://www.facebook.com/groups/1675310160982493) · donations: [ko-fi.com/ic8tem](https://ko-fi.com/ic8tem)
