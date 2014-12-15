#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-15 20:31:51
# Filename        : run.py
# Description     : 
from tornado import httpserver, ioloop, web
from tornado import options
from tornado.options import options, define
define('port', default=1234, type=int, help="listen port")

from app import TuxpyApplication

if __name__ == "__main__":
    options.parse_command_line()
    http_server = httpserver.HTTPServer(TuxpyApplication())
    http_server.listen(1234)
    ioloop.IOLoop.instance().start()

