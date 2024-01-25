AUTHOR = 'The Unbound Nomad'
SITENAME = 'The Unbound Nomad'
SITEURL = 'http://unboundnomad.com'
PATH = 'content'
OUTPUT_PATH = 'output'
STATIC_PATHS = ['images']

DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'
#THEME = '..\\Flex'
THEME = 'D:\\Dropbox\\projects\\code\\github\\pelican-themes\\Flex'
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
ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_ORDER_BY = 'date'
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
LINKS = (
    ("Indian Motorcycles", "https://www.indianmotorcycle.com"),
    ("Lexin Moto", "https://lexin-moto.com"),
    ("Shoei Helmets", "https://shoei-helmets.com/"),
)

# Social widget
SOCIAL = (('youtube', 'https://www.youtube.com/channel/UCvAAwLc11f4EUAAhSuLK5pw'),
          ('facebook', 'https://www.facebook.com/profile.php?id=61554818544356'),
          ('twitter (@unbound_nomad)', 'https://x.com/unbound_nomad/'),
          ('instagram (@unbound_nomad)', 'https://www.instagram.com/unbound_nomad/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#DISPLAY_CATEGORIES_ON_MENU = False
#DISPLAY_PAGES_ON_MENU = False
#MENUITEMS = (
#    ('Home', '/'),
#    ('Blog', '/blog/index.html'),
#)