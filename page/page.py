#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-15 21:26:04
# Filename        : page/page.py
# Description     : 
from admin.base import BaseHandler
from .do import get_blog

class PageHandler(BaseHandler):
    def get(self, uuid):
        blog = get_blog(uuid)
        self.render('page.html', title=blog['title'], blog = blog,)
            
        
