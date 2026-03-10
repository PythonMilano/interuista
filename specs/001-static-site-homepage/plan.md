# Implementation Plan: Static Site Homepage

**Branch**: `001-static-site-homepage` | **Date**: 2026-03-10 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-static-site-homepage/spec.md`

## Summary

Build the Intervista Pythonista static site using Pelican with a custom
single-file CSS theme. The home page replicates the content from
www.intervistapythonista.com: podcast description, host profiles (Marco
Santoni and Cesare Placanica), podcast platform links (Spotify, Apple
Podcasts, YouTube, RSS), and community links (LinkedIn, Slack, email).
Zero JavaScript. Perfect Lighthouse scores. Deployable to GitHub Pages,
Netlify, or Cloudflare Pages.

## Technical Context

**Language/Version**: Python 3.13
**Primary Dependencies**: Pelican (latest stable), Markdown (Pelican plugin)
**Storage**: N/A (static file output)
**Testing**: Lighthouse CLI for performance/accessibility audits
**Target Platform**: Static hosting (GitHub Pages, Netlify, Cloudflare Pages)
**Project Type**: Static site (Pelican)
**Performance Goals**: 100/100 Lighthouse all categories, < 1s load, < 100 KB total
**Constraints**: Zero JavaScript, vanilla CSS only, no third-party resources at render time
**Scale/Scope**: Single page site, 2 host profiles, 7 external links

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|-----------|--------|----------|
| I. Extreme Minimalism | PASS | Zero JavaScript. Single CSS file. No build tools beyond Pelican. |
| II. Tooling — Pelican | PASS | Pelican is the sole generator. Config in `pelicanconf.py` + `publishconf.py`. |
| III. Content — Pure Markdown | PASS | Home page content authored as Markdown in `content/pages/`. |
| IV. Styling — Vanilla CSS | PASS | Custom single-file CSS theme. No preprocessors. CSS variables for theming. |
| V. Performance — Lighthouse 100 | PASS | Semantic HTML, no JS, minimal CSS, self-hosted SVG icons, modern image formats. |
| VI. Portability — CI/CD | PASS | Standard `pelican content` build. `output/` directory published. No vendor lock-in. |

## Project Structure

### Documentation (this feature)

```text
specs/001-static-site-homepage/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
└── tasks.md
```

### Source Code (repository root)

```text
pelicanconf.py               # Main Pelican configuration
publishconf.py               # Production overrides (SITEURL, feeds off)
content/
└── pages/
    └── home.md              # Home page content (Markdown + metadata)
theme/
└── flavor/                  # Custom theme (Pelican theme structure)
    ├── static/
    │   └── css/
    │       └── style.css    # Single CSS file for entire site
    └── templates/
        └── page.html        # Jinja2 template for pages
output/                      # Generated site (gitignored)
.github/
└── workflows/
    └── deploy.yml           # CI/CD pipeline for deployment
.gitignore
pyproject.toml
README.md
```

**Structure Decision**: Default Pelican directory layout with a custom theme
named "flavor" containing a single CSS file and minimal Jinja2 templates.
The `content/pages/` directory holds the home page as a Markdown file.
No `src/` or `tests/` directories — this is a content site, not a Python
application.

## Complexity Tracking

> No violations. All principles satisfied with straightforward choices.
