#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-05 22:51:05
# Filename        : sider/blog_new.py
# Description     : 
from page.do import get_blog_list_new
SIDER_TITLE = '最新博客'
SIDER_NAME  = '_Sider_BlogListNew'

class _Sider_BlogListNew():
    def make_html(self):
        template = """ <div class="sider_title">最新的博客</div>
        <div class="sider_content">
            %s 
        </div>
            """
        return  template % (
            '\n'.join([ '<a href="/page/{uuid}">{title}</a><div style="display:none">{summary}</div>'.format(
                uuid = blog['uuid'],
                title = blog['title'].encode('utf-8'),
                summary = blog['summary'].encode('utf-8')) for blog in get_blog_list_new()])
                )
