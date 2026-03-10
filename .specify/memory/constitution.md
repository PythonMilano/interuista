<!--
Sync Impact Report
- Version change: N/A (new) -> 1.0.0
- Modified principles: N/A (initial ratification)
- Added sections:
  - Core Principles (6 principles)
  - Technology Constraints
  - Development Workflow
  - Governance
- Removed sections: N/A
- Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ no changes needed (Constitution Check is dynamic)
  - .specify/templates/spec-template.md: ✅ no changes needed (generic template)
  - .specify/templates/tasks-template.md: ✅ no changes needed (generic template)
  - .specify/templates/commands/*.md: ✅ no command files exist
- Follow-up TODOs: none
-->

# Interuista Constitution

## Core Principles

### I. Extreme Minimalism

Zero unnecessary JavaScript. Every byte shipped to the browser MUST justify
its existence. If a feature can be achieved with pure HTML and CSS, JavaScript
MUST NOT be used. No JS frameworks, no JS build steps, no client-side
rendering. The only acceptable JavaScript is for functionality that is
literally impossible without it (e.g., analytics snippet if required), and
each exception MUST be documented with a rationale.

### II. Tooling — Pelican

Pelican MUST be the sole static site generator. All site generation logic
MUST flow through Pelican's plugin and theme system. Custom build scripts
outside of Pelican's standard workflow are prohibited unless they serve
CI/CD deployment (see Principle VI). Pelican configuration MUST be kept in
a single `pelicanconf.py` with a `publishconf.py` overlay for production.

### III. Content — Pure Markdown

All content MUST be authored in Markdown files. No reStructuredText, no
HTML-in-content (except where Markdown lacks expressiveness for a specific
element, e.g., `<details>` blocks). Metadata MUST use Pelican's standard
Markdown metadata format. Content MUST be portable — extracting the
`content/` directory MUST yield a readable archive independent of the
generator.

### IV. Styling — Vanilla CSS

All styling MUST use plain CSS. No Sass, Less, PostCSS, Tailwind, or any
CSS preprocessor or utility framework. CSS MUST be organized in a small
number of files (ideally one). Custom properties (CSS variables) are the
preferred mechanism for theming and consistency. The total CSS payload
SHOULD remain under 10 KB uncompressed.

### V. Performance — Perfect Lighthouse Scores

The site MUST achieve 100/100 on all four Lighthouse audit categories
(Performance, Accessibility, Best Practices, SEO) for every page. This is
a hard gate — no deployment MUST proceed if any score drops below 100.
Images MUST use modern formats (WebP/AVIF) with appropriate sizing. HTML
output MUST be semantic and valid.

### VI. Portability — Standard CI/CD Deployment

The site MUST be deployable to GitHub Pages, Netlify, or Cloudflare Pages
with no vendor-specific code in the source. Deployment MUST be driven by a
single CI/CD pipeline (e.g., GitHub Actions) that runs `pelican content`
and publishes the `output/` directory. No platform-specific plugins,
serverless functions, or edge compute. The build MUST be reproducible given
only the repository and a Python environment.

## Technology Constraints

- **Language**: Python 3.13
- **Generator**: Pelican (latest stable)
- **Content format**: Markdown (`.md`)
- **Styling**: Vanilla CSS only
- **JavaScript**: Zero by default; exceptions require documented rationale
- **Image formats**: WebP or AVIF preferred; PNG/JPEG acceptable as
  fallbacks with automated conversion
- **Deployment targets**: GitHub Pages, Netlify, Cloudflare Pages
- **Package management**: `pyproject.toml` with standard Python tooling
- **Content source**: Migrated from www.intervistapythonista.com

## Development Workflow

- All changes MUST be committed to version control before deployment.
- Content and theme changes MUST be previewed locally with `pelican --listen`
  before pushing.
- Lighthouse audits MUST be run against the production build (`publishconf.py`)
  before any release. A score below 100 in any category blocks the release.
- Dependencies MUST be pinned to exact versions in a lock file to guarantee
  reproducible builds.
- The `output/` directory MUST NOT be committed to the repository.

## Governance

This constitution is the authoritative source of project constraints and
principles. All design decisions, spec reviews, and implementation plans
MUST verify compliance with these principles.

- **Amendments**: Any change to this constitution MUST be documented with a
  version bump, rationale, and updated date. Principle removals or
  redefinitions require a MAJOR version bump.
- **Versioning**: This document follows semantic versioning
  (MAJOR.MINOR.PATCH). MAJOR for breaking governance changes, MINOR for
  new principles or material expansions, PATCH for clarifications.
- **Compliance**: Every spec and plan MUST include a Constitution Check
  section verifying alignment with all six principles.

**Version**: 1.0.0 | **Ratified**: 2026-03-10 | **Last Amended**: 2026-03-10
