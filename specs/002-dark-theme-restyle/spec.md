# Feature Specification: Dark Theme Restyle

**Feature Branch**: `002-dark-theme-restyle`
**Created**: 2026-03-11
**Status**: Draft
**Input**: User description: "Restyle the site with a dark theme inspired by the podcast logo. Black background, white text, yellow 'Py' highlight in the title, no logo image on site. Maintain accessibility and Lighthouse 100/100 scores."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Dark Theme Visual Identity (Priority: P1)

A visitor opens the Intervista Pythonista website and immediately sees a dark-themed page with a black background and white text. The site title "Intervista Pythonista" appears on a single line, with the letters "Py" in "Pythonista" displayed in a warm golden yellow color that matches the podcast logo, and the rest of the title in white. The overall impression is clean, minimal, and professional — consistent with the podcast's brand identity.

**Why this priority**: The dark theme and yellow "Py" accent are the core visual identity change. Without this, the feature has no value.

**Independent Test**: Can be fully tested by loading the homepage and verifying the background is black, text is white, the title renders on one line, and the "Py" letters are yellow. Delivers the primary brand-aligned visual identity.

**Acceptance Scenarios**:

1. **Given** a visitor on any modern browser, **When** they load the homepage, **Then** the page background is black and all body text is white or light-colored
2. **Given** the page title "Intervista Pythonista", **When** displayed in the header, **Then** it appears on a single line with "Py" in "Pythonista" colored in golden yellow and all other title characters in white
3. **Given** the yellow color used for "Py", **When** compared to the podcast logo, **Then** the yellow matches or closely complements the logo's golden yellow
4. **Given** the current site, **When** restyled, **Then** the logo image is NOT displayed anywhere on the page

---

### User Story 2 - Readable Content on Dark Background (Priority: P2)

A visitor reads the podcast description and host bios on the dark-themed page. All text content — body paragraphs, host names, host bios, section headings — is clearly legible against the black background. Links stand out from surrounding text and are visually distinct in both default and hover/focus states.

**Why this priority**: Content readability is essential for the site to serve its purpose. A dark theme that makes content hard to read defeats the goal.

**Independent Test**: Can be tested by reading all page content and verifying text contrast, link visibility, and heading hierarchy are all clear and comfortable to read.

**Acceptance Scenarios**:

1. **Given** the dark-themed page, **When** a visitor reads body text, **Then** the text has sufficient contrast against the background for comfortable reading
2. **Given** links on the page, **When** displayed, **Then** they are visually distinguishable from surrounding text and have clear hover/focus states
3. **Given** section headings (h2), **When** displayed, **Then** they are clearly distinguishable from body text and maintain visual hierarchy
4. **Given** host profile sections, **When** displayed, **Then** host names, bios, and photos are clearly visible and well-formatted on the dark background

---

### User Story 3 - Accessibility and Performance Preservation (Priority: P3)

The restyled site maintains its existing high accessibility and performance standards. All text meets WCAG AA contrast requirements against the dark background. The site continues to achieve Lighthouse scores of 100/100 across all categories. No new accessibility issues are introduced by the dark theme.

**Why this priority**: The site currently achieves perfect Lighthouse scores. The restyle must not degrade these standards, but achieving the visual goals (P1, P2) takes precedence in implementation order.

**Independent Test**: Can be tested by running Lighthouse audit on the restyled site and verifying all scores remain at 100/100, and by checking WCAG AA contrast ratios for all text/background combinations.

**Acceptance Scenarios**:

1. **Given** all text/background color combinations on the restyled site, **When** checked with a contrast ratio tool, **Then** all combinations meet WCAG AA minimum contrast ratio (4.5:1 for normal text, 3:1 for large text)
2. **Given** the restyled site, **When** audited with Lighthouse, **Then** all four categories (Performance, Accessibility, Best Practices, SEO) score 100/100
3. **Given** interactive elements (links, buttons), **When** navigated with keyboard, **Then** focus indicators are clearly visible against the dark background

---

### Edge Cases

- What happens when the title wraps on very narrow screens (below 320px)? The title should still display the correct yellow "Py" coloring even if it wraps to a second line.
- How do the podcast and contact link buttons (bordered style) appear on the dark background? Borders and SVG icons must remain visible.
- How do host profile photos (circular, 120x120) appear on the dark background? The circular crop should remain clear.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The page background MUST be black
- **FR-002**: Body text MUST be white or near-white for readability on the dark background
- **FR-003**: The site title "Intervista Pythonista" MUST appear on a single line in the header
- **FR-004**: The letters "Py" in "Pythonista" MUST be colored in a golden yellow that matches or complements the podcast logo's yellow
- **FR-005**: The yellow "Py" treatment MUST be implemented purely with CSS, using a span or similar markup element in the template for the "Py" portion
- **FR-006**: The rest of the title text (all characters except "Py") MUST be white
- **FR-007**: The podcast logo image MUST NOT appear on the site
- **FR-008**: All links MUST be visually distinct from surrounding text on the dark background and MUST have visible hover and focus states
- **FR-009**: Section headings, host bios, footer text, and all other content MUST be restyled for readability on the dark background
- **FR-010**: Bordered link buttons (podcast and contact sections) MUST have visible borders and icons on the dark background
- **FR-011**: All text/background color combinations MUST meet WCAG AA contrast requirements (4.5:1 for normal text, 3:1 for large text)
- **FR-012**: The site MUST maintain Lighthouse 100/100 scores across all categories after restyling
- **FR-013**: The overall visual feel MUST remain clean and minimal, consistent with the existing site structure

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of site text meets WCAG AA contrast ratio requirements against the dark background
- **SC-002**: Lighthouse audit scores remain at 100/100 in all four categories (Performance, Accessibility, Best Practices, SEO)
- **SC-003**: The title "Intervista Pythonista" renders on a single line on viewports 375px wide and above
- **SC-004**: The "Py" yellow color has a delta-E (color difference) of less than 10 compared to the logo's yellow, confirming visual consistency with the podcast brand

## Assumptions

- The golden yellow in the podcast logo is approximately #E8A317 (warm golden yellow). The exact hex value will be confirmed during implementation by sampling the logo.
- "Single line" for the title refers to standard mobile and desktop viewports (375px and above). On extremely narrow viewports below 375px, wrapping is acceptable.
- The existing CSS custom properties (CSS variables) approach will be leveraged for the dark theme, making the change primarily a matter of updating variable values.
- No new fonts, images, or external resources are needed — the restyle is purely CSS and minor template markup changes.
- The site does not currently display the logo image, so FR-007 is a constraint to ensure it is not added, not a removal.
