#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-07 15:21:40
# Filename        : data/db.py
# Description     : 
import pymongo
from config import db_config, cfg_file

cfg = db_config()
db = pymongo.Connection(cfg.get('mongodb', 'host'),
        int(cfg.get('mongodb', 'port'))).tuxpy

