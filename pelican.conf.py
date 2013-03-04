#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Titus Brown"
SITENAME = u"Living in an Ivory Basement"
SITEURL = 'http://ivory.idyll.org/blog'
SITESUBTITLE = u"Stochastic thoughts on science, testing, and programming."

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG='en'

# Blogroll
LINKS =  (
#    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#    ('Python.org', 'http://python.org'),
#    ('Jinja2', 'http://jinja.pocoo.org'),
#    ('You can modify those links in your config file', '#')
         )

# Social widget
SOCIAL = (
#          ('You can add links in your config file', '#'),
         )

DEFAULT_PAGINATION = 7

FEED_MAX_ITEMS = 10

import os.path
THEME = os.path.join(os.getcwd(), 'ivory')

DISQUS_SITENAME='ivory-blog'

STATIC_PATHS = ["images"]
