# IP-TRX-CTRL

Remote control of an HF radio over the internet: two-way audio with AES-256 encryption (Opus from 0.3.6, 8 kHz PCM with earlier versions and the browser), CAT control with Hamlib or TCI (also the radio's audio over TCI, without sound cards or cables), PTT (CAT, RTS, DTR, VOX, TCI), keyer with WAV messages in SSB and text macros in CW, CW waterfall and decoder, VFO B with split, TX power, access also from the browser of a phone, tablet or PC without installing anything (from 0.3.1), SWR protection (warning and transmit lock), maximum transmit time, priority to whoever is at the radio, listen-only clients, radio controls (NR, NB, Notch, ATT, preamp, AGC, compressor, squelch, ALC), bands, step and memories, the radio's panadapter (Icom via CI-V, SDR via TCI), mute of the server's sound cards. On the client: digital programs (WSJT-X, JTDX, fldigi…) with a local rigctld and virtual audio cables, PTT foot switch and mechanical CW key on a serial port, USB and MIDI CW keys (VBand, Vail) with an iambic keyer, QSO log sent over UDP to logging programs (GridTracker, JTAlert, Log4OM) and ADIF export. On the server: several listeners at the same time while one operates, and network-connected Icom radios (IC-7610, IC-9700, IC-705…) without USB cables, like wfview (from 0.3.6). From 0.3.8: encrypted (TLS) link to the MQTT brokers, ephemeral keys for every session and a global limit on code attempts. From 0.3.7: neural noise reduction (HamNoise) for voice and CW, VOX with the button next to PTT, voice squelch, notes between operator and listeners, QSO recording, direct IPv6 connection with PCP, windowless server (headless Raspberry Pi, systemd service) and WinKeyer emulation for logging programs. Ports opened with UPnP and checked from outside, reverse connection and audio over UDP when possible.

A single program for both PCs: **server** (the radio is connected here) and **client** (the operator). The roles are chosen at first start and can be swapped.

Versions: Windows 10/11 64 and 32 bit and ARM, Windows 7 SP1, 8 and 8.1 (64 and 32 bit), Linux (Debian and derivatives, Fedora, openSUSE, Arch, Slackware, Alpine, AppImage for all), Raspberry Pi 64 and 32 bit, macOS Apple Silicon and Intel.

## Download

The files are on the **Releases** page; at the top of every release there is the table «Download the version for your system» with a direct link to every package.

| Distribution | File to download | Updates itself | Notes |
|---|---|---|---|
| **Windows 64 bit** | `IP-TRX-CTRL-…-win-x64-setup.exe` (portable: `…-win-x64-portatile.zip`) | yes | Hamlib included; the setup also offers the VB-CABLE virtual audio cable for digital programs |
| **Windows 32 bit** | `IP-TRX-CTRL-…-win-x86-setup.exe` (portable: `…-win-x86-portatile.zip`) | yes | Hamlib included |
| **Windows 7 SP1, 8, 8.1** (64 and 32 bit) | `IP-TRX-CTRL-…-win7-x64-setup.exe` or `…-win7-x86-setup.exe` (portable: `…-win7-x64-portatile.zip`, `…-win7-x86-portatile.zip`) | yes | from 0.3.5, with .NET 6 (the last one that runs on these Windows versions); Hamlib included. The `-win-` packages require Windows 10 or 11 |
| **Windows ARM** (Snapdragon) | `IP-TRX-CTRL-…-win-arm64-setup.exe` (portable: `…-win-arm64-portatile.zip`) | yes | Hamlib included (x64 rigctld, run by Windows 11 emulation) |
| **Debian, Ubuntu, Mint** (x86_64) | `ip-trx-ctrl_…_amd64.deb` | no, it notifies | `sudo apt install ./<file>.deb` also installs Hamlib |
| **Fedora, openSUSE, RHEL** | `ip-trx-ctrl-….x86_64.rpm` (or `.aarch64.rpm`, `.armv7hl.rpm`) | no, it notifies | `sudo dnf install ./<file>.rpm` or `sudo zypper install ./<file>.rpm`; Hamlib recommended (`hamlib`) |
| **Arch, Manjaro, EndeavourOS, Arch Linux ARM** | `ip-trx-ctrl-…-x86_64.pkg.tar.zst` (or `-aarch64`) | no, it notifies | `sudo pacman -U ./<file>.pkg.tar.zst` also installs Hamlib |
| **Slackware** (x86_64 and ARM64) | `ip-trx-ctrl-…-x86_64-1_ic8tem.txz` (or `-aarch64-`) | no, it notifies | as root `installpkg <file>.txz` (later versions: `upgradepkg`); Hamlib from SlackBuilds |
| **Any Linux** (x86_64 and ARM64) | `IP-TRX-CTRL-…-x86_64.AppImage` (or `-aarch64`) | yes | a single file: make it executable and run it; Hamlib and ALSA from the system |
| **Linux x86_64 portable** | `IP-TRX-CTRL-…-linux-x64-portatile.tar.gz` | yes | unpack and run; Hamlib from the package manager |
| **Linux i686** (32 bit) | — | — | not available: .NET 8, on which the program is built, does not exist for 32-bit Linux on PCs |
| **Alpine Linux** (musl, x86_64 and ARM64) | `IP-TRX-CTRL-…-linux-musl-x64-portatile.tar.gz` (or `-linux-musl-arm64-`) | yes | `apk add libstdc++ fontconfig libx11 libice libsm alsa-lib hamlib` |
| **Raspberry Pi (ARM)** | `ip-trx-ctrl_…_arm64.deb` (Raspberry Pi OS 64 bit) or `…_armhf.deb` (32 bit) | no, it notifies | `sudo apt install ./<file>.deb` also installs Hamlib; for automatic updates there is the portable `…-linux-arm64-` / `…-linux-arm-portatile.tar.gz` |
| **Raspberry Pi Slackware ARM64** | `ip-trx-ctrl-…-aarch64-1_ic8tem.txz` or `IP-TRX-CTRL-…-linux-arm64-portatile.tar.gz` | the portable one does | Hamlib from SlackBuilds (`hamlib`) |
| **Linux armv7l** | `ip-trx-ctrl_…_armhf.deb`, `ip-trx-ctrl-….armv7hl.rpm` or `IP-TRX-CTRL-…-linux-arm-portatile.tar.gz` | the portable one does | 32-bit ARM; Hamlib from the package manager |
| **FreeBSD amd64** | — | — | not available: .NET 8 has no official FreeBSD version (only community builds, not suitable for a program that controls a transmitter) |
| **macOS** | `…-osx-arm64.dmg` (Apple Silicon) or `…-osx-x64.dmg` (Intel); app only: `…-app.zip` | yes, if the app is in Applications or another writable folder | Hamlib with `brew install hamlib`; at first start right-click the app › Open |

## Automatic updates

From **0.3.2** the program updates itself. At start-up and then every 6 hours it checks the latest version published here on GitHub; if it is newer, it downloads the package for the PC, checks its size and SHA-256 fingerprint and restarts in the new version. It does so **only when no session is running and nothing is being transmitted**: if a session is open, the new version waits and is installed as soon as it ends. A server left on updates and restarts by itself, with the same settings. Settings, keys, pairings and logs are not touched.

These update themselves: the Windows installer and portable zip, the portable tar.gz archives (Linux, Raspberry Pi, Alpine), the AppImage, IP-TRX-CTRL.app on the Mac (moved to Applications or another folder the user can write to).

The system package managers' packages do **not** update themselves: **.deb** (Debian, Ubuntu, Mint, Raspberry Pi OS), **.rpm** (Fedora, openSUSE), **Arch** and **Slackware**. They are installed by root in `/opt` and belong to the package manager: the program only shows the new-version notice, and you install it with the same command as the first time. If you want automatic updates, use the AppImage or the portable tar.gz.

They can be turned off in **Settings › Main window** («Automatic updates» box): the notice stays, with the «Update now» button. 0.3.0 and 0.3.1 do not update themselves: install 0.3.2 by hand once, and later versions arrive by themselves. New versions of the same protocol talk to earlier ones; if one day the protocol changes, the two PCs align themselves at the first check (at start-up or within 6 hours).

You can also use the **browser** without installing anything (from 0.3.1): see [docs/Accesso-dal-browser.md](docs/Accesso-dal-browser.md).

## Errors and logs

The program writes errors to `errori.log` and the connection log to `sessioni.log`, in the data folder:

- Windows: `%APPDATA%\IP-TRX-CTRL` (Win+R, type the path and press Enter)
- Linux and Raspberry Pi: `~/.config/IP-TRX-CTRL`
- macOS: `~/.config/IP-TRX-CTRL`

From the program: **Settings › Open data folder**. To report a problem open an **Issue** and attach `errori.log` (and `sessioni.log` for connection problems). Details in `docs/Registri-e-risoluzione-problemi.md`.

The documentation is in the `docs` folder. The license notes of third-party components are in `THIRD-PARTY-NOTICES.txt` and in the program's «About and licenses» window.

Declared use: amateur radio activity.

## Compatible versions

Server and client must have versions of the same protocol:

| Versions | Protocol | Compatible with |
|---|---|---|
| 0.1.0 – 0.1.3 | 1 | only 0.1.x |
| 0.2.0 – 0.2.8 | 2 | all 0.2.x (some functions require a minimum version on both PCs) |
| 0.3.0 – 0.3.8 | 3 | only 0.3.x (10-digit number, fixed server code, several clients on the server, transmit safety, panadapter; from 0.3.1 browser access; from 0.3.2 automatic updates) |

Details and automatic check: [docs/Versioni-compatibili.md](docs/Versioni-compatibili.md).

## Support the project

IP-TRX-CTRL is free. If you find it useful and want to support its development: [ko-fi.com/ic8tem](https://ko-fi.com/ic8tem).

## License

IP-TRX-CTRL is free software, Copyright (C) 2026 Costantino Cerrotta IC8TEM, distributed under the **GNU Affero General Public License version 3 or later** (AGPL-3.0-or-later, file [`LICENSE`](LICENSE)), without any warranty. It is the GPL 3 with one more clause for programs used over a network: whoever modifies the program and lets others use their version over the network (for example the «Browser access» page) must offer them the source code too. From 0.3.6; versions up to 0.3.5 remain under GPL 3.0 or later. GPL 3 code from other projects (for example wfview) can still be used, because the two licenses can be combined. The licenses of third-party components are in `THIRD-PARTY-NOTICES.txt`.
