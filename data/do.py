#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-12 11:26:40
# Filename        : data/do.py
# Description     : 
from .db import cfg, db
from data import db
import tornado

def get_server_info():
    import time
    import platform
    server_info = db.connection.server_info()
    server_info['server_time'] =  time.ctime()
    server_info['os'] = platform.platform()
    server_info['python'] = platform.python_version()
    server_info['time'] = time.ctime()
    server_info['tornado_version'] = tornado.version
    return server_info

def get_site_options():
    return db.config.site.find_one() or db.config.site.insert(dict(site_name = '疯狂的小企鹅',
                site_name_sub = '一只玩蟒蛇的企鹅',
                site_host = 'http://localhost:1234',
                email = 'q8886888@qq.com',
                ))

def get_blog_options():
    return db.config.blog.find_one() or db.config.blog.insert(dict(
        start_n = 200, page_limit = 5))

def set_site_blog_options(item, key, value):
    db.config[item].update({} ,{"$set":{key:value}}, multi=True)

def get_page_view():
    view = db.var.find_and_modify(query= {},
        update = {"$inc": {'view':1}},
        new = True)
    if not view:
        db.var.insert({'view': 1})
        view = 1
    else:
        view = view['view']
    return view

def get_view_count():
    return db.var.find_one()['view']

class Notification():
    callbacks = {}
    def register(self, status, func):
        self.callbacks.setdefault(status, []).append(func)

    def send(self, status, data):
        if status not in self.callbacks:
            return
        for c in self.callbacks[status]:
            c(data)
        self.callbacks[status] = []

