#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-10 13:09:18
# Filename        : admin/listpage.py
# Description     : 
from base import BaseHandler
from .do import get_blog_list

class ListPageHandler(BaseHandler):
    def get(self):
        blog_list = get_blog_list()
        self.render('tuxpy/page.html', blog_list = blog_list, mess = '')


    def post(self):
        print self.request.arguments
