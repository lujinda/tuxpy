#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-09 12:14:09
# Filename        : admin/write.py
# Description     : 
from tornado.web import  authenticated
from .base import BaseHandler
from .do import get_sort_list, write_blog
from data.do import get_blog_options
from page.do import get_blog
import time
from config import config

class WriteHandler(BaseHandler):
    @authenticated
    def get(self):
        uuid = self.get_argument('uuid', '')
        blog = get_blog(uuid, is_edit = True)
        print blog
        self.render('tuxpy/write.html', sort_list = get_sort_list(), blog = blog
                )

    @authenticated
    def post(self):
        title = self.get_argument('title')
        page_content = self.get_argument('page_content')
        summary = self.get_argument('summary', '')
        is_top = self.get_argument('is_top', '')

        start_n = get_blog_options()['start_n']
        if start_n.isdigit() and int(start_n) > 0 and summary == '':
            summary = page_content[:int(start_n)]
        tag = (self.get_argument('tag') or []) and self.get_argument('tag').split(';')
        sort = self.get_argument('sort', '')
        author = self.current_user
        uuid = self.get_argument('uuid', '')
        mess = write_blog(title=title, page_content=page_content, summary=summary, 
                tag=tag, sort=sort, author=author, uuid=uuid, is_top = is_top
                )

