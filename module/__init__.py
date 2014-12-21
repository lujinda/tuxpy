#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-21 22:57:49
# Filename        : module/__init__.py
# Description     : 
from tornado import web
from admin.base import BaseHandler
from admin.do import get_nav_list
from data.do import get_site_options, get_page_view
from page.do import get_blog_list_new, get_blog_list_hot, get_blog_list_rand

class HeaderModule(web.UIModule):
    def render(self, render_file):
        site_options = get_site_options()
        nav_list = get_nav_list()
        return self.render_string(render_file, site_options = site_options,
                nav_list = nav_list)

class AdminHeaderModule(HeaderModule):
    pass

class FooterModule(web.UIModule):
    def render(self, render_file):
        return self.render_string(render_file, view = get_page_view(), site_options = get_site_options())

class SiderHandlerModule(web.UIModule):
    def render(self, render_file):
        return self.render_string(render_file,
                blog_list_new = get_blog_list_new(), 
                blog_list_hot = get_blog_list_hot(),
                blog_list_rand = get_blog_list_rand())

