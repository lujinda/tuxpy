#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-15 20:34:19
# Filename        : admin/base.py
# Description     : 
from tornado.web import RequestHandler
from do import check_user_pass, enc_password
from data import db


class BaseHandler(RequestHandler):
    def is_create_default(self):
        if not db.users.count():
            db.users.insert(dict(
                username="tuxpy",
                password=enc_password('tuxpy'),
                uid=0,

                )) 

    def get_current_user(self):
        self.is_create_default() # 如果数据库中没有用户名，则会自己建立一个
        username = self.get_secure_cookie('username')
        password = self.get_secure_cookie('password')
        if username and password and check_user_pass(username,
                password):
            return username
        return None
