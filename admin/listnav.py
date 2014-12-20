#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-21 00:12:56
# Filename        : admin/listnav.py
# Description     : 
from .base import BaseHandler
from .do import write_nav, get_nav_list, get_sort_list
from page.do import get_sort_name_alias
from tornado.web import authenticated

class ListNavHandler(BaseHandler):
    def get_No_name_url_list(self):
        No_name_url_list = []
        is_add_sort = int(self.get_query_argument('is_add_sort', 
            '0'))
        if not is_add_sort:
            No = self.get_argument('No', '0')
            name = self.get_argument('name')
            url = self.get_argument('url')
            if not (name and url):
                return []
            No_name_url_list = [[No, name, url]]
        else:
            sort_list = self.get_arguments('sort_list', [])
            for sort_uuid in sort_list:
                sort_uuid = sort_uuid.replace(' ', '+')
                sort_name, sort_alias = get_sort_name_alias(sort_uuid)
                No_name_url_list.append([
                    0, sort_name, u'/sort/%s' % sort_alias,
                    ])

        return No_name_url_list

    def get(self, mess=''):
        nav_list = get_nav_list()
        self.render('tuxpy/nav.html', nav_list = nav_list, sort_list = get_sort_list(), mess=mess)

    def post(self):
        No_name_url_list = self.get_No_name_url_list()
        if not No_name_url_list: # 如果有内容为空，则这会返回空列表
            self.get(mess = '请保证不要有空内容')
            return 
        for No, name, url in No_name_url_list:
            mess = write_nav(int(No), name, url)

        self.get(mess = mess)

