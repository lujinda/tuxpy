#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-12 10:29:25
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
from admin import ListTagHandler
from admin import ListNavHandler
from admin import ListSiderHandler
from files import FilesHandler
from page.index import IndexHandler
from page.sort import SortPageHandler 
from page.tag import TagHandler
from page.search import SearchHandler
from page.page import PageHandler
from data.status import StatusHandler
from data.do import Notification
from os import path

from module import AdminHeaderModule, HeaderModule, FooterModule, SiderHandlerModule
class TuxpyApplication(Application):
    notification = Notification()
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
                (r'/tuxpy/listtag.py', ListTagHandler),
                (r'/tuxpy/listnav.py', ListNavHandler),
                (r'/tuxpy/listsider.py', ListSiderHandler),
                (r'/files/(.+)', FilesHandler),
                (r'/sort/(.+)?', SortPageHandler),
                (r'/page/(.+)?', PageHandler),
                (r'/search/(.+)?', SearchHandler),
                (r'/status.py', StatusHandler),
                (r'/tag/(.+)?', TagHandler), # 这里的url参数是tag名字，不是uuid 其他的都是uuid
                ]
        settings = {
                'template_path': path.join(path.dirname(__file__),
                    'templates'),
                'static_path': path.join(path.dirname(__file__),
                    'static'),
                'cookie_secret':get_uuid(),
                'login_url':'/tuxpy/login.py',
                'ui_modules': {'admin_header':AdminHeaderModule, # 后台header部分模块
                    'header':HeaderModule, 'footer': FooterModule,
                    'right':SiderHandlerModule}, # 网站右侧栏，打算做成自定义式
                'debug':True,
                }
        Application.__init__(self, handlers, **settings)

