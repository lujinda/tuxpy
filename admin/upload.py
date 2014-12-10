#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-04 18:31:37
# Filename        : admin/upload.py
# Description     : 
from base import BaseHandler
from .do import upload_file
import json
import time

class UploadHandler(BaseHandler):
    def post(self):
        files_meta = self.request.files['imgFile']
        for file_data in files_meta:
            file_url = upload_file(file_data['filename'],
                    file_data['body'])
        if file_url:
            self.write(json.dumps(dict(
                error=0, url=file_url)))
        else:
            self.write(json.dumps(dict(
                error=1, message="上传出错了",
                )))

