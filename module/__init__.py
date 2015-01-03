#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-04 00:14:54
# Filename        : module/__init__.py
# Description     : 
from tornado import web
from admin.base import BaseHandler
from admin.do import get_nav_list
from data.do import get_site_options, get_page_view
from .sider_module import get_sider_content_list

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
        sider_content_list = get_sider_content_list()
        return self.render_string(render_file, 
                sider_content_list = sider_content_list)

