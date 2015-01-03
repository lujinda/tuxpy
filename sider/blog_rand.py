#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-04 00:19:20
# Filename        : blog_rand.py
# Description     : 
from page.do import get_blog_list_rand
__all__ = ['_Sider_BlogListRand']

class _Sider_BlogListRand():
    def make_html(self):
        template = """ <div class="sider_title">随机博客</div>
        <div class="sider_content">
            %s 
        </div>
            """
        return  template % (
            '\n'.join([ '<a href="/page/{uuid}">{title}</a><div style="display:none">{summary}</div>'.format(
                uuid = blog['uuid'],
                title = blog['title'].encode('utf-8'),
                summary = blog['summary'].encode('utf-8')) for blog in get_blog_list_rand()])
                )
