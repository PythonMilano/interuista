SITENAME = "Intervista Pythonista"
SITEURL = ""

PATH = "content"
TIMEZONE = "Europe/Rome"
DEFAULT_LANG = "it"

THEME = "theme/flavor"

# URL settings for pages
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"

# Disable article-related pages (this is a pages-only site)
INDEX_SAVE_AS = ""
ARTICLE_SAVE_AS = ""
ARTICLE_LANG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
TAG_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAGS_SAVE_AS = ""

# Disable feeds during development
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
    },
}

RELATIVE_URLS = True
