#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-10 14:35:04
# Filename        : sider/__init__.py
# Description     : 把每个启动的插件都加载进来，每个插件都是一个class，都需要有一个make_html，插件源文件的__all__需要指定
import glob
import os
from config.do import update_sider

__all__ = []
all_sider = {}

for plug in glob.glob(os.path.dirname(os.path.abspath(__file__)) + '/*.py'):
    plug = os.path.basename(plug)
    if plug.startswith('_'):
        continue
    plug = plug[:-3]
    p = __import__('sider.%s' % plug, fromlist = [plug, ]) # 相当于from aaa import bbb
    sider_title = p.SIDER_TITLE
    sider_name = p.SIDER_NAME
    sider_description = p.SIDER_DESCRIPTION
    all_sider[sider_name] = [sider_title, sider_description]
    __all__.append(sider_name)
    exec('from sider.%s import %s' % (plug, sider_name) ) # 动态载入

update_sider(all_sider) # 把sider的信息记录到数据库

