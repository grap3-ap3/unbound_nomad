AUTHOR = 'The Unbound Nomad'
SITENAME = 'The Unbound Nomad'
#SITEURL = "https://unboundnomad.com"
SITEURL = 'http://localhost:8000/blog'
PATH = "content"
STATIC_PATHS = ['images']

DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'
#THEME = '..\\Flex'
THEME = 'D:\\Dropbox\\projects\\code\\github\\pelican-themes\\Flex'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

############
# Added 1/24
ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_ORDER_BY = 'date'
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