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

## What's new in 1.5.6

- **Calculators > HF > Wire antennas** (new): end-fed wire antennas. EFHW multiband, single band and with coil (49:1 or 64:1), non-resonant wire with 9:1 or 4:1; six layouts (sloping up or down, vertical, inverted L and U, straight); 0.05 λ counterpoise or coax shield, capacitor, end voltage, SWR per band from the TF5NN model and from NEC; **Tune the length (NEC)**.
- **Jump buttons**: from the wire antennas and the other wire pages (dipoles, OCF/Windom, T2FD, G5RV, Delta, Quad, Loop, Skywire, Moxon, Hexbeam) the balun, choke (FT toroids), quarter-wave (RG cables) or loads page opens already filled in, with «‹ Back».
- **Discone**: moved from the HF family to the VHF family.

## What's new in 1.5.5

- **Calculators > HEN**: the card shows horizontal polarization, as the NEC check does (it said vertical).
- **VNA measurements**: titles, legend and correction proposal translated (they stayed in Italian).
- **Video course**: 32 lessons, with the new 30 «Cables and VNA measurements» and 31 «More calculators».

## What's new in 1.5.4

- **Hand-written model**: wires applied before the source give an orange warning in the status bar, with no window; real error windows take the focus (Enter or Esc close them).
- **Translations**: Boom page (from the survey to the electrical model) translated into English.
- **Complete video course**: 30 lessons recorded with 1.5.3-1.5.4, in Italian and English, with the new lesson 29 «Resize and recentre».

## What's new in 1.5.3

- **Resize and recentre** (Variables and optimization): an MMANA model or a design moved to the wanted frequency in one click; scaled, equal or commercial diameters (solid rods 3-6 mm, rods or tubes 8-40 mm); trimming the driven element zeroes the reactance.
- **Patterns**: the first item is **Lobes**, the Frequency tab becomes **Parameters**; **angle step** adapted to the computer; **Reception (RDF)** on the open model.
- **Fixes**: 2-3 element quad in Automatic brought to resonance by NEC (Cebik holds for a single loop); a single warning for a model without a source; video course re-recorded with 1.5.3.

## What's new in 1.5.2

- **Reorganised tabs** (from 16 to 13): the Smith chart in the Patterns band, **NEC/currents**, **Variables and optimization**; VHF stack spacings and HF stacking distances + HFTA; new order of the Calculator families.
- **3D structure**: transmission lines, loads and networks drawn on the wires; the ground legend opens from **Show ground** in the status bar; every error in bold and in an OK window. **Frequency**: amateur bands shaded behind the charts.
- **Real terrain**: calculation status and manual site height. **Optimizer**: **Measures to the millimetre** (coordinates and commercial diameters, NEC check, cutting list). Patterns, charts and cards translated in 36 languages.

## What's new in 1.5.1

- **Optimizer**: "+ add variable" creates a variable from the model (length or perimeter, position, radius of each element, loops included; antenna height), with an ochre preview.
- **Variables**: on the right, the 3D structure shows in ochre where the chosen variable acts.
- Fixes (capacitive loop, stack with no valid distance, Wind on first opening) and completed English translation.

## What's new in 1.5

- **Calculators**: Mechanical calculations moved into Calculators; short-dipole reactance, folded dipole versus frequency, multi-turn magnetic loop with capacitive coupling (Antenna Engineering Handbook, 4th ed.). **HF stacking distances** as a separate item.
- **AutoEZ, MultiNEC, EZNEC models**: "mark out" sources, virtual wires, transformers, calculated cells; the saved .nec writes current sources as the computed voltages.

## What's new in 1.4.2

- **Calculators**: NVIS (best height and ground screen, after Cebik), Hairpin (beta) match, Quad with Cebik's method and NEC resonance at VHF, J-pole with the Slim Jim.
- **Optimizer**: Monte Carlo with construction tolerances. **Stacks**: spacing checked on two frequencies.
- **Settings**: Force update, Report a problem.

## What's new in 1.4

- **Technical documents**: user manual, new calculation and sources manual (formulas, assumptions, limits, sources with similarities and differences, test cases) and numbered citations, each with its contents and PDF; search across all three (documents in Italian).
- **Stack distances**: active SWR and realized gain; distances with high active SWR are marked "do not choose".
- **Closing**: confirmation window with a thank-you.

## What's new in 1.3

- **Receiving antennas**: in the Calculators **Low dipole**, **K9AY** (termination with "optimize for F/B"), **4-square RX** and the **Hi-Z** arrays of 2, 3 and 8 verticals are enabled, with the **phase between rows** and the "optimize the phase (RDF)" button. Each item creates the NEC model and gives RDF, DMF, F/B and its place in the ranking; a yellow warning recalls the NEC-2 limit with wires connected to real ground.
- **Reception (RDF)**: the 8 verticals in a circle use a 220-degree phase and the lobe points forward.
- **Video course**: lessons 22 (Real terrain), 23 (Receiving antennas), 24 (VHF tools) and 25 (Mechanical calculations and HF loads), in Italian and English with voice.
- **Languages**: texts not yet translated are shown in English instead of Italian; polar plots, model objects, Cable and balun, H-frame, Dividers and yellow warnings are now in English.
- **Fixes**: HF loads no longer closes when switching to "Loading coil"; clicking another item with the cursor in a field no longer closes the program; the receiving-antenna warnings no longer pile up; wide windows no longer spill to the right.
- Everything in chapter 24 of the manual, with the sources (K9AY, Hi-Z Antennas, IV3PRK, ON4UN, W7EL).

## What's new in 1.2

