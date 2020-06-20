#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @File    : utils.py
import os
from easyleetcode.config import root_path


def add_file_txt_count(file_path):
    count = 0
    try:
        with open(file_path, encoding='utf-8', mode='r') as f:
            txt = f.read()
            txt = txt.replace('\n', '').strip()
            count = int(txt)
    except:
        count = 0
    count += 1
    with open(file_path, encoding='utf-8', mode='w') as f:
        f.write(str(count))


def get_file_txt_count(file_path):
    count = 0
    try:
        with open(file_path, encoding='utf-8', mode='r') as f:
            txt = f.read()
            txt = txt.replace('\n', '').strip()
            count = int(txt)
    except:
        count = 0
    return count


def del_file(path):
    os.remove(path)


def get_all_code_name_map(code_dir=os.path.join(root_path, 'leetcodes'),
                          code_md_dir=os.path.join(root_path, 'leetcodes_md')):
    code_name_map = {}
    code_name_map['root'] = ('root', code_dir, code_md_dir)
    for fname in os.listdir(code_dir):
        if '.py' not in fname:
            continue
        name = fname[:-3]
        path = os.path.join(code_dir, fname)
        md_path = os.path.join(code_md_dir, name + '.md')
        code_name_map[name] = (name, path, md_path)
    return code_name_map


def load_data():
    code_name_map = get_all_code_name_map()

    code_name_list = []
    for i, name in enumerate(sorted(code_name_map)):
        name, _, _ = code_name_map[name]
        if name == 'root':
            continue
        title = ' '.join(name.split('_'))
        code_name_list.append([name, str(i + 1) + ' : ' + title])
    code_name_list = sorted(code_name_list)
    return code_name_map, code_name_list
