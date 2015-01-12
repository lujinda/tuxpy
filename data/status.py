#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-12 11:25:09
# Filename        : data/status.py
# Description     : 

from tornado import web

ALL_STATUS = ['view_count']

class StatusHandler(web.RequestHandler):
    @web.asynchronous
    def get(self):
        status = self.get_query_argument('status', '')
        if status not in ALL_STATUS:
            return
        self.application.notification.register(status, self.send_status)

    def send_status(self, data):
        self.write(data)
        self.finish()

