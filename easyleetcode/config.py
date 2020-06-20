#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @File    : config.py
import os
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

root_path = os.path.dirname(__file__)

web_path = os.path.join(root_path, 'web')
logs_path = os.path.join(root_path, 'logs')
s_path = os.path.join(web_path, 'static')
statics = StaticFiles(directory=s_path)

#  python ide
python_path = os.path.join(web_path, 'codemirror_python')
python_statics = StaticFiles(directory=python_path)

#  python js running
python_rpath = os.path.join(web_path, 'Skulpt')
python_rstatics = StaticFiles(directory=python_rpath)
# python_rtemplates = Jinja2Templates(directory=python_rpath)

# other
templates = Jinja2Templates(directory=os.path.join(web_path, 'templates'))



python_path = 'python3 '
count_day = os.path.join(logs_path, 'count_day.txt')
count_view_code = os.path.join(logs_path, 'count_view_code.txt')
