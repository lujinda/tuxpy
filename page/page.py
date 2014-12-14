#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-15 00:08:38
# Filename        : page/page.py
# Description     : 
from admin.base import BaseHandler
from .do import get_blog
from .do import get_blog_list_new, get_blog_list_hot, get_blog_list_rand

class PageHandler(BaseHandler):
    def get(self, uuid):
        blog = get_blog(uuid)
        self.render('page.html', title=blog['title'], blog = blog,
                blog_list_new = get_blog_list_new(),
                blog_list_hot = get_blog_list_hot(),
                blog_list_rand = get_blog_list_rand())
        
