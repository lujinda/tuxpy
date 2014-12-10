#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-07 22:15:57
# Filename        : page/sort.py
# Description     : 
from tornado.web import RequestHandler
from .do import  get_sort_uuid, get_sort_name_alias, PageListHandler
from data.do import get_site_options, get_blog_options


class SortPageHandler(PageListHandler):
    def get(self, sort_alias):
        uuid = get_sort_uuid(sort_alias)
        condition = {'sort': uuid}
        sort_name, sort_alias = get_sort_name_alias(uuid)
        title = "%s - %s" %(sort_name, get_site_options()['site_name'])
        self.render_page(condition = condition, title = title)

