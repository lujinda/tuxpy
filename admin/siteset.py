#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-07 22:32:19
# Filename        : admin/siteset.py
# Description     : 
from tornado.web import  authenticated
from data.do import get_site_options, set_site_blog_options, get_blog_options 
from base import BaseHandler
from .do import change_user_pass, check_user_pass, enc_password

MESS_HTML = 'tuxpy/mess.html'

class ConfigureHandler(BaseHandler):
    #@authenticated
    def get(self):
        self.render('tuxpy/configure.html', site_options=get_site_options())

    #@authenticated
    def post(self):
        for key, value in self.request.arguments.items():
            set_site_blog_options('site', key, *value)
        self.render(MESS_HTML, mess="保存成功")

class ConfblogHandler(BaseHandler):
    def get(self):
        self.render('tuxpy/confblog.html', blog_options = get_blog_options())
    
    def post(self):
        page_limit = self.get_argument('page_limit', '')
        start_n = self.get_argument('start_n', '')
        if len(filter(lambda x:x.isdigit() and int(x) > 0, [page_limit, start_n])) != 2:
            self.render(MESS_HTML, mess = '修改失败，请确定内容无误')
        else:
            for key, value in self.request.arguments.items():
                set_site_blog_options('blog', key, *value)
            self.render(MESS_HTML, mess="保存成功")


class BloggerHandler(BaseHandler):
    @authenticated
    def get(self):
        self.render('tuxpy/blogger.html', username=self.current_user)

    #@authenticated
    def post(self):
        
        if len(self.get_argument('pass_new'))< 6:
            mess = '新密码长度必须大于5位'
        else:
            user_old = self.get_argument('user_old')
            user_new = self.get_argument('user_new')
            pass_old = enc_password(self.get_argument('pass_old'))
            pass_new = enc_password(self.get_argument('pass_new'))

            if not check_user_pass(user_old, pass_old):
                mess = '用户名密码不匹配，无权修改'
            else:
                change_user_pass(user_new, pass_new)
                mess = '修改成功'

        self.render(MESS_HTML, mess = mess)


class BloggerHandler(BaseHandler):
    @authenticated
    def get(self):
        self.render('tuxpy/blogger.html', username=self.current_user)

    #@authenticated
    def post(self):
        
        if len(self.get_argument('pass_new'))< 6:
            mess = '新密码长度必须大于5位'
        else:
            user_old = self.get_argument('user_old')
            user_new = self.get_argument('user_new')
            pass_old = enc_password(self.get_argument('pass_old'))
            pass_new = enc_password(self.get_argument('pass_new'))

            if not check_user_pass(user_old, pass_old):
                mess = '用户名密码不匹配，无权修改'
            else:
                change_user_pass(user_new, pass_new)
                mess = '修改成功'

        self.render(MESS_HTML, mess = mess)

