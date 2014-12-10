#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-04 19:40:02
# Filename        : files/files.py
# Description     : 
from tornado.web import RequestHandler
from data import db

class FilesHandler(RequestHandler):
    def get(self, url_filename):
        file_obj = db.files.find_one({'url_filename': url_filename})
        self.add_header('Content-Type','application/octet-stream')
        if not file_obj:
            self.write('')
        else:
            self.write(file_obj['body'])

