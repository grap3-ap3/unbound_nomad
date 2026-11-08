# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://unboundnomad.com"
RELATIVE_URLS = False

WITH_FUTURE_DATES = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""

# Cloudflare Web Analytics (cookie-free). Paste the beacon token from
# Cloudflare dashboard > Analytics & Logs > Web Analytics. Empty = analytics off.
# Only set here (not pelicanconf.py) so local test builds don't count as visits.
CLOUDFLARE_WEB_ANALYTICS_TOKEN = ""
