# LIVETROPOVHF

**Live VHF/UHF tropospheric propagation for radio amateurs — by IC8TEM**
*Propagazione troposferica VHF/UHF in tempo reale per radioamatori*

LIVETROPOVHF puts on one map the tropo forecast and what is really happening on the air from 144 MHz up.

![release](https://img.shields.io/github/v/release/ic8tem/LIVETROPOVHF) ![platforms](https://img.shields.io/badge/Windows%20%7C%20Linux%20%7C%20Raspberry%20Pi%20%7C%20Mac-blue) ![.NET](https://img.shields.io/badge/.NET-10-purple)

![LIVETROPOVHF](TropoVHF/Assets/splash.jpg)

## What it does / Che cosa fa
- **Forecast** – Hepburn and F5LEN tropo maps, merged worldwide; isobars, 850 hPa isotherms and thermal inversion (Open-Meteo).
- **Live** – spots from DX clusters (ON0DXK, DXMAPS with RBN skimmer, S50CLX), RBN and DM4X, PSKReporter (MQTT), your own WSJT-X / JTDX / MSHV decodes (UDP), QSOs inferred from RR73/73.
- **Clean data** – only 144 MHz and up (GRAVES 143.050 kept); meteor scatter, EME, QO-100 and fake listeners filtered out; paths over 1000 km held until confirmed.
- **Locators** – always 6 characters: CALL3.TXT, manual entries, layered files, automatic corrections from DM4X/RBN, MMMonVHF updates and G7VRD as last source.
- **Own forecast (experimental, 1.2.0)** – gain map computed from GFS vertical profiles (Bean & Dutton, Kerr), signal prediction between two stations over Copernicus GLO-30 terrain (SRTM1 before 1.3.2) (diffraction, troposcatter, ducts, ITU-R P.372 noise), optional gain contours, isobars and inversion lines. Also in the Windows 7 build from 1.2.3.
- **Tabs (five groups)** – Map; Forecasts (own β, Hepburn, F5LEN); GRAVES; Data & sources; Guides. Older list: Map, Hepburn, F5LEN, Forecast (experimental), GRAVES, Suspicious reports (self-learning), Data collection, three technical manuals with sources.
- **Portable** – everything next to the program (LIVETROPOVHF.ini, LIVETROPOVHF.db, Dati\\): no registry, no AppData. Interface in 36 languages.

## Download / Scarica
Get the latest version from **[Releases](../../releases/latest)**:
- **Windows 10/11**: `LIVETROPOVHF-…-windows-x64-setup.exe` (installs in `C:\LIVETROPOVHF`, no admin rights) or the portable zip; x86 and ARM64 builds too.
- **Windows 7 SP1 / 8.1**: `LIVETROPOVHF-…-windows7-x64-setup.exe` (or x86, or the portable zip): a native .NET Framework 4.8 build.
- **Linux**: `.deb`, `.rpm`, Arch `.pkg.tar.zst`, Slackware `.txz`, `AppImage`, `tar.gz`; **Raspberry Pi** 64/32 bit; **Alpine**.
- **Mac**: `.dmg` for Apple Silicon or Intel.

To build from source on Windows: double-click `build-win64.bat` (it installs the .NET 10 SDK locally if missing).

## Windows 7 SP1 / 8.1
The standard Windows build uses .NET 10, which does not start on Windows 7 (*"Impossibile trovare il punto di ingresso GetSystemTimePreciseAsFileTime…"*); the .NET 6 packages of 1.0.1 did not start on every Windows 7 either.
- From **1.0.2** the **`-windows7-x64`** and **`-windows7-x86`** packages (setup or portable zip) are a separate program written for **.NET Framework 4.8** with a WinForms window (folder `Win7` in the sources). Engine, map and GRAVES view are the same code as the standard build; the window and the drawing (GDI+) are rewritten. Same tabs, same 36 languages.
- It needs **Microsoft .NET Framework 4.8** (included in Windows 10/11, free download for Windows 7 SP1 and 8.1): the setup checks and opens the Microsoft download page if it is missing.
- Missing on Windows 7: OCR reading of map axes and the manual calibration bench (Hepburn and F5LEN regions have factory extents, so in practice nothing changes).
- If you installed 1.0.0 or 1.0.1 on Windows 7, download the `windows7` setup manually and install it over the old one. Settings and data are kept; from then on updates are automatic. Details: [Wiki – Windows 7 e 8.1](../../wiki/Windows-7-e-8.1).

## Automatic updates
Every 30 minutes the program checks the latest Release and, if newer, downloads the portable package for its platform and replaces its own files silently; the new version starts at the next launch. Settings, archive, `Dati\` and `CALL3.TXT` are never touched.

## Documentation
- [Wiki](../../wiki) – quick start, discard criteria, map colours.
- [CHANGELOG.md](CHANGELOG.md) – version history.
- In the program: tabs *Funzionamento*, *Costruzione della mappa*, *Come si forma la tropo* (Italian, exportable to Word).

## Credits
Tropo maps: W. R. Hepburn (DX Info Centre), F5LEN. Weather: NOAA GFS (NOMADS) and Open-Meteo; radio climate from ECMWF ERA5 via Open-Meteo (Copernicus Climate Change Service, CC BY 4.0). Terrain: Copernicus DEM GLO-30 (© DLR e.V. 2010–2014 and © Airbus Defence and Space GmbH 2014–2018, provided under COPERNICUS by the European Union and ESA). Propagation models: NTIA/ITS Irregular Terrain Model (U.S. Government work), ITU-R P.452, P.617, P.453, NBS TN101. Coastlines: Natural Earth. Spots: DX clusters, Reverse Beacon Network, DM4X, PSKReporter. Callsign database: CALL3.TXT / MMMonVHF, G7VRD locator API. GRAVES data: PE1ITR and the YA-MS project.

Thanks to **I5MZY Massimo Zannoni** for testing on Windows 7 and Windows 8.

## License / Licenza
LIVETROPOVHF is free software under the **GNU General Public License v3.0** ([LICENSE](LICENSE)): you may use, study, share and modify it; modified versions you distribute must stay under GPL-3.0 with their source code. No warranty.
LIVETROPOVHF è software libero con licenza **GNU GPL v3.0**: si può usare, studiare, condividere e modificare; le versioni modificate distribuite restano GPL-3.0, con il codice sorgente. Nessuna garanzia.

Third-party components (all GPL-3.0 compatible): Avalonia (MIT), MQTTnet (MIT), Microsoft.Data.Sqlite and System.Text.Json (MIT), SQLite (public domain), ITM port from NTIA/ITS code (U.S. Government work). Data are downloaded at run time from their providers and are not redistributed here (ITU-R data, Copernicus DEM, GFS, ERA5, maps and spot networks keep their own terms).

---
*Software for amateur radio use. Forecasts are indications, not guarantees.*
