AUTHOR = 'The Unbound Nomad'
SITENAME = 'The Unbound Nomad'
SITEURL = 'https://www.unboundnomad.com'
PATH = 'content'
OUTPUT_PATH = 'output'
STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/favicon.png': {'path': 'favicon.png'},
}

# Flex supports loading a custom CSS file via CUSTOM_CSS
CUSTOM_CSS = 'static/custom.css'  # :contentReference[oaicite:1]{index=1}

# --- Template overrides (so we can replace only the footer without forking Flex) ---
THEME_TEMPLATES_OVERRIDES = ['theme_overrides/templates']  # :contentReference[oaicite:2]{index=2}

# --- Choose footer style: "biker" or "premium" ---
FOOTER_STYLE = 'biker'
FOOTER_TAGLINE = "All-inclusive motorcycle adventures. You show up. We handle the rest."
FOOTER_CTA_TEXT = "Book a Ride"
FOOTER_CTA_URL = "/pages/contact.html"   # change if your contact URL differs

DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'
#THEME = '..\\Flex'
THEME = 'D:\\Dropbox\\projects\\code\\github\\pelican-themes\\Flex'
SITELOGO = '/images/logo.png'
FAVICON = 'favicon.png'
# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

############
# Added 1/24
ARTICLE_PATHS = ['articles']
articles_page = 'articles_page'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_ORDER_BY = 'reversed-date'
PAGE_PATHS = ['pages']
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGES_ORDER_BY = 'date'
#DIRECT_TEMPLATES = ['index']
#PAGINATED_TEMPLATES = ['index']
#TEMPLATE_PAGES = {'index': 'blog/index.html'}
# END ADD
############
# Blogroll
#LINKS = (
#    ("Indian Motorcycles", "https://www.indianmotorcycle.com"),
#    ("Lexin Moto", "https://lexin-moto.com"),
#    ("Shoei Helmets", "https://shoei-helmets.com/"),
#)

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/profile.php?id=61554818544356'),
          ('youtube', 'https://www.youtube.com/channel/UCvAAwLc11f4EUAAhSuLK5pw'),
#          ('twitter (@unbound_nomad)', 'https://x.com/unbound_nomad/'),
          ('instagram (@unbound_nomad)', 'https://www.instagram.com/unbound_nomad/'),)
#          ('TikTok', 'https://www.tiktok.com/@unbound_nomad'),)


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#DISPLAY_CATEGORIES_ON_MENU = False
#DISPLAY_PAGES_ON_MENU = False
#MENUITEMS = (
#    ('Home', '/'),
#    ('Blog', '/blog/index.html'),
#)

from datetime import date
CURRENT_YEAR = str(date.today().year)
