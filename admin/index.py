#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-02 22:27:14
# Filename        : admin/index.py
# Description     : 
from tornado.web import RequestHandler, authenticated
from .base import BaseHandler
from data.do import get_server_info, get_site_options

class AdminHandler(BaseHandler):
    @authenticated
    def get(self):
        site_options = get_site_options()
        server_info = get_server_info()
        self.render('tuxpy/index.html', site_options = site_options, server_info = server_info)

