# Quickstart: Static Site Homepage

## Prerequisites

- Python 3.13
- A Python package manager (pip, uv, etc.)

## Setup

```bash
# Clone the repository
git clone <repo-url>
cd interuista

# Install dependencies
pip install -e .
# or: uv sync
```

## Local Development

```bash
# Generate the site and serve locally with auto-reload
pelican content --listen --autoreload
```

Open http://localhost:8000 in your browser.

## Production Build

```bash
# Generate the site with production settings
pelican content -s publishconf.py
```

The generated site is in the `output/` directory.

## Deployment

The site deploys automatically via GitHub Actions on push to `main`.
The pipeline:
1. Installs Python and dependencies
2. Runs `pelican content -s publishconf.py`
3. Publishes `output/` to the configured hosting platform

## Lighthouse Audit

```bash
# Install Lighthouse CLI (requires Node.js)
npm install -g lighthouse

# Run audit against production build
pelican content -s publishconf.py
cd output && python -m http.server 8080 &
lighthouse http://localhost:8080 --output=json --output-path=./report.json
```

All four categories MUST score 100/100 before deployment.
