#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-07 15:12:24
# Filename        : config/config.py
# Description     : 
import ConfigParser
import os.path

cfg_file = os.path.join(os.path.dirname(__file__), 'define.cfg')

def db_config():
    cfg = ConfigParser.ConfigParser()
    for f in [cfg_file, ]:
        if os.path.exists(f):
            cfg.read(f)
            return cfg
