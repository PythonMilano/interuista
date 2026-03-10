# Intervista Pythonista

Sito statico per il podcast Intervista Pythonista della community Python Milano.

Generato con [Pelican](https://getpelican.com/). Zero JavaScript. Vanilla CSS.

## Sviluppo locale

```bash
# Installa le dipendenze
pip install -e .

# Genera il sito e avvia il server locale con auto-reload
pelican content --listen --autoreload
```

Apri http://localhost:8000 nel browser.

## Build di produzione

```bash
pelican content -s publishconf.py
```

Il sito generato si trova nella directory `output/`.

## Deploy

Il deploy avviene automaticamente via GitHub Actions al push su `main`.
Il sito e' anche deployabile su Netlify o Cloudflare Pages puntando alla
directory `output/` dopo aver eseguito `pelican content -s publishconf.py`.
