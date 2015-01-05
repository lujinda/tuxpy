#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-05 21:12:32
# Filename        : sider/blog_search.py
# Description     : 

SIDER_TITLE = '搜索博客'
SIDER_NAME = '_Sider_BlogSearch'

class _Sider_BlogSearch:
    def make_html(self):
        return  """
        <div class="sider_title">搜索博客</div>
        <div class="sider_content">
            <form method="POST" action="/search/">
                <input name="keyword" id="search_input" />
            </form>
        </div>
        """

