#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-16 15:35:59
# Filename        : page.py
# Description     : 
from admin.base import BaseHandler
from .do import get_blog

class PageHandler(BaseHandler):
    def get(self, uuid):
        blog = get_blog(uuid)
        self.render('page.html', title=blog['title'], blog = blog,)
        
