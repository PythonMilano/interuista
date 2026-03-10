# Data Model: Static Site Homepage

This is a static site with no database. The "data model" describes the
content structure as it exists in Markdown files and Pelican configuration.

## Page (content/pages/home.md)

The home page is a Pelican page with the following metadata fields:

| Field     | Type   | Description                                    |
|-----------|--------|------------------------------------------------|
| Title     | string | "Intervista Pythonista"                        |
| Slug      | string | Page slug (empty for root)                     |
| URL       | string | "" (site root)                                 |
| Save_as   | string | "index.html"                                   |
| Lang      | string | "it"                                           |
| Status    | string | "published"                                    |

The page body (Markdown content) contains:
- Podcast description paragraph
- Host profiles section
- Platform links section
- Community links section

## Host Profile (inline in page content)

| Field       | Type   | Description                              |
|-------------|--------|------------------------------------------|
| Name        | string | Full name of the host                    |
| Description | string | Brief bio (1-2 sentences)                |

**Instances**:
- Marco Santoni: data science/AI background
- Cesare Placanica: telecom/coding/DevOps, Python Milano veteran

## Platform Link (inline in page content or template)

| Field | Type   | Description                              |
|-------|--------|------------------------------------------|
| Name  | string | Platform display name                    |
| URL   | string | External URL to the podcast on platform  |
| Icon  | SVG    | Inline SVG icon for the platform         |

**Instances**: Spotify, Apple Podcasts, YouTube, RSS

## Community Link (inline in page content or template)

| Field | Type   | Description                              |
|-------|--------|------------------------------------------|
| Name  | string | Channel display name                     |
| URL   | string | External URL to the community channel    |
| Icon  | SVG    | Inline SVG icon for the channel          |

**Instances**: LinkedIn, Slack, Email
