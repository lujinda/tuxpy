#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-12 11:26:18
# Filename        : page/do.py
# Description     : 
from data.db import db
from data.do import get_blog_options, get_page_view
from tornado.web import RequestHandler
import json


def get_sort_uuid(alias):
    sort = db.sort.find_one({'alias': alias})
    if sort:
        return sort['uuid']
    else:
        return ''
    
def get_sort_name_alias(uuid):
    sort = db.sort.find_one({'uuid':uuid})
    if sort:
        sort_name = sort['name']
        sort_alias = sort['alias']
    else:
        sort_name = u'未分类'
        sort_alias = ''

    return sort_name, sort_alias

def deal_blog(blog): # 处理一些博客的信息，比如说把时间做一个转换
    import time
    blog['date'] = time.strftime('%Y-%m-%d %H:%M:%S',
            time.localtime(float(blog['date'])))
    blog['sort_name'], blog['sort_alias'] = get_sort_name_alias(blog['sort'])
    if blog['sort_alias'] == '' and blog['sort']: # 当某个博客的分类被删除时，它所属于的分类就应该变成''
        db.blog.update({'uuid': blog['uuid']}, 
                {"$set":{'sort':''}})

    return blog

def get_blog_list(condition = {}, now_page = 1, page_limit = None): 
    now_page -= 1
    page_limit = page_limit or int(get_blog_options()['page_limit'])
    blog_list = [] 
    for blog in db.blog.find(condition).limit(page_limit).skip(page_limit * now_page).sort([('is_top', -1), ('date', -1)]):
        blog = deal_blog(blog)
        blog_list.append(blog)
        
    return blog_list


def get_blog_count(condition):
    return db.blog.find(condition).count()

class PageListHandler(RequestHandler): # 完成一些共用的列出日志的工作
    # 主要完成一些博客参数的获取，比如像当前怘，第页的限制, 和最大页
    def render_page(self, condition, title):
        now_page = int(self.get_argument('page', 1))
        page_limit = get_blog_options()['page_limit']
        max_page = (int(get_blog_count(condition)) -1 ) / int(page_limit) + 1
        blog_list = get_blog_list(condition, now_page = now_page)
        self.application.notification.send('view_count', {'view_count': get_page_view()})
        self.render('index.html', blog_list = blog_list,
                title = title, now_page = now_page, max_page = max_page, page_navi_sort = '')


def get_blog(uuid, is_edit = False):
    if is_edit:
        blog = db.blog.find_one({'uuid':uuid})
    else:
        blog = db.blog.find_and_modify({'uuid': uuid},
            update = {"$inc": {'view': 1}},
            new = True) 
    if not blog:
        return {}
    return deal_blog(blog)

def get_blog_list_new():
    return db.blog.find().sort([('date', -1)])[:5]

def get_blog_list_hot():
    return db.blog.find().sort([('view', -1)])[:5]

def get_blog_list_rand(): # 随机获取博客数，需要改进
    import random
    blog_list = list(db.blog.find())
    random.shuffle(blog_list)
    return blog_list[:5]

def get_tag_b_uuid(tag):
    return db.tag.find_one({'name': tag})['b_uuid']

def get_sider_list_show():
    return db.sider.find({'sider_show': 1}).sort([('sider_no', 1)])

