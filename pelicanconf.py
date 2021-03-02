#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cyril'
SITENAME = 'Work Blog'
SITEURL = 'https://cyrilb38.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = "pelican-themes/medius"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MEDIUS_CATEGORIES = {
    'Data insight': {
        'description': 'All about messing around with data to learn something new.',
        'logo': 'https://raw.githubusercontent.com/cyrilb38/work-blog/master/ressources/category/data%20insight.jpg',
        'thumbnail': 'https://raw.githubusercontent.com/cyrilb38/work-blog/master/ressources/category/data%20insight.jpg'
    }
}