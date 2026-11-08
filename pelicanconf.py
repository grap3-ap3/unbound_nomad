AUTHOR = 'The Unbound Nomad'
SITENAME = 'The Unbound Nomad'
SITEURL = 'https://www.unboundnomad.com'
PATH = 'content'
OUTPUT_PATH = 'output'
STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
# Everything in content/extra/root is copied to the site root as-is:
# CNAME (keeps the custom domain on GitHub Pages), robots.txt, favicon set, web manifest.
import os
_ROOT_EXTRAS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content', 'extra', 'root')
for _f in os.listdir(_ROOT_EXTRAS):
    EXTRA_PATH_METADATA['extra/root/' + _f] = {'path': _f}

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
SITELOGO = '/images/logo-web.jpg'
FAVICON = 'favicon.png'

# --- SEO / sharing ---
# Pages and articles can override these with `Meta_title:`, `Description:` and `Og_image:` metadata.
SITE_META_TITLE = 'The Unbound Nomad | Guided Motorcycle Rides & Trip Planning'
SITEDESCRIPTION = ("Guided motorcycle rides, concierge trip planning, and rider resources from "
                   "The Unbound Nomad. You show up. We handle the rest.")
OG_DEFAULT_IMAGE = 'images/og-default.jpg'
REL_CANONICAL = True
ROBOTS = 'index, follow'

# sitemap.xml is rendered from theme_overrides/templates/sitemap.html
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'
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
SOCIAL = (('facebook', 'https://www.facebook.com/theunboundnomad'),
          ('instagram', 'https://www.instagram.com/unbound_nomad/'),
          ('tiktok', 'https://www.tiktok.com/@unbound_nomad'),
          ('youtube', 'https://www.youtube.com/channel/UCSwqxCzCY1_h9rxFOdAtbBg'),)


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
MAIN_MENU = False

from datetime import date
CURRENT_YEAR = str(date.today().year)
