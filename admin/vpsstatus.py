#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-11 15:37:21
# Filename        : admin/vpsstatus.py
# Description     : 
from tornado import web
import json

class VpsStatus():
    def memory_stat(self):
        mem = {}
        f = open('/proc/meminfo')
        for line in f:
            name = line.split(':')[0]
            var = line.split(':')[1].split()[0]
            mem[name] = long(var) * 1024.0
        mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
        f.close()
        return mem['MemTotal'], mem['MemUsed']

class VpsStatusHandler(web.RequestHandler):
    @web.asynchronous
    def get(self):
        status = VpsStatus()
        response = json.dumps({
            'mem': status.memory_stat(),
            })
        self.write(response)
        self.finish()
