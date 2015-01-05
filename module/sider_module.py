#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-05 20:32:32
# Filename        : module/sider_module.py
# Description     : 


# 插件全在sider目录下放着
from sider import *

# 生成右侧sider的主要html代码列表
def get_sider_content_list():
    sider_content_list = []
    for sider_obj_name in globals():
        if sider_obj_name.startswith('_Sider_'):
            sider_obj = globals()[sider_obj_name]
            sider_content_list.append(sider_obj().make_html())
        
    return sider_content_list
