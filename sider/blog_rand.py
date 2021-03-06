#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-11 12:05:14
# Filename        : sider/blog_rand.py
# Description     : 
from page.do import get_blog_list_rand

SIDER_TITLE = '随机博客'
SIDER_NAME = '_Sider_BlogListRand'
SIDER_DESCRIPTION = '随机显示博客'

class _Sider_BlogListRand():
    def make_html(self):
        return (SIDER_TITLE, '\n'.join([ '<a href="/page/{uuid}">{title}</a><div style="display:none">{summary}</div>'.format(
                uuid = blog['uuid'],
                title = blog['title'].encode('utf-8'),
                summary = blog['summary'].encode('utf-8')) for blog in get_blog_list_rand()])
                )
