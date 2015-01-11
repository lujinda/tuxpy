#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-11 12:34:27
# Filename        : weibo.py
# Description     : 

SIDER_TITLE = '收听我!'
SIDER_NAME = '_Sider_Weibo'
SIDER_DESCRIPTION = '收听微博'

class _Sider_Weibo:
    def make_html(self):
        return  (SIDER_TITLE, """
        <iframe src="http://follow.v.t.qq.com/index.php?c=follow&a=quick&appkey=801353005&sign=86fe06da&v=2&name=q8886888&style=2&t=1420950853611&f=1" scrolling="auto" marginwidth="0" marginheight="0" allowtransparency="true" frameborder="0" height="38" width="191"></iframe>
        """ )