- **Real terrain** (as in N6BV's HFTA): elevation pattern over the true terrain profile, from the **TINITALY** DEM (Italy, 10 m) or **SRTM1** (worldwide), from a HorizonProfiler file or flat. Facet-by-facet reflections weighted with the Fresnel zones, diffraction over ridges, sea, curved earth; traffic directions from the locator (up to 12 characters) and a **map** with aerial photo, OpenStreetMap and locator grid. On VHF full view and 0-15 degree zoom.
- **Reception (RDF)**: RDF, DMF, average F/R, antenna noise (ITU-R P.372) and receiver margin for Beverage, BOG, K9AY, Flag, EWE, 4-square and 8-circle arrays.
- **VNA measurements**: .s1p and CSV files over the calculation, with the cable removed (de-embedding), Smith chart and a suggested correction.
- **Build tolerances**: repeatable Monte Carlo, per-element sensitivity and a cutting list with the allowed tolerance.
- **Mechanical calculations** (new tab): **wind** with NTC 2018, CNR-DT 207 and EN 1991-1-4 (zone from the locator, cross-flow) and **balance** on the mast; forces in N and kgf.
- **Cable and balun** from 1.8 to 1296 MHz (the shield becomes a NEC wire), **H-frame and mast** in the stack, λ/4 and Wilkinson **dividers** with a 1:1 drawing, **crossed Yagis** (RHCP, LHCP, X-pol), **HF loads** (W8NX coax traps, coils, linear loading), **average F/R** also in the optimizer and an automatic **AGT test**.
- Everything explained in chapter 23 of the manual, with the sources; new items translated into the 37 languages.

## What's new in 1.1

> **Author's note.** In this version I thought long and hard about noise temperature. Some MATLAB studies on the stacking of directional antennas were brought to my attention, and I wanted to try it right away: to give YA-NEC users the chance to go beyond the DL6WU stacking distance (the trigonometric formula) and to guide them, if they wish, in choosing a stacking distance of their own. Together with this, a deep revision of the user interface. — *Costantino IC8TEM*

- **Noise from the real sky.** New page in the **Noise/GT/Stack** super-tab: the pattern of the antenna or of the stack is laid over the real sky map (Haslam 408 MHz survey, reprocessed by Remazeilles, scaled to 144 and 432 MHz by G8ONH), from your QTH (locator or coordinates) at the chosen time, pointing wherever you want, at the Moon or at the coldest patch of sky. Two G/T values side by side: with a uniform sky, comparable with VE7BQH's tables (30 degrees, 2 x 2 stack at DL6WU spacing), and with the real sky, with the antenna temperature curve over 24 hours and its minimum and maximum. The calculation is **skynoise by John C. Sager G8ONH** (MIT license), ported to C#.
- **Stacking distance chosen with NEC.** In the **Stack spacings** page (moved out of the Calculators) the stack is really computed for a range of spacings around the DL6WU one: gain, highest side lobe, G/T and the coupling matrix between the ports (S11, S21...). A criterion picks the proposed spacing (maximum gain, lowest lobes, best G/T, or gain with the lobes below a threshold) and a button uses it to build the stack. On **HF** the DL6WU formula does not apply: the stack above ground is chosen on the wanted take-off angles, with elevation patterns in phase (BIP), single antennas and out of phase (BOP).
- **Calculators by family.** A bar under the tabs splits the calculators into **HF**, **VHF**, **Receiving antennas** (no longer a separate tab), **Tools**, **Dishes and feeds** and **2.4 GHz**; the list on the left shows only the chosen family.
- **Pattern measurements.** Besides the -3 dB beamwidth: first-null beamwidth (FNBW), highest side lobe (SLL) and two cursors C1 and C2 placed with a click, with level, angle and the difference between them.
- **F/B along the axis** fixed for free-space models whose beam points along the Z axis (like the MathWorks Antenna Toolbox Yagi).
- **New calculators**: biquad and double biquad (dish feeds), Big Wheel and three dipoles, horizontal multiband loop (Skywire) with the feed line loss on every band.
- **Translations**: all the new items in the 37 languages of the program. **Video course** updated with lessons on the new topics.

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

Every 30 minutes the program silently checks for a new version here. If there is one, it downloads the zip for its platform, verifies the SHA-256 checksum and installs it: the new version starts **at the next launch**, with a message in the status bar. The previous version is kept in `data/aggiornamenti/precedente-<version>`; settings (`data/config.ini`) and user models are not touched. Without a checksum, or with a different one, nothing is installed. Updates can be turned off in **Settings > Update**.

**Exception: Debian/Ubuntu (.deb) and Fedora/openSUSE (.rpm) packages.** When available, they will install into system folders with administrator rights, so the program cannot (and must not) change itself: they will be updated with the package manager. In those packages automatic update is off, and Settings says so.

## Building from source

.NET 8 SDK required. Windows: `compila.bat` (program in `build\win-x64`), `compila.bat /distribuzione` for the self-contained version, `compila_win7.bat` for Windows 7. Linux and macOS: `./compila.sh`. Details in [LEGGIMI.txt](LEGGIMI.txt) (Italian).

## Credits and license

**GPL-3.0** ([LICENSE](LICENSE), [THIRD-PARTY-NOTICES.txt](THIRD-PARTY-NOTICES.txt)), like nec2c and xnec2c from which the engine derives. YA-NEC exists thanks to the work of fellow radio amateurs and researchers: the full list is in [CREDITI.txt](CREDITI.txt) and in the **Credits** tab. Thanks to Luis IV3PRK for the free publications on his website.

## Contacts

ic8tem@gmail.com · [QRZ](https://www.qrz.com/db/ic8tem) · [Facebook group](https://www.facebook.com/groups/1675310160982493) · donations: [ko-fi.com/ic8tem](https://ko-fi.com/ic8tem)
