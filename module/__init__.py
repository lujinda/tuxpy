#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-07 21:37:13
# Filename        : module/__init__.py
# Description     : 
from tornado import web
from data.do import get_site_options, get_page_view

class HeaderModule(web.UIModule):
    def render(self, render_file):
        site_options = get_site_options()
        return self.render_string(render_file, site_options = site_options)

class AdminHeaderModule(HeaderModule):
    pass

class FooterModule(web.UIModule):
    def render(self, render_file):
        return self.render_string(render_file, view = get_page_view(), site_options = get_site_options())
