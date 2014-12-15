#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-15 23:45:16
# Filename        : search.py
# Description     : 
from .do import PageListHandler, get_blog_list
class SearchHandler(PageListHandler):
    def get(self, keyword = ''):
        if (not self.get_argument('keyword', '')) and keyword:
            self.render_page(condition = {'title': {"$regex": r".*%s.*" % keyword}}, title = u'%s 搜索结果' % 
                keyword)
    def post(self, keyword = ''):
        keyword = self.get_argument('keyword', '')
        if keyword:
            self.redirect('/search/%s' % keyword)

