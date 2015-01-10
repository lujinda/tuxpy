#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-10 14:39:12
# Filename        : sider/blog_search.py
# Description     : 

SIDER_TITLE = '搜索博客!'
SIDER_NAME = '_Sider_BlogSearch'
SIDER_DESCRIPTION = '搜索博客'

class _Sider_BlogSearch:
    def make_html(self):
        return  """
        <div class="sider_title">%s</div>
        <div class="sider_content">
            <form method="POST" action="/search/">
                <input name="keyword" autocomplete="off" id="search_input" />
            </form>
        </div>
        """ % (SIDER_TITLE, )

