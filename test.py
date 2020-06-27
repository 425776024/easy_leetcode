#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @File    : test.py

from easyleetcode import run
run(host="127.0.0.1", port=8080, py_cmd_path='python3 ')

import os
from shutil import copyfile
from easyleetcode.web.code_util import get_file_read

# rt = 'easyleetcode/leetcodes/'
# rt_md = 'easyleetcode/leetcodes_md/'
# for p in os.listdir(rt):
#     p_code = os.path.join(rt, p)
#     if 'SYL' in p or 'Leetcode' in p:
#         continue
#     if 'SYL' in p:
#         np = 'SYL_' + p.replace('SYL_', '')
#     else:
#         np = p.replace('L_', 'Leetcode_')
#     r_p_code = os.path.join(rt, np)
#     os.rename(p_code, r_p_code)
#
#     p_md = os.path.join(rt_md, p.replace('.py', '.md'))
#     r_p_md = os.path.join(rt_md, np.replace('.py', '.md'))
#     os.rename(p_md, r_p_md)
