#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-09 12:43:12
# Filename        : listsort.py
# Description     : 

from tornado.web import RequestHandler
from .do import add_sort, del_sort, set_sort, get_sort_list

class ListSortHandler(RequestHandler):
    def get(self, mess=''):
        for key, value in self.request.arguments.items(): # 把一些预操作完成一下
            try:
                func = getattr(self, key)
                mess = func(value[0])
            except:
                pass
            else:
                break
        sort_list = get_sort_list()
        self.render("tuxpy/sort.html", sort_list = sort_list, mess = mess)

    def del_sort(self, uuid):
        return del_sort(uuid)


    def post(self):
        if 'set_name' in self.request.arguments:
            mess = set_sort(self.get_argument('set_name'),
                    self.get_argument('value'), 'name')
        elif 'set_alias' in self.request.arguments:
            mess = set_sort(self.get_argument('set_alias'),
                    self.get_argument('value'), 'alias')
        else:
            new_sort_name = self.get_argument('name')
            new_sort_alias = self.get_argument('alias')
            mess = add_sort(new_sort_name, new_sort_alias)

        self.get(mess)

