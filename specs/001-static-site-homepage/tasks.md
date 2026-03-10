# Tasks: Static Site Homepage

**Input**: Design documents from `/specs/001-static-site-homepage/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md

**Tests**: Not explicitly requested in the feature specification. No test tasks generated.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization, Pelican configuration, and custom theme skeleton

- [x] T001 Update pyproject.toml to add Pelican and Markdown dependencies in pyproject.toml
- [x] T002 Create .gitignore with output/ directory and Python/Pelican standard ignores in .gitignore
- [x] T003 [P] Create Pelican configuration with site metadata (SITENAME="Intervista Pythonista", DEFAULT_LANG="it", TIMEZONE, PATH="content", PAGE_URL="{slug}", PAGE_SAVE_AS="{slug}.html", INDEX_SAVE_AS="", FEED_ALL_ATOM=None, THEME="theme/flavor") in pelicanconf.py
- [x] T004 [P] Create production configuration overlay importing pelicanconf and setting SITEURL, RELATIVE_URLS=False in publishconf.py
- [x] T005 [P] Create custom theme directory structure: theme/flavor/static/css/ and theme/flavor/templates/
- [x] T006 Remove scaffold main.py (no longer needed for static site)

**Checkpoint**: Pelican project skeleton ready. Running `pelican content` should succeed (with empty output).

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Base Jinja2 template with semantic HTML structure and CSS foundation that all user stories depend on

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 Create base page template with semantic HTML5 structure (<!DOCTYPE html>, html lang="it", head with meta charset/viewport/description/OG tags, header, main, footer, nav landmarks) in theme/flavor/templates/page.html
- [x] T008 Create single CSS file with CSS custom properties for colors/fonts/spacing, base reset, typography, mobile-first responsive layout (min-width breakpoint for desktop), and semantic element styling in theme/flavor/static/css/style.css

**Checkpoint**: Foundation ready. `pelican content` generates a valid HTML page with proper semantic structure and responsive CSS. No content yet.

---

## Phase 3: User Story 1 - Discover the Podcast (Priority: P1) MVP

**Goal**: Visitor sees podcast title, description, host profiles, and platform links on the home page

**Independent Test**: Open http://localhost:8000 and verify the title "Intervista Pythonista", podcast description, both host profiles, and all four platform links (Spotify, Apple Podcasts, YouTube, RSS) are visible and clickable

### Implementation for User Story 1

- [x] T009 [US1] Create home page Markdown file with Pelican metadata (Title: Intervista Pythonista, URL: "", Save_as: index.html, Status: published, Lang: it) and podcast description paragraph in Italian in content/pages/home.md
- [x] T010 [US1] Add host profiles section to home page content with Marco Santoni (data science/AI) and Cesare Placanica (telecom/coding/DevOps, Python Milano veteran) in content/pages/home.md
- [x] T011 [US1] Add inline SVG icons for podcast platforms (Spotify, Apple Podcasts, YouTube, RSS) to the page template with links opening in new tab (target="_blank" rel="noopener") in theme/flavor/templates/page.html
- [x] T012 [US1] Add podcast platform links section styling (icon grid/row layout, hover states, accessible focus indicators) to theme/flavor/static/css/style.css

**Checkpoint**: User Story 1 fully functional. Home page displays all podcast discovery content. Platform links work.

---

## Phase 4: User Story 2 - Connect with the Community (Priority: P2)

**Goal**: Visitor finds community engagement links (LinkedIn, Slack, email) on the home page

**Independent Test**: Verify LinkedIn, Slack, and email links are visible on the page and navigate to correct destinations in new tabs

### Implementation for User Story 2

- [x] T013 [US2] Add community links section (LinkedIn Python Milano page, Slack workspace, email contact) to home page content in content/pages/home.md
- [x] T014 [US2] Add inline SVG icons for community channels (LinkedIn, Slack, email/envelope) to the page template in theme/flavor/templates/page.html
- [x] T015 [US2] Add community links section styling (consistent with platform links layout) to theme/flavor/static/css/style.css

**Checkpoint**: User Stories 1 AND 2 both work. All external links on the page function correctly.

---

## Phase 5: User Story 3 - Fast, Accessible Site (Priority: P3)

**Goal**: Site achieves 100/100 Lighthouse scores across all four categories and is fully accessible

**Independent Test**: Run Lighthouse CLI against `pelican content -s publishconf.py` output and verify 100/100 on Performance, Accessibility, Best Practices, SEO

### Implementation for User Story 3

- [x] T016 [US3] Add complete SEO meta tags (title, description, canonical URL, Open Graph og:title/og:description/og:type/og:url/og:locale) to head section in theme/flavor/templates/page.html
- [x] T017 [US3] Add ARIA landmarks and roles, ensure all images/icons have alt text or aria-hidden="true" for decorative SVGs, verify heading hierarchy (single h1) in theme/flavor/templates/page.html
- [x] T018 [US3] Audit and optimize CSS for minimal payload: remove unused rules, verify total size < 10 KB, ensure sufficient color contrast ratios (WCAG AA) in theme/flavor/static/css/style.css
- [x] T019 [US3] Verify all external links have target="_blank" rel="noopener", verify no JavaScript is included anywhere, verify no third-party resources are loaded in theme/flavor/templates/page.html

**Checkpoint**: All user stories functional. Lighthouse scores 100/100 across all categories.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Deployment pipeline, documentation, and final validation

- [x] T020 [P] Create GitHub Actions workflow: checkout, setup Python 3.13, install dependencies, run `pelican content -s publishconf.py`, deploy output/ to GitHub Pages in .github/workflows/deploy.yml
- [x] T021 [P] Update README.md with project description, local development instructions (pelican content --listen --autoreload), and deployment info in README.md
- [x] T022 Verify total page weight (HTML + CSS) is under 100 KB by running production build and checking output file sizes
- [x] T023 Run final Lighthouse audit against production build and fix any remaining issues

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - US1 (Phase 3): Can start after Phase 2
  - US2 (Phase 4): Can start after Phase 2, but logically follows US1 (shares content/pages/home.md and template)
  - US3 (Phase 5): Should follow US1 and US2 (audits the complete page)
- **Polish (Phase 6)**: Depends on all user stories being complete

### Within Each User Story

- Content (Markdown) before template updates
- Template updates before CSS styling
- Story complete before moving to next priority

### Parallel Opportunities

- T003, T004, T005 can run in parallel (different files, no dependencies)
- T020 and T021 can run in parallel (different files)

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (template + CSS skeleton)
3. Complete Phase 3: User Story 1 (podcast discovery)
4. **STOP and VALIDATE**: Open localhost:8000 and verify content
5. Deploy/demo if ready

### Incremental Delivery

1. Setup + Foundational -> Pelican skeleton ready
2. Add User Story 1 -> Podcast content visible (MVP!)
3. Add User Story 2 -> Community links added
4. Add User Story 3 -> Lighthouse 100/100 verified
5. Polish -> CI/CD pipeline, README, final audit

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- US2 and US3 both modify files touched by US1 (home.md, page.html, style.css) so they should run sequentially
- Commit after each task or logical group
- No JavaScript anywhere — verify at every checkpoint
- Total file count is very small (~8 source files) so parallelism is limited
