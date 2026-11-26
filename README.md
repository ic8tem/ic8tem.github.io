# ic8tem.github.io

Sito di **IC8TEM'S SOFTWARE FARM** – programmi gratuiti per radioamatori di Costantino Cerrotta IC8TEM: https://ic8tem.github.io

- `index.html`: pagina principale (italiano/inglese), con le novità, i programmi, la ricerca del file per il proprio sistema, i video e i contatti.
- `programs/*.html`: le schede dei programmi in inglese, generate dai README.
- Per rigenerare le schede e la tabella dei download: `python3 tools/build.py` (README in `src/readmes`, elenco dei file delle release in `src/releases.json`).

## Aggiornamento automatico dei link

Il workflow `.github/workflows/aggiorna-link.yml` gira ogni 3 ore (e a mano da Actions → *Aggiornamento automatico dei link* → *Run workflow*):

1. `tools/update.py` legge l'ultima release di ogni programma (elenco in `src/auto.json`) e aggiorna `src/releases.json`; una release a cui mancano ancora i file principali (setup Windows x64, AppImage x86_64, i due .dmg) viene saltata finché non è completa.
2. Copia i README inglesi aggiornati in `src/readmes` (non quelli di E-LAYER ANALYZER e IP-TRX-CTRL, tradotti a mano).
3. Conta le lezioni del videocorso di YA-NEC nel wiki e aggiorna il numero nelle 10 lingue.
4. Aggiunge in cima ai video (`src/videos.json`, sezione `auto`) i video nuovi del canale YouTube, escluse le singole lezioni dei corsi. Per nascondere un video basta mettere il suo ID in `ignore`.
5. Controlla che video e playlist esistano ancora: se qualcuno non risponde apre (o aggiorna) la issue *Link del sito da controllare*, che si chiude da sola quando tutto torna a posto.
6. `tools/build.py` rigenera le pagine e, se qualcosa è cambiato, il workflow pubblica.

Le notizie nelle 10 lingue restano da scrivere a mano.
