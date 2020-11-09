#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Greg Pawin'
SITENAME = "Greg's Blog"
SITEURL = 'https://gregpawin.com'
DEFAULT_CATEGORY = 'Posts'
PATH = 'content'
PLUGINS = ['pelican_dynamic']
TIMEZONE = 'America/Los_Angeles'
THEME = 'medius'
TYPOGRIFY = True
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('LinkedIn', 'https://www.linkedin.com/in/gregpawin'),
         ('GitHub | gregpawin', 'https://github.com/gregpawin'),
         ('Hack for LA', 'https://www.hackforla.org/'),
         ('North Valley Caring Services', 'https://www.nvcs.org'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/gregpawin'),
          ('GitHub | gregpawin', 'https://github.com/gregpawin'),
	  ('My Publications', 'https://scholar.google.com/citations?user=431TkhYAAAAJ&hl=en'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
