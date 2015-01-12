#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-12 11:17:54
# Filename        : sider/view_count.py
# Description     : 

from data.do import get_view_count
SIDER_TITLE = '访问量'
SIDER_NAME = '_Sider_ViewCount'
SIDER_DESCRIPTION = '界面共访问量'

class _Sider_ViewCount:
    def make_html(self):
        return  (SIDER_TITLE, """
        <span id="view_count_span">%s</span>
        <script>
        setTimeout(request_view_count, 100);
        function request_view_count(){
            $.getJSON('/status.py?status=view_count',{}, function(data, status, xhr){
                $('#view_count_span').html(data['view_count']);
            });
            setTimeout(request_view_count, 0);
        }
        </script>
        """ % (get_view_count(),) )

