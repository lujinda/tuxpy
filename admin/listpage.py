#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-24 22:38:29
# Filename        : admin/listpage.py
# Description     : 
from base import BaseHandler
from tornado.web import authenticated
from page.do import get_blog_list, get_blog_count, get_tag_b_uuid
from .do import del_blog
from .do import get_sort_list, move_blog, top_blog, notop_blog, get_tag_list

class ListPageHandler(BaseHandler):
    #@authenticated
    def get(self, mess=''):
        page_navi_sort, filter_id, condition = self.make_title_condition() # filter_id 用来获取筛选的那个分类的id值，根据这个id值分析出它的父节点，并把它显示
        self.list_blog(condition = condition, mess = mess, filter_id = filter_id, page_navi_sort =  page_navi_sort) # page_navi_sort 主要用来避免分类过滤时的选页

    def make_title_condition(self):
        print dir(self)
        if 'now_sort' in self.request.arguments:
            sort_uuid = self.get_query_argument('now_sort', '').replace(' ', '+')
            return "&now_sort=%s" %(sort_uuid,), '_' + sort_uuid, {'sort': sort_uuid}

        if 'now_tag' in self.request.arguments:
            tag_name = self.get_query_argument('now_tag', '')
            blog_uuid_list = get_tag_b_uuid(tag_name)
            return "&now_tag=%s" % (tag_name, ), '_' + tag_name, {'uuid': {"$in": blog_uuid_list}}

        return '', None, {}

    def list_blog(self, mess, condition = {}, filter_id='', page_navi_sort=''):
        now_page = int(self.get_argument('page', 1))
        max_page = (int(get_blog_count(condition)) - 1 ) / 15
        blog_list = get_blog_list(condition,
                now_page=now_page, page_limit = 15)
        self.render('tuxpy/page.html', blog_list = blog_list,
                sort_list = get_sort_list(), mess = mess,filter_id = filter_id,
                now_page = now_page, max_page = max_page, tag_list = get_tag_list(),
                page_navi_sort = page_navi_sort)

#    @authenticated
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
