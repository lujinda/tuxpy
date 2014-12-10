#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-04 21:02:02
# Filename        : admin/login.py
# Description     : 
from tornado.web import RequestHandler
from .base import enc_password

class LoginHandler(RequestHandler):
    def get(self):
        if self.get_argument('next', ''):
            err_mess = '请输入正确的用户名密码'
        else:
            err_mess=''
        self.render('tuxpy/login.html', err_mess = err_mess)

    def post(self):
        next_url = self.get_argument('next', '/tuxpy')
        self.set_secure_cookie("username", self.get_argument("login_user"))
        self.set_secure_cookie("password", enc_password(self.get_argument("login_pass")))
        self.redirect(next_url)

