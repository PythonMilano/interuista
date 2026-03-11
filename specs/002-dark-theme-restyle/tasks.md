# Tasks: Dark Theme Restyle

**Input**: Design documents from `/specs/002-dark-theme-restyle/`
**Prerequisites**: plan.md, spec.md, research.md

**Tests**: No automated tests. Verification is manual (Lighthouse audit, visual inspection, contrast ratio check).

**Organization**: Tasks follow user story priority order. This is a small CSS/template change touching 2 files.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: User Story 1 — Dark Theme Visual Identity (Priority: P1) MVP

**Goal**: Black background, white text, golden yellow "Py" accent in the title

**Independent Test**: Load the homepage and verify black background, white text, title on one line with yellow "Py"

### Implementation for User Story 1

- [x] T001 [P] [US1] Update the `<h1>` in `theme/flavor/templates/page.html` to hardcode the title as `Intervista <span class="py-accent">Py</span>thonista` (replacing `{{ page.title }}`)
- [x] T002 [P] [US1] Update CSS custom properties in `theme/flavor/static/css/style.css` `:root` block: change `--color-bg` to `#000000`, `--color-text` to `#f0f0f0`, `--color-heading` to `#ffffff`, add `--color-py: #e8a317`. Add `.py-accent { color: var(--color-py); }` rule

**Checkpoint**: Title displays with yellow "Py" on black background

---

## Phase 2: User Story 2 — Readable Content on Dark Background (Priority: P2)

**Goal**: All page content (links, buttons, borders, muted text, host bios) is clearly readable on the dark background

**Independent Test**: Read all page content and verify link visibility, heading hierarchy, and button/border visibility

### Implementation for User Story 2

- [x] T003 [US2] Update remaining CSS custom properties in `theme/flavor/static/css/style.css` `:root` block: change `--color-accent` to `#6ea8fe`, `--color-accent-hover` to `#9ec5fe`, `--color-muted` to `#aaaaaa`, `--color-border` to `#333333`

**Checkpoint**: All content is legible — links are light blue, borders and buttons visible, footer text readable

---

## Phase 3: User Story 3 — Accessibility and Performance Verification (Priority: P3)

**Goal**: Confirm WCAG AA compliance and Lighthouse 100/100

**Independent Test**: Run Lighthouse audit, check contrast ratios for all color combinations

### Verification for User Story 3

- [x] T004 [US3] Build the site with `pelican content` and visually inspect the output in a browser. Verify: (1) all text/background combinations have sufficient contrast, (2) focus indicators are visible on dark background, (3) SVG icons in link buttons are visible against dark background. Fix `a:focus-visible` outline color in `theme/flavor/static/css/style.css` if needed (current outline uses `--color-accent` which will be light blue — should be fine)
- [x] T005 [US3] Run Lighthouse audit on the built site (all 4 categories). Verify scores remain 100/100. Document any issues and fix if needed

**Checkpoint**: All accessibility and performance criteria met

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (US1)**: No dependencies — start immediately
- **Phase 2 (US2)**: Can run in parallel with Phase 1 (T003 modifies same file as T002 but different variables — execute T002 before T003 to avoid conflicts)
- **Phase 3 (US3)**: Depends on Phase 1 and Phase 2 completion (needs final colors to verify)

### Parallel Opportunities

- T001 and T002 can run in parallel (different files: `page.html` vs `style.css`)
- T004 and T005 are sequential (fix issues before final Lighthouse audit)

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete T001 + T002 in parallel → dark theme with yellow "Py" working
2. **STOP and VALIDATE**: Visual check of the homepage
3. Proceed to T003 for full content readability

### Full Delivery

1. T001 + T002 (parallel) → Core dark theme
2. T003 → Content readability polish
3. T004 → Accessibility verification and fixes
4. T005 → Final Lighthouse audit confirmation

---

## Notes

- Total tasks: 5
- Files modified: 2 (`theme/flavor/static/css/style.css`, `theme/flavor/templates/page.html`)
- No new files created
- No automated tests — manual verification only
- Commit after T001+T002+T003 (all CSS/template changes), then after T004 if fixes needed
