#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-21 23:27:47
# Filename        : admin/listnav.py
# Description     : 
from .base import BaseHandler
from .do import write_nav, get_nav_list, get_sort_list, del_nav, switch_nav, order_nav
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

    @authenticated
    def get(self, mess=''):
        if 'del' in self.request.arguments:
            del_nav(self.get_query_argument('del', ''))
        if 'switch_display' in self.request.arguments:
            switch_nav(self.get_query_argument('switch_display', ''))

        nav_list = get_nav_list()
        self.render('tuxpy/nav.html', nav_list = nav_list, sort_list = get_sort_list(), mess=mess)

    @authenticated
    def post(self):
        if 'order' in self.request.arguments:
            mess = self.order_nav()
            self.get(mess = '最新顺序已保存')
            return 
        No_name_url_list = self.get_No_name_url_list()
        if not No_name_url_list: # 如果有内容为空，则这会返回空列表
            self.get(mess = '请保证不要有空内容')
            return 
        for No, name, url in No_name_url_list:
            mess = write_nav(int(No), name, url)

        self.get(mess = mess)

    def order_nav(self):
        for argument in self.request.arguments: # 修改序列传入的数据形式为：nav_uuid No
            if argument.startswith('nav_'):
                uuid = argument.split('_', 1)[1]
                No = self.get_argument(argument)
                if not No.isdigit():
                    continue
                order_nav(uuid, No)

