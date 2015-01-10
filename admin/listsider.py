#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-10 16:00:00
# Filename        : admin/listsider.py
# Description     : 
from .base import BaseHandler
from tornado.web import authenticated
from .do import get_sider_list, switch_sider, order_sider

class ListSiderHandler(BaseHandler):
    @authenticated
    def get(self, mess=''):
        if 'switch_display' in self.request.arguments:
            switch_sider(self.get_query_argument('switch_display', ''))
        self.render('tuxpy/sider.html', sider_list = get_sider_list())

    @authenticated
    def post(self):
        if 'order' in self.request.arguments:
            self.order_sider()
        self.get()

    def order_sider(self):
        for argument in self.request.arguments:
            if argument.startswith('sider_'):
                uuid = argument.split('_', 1)[1]
                sider_no = self.get_argument(argument)
                if not sider_no.isdigit():
                    continue
                order_sider(uuid, sider_no)

