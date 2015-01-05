#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-05 20:13:01
# Filename        : admin/listsider.py
# Description     : 
from .base import BaseHandler
from tornado.web import authenticated

class ListSiderHandler(BaseHandler):
    def get(self, mess=''):
        self.render('tuxpy/sider.html')

