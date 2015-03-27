# -*- coding: utf-8 -*-

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

#response.logo = A(B('web scraping example'), _class="brand",_href="/")
response.title = 'Example web scraping website'
#response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Richard Penman'
response.meta.keywords = 'web2py, python, web scraping'
response.meta.generator = 'Web2py Web Framework'

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Search'), False, URL('default', 'search'), [])
]

