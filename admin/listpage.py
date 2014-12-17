#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-17 19:00:29
# Filename        : admin/listpage.py
# Description     : 
from base import BaseHandler
from page.do import get_blog_list, get_blog_count
from .do import del_blog
from .do import get_sort_list, move_blog, top_blog, notop_blog

class ListPageHandler(BaseHandler):
    def get(self, mess=''):
        self.list_blog(mess)

    def list_blog(self, mess, condition = {}):
        now_page = int(self.get_argument('page', 1))
        max_page = (int(get_blog_count(condition)) - 1 ) / 15
        blog_list = get_blog_list(condition,
                now_page=now_page, page_limit = 15)
        self.render('tuxpy/page.html', blog_list = blog_list,
                sort_list = get_sort_list(), mess = mess,
                now_page = now_page, max_page = max_page)


    def post(self):
        blog_uuid_list = self.get_arguments('blog_checkbox')
        for key, value in self.request.arguments.items(): # 假
            value = value[0]
            if value == '1':
                func = getattr(self, key + '_blog')
                try:
                    mess = func(blog_uuid_list)
                except:
                    mess = '操作失败，请重试'
                finally:
                    break
        self.get(mess)
        

    def del_blog(self, blog_uuid_list):
        for blog_uuid in blog_uuid_list:
            del_blog(blog_uuid)
        return '删除成功'

    def move_blog(self, blog_uuid_list):
        sort_uuid = self.get_argument('sort', '-1') # -1代表着没有选中任何

        if sort_uuid == '-1':
            return ''

        for blog_uuid in blog_uuid_list:
            move_blog(blog_uuid, sort_uuid)
        return '修改分类成功'
    
    def top_blog(self, blog_uuid_list):
        for blog_uuid in blog_uuid_list:
            top_blog(blog_uuid)

        return '置顶成功'

    def notop_blog(self, blog_uuid_list):
        for blog_uuid in blog_uuid_list:
            notop_blog(blog_uuid)

        return '取消置顶成功'
