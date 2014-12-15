#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-15 22:09:37
# Filename        : app.py
# Description     : 

from tornado.web import Application
from admin import AdminHandler
from admin import LoginHandler, LogoutHandler
from admin import ConfigureHandler, BloggerHandler, ConfblogHandler
from admin import WriteHandler, ListSortHandler
from admin import UploadHandler
from admin.do import get_uuid
from admin import ListPageHandler
from files import FilesHandler
from page.index import IndexHandler
from page.sort import SortPageHandler 
from page.search import SearchHandler
from page.page import PageHandler
from os import path

from module import AdminHeaderModule, HeaderModule, FooterModule, SiderHandlerModule
class TuxpyApplication(Application):
    def __init__(self):
        handlers = [
                (r'/', IndexHandler),
                (r'/tuxpy/index.py', AdminHandler),
                (r'/tuxpy/?', AdminHandler),
                (r'/tuxpy/login.py', LoginHandler),
                (r'/tuxpy/logout.py', LogoutHandler),
                (r'/tuxpy/configure.py', ConfigureHandler),
                (r'/tuxpy/confblog.py', ConfblogHandler),
                (r'/tuxpy/blogger.py', BloggerHandler),
                (r'/tuxpy/write.py', WriteHandler),
                (r'/tuxpy/listpage.py', ListPageHandler),
                (r'/tuxpy/listsort.py', ListSortHandler),
                (r'/tuxpy/upload.py', UploadHandler),
                (r'/files/(.+)', FilesHandler),
                (r'/sort/(.+)?', SortPageHandler),
                (r'/page/(.+)?', PageHandler),
                (r'/search/(.+)?', SearchHandler),
                ]
        settings = {
                'template_path': path.join(path.dirname(__file__),
                    'templates'),
                'static_path': path.join(path.dirname(__file__),
                    'static'),
                'cookie_secret':get_uuid(),
                'login_url':'/tuxpy/login.py',
                'ui_modules': {'admin_header':AdminHeaderModule,
                    'header':HeaderModule, 'footer': FooterModule,
                    'right':SiderHandlerModule},
                'debug':True,
                }
        Application.__init__(self, handlers, **settings)

