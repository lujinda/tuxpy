#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-01 00:06:15
# Filename        : admin/logout.py
# Description     : 
from tornado.web import RequestHandler
class LogoutHandler(RequestHandler):
    def get(self):
        self.clear_cookie('username')
        self.clear_cookie('password')
        self.redirect('/')

