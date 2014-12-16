#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-16 15:44:04
# Filename        : page/tag.py
# Description     : 
from .do import PageListHandler, get_tag_b_uuid

class TagHandler(PageListHandler):
    def get(self, tag):
        blog_uuid_list = get_tag_b_uuid(tag)
        self.render_page(condition = {"uuid":{"$in": blog_uuid_list}},
                title = tag)

