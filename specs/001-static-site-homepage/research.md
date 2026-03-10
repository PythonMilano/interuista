# Research: Static Site Homepage

## Pelican Theme Structure

**Decision**: Create a minimal custom theme named "flavor" following
Pelican's standard theme structure.

**Rationale**: Pelican themes require a specific directory layout
(`static/`, `templates/`). A custom theme gives full control over HTML
output (critical for Lighthouse 100) and avoids inheriting bloat from
existing themes. The name "flavor" is short and distinctive.

**Alternatives considered**:
- **Built-in "simple" theme**: Too bare, would need heavy overrides anyway.
- **Existing community themes (Flex, Elegant)**: All include JavaScript
  and CSS that would violate Principle I and IV. Stripping them down is
  more work than starting fresh.

## Pelican Page vs Article

**Decision**: Use Pelican's "pages" content type (not "articles") for the
home page.

**Rationale**: Pages are for static content that doesn't have a date or
belong to a feed. The home page is not a blog post — it's a permanent
landing page. Pelican pages live in `content/pages/` and use metadata to
control URL routing. Setting `URL: ""` and `SAVE_AS: "index.html"` makes
the page the site root.

**Alternatives considered**:
- **INDEX_SAVE_AS with articles**: Would require generating an article
  index, which is unnecessary for a single-page site.
- **Direct HTML template**: Would violate Principle III (content in Markdown).

## Icons for Platform/Community Links

**Decision**: Use inline SVG icons embedded directly in the Jinja2 template.

**Rationale**: Inline SVG avoids external HTTP requests (Principle V
performance), avoids third-party resources (FR-010), and produces crisp
icons at any resolution. SVG icons for Spotify, Apple Podcasts, YouTube,
RSS, LinkedIn, Slack, and email are widely available under permissive
licenses (e.g., Simple Icons, MIT/CC0).

**Alternatives considered**:
- **Font Awesome / icon font**: Adds JS or large CSS payload. Violates
  Principle I and IV.
- **PNG/WebP icon images**: Adds HTTP requests and file weight. Worse
  quality at high DPI.
- **External SVG files**: Adds HTTP requests per icon. Inline is simpler
  for ~7 small icons.

## CSS Architecture

**Decision**: Single `style.css` file using CSS custom properties for
theming. Mobile-first responsive design with minimal media queries.

**Rationale**: One file means one HTTP request. CSS custom properties
provide a clean theming mechanism without preprocessors (Principle IV).
Mobile-first ensures the base styles work on small viewports, and a
single `min-width` breakpoint handles desktop layout.

**Alternatives considered**:
- **Multiple CSS files by concern**: Adds HTTP requests without benefit
  for a single-page site.
- **Inlining CSS in HTML**: Would work for performance but makes the
  theme harder to maintain. A single small CSS file with proper
  caching is equivalent.

## Deployment Pipeline

**Decision**: GitHub Actions workflow that installs Python + Pelican,
runs `pelican content -s publishconf.py`, and deploys the `output/`
directory.

**Rationale**: GitHub Actions is free for public repos and directly
integrates with GitHub Pages. The same `output/` directory can be
deployed to Netlify or Cloudflare Pages by changing the deploy step
(Principle VI portability).

**Alternatives considered**:
- **Netlify build**: Vendor-specific `netlify.toml`. Would work but
  locks the CI to one platform.
- **Manual deployment**: Error-prone, not reproducible.

## Site Language

**Decision**: Italian (`lang="it"` in HTML). All content in Italian.

**Rationale**: The original intervistapythonista.com is entirely in
Italian. The podcast targets Italian Python developers. Setting the
correct `lang` attribute is required for Lighthouse accessibility score.
