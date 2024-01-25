#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# --------------------------------------
# Now compatible with Pelican 4.0.x!
# --------------------------------------

# Added by me
import time

AUTHOR = 'Unbound Nomad'
SITENAME = 'The Unbound Nomad'
SITEURL = 'https://unboundnomad.com'
TIMEZONE = 'America/New_York'
LOCALE = 'en_US'

FEED_DOMAIN = SITEURL

# Custom settings for my own site to use in the copyright notice.
CURRENT_YEAR = time.strftime("%Y")

THEME = '..\\Flex'

# Defines whether Pelican should use document-relative URLs or not. Only set this to True when developing/testing and only if you fully understand the effect it can have on links/feeds

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# The default date format you want to use.
DEFAULT_DATE_FORMAT = '%d %B %Y'

DEFAULT_LANG = 'en-us'

# Whether to display pages on the menu of the template. Templates may or may not honor this setting.
DISPLAY_PAGES_ON_MENU = True

# Whether to display categories on the menu of the template.
#This does nothing, so commenting it out. Possibly remove.
#DISPLAY_CATEGORIES_ON_MENU = True

# When you don’t specify a category in your post metadata, set this setting to True, and organize your articles in subfolders, the subfolder will become the category of your post. If set to False, DEFAULT_CATEGORY will be used as a fallback.
#USE_FOLDER_AS_CATEGORY = True

# The default metadata you want to use for all articles and pages.
#DEFAULT_METADATA = {
#  'description': 'Custom motorcycle adventure vacation packages.',
#  'status': 'draft'
#}

# Delete the output directory, and all of its contents, before generating new files. This can be useful in preventing older, unnecessary files from persisting in your output. However, this is a destructive setting and should be handled with extreme care.
DELETE_OUTPUT_DIRECTORY = True

# Path to content directory to be processed by Pelican.
PATH = 'posts'

# Name your content directory posts
ARTICLE_PATHS = ['articles']
ARTICLES_PAGE = 'articles_page'
# Exclude the pages directory from post processing - Not 100% sure this is necessary 
#ARTICLE_EXCLUDES = ['pages']

ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_ORDER_BY = 'date'

# List of templates that are used directly to render content. Typically direct templates are used to generate index pages for collections of content (e.g., tags and category index pages). If the tag and category collections are not needed, set DIRECT_TEMPLATES = ('index', 'archives')
DIRECT_TEMPLATES = ['index','archives']

# Provides the direct templates that should be paginated, and how many posst to display per page. If None, will fall back to the DEFAULT_PAGINATION value.
PAGINATED_TEMPLATES =  {'index': 6, 'archives': 9}

# Where to output the generated files.
OUTPUT_PATH = 'output'

# Auto generate slug from this source. Overridden by the Slug: property
SLUGIFY_SOURCE = 'slug'

# When creating a short summary of an article, this will be the default length (measured in words) of the text created. This only applies if your content does not otherwise specify a summary. Setting to None will cause the summary to be a copy of the original content.
SUMMARY_MAX_LENGTH = 65

# Articles per page
DEFAULT_PAGINATION = 9

# Leave no orphans
DEFAULT_ORPHANS = 0

ARCHIVES_SAVE_AS = 'blog/archives.html'

#PAGINATION_PATTERNS = (
#    (1, '{base_name}/', '{base_name}/index.html'),
#    (2, '{base_name}/{number}/','{base_name}/{number}/index.html'),
#)

# The static paths you want to have accessible on the output path “static”.
# By default, Pelican will copy the “images” folder to the output folder.
STATIC_PATHS = ['images', 'pages']
#STATIC_EXCLUDES = ['_scss']

# Can include multiple paths
#PLUGIN_PATHS = ['/path/to/pelican-plugins/']
#PLUGINS = ['simple_footnotes']

#CATEGORY_URL = 'category/{slug}/'
#CATEGORY_SAVE_AS = 'category/{slug}/index.html'

#TAG_URL = 'tag/{slug}/'
#TAG_SAVE_AS = 'tag/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# The URL to refer to an article draft.
#DRAFT_URL = 'blog/drafts/{slug}/'
#DRAFT_SAVE_AS = 'blog/drafts/{slug}/index.html'

# Build only modified content instead of all content
LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False

# Allow Markdown in the summary and title
FORMATTED_FIELDS = ['summary', 'title']

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'blog/feeds/all.rss.xml'
FEED_ALL_ATOM = 'blog/feeds/all.atom.xml'
FEED_MAX_ITEMS = 15

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

NEWEST_FIRST_ARCHIVES = True

# See https://pythonhosted.org/Markdown/reference.html#lazy_ol for lazy_ol settings
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
    'lazy_ol': False 
}

MENUITEMS = (
  ('Home','/'),
  ('About','/about/'),
  ('Contact','/contact/'),
  ('Blog','/blog/'),
)