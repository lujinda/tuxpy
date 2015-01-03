#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-04 00:17:59
# Filename        : sider/__init__.py
# Description     : 把每个启动的插件都加载进来，每个插件都是一个class，都需要有一个make_html，插件源文件的__all__需要指定
import glob
import os

__all__ = []

for plug in glob.glob('sider/*.py'):
    plug = os.path.basename(plug)
    if plug.startswith('_'):
        continue
    plug = plug[:-3]
    p = __import__('sider.%s' % plug, fromlist = [plug, ]) # 相当于from aaa import bbb
    __all__.extend(p.__all__) # 每一个插件的__all__属性都会被设置只允许插件元素
    exec('from sider.%s import *' % plug ) # 动态载入

