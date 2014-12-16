#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-16 18:56:46
# Filename        : admin/listtag.py
# Description     : 

from base import BaseHandler
from .do import get_tag_list
from tornado.web import authenticated

class ListTagHandler(BaseHandler):
    @authenticated
    def get(self):
        tag_list = get_tag_list()
        self.render('tuxpy/tag.html', tag_list = tag_list)

