#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-11 12:04:35
# Filename        : module/sider_module.py
# Description     : 


# 插件全在sider目录下放着
from sider import *
from page.do import get_sider_list_show
template = """ <div class="sider_title">{0}</div>
        <div class="sider_content">
        {1}
        </div>
            """

# 生成右侧sider的主要html代码列表
def get_sider_content_list():
    sider_content_list = []
    for sider in get_sider_list_show():
        sider_obj = globals()[sider['sider_name']]()
        sider_content_list.append(template.format(*sider_obj.make_html()))
        
    return sider_content_list

