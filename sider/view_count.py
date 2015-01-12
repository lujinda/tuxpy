#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-12 11:40:32
# Filename        : sider/view_count.py
# Description     : 

from data.do import get_view_count
SIDER_TITLE = '访问量'
SIDER_NAME = '_Sider_ViewCount'
SIDER_DESCRIPTION = '界面共访问量'

class _Sider_ViewCount:
    def make_html(self):
        return  (SIDER_TITLE, """
        <div style="height:20px;background-color:#ccc;text-align:center;padding:6px;font-weight:bold;">
        <div id="view_count_div">%s</div>
        </div>
        <script>
        setTimeout(request_view_count, 100);
        function request_view_count(){
            $.getJSON('/status.py?status=view_count',{}, function(data, status, xhr){
                $('#view_count_div').fadeOut(500).html(data['view_count']).fadeIn(500);
            });
            setTimeout(request_view_count, 0);
        }
        </script>
        """ % (get_view_count(),) )

