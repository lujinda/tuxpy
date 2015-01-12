#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-12 11:25:49
# Filename        : page/index.py
# Description     : 
from tornado.web import RequestHandler
from .do import get_blog_list, PageListHandler
from data.do import get_site_options

class IndexHandler(PageListHandler):
    def get(self):
        self.render_page(condition = {}, title = get_site_options()['site_name'])

