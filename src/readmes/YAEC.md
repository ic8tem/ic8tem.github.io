# YAEC – Yet Another EME Calc

*by Costantino IC8TEM*

Moon position, pointing windows, EME link budget, sky and solar noise calculator for radio amateurs, in 37 languages.
Windows, Linux and macOS (Linux and macOS with Mono).


[![Ko-fi](https://img.shields.io/badge/Ko--fi-ic8tem-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/ic8tem)

## Videos

| | English | Italiano |
|---|---|---|
| [▶ What YAEC calculates](docs/video/YAEC_presentation_en.mp4) (2 min) · [subtitles](docs/video/YAEC_presentation_en.srt) | A tour of the calculation tabs, with English subtitles | Le linguette di calcolo, sottotitoli in inglese |
| [▶ Getting started](docs/video/YAEC_getting_started_en.mp4) (5 min) · [subtitles](docs/video/YAEC_getting_started_en.srt) | A first EME evening step by step: locator, DX from CALL3.TXT, horizon, Dgrd, budget, Stations to try, manuals | Una prima serata EME passo passo: locator, DX dal CALL3.TXT, orizzonte, Dgrd, budget, Stazioni da provare, manuali |

## Languages

YAEC, its two manuals (user manual and *Theory and tips on EME*), the licence and the README are available in **37 languages**; the language is chosen at the top of the main screen. Licence and README in every language are in the [`lingue`](lingue) folder.

| | | | |
|---|---|---|---|
| English `en` | Italiano `it` | Deutsch `de` | Français `fr` |
| Español `es` | Português `pt` | Nederlands `nl` | Svenska `sv` |
| Norsk (bokmål) `nb` | Íslenska `is` | Eesti `et` | Latviešu `lv` |
| Lietuvių `lt` | Русский `ru` | Українська `uk` | Türkçe `tr` |
| Afrikaans `af` | العربية `ar` | עברית `he` | اردو `ur` |
| हिन्दी `hi` | বাংলা `bn` | 中文 (简体) `zh` | 日本語 `ja` |
| 한국어 `ko` | Bahasa Indonesia `id` | Dansk `da` | Tagalog `tl` |
| Português (Brasil) `pt-BR` | ไทย `th` | 中文 (繁體) `zh-TW` | Polski `pl` |
| Čeština `cs` | Română `ro` | Ελληνικά `el` | Magyar `hu` |
| Slovenčina `sk` | | | |

## Installation



Download the files from the **[Releases](../../releases/latest)** page (x.y = version number).

| Distribution | Files |
|---|---|
| **Windows 64 bit** | `YAEC-x.y-windows-x64-setup.exe`, `YAEC-x.y-windows-x64-portatile.zip` |
| **Windows 32 bit** | `YAEC-x.y-windows-x86-setup.exe`, `YAEC-x.y-windows-x86-portatile.zip` |
| **Windows 7 SP1** (with .NET Framework 4.8 and the TLS 1.2 updates) ¹ | the same packages as Windows 64 and 32 bit |
| **Windows ARM64** (PC with Snapdragon) ¹ | `YAEC-x.y-windows-arm64-setup.exe`, `YAEC-x.y-windows-arm64-portatile.zip` |
| **Linux x86_64** (64 bit) | `YAEC-x.y-linux-x64.tar.gz` |
| **Linux i686** (32 bit) ¹ | `YAEC-x.y-linux-x86.tar.gz` |
| **Linux aarch64** (ARM 64-bit, PCs and mini PCs other than Raspberry Pi) | `YAEC-x.y-linux-arm64.tar.gz` |
| **Debian / Ubuntu / Mint** (.deb package) | `yaec_x.y_amd64.deb` |
| **Fedora / openSUSE** (.rpm package) | `yaec-x.y.x86_64.rpm` |
| **Arch Linux / Manjaro** (.pkg.tar.zst package) | `yaec-x.y-1-x86_64.pkg.tar.zst` |
| **Slackware** (.txz package) ¹ | `yaec-x.y-x86_64-1_ic8tem.txz` |
| **AppImage** (any Linux) ¹ | `YAEC-x.y-x86_64.AppImage`, `YAEC-x.y-aarch64.AppImage` |
| **Alpine Linux** (musl) ¹ | `YAEC-x.y-alpine-x64.tar.gz`, `YAEC-x.y-alpine-arm64.tar.gz` |
| **Raspberry Pi (ARM)** → Raspberry Pi OS 32 bit (armhf) ¹ | `yaec_x.y_armhf.deb`, `YAEC-x.y-linux-armv7l.tar.gz` |
| **Raspberry Pi OS 64 bit** (arm64) | `yaec_x.y_arm64.deb`, `YAEC-x.y-linux-arm64.tar.gz` |
| **Raspberry Pi Slackware ARM64** ¹ | `YAEC-x.y-linux-arm64.tar.gz` |
| **Linux armv7l** | `YAEC-x.y-linux-armv7l.tar.gz` |
| **FreeBSD amd64** ¹ | `YAEC-x.y-freebsd-x64.tar.gz` |
| **OpenBSD amd64** ¹ | `YAEC-x.y-openbsd-x64.tar.gz` |
| **macOS** → macOS Apple Silicon (M1-M4) | `YAEC-x.y-mac-apple-silicon.dmg`, `YAEC-x.y-mac-apple-silicon-app.zip` |
| **macOS Intel** | `YAEC-x.y-mac-intel.dmg`, `YAEC-x.y-mac-intel-app.zip` |

¹ Not yet tested on this platform: reports from users are welcome.

**Automatic updates** — from 1.9.1: at start-up YAEC checks GitHub for a new version and updates itself with the Windows installer or zip, the portable .tar.gz archives (Linux, Raspberry Pi, FreeBSD, OpenBSD, Alpine), the AppImage and the macOS app; every package is checked against SHA256SUMS.txt. The .deb, .rpm, Arch (.pkg.tar.zst) and Slackware (.txz) packages are updated with the system package manager instead: YAEC announces the new version and opens the GitHub page.

- **Windows** – download `YAEC-x.y-windows-x64-setup.exe` and run it. It installs YAEC into *Documents\YAEC* without administrator rights, with Start menu and desktop shortcuts and an uninstaller. If SmartScreen warns you: *More info* → *Run anyway*. No installation wanted? Extract `YAEC-x.y-windows-x64-portatile.zip` into a folder where you can write and run `YAEC.exe`.
- **Linux – Debian, Ubuntu, Mint** – download `yaec_x.y_amd64.deb` and run `sudo apt install ./yaec_x.y_amd64.deb` (Mono is installed too); start YAEC from the applications menu or with `yaec`.
- **Windows 32-bit** – `YAEC-x.y-windows-x86-setup.exe` or `YAEC-x.y-windows-x86-portatile.zip`.
- **Raspberry Pi** (Raspberry Pi OS 64-bit, Pi 4/5) – download `yaec_x.y_arm64.deb` and run `sudo apt install ./yaec_x.y_arm64.deb`.
- **Linux – other distributions** – install Mono (`sudo dnf install mono-complete`, `sudo pacman -S mono`, `sudo zypper install mono-complete`), extract `YAEC-x.y-linux-x64.tar.gz` (ARM: `YAEC-x.y-linux-arm64.tar.gz`, `YAEC-x.y-linux-armv7l.tar.gz`; Linux i686: `YAEC-x.y-linux-x86.tar.gz`; FreeBSD amd64: `YAEC-x.y-freebsd-x64.tar.gz`; OpenBSD amd64: `YAEC-x.y-openbsd-x64.tar.gz`) and run `./install.sh`.
- **macOS (experimental)** – install Mono for macOS and XQuartz, open `YAEC-x.y-mac-apple-silicon.dmg` (Apple Silicon) / `YAEC-x.y-mac-intel.dmg` (Intel) and drag YAEC into Applications; the first time, right-click → *Open*.
- Every release has `SHA256SUMS.txt` to check the downloaded files.

## Features



<table><tr><td width="33%" align="center"><a href="docs/screenshots/en-1.jpg"><img src="docs/screenshots/en-1.jpg" alt="Live position and +- 24h"></a><br><sub>Live position and +- 24h</sub></td><td width="33%" align="center"><a href="docs/screenshots/en-2.jpg"><img src="docs/screenshots/en-2.jpg" alt="EME budget Yagi"></a><br><sub>EME budget Yagi</sub></td><td width="33%" align="center"><a href="docs/screenshots/en-3.jpg"><img src="docs/screenshots/en-3.jpg" alt="Distance and Dgrd"></a><br><sub>Distance and Dgrd</sub></td></tr></table>

YAEC puts in one program everything you need to run an EME (Earth–Moon–Earth) station on 50, 70, 144, 222, 432 and 902 MHz and 23 cm (1296 MHz), especially when the station has limits: an antenna without elevation, a rotator with limited travel, obstacles that hide part of the sky. It tells you not only where the Moon is, but whether **your** antenna can really reach it, when, and under which conditions. The bands above 432 MHz are still being completed, but the DGRD is already computed correctly at every frequency; more advice for newcomers above 900 MHz will follow.

**Live**
- **Live position and +- 24h** – main screen updated every second: your locator and the DX's (4 to 14 characters), frequency, UTC, local and DX clocks, a status band (pointable, outside the limits, below the horizon, common window) with countdown, compass and elevation arc. Typing the DX callsign fills in its locator from CALL3.TXT.
- **Reconnaissance of my obstacles** – aerial or topographic map centred on your station with the sky drawn on it: Moon position, its path over the next 24 hours, rise and set, antenna limits that you drag with the mouse.
- **My horizon** – *Horizon from terrain*: panorama of the terrain around your station from SRTM1 elevation data (about 30 m), with Earth curvature and refraction, over the sky view (three colour scales) or a light-blue sky; Moon path, rise and set above the terrain, main obstacles named from OpenStreetMap and minutes of Moon lost. One checkbox makes the terrain the minimum elevation in the whole program. *Local noise map (NJ9R)*: azimuth × elevation grid where you type the noise seen in WSJT-X while turning the antenna; the hours with the Moon in a noisy direction get a ⚠.
- **Sky view** – the sky seen from your QTH with the sky-noise colours at your frequency, antenna limits, the DX horizon, radio sources, the Sun and the Moon path.

**Planning**
- **Distance and Dgrd** – 7 to 61 days of Dgrd and mean Moon distance, with the declination overlaid, perigee, apogee, new Moon, the three best days (in date order), a possible fourth useful day and a warning for the days when the Moon is close to the Sun. Only the hours in which the Moon is really pointable with your limits are counted.
- **DGRD by frequency** – the Dgrd at your working frequency with the real noise of your station and the sky averaged over the antenna beam, compared with the usual WSJT-X calculation; the choice applies to the whole program.
- **Sky noise (Skynoise)** – Antenna temperature computed with the Skynoise method (G8ONH, G4SWX): the full antenna pattern (NEC .out file, YA-NEC file or Gaussian beam of the EME budget) is pointed at the Moon and each direction reads the sky map at the chosen band (Remazeilles, Haslam, GSM 2008 or LFmap); below the horizon it is 290 K or the terrain of My horizon. It shows the map with the Moon path over the month (click a day for its pass), the antenna temperature during the pass for you and for the DX, the sky behind the Moon, the check average gain, the effect on the EME budget Yagi and the comparison with the Gaussian beam and with the DJ9BV method.
- **Stations to try** – for the chosen day, the stations active in the N0UK EME chat (144 MHz) with a common window with you, the best per locator field, ranked by an index from 0 to 100 from the S/N in both directions; the DX setup is read from what it writes in the chat. A rough example calculation, idea by Matteo IW5DHN.
- **Moon position** – table for the chosen period, coloured by pointability, with the common windows for you and the DX; CSV export for Excel.
- **Moon over the world** – world map coloured by the Moon elevation seen from every place; one click makes that point the DX.

**Link**
- **EME budget Yagi** – link budget for every band, stored band by band: six indicators (link possible, my EIRP, DX EIRP, path loss, S/N me → DX and DX → me, also with the Sun and in 2500 Hz), the full table of steps and an interactive diagram of the station (antenna, cables, relay, preamplifier, transverter, radio). Ground gain for antennas without elevation. Modes with a 60 s period: JT65, Q65-60A, Q65-60B, Q65-60C and custom. Echo mode (*I transmit and receive my own echo*): echo level, delay and Doppler.
- **EME budget dishes** – the same budget, echo included, for dish antennas at 432, 902 and 1296 MHz, prime focus or offset (W2IMU): gain with the PE1RKI formula, beamwidth 70·λ/D, single- or two-stage preamplifier, transverter and PA drive; on 23 cm, circular polarization with 0.4 dB of loss (KA1GT).
- **GRAVES radar** – the French GRAVES radar (143.050 MHz) as a test bench: when the Moon is in its beam and within your antenna limits, with Doppler and echo delay.
- **Solar noise** – downloads the solar fluxes measured by the RSTN network (NOAA) and estimates how much the Sun raises the receiver noise near new Moon.
- **Export calculations to Excel** and **Calculation check** – the budget as an Excel sheet, and every formula with the substituted values, step by step, for the Yagi or the dish budget.

**Log, help and tools**
- **WWL map and ADIF** – Maidenhead grid with worked and confirmed squares from your ADIF file or downloaded directly from LoTW, also by band and EME only.
- **USER MANUAL** and **THEORY AND TIPS ON EME** – full manuals inside the program in every language, with clickable index, search, formulas and sources; exportable to Word. The theory manual includes the advice of experienced EME operators, a section on internet chats and the VE7BQH antenna tables.
- **COAXIAL CABLES** – database of 50 Ω cables with attenuation from 50 to 1296 MHz (data-sheet values and the formula α = k1·√f + k2·f) and the source of every value; sortable, filterable, with a loss calculator and a button that sends the cable to the EME budget. You can add your own cables.

**Also**
- CALL3.TXT downloaded from W7GJ and WSJT-X Improved, merged, refreshed every 7 days and copied into WSJT-X on request.
- Warnings for polar-cap and auroral absorption (PCA) when a station is beyond the polar circles or in the auroral zone.
- 37 languages; light, night (blue), black and eight pastel and three IP-TRX-CTRL (blue, violet, green) colour schemes.
- Moon positions accurate to about 0.01° (Meeus, ELP-2000/82), all calculations on your computer; data in a single `data` folder.

## Version history


From the first stable version (1.0) to the current one; the full history, including the beta versions, is in the program (*Help and tools*) and in the README of every language in the [`lingue`](lingue) folder.



- **1.9.5** – EME budget yagi and dishes: cost of 0.1 dB more loss ahead of the preamp (PA3CSG) and new Station test section with G/T on cold sky and the predicted Y-factor on the Sun, Moon, Cas A and ground (G3LTF, VK3UM's EMECalc); EME budget dishes: illumination drop at the edge and dish mesh, with Tant estimated from sky, spillover and mesh, and G3LTF's measured G/T for comparison; new paragraph in the manual; DX terrain: SRTM1 horizon around its locator in the My horizon tab, taken into account by common windows, the 24-hour bar, the Sky view and Stations to try (locator of at least 6 characters); antenna SWR in the station test (AEH eq. 41-19); Sun diameter from 0.524° to 0.542° with the Earth–Sun distance; note «YAEC computes, it does not design equipment» in the sources and tips.
- **1.9.3** – Package names the same as YA-MS (-windows-x64/-x86/-arm64, -windows7-x64/-x86, -mac-apple-silicon, -mac-intel, -linux-x64/-arm64/-armv7l/-x86, -raspberry-pi-64bit/-32bit, -alpine-x64/-arm64); .rpm, Arch and Slackware packages for ARM too; the release notes have a table with a link to each package for each system. This version also contains the files with the old names, only for the automatic update from 1.9.1 and 1.9.2.
- **1.9.2** – New tab Sky noise (Skynoise) in Planning: antenna temperature computed with the G8ONH and G4SWX method from the full antenna pattern (NEC .out file, YA-NEC or Gaussian beam) and the sky map (Remazeilles, Haslam, GSM 2008 or LFmap) at 50, 144, 432 MHz and 23 cm, with the Moon path over the month, the temperature during the pass for you and for the DX, the effect on the EME budget Yagi and the comparison with DJ9BV; automatic test in compila.bat; in the THEORY AND TIPS ON EME manual: sky noise with the sources compared, dish gain (PE1RKI or itemised calculation, Ruze), prime focus above 2320 MHz, feed rotation and the Moon illuminated by the beam (BWF).
- **1.9.1** – Automatic update from GitHub, with SHA-256 fingerprint check, on Windows, with the portable archives (Linux, FreeBSD, OpenBSD, Alpine), the AppImage and the macOS app (the .deb, .rpm, Arch, Slackware packages are updated with the package manager), and warning about missing files; new packages for Windows ARM64, Fedora/openSUSE (.rpm), Arch Linux, Slackware, Raspberry Pi OS 32 bit, Alpine, FreeBSD, OpenBSD, Linux i686, AppImage; CORRECT button to correct a station's locator in CALL3.TXT; Distance and Dgrd with the classic Dgrd at 144 MHz, while the per-band Dgrd stays in DGRD by frequency; My horizon with the violet boxes of Sky view and the time taken from the planning table; Stations to try with the time from the table, a scroll bar and the option to leave out the stations of your own country (cty.dat); Yagi gain from the DL6WU table (G3SEK), with the formula attributed to W8IO only below 10 elements; drop-down lists and numeric boxes in the YA-MS style; 144 MHz transverters in the manual.
- **1.9** – New tab My horizon (Live): horizon from the terrain computed from SRTM1 data with Earth curvature and refraction, over the Sky view background in one of the three colour scales, Moon path, main obstacles with OpenStreetMap names and minutes of Moon lost; checkbox to use the terrain as minimum elevation throughout the program; local noise map after NJ9R, with ⚠ in the hours when the Moon is in a noisy direction; new tab Stations to try (Planning), idea by Matteo IW5DHN: the active stations of the N0UK chat ranked by an index from 0 to 100; numeric boxes with side-by-side arrows, pill-shaped tabs and three new colour schemes taken from IP-TRX-CTRL.
- **1.8** – New Slovak language (37 in total), with the manuals, the README and the licence; one beamwidth throughout the program: 0.93·√(41253/G) for Yagis (Kraus's rule corrected with W4RNL's NEC simulations, as in YA-MS) and 70·λ/D for dishes (IZ0JNY), replacing the unsourced √(32000/G) in DGRD by frequency; manual updated with the new formula and the pointing example; on macOS the launcher starts XQuartz by itself, writes the Mono version to the log and warns if YAEC does not start; README presentation also in Portuguese, Turkish, Czech, Slovak, Chinese, Japanese and Korean; translations corrected in Thai, Romanian, Greek, Brazilian Portuguese, Polish, Czech and Hungarian.
- **1.7** – Eight new languages: Brazilian Portuguese, Thai, Traditional Chinese, Polish, Czech, Romanian, Greek and Hungarian (36 in all), with the manuals and the READMEs; in EME budget Yagi and EME budget dishes, the echo calculation for your own station (I transmit and receive my own echo); prime-focus or offset dish (W2IMU); at 1296 MHz with dishes, the circular polarization loss of real feeds (KA1GT); in Calculation check, the choice between EME budget Yagi and EME budget dishes; formulas of DGRD by frequency written as in an equation editor; manual: Faraday rotation at 1296 MHz according to ITU-R P.531, depolarization at 23 cm (Hagfors) and circular polarization on 23 cm.
- **1.6** – 902 MHz and 23 cm (1296 and 1298 MHz) bands throughout the program, with all the bands in the MHz drop-down list; the EME budget tab becomes EME budget Yagi and there is the new EME budget dishes tab (prime-focus dish, gain with the PE1RKI formula, preamplifier also with two stages, transverter and PA drive); new DGRD by frequency tab, with the real noise of the station and the sky averaged over the beam, used throughout the program; coaxial cables calculated with the formula α = k1·√f + k2·f from the datasheet data, also at 902 and 1296 MHz; new style of the controls in all tabs; in Live position and +- 24h, the tooltip on the red cursor and the red DX lines at the cursor time; manual revised after comparing the sources (path loss band by band, thresholds of Q65-60B and Q65-60C, ground gain according to IK1UWL's measurements, connectors, Dgrd of other programs, dishes above 432 MHz); packages for every architecture (Windows x64 and x86, Linux x64, arm64 and arm, macOS Apple Silicon and Intel); thanks to Robert HA5OLA. The bands above 432 MHz are still being completed.
- **1.5** – New GRAVES radar tab in the Link group: Moon in the radar beam with sector and step, common window with you, Doppler and delay of the echo, next beam pass on the Moon, sky seen from GRAVES, reconstruction of the 24 UTC hours with the detail of the next 10 seconds, tips for hearing the echo and sources; list of active stations also in JSON and text for LunaCalc Mobile; two new languages, Danish and Tagalog (28 in all), with the manuals.
- **1.4** – Active stations: the DX callsign box gets an orange border if the station has written in the N0UK EME chat in the last 90 days, with the date of the last message in the tooltip; Font type with 10 recommended fonts for Windows, Linux and macOS, tested tab by tab; packages for 32-bit Windows and for Raspberry Pi (arm64); Sky view with dashed purple boxes around the area you can point at; Distance and Dgrd with the fourth useful day and the chosen day also selectable with a click in the chart; number boxes with a rounded frame and the arrows one above the other; dialog buttons at the edges (left, centre, right); acknowledgements box at full width; in narrow windows IN-DEPTH CALCULATIONS goes on two lines and no text ends up under the buttons.
- **1.3** – Nine new languages: Dutch, Estonian, Latvian, Lithuanian, Swedish, Norwegian, Icelandic, Hebrew and Urdu (26 in all), with the manuals; licence and README in all languages, licence in the installer's language; GRAVES button; TX connectors and RX connectors in the EME budget (advice from NJ9R); draggable splitter between the left column and the EME budget diagram; Grey veil checkbox in Reconnaissance of my obstacles; FORMULA DEBUG becomes Calculation check and ABOUT & CREDITS is now translated in every language; technical chapters of the user manual in Bengali, Arabic and Turkish; pastel schemes fixed; the CALL3.TXT window closes by itself after the update; dialog box buttons spaced out.
- **1.2.1** – The AUTHOR CONTACTS AND ACKNOWLEDGEMENTS page opens correctly again on Linux and macOS; the reference for the transverters points to § 1.7.1.
- **1.2** – EME budget with the indicators My EIRP, DX EIRP, path loss and S/N in both directions (with the Sun); Word document formulas in a single size, within the margins; filled buttons and flat drop-down lists with rounded borders in all schemes; eight pastel colour schemes; value boxes with side-by-side arrows; the three best days in date order; blurred sky background; FORMULA DEBUG translated; THEORY AND TIPS ON EME manual with the advice of Relu NJ9R (GRAVES, pointing, connectors, antenna gain, JT65B and MAP65, polarization relay), the new sections on the first reception and on internet chats, and the VE7BQH tables in the preface; thanks to NJ9R, the memory of IK1UWL and the authors of articles, hardware and software, with a tooltip on their works.
- **1.1** – Live position and +- 24h (formerly Tracking) also in the past and in the future: day from the calendar and time by dragging the red line, frequency in the Echo and frequencies box; DX callsign box with CALL3.TXT downloaded from W7GJ and WSJT-X Improved and merged, suggested locator and copy into the WSJT-X folder; Distance and Dgrd without the ranking, with the declination overlaid, rows colored like the chart and optional green usable hours; tickboxes in the program's style; cables sorted by diameter in the drop-down lists and by name, manufacturer and type in the table, with translated sources; EME budget with only the 60 s modes (JT65, Q65-60A, Q65-60B, Q65-60C) and a station diagram that adapts to the texts; USER MANUAL reviewing every screen; THEORY AND TIPS ON EME with the author's preface, numbering from 1 and the solar noise formulas; HTTPS on Linux and macOS with the system certificates.
- **1.0.1** – The GitHub release page now has the file SHA256SUMS.txt with the SHA-256 fingerprints of all the packages: use them to check that the downloaded files are the original ones (instructions in the README).
- **1.0** – First stable version, for Windows, Linux and macOS (Linux and macOS with Mono; data in ~/.local/share/YAEC/data or in ~/Library/Application Support/YAEC/data); Windows installer and Linux and macOS packages built on GitHub; earlier versions are called beta. New Moon over the world tab (Moon elevation over the land areas of the whole world, DX station with one click, status of your antenna); manual split into IN-DEPTH USER MANUAL and THEORY AND TIPS ON EME; Help and tools and Credits and thanks groups; Export calculations to Excel tab; no more mode margin: S/N in 2500 Hz with the typical threshold as reference and the JT65 limits in the manual; the manual also has the Q65 table for TX1 – TX6, Faraday rotation and the summary of the SM5BSZ article; cable table sortable by loss, with new Messi & Paoloni, SSB (SeaTex for marine environments, Aircom Premium), Belden and Tasker cables; boxes with a unit no longer show leftover text.


## For developers

You do not need to compile anything to use YAEC: the installer and the packages above are built automatically. If you want to build it yourself on Windows, `compila.bat` compiles `YAEC.cs` with the C# compiler included in Windows (.NET Framework 4, C# 5). Every push is compiled by GitHub Actions on Windows and started on Linux with Mono; when the `VERSION` file on `main` holds a new version, the workflow publishes the release with the Windows installer (Inno Setup) and the Linux and macOS packages (`.github/workflows/build.yml`).

## License

See `LICENZA.txt`.
