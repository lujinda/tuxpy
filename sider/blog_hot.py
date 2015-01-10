#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-10 14:28:45
# Filename        : sider/blog_hot.py
# Description     : 

from page.do import get_blog_list_hot

SIDER_TITLE = '最热博客'
SIDER_DESCRIPTION = '显示查看数最高的博客'

SIDER_NAME = '_Sider_BlogListHot'
class _Sider_BlogListHot():
    def make_html(self):
        template = """ <div class="sider_title">%s</div>
        <div class="sider_content">
            %s 
        </div>
            """
        return  template % (SIDER_TITLE,
            '\n'.join([ '<a href="/page/{uuid}">{title}</a><div style="display:none">{summary}</div>'.format(
                uuid = blog['uuid'],
                title = blog['title'].encode('utf-8'),
                summary = blog['summary'].encode('utf-8')) for blog in get_blog_list_hot()])
                )
