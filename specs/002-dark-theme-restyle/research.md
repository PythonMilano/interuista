# Research: Dark Theme Restyle

**Feature**: 002-dark-theme-restyle
**Date**: 2026-03-11

## Research Topic 1: Logo Yellow Color Identification

**Decision**: Use `#E8A317` as the golden yellow accent color for the "Py" text.

**Rationale**: Visual inspection of the podcast logo (`logo_squared.png`) shows a warm golden yellow used for the letters "py" in "pythonista". The color is a saturated amber/golden yellow, distinct from pure yellow (#FFFF00) or pale yellow. The hex value #E8A317 closely matches the logo's yellow and provides strong contrast on a black background.

**Alternatives considered**:
- `#FFD700` (Gold): Too bright/saturated, doesn't match the warmer tone in the logo
- `#DAA520` (Goldenrod): Slightly too brownish, lacks the vibrancy of the logo yellow
- `#F0A500`: Close match but slightly more orange; #E8A317 is a better middle ground

## Research Topic 2: WCAG AA Contrast Ratios on Black Background

**Decision**: All proposed text colors pass WCAG AA contrast requirements against `#000000`.

**Rationale**: WCAG AA requires a minimum contrast ratio of 4.5:1 for normal text and 3:1 for large text (18pt+ or 14pt+ bold). The h1 title qualifies as large text (2rem = ~32px).

### Contrast Calculations

Relative luminance formula: `L = 0.2126 * R + 0.7152 * G + 0.0722 * B`
(where R, G, B are linearized sRGB values)

Contrast ratio: `(L1 + 0.05) / (L2 + 0.05)` where L1 is the lighter color.

| Color | Hex | Relative Luminance | Ratio vs #000 | Min Required | Result |
|-------|-----|-------------------|----------------|--------------|--------|
| Body text | `#f0f0f0` | 0.870 | 18.4:1 | 4.5:1 | PASS |
| Headings | `#ffffff` | 1.000 | 21.0:1 | 4.5:1 | PASS |
| Py accent | `#e8a317` | 0.436 | 9.7:1 | 3.0:1 (large) | PASS |
| Links | `#6ea8fe` | 0.367 | 8.3:1 | 4.5:1 | PASS |
| Link hover | `#9ec5fe` | 0.530 | 11.6:1 | 4.5:1 | PASS |
| Muted text | `#aaaaaa` | 0.402 | 9.0:1 | 4.5:1 | PASS |

All combinations exceed WCAG AA thresholds by comfortable margins.

## Research Topic 3: Dark Theme Best Practices for Static Sites

**Decision**: Use CSS custom properties for the full color scheme swap, keeping the same structural CSS.

**Rationale**: The existing site already uses CSS custom properties (`:root` variables) for all colors. Changing the theme is a matter of updating variable values — no structural CSS changes needed. This approach:
- Minimizes diff size and risk of regressions
- Maintains the existing responsive layout unchanged
- Keeps CSS payload well under the 10 KB constitution limit
- Requires no JavaScript for theme switching (single dark theme, not a toggle)

**Alternatives considered**:
- Adding a `prefers-color-scheme` media query for automatic light/dark switching: Rejected because the spec explicitly calls for a dark theme only, not a toggle
- Using `filter: invert(1)` on the body: Rejected because it inverts images too and provides no fine-grained control over accent colors

## Research Topic 4: Title "Py" Markup Approach

**Decision**: Hardcode the title in the template with a `<span class="py-accent">` wrapping the "Py" letters.

**Rationale**: The site name "Intervista Pythonista" is fixed and will not change. Hardcoding the title with inline `<span>` markup is the simplest approach that satisfies the requirement of CSS-only color treatment. The `<span>` is semantically neutral and does not affect accessibility — screen readers will read the full title naturally.

**Alternatives considered**:
- Using `page.title` with a Pelican/Jinja2 filter to inject the span: Over-engineered for a fixed site name; adds complexity with no benefit
- Using CSS `::first-letter` or text coloring pseudo-elements: CSS cannot target arbitrary letter ranges within a word; a markup element is required
- Using JavaScript to find and wrap "Py": Violates Principle I (Extreme Minimalism — zero JS)
