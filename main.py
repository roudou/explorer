#!/usr/bin/python -O
# -*- coding: utf-8 -*-
#

import streaming 
from bottle import route, run, request, response, redirect, template, static_file



@route('/')
def index():
  return template('index.tpl')

run(host='192.168.0.246', port='80', debug=True)
