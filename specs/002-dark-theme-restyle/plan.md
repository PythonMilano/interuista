# Implementation Plan: Dark Theme Restyle

**Branch**: `002-dark-theme-restyle` | **Date**: 2026-03-11 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/002-dark-theme-restyle/spec.md`

## Summary

Restyle the Intervista Pythonista site with a dark theme inspired by the podcast logo. The implementation requires two changes: (1) update the CSS custom properties in `style.css` to swap from a light color scheme to a dark one (black background, white text, golden yellow accent), and (2) modify the Jinja2 template `page.html` to wrap the "Py" portion of the title in a `<span>` element for targeted CSS coloring. The existing CSS variables architecture makes the color scheme swap straightforward.

## Technical Context

**Language/Version**: Python 3.13 (Pelican build tooling only; changes are CSS/HTML)
**Primary Dependencies**: Pelican (latest stable) — no new dependencies
**Storage**: N/A (static site)
**Testing**: Manual Lighthouse audit, visual inspection, WCAG contrast ratio verification
**Target Platform**: Web browsers (GitHub Pages deployment)
**Project Type**: Static website (Pelican)
**Performance Goals**: Lighthouse 100/100 in all four categories
**Constraints**: Zero JavaScript, vanilla CSS only, CSS payload under 10 KB
**Scale/Scope**: Single-page site, 1 CSS file (~150 lines), 1 HTML template (43 lines)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Justification |
|-----------|--------|---------------|
| I. Extreme Minimalism | PASS | No JavaScript. Changes are pure CSS variable updates and one `<span>` in HTML template. |
| II. Tooling — Pelican | PASS | All changes within Pelican's theme system (`theme/flavor/`). No custom build scripts. |
| III. Content — Pure Markdown | PASS | No content file changes. Only theme template and stylesheet modified. |
| IV. Styling — Vanilla CSS | PASS | Plain CSS only. CSS custom properties for theming. No preprocessors or frameworks. |
| V. Performance — Perfect Lighthouse | PASS | Color-only changes. No new assets, fonts, or resources. Contrast ratios verified (see research.md). Must validate post-implementation. |
| VI. Portability — Standard CI/CD | PASS | No deployment changes. Same build process produces updated output. |

**Gate result**: ALL PASS — proceed to implementation.

## Project Structure

### Documentation (this feature)

```text
specs/002-dark-theme-restyle/
├── plan.md              # This file
├── research.md          # Phase 0: color research and contrast verification
├── spec.md              # Feature specification
├── checklists/
│   └── requirements.md  # Spec quality checklist
└── tasks.md             # Phase 2 output (created by /speckit.tasks)
```

### Source Code (repository root)

```text
theme/flavor/
├── static/css/
│   └── style.css          # UPDATE: dark color scheme via CSS variables
└── templates/
    └── page.html          # UPDATE: wrap "Py" in <span> for yellow styling
```

**Structure Decision**: No new files or directories needed. This feature modifies exactly 2 existing files in the Pelican custom theme.

## Complexity Tracking

> No constitution violations. No complexity justifications needed.

## Implementation Details

### File 1: `theme/flavor/static/css/style.css`

**Changes to `:root` CSS variables:**

| Variable | Current Value | New Value | Purpose |
|----------|--------------|-----------|---------|
| `--color-bg` | `#ffffff` | `#000000` | Black background |
| `--color-text` | `#1a1a2e` | `#f0f0f0` | Near-white body text |
| `--color-heading` | `#16213e` | `#ffffff` | White headings |
| `--color-accent` | `#3066be` | `#6ea8fe` | Light blue links (visible on dark bg) |
| `--color-accent-hover` | `#1e4a8e` | `#9ec5fe` | Lighter blue on hover |
| `--color-muted` | `#555` | `#aaa` | Lighter gray for footer/secondary text |
| `--color-border` | `#e0e0e0` | `#333` | Dark gray borders |

**New CSS variable:**

| Variable | Value | Purpose |
|----------|-------|---------|
| `--color-py` | `#e8a317` | Golden yellow for "Py" accent, sampled from logo |

**New CSS rule:**

```css
.py-accent {
    color: var(--color-py);
}
```

### File 2: `theme/flavor/templates/page.html`

**Change the `<h1>` from:**
```html
<h1>{{ page.title }}</h1>
```

**To:**
```html
<h1>Intervista <span class="py-accent">Py</span>thonista</h1>
```

This hardcodes the title with the `<span>` wrapping "Py". This is acceptable because:
- The site name is fixed ("Intervista Pythonista")
- The `<span>` is semantically neutral (no accessibility impact)
- The yellow coloring is purely presentational via CSS class

### Contrast Ratio Verification

All proposed color combinations meet WCAG AA (see research.md for calculations):

| Combination | Ratio | Requirement | Status |
|-------------|-------|-------------|--------|
| `#f0f0f0` on `#000000` (body text) | 18.4:1 | 4.5:1 | PASS |
| `#ffffff` on `#000000` (headings) | 21:1 | 4.5:1 | PASS |
| `#e8a317` on `#000000` (Py accent) | 9.7:1 | 3:1 (large text) | PASS |
| `#6ea8fe` on `#000000` (links) | 8.3:1 | 4.5:1 | PASS |
| `#9ec5fe` on `#000000` (link hover) | 11.6:1 | 4.5:1 | PASS |
| `#aaa` on `#000000` (muted/footer) | 9.3:1 | 4.5:1 | PASS |
