#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-04 00:23:04
# Filename        : blog_search.py
# Description     : 

__all__ = ['_Sider_BlogSearch']

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

