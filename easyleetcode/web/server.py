#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @File    : server.py
import os
from fastapi import APIRouter

from fastapi import Request
from easyleetcode.config import templates
import easyleetcode.web.code_util as code_util
from easyleetcode.web.Items import Item
import easyleetcode.web.utils as utils
import easyleetcode.config as config

router = APIRouter()

code_name_map, code_name_list = utils.load_data()


def remove_name(name):
    global code_name_map, code_name_list
    del code_name_map[name]

    ci = None
    for ci in code_name_list:
        if ci[0] == name:
            break
    if ci is not None:
        code_name_list.remove(ci)


@router.get('/view')
async def view(request: Request):
    count_day = utils.get_file_txt_count(config.count_day)
    count_view_code = utils.get_file_txt_count(config.count_view_code)
    data = {
        'all_num': len(code_name_list),
        'count_day': count_day,
        'count_view_code': count_view_code,
        'code_name_list': code_name_list
    }
    return templates.TemplateResponse("code_list.html", {"request": request, "data": data, "message": "Leetcode List"})


@router.get('/filter_view/{keyword}')
async def view(request: Request, keyword: str = 'L'):
    count_day = utils.get_file_txt_count(config.count_day)
    count_view_code = utils.get_file_txt_count(config.count_view_code)
    f_code_name_list = [ni for ni in code_name_list if keyword in ni[1]]
    data = {
        'all_num': len(code_name_list),
        'count_day': count_day,
        'count_view_code': count_view_code,
        'code_name_list': f_code_name_list
    }
    return templates.TemplateResponse("code_list.html", {"request": request, "data": data, "message": "Leetcode List"})


@router.get('/code/{name}')
async def view_code(request: Request, name: str = '001_Two_Sum'):
    global code_name_map
    if name not in code_name_map:
        return templates.TemplateResponse("index.html", {"request": request, "message": 'Easy Leetcode'})
    # 代码路径
    code_path = code_name_map[name][1]
    # 代码markdwon路径
    code_md_path = code_name_map[name][2]
    code_str = code_util.get_file_read(code_path)
    code_md_str = code_util.get_file_read(code_md_path)
    data = {
        'code_str': code_str,
        'code_md_str': code_md_str,
        'name': name,
    }
    # every times view code,path config.count_view_code 's count +=1 (view code count log)
    utils.add_file_txt_count(config.count_view_code)
    return templates.TemplateResponse("python_index.html", {"request": request, "data": data})


@router.put('/save')
async def save(item: Item):
    global code_name_map
    name = item.name
    # python code
    code_str = item.code_str
    # python code's Markdown note
    code_md_str = item.code_md_str
    # python code's path
    code_path = code_name_map[name][1]
    # python code's Markdown note 's path
    code_md_path = code_name_map[name][2]
    if code_str is not None:
        with open(code_path, 'w', encoding='utf-8') as of:
            of.write(code_str)
    if code_md_str is not None:
        with open(code_md_path, 'w', encoding='utf-8') as of:
            of.write(code_md_str)
    return {
        'status': 'success',
        'name': name
    }


@router.put('/delete')
async def delete(item: Item):
    global code_name_map
    name = None
    try:
        name = item.name
        # python code's path
        code_path = code_name_map[name][1]
        # python code's Markdown note 's path
        code_md_path = code_name_map[name][2]
        remove_name(name)
        utils.del_file(code_path)
        utils.del_file(code_md_path)
        return {
            'status': 'success',
            'name': name
        }
    except Exception as e:
        print(e)
    return {
        'status': 'error',
        'name': name
    }


@router.put('/add')
async def add_file(item: Item):
    global code_name_map, code_name_list
    name = item.name.strip().replace(' ', '_')
    code_str = item.code_str
    code_md_str = item.code_md_str
    if name not in code_name_map:
        code_path = os.path.join(code_name_map['root'][1], name + '.py')
        code_md_path = os.path.join(code_name_map['root'][2], name + '.md')
    else:
        return {
            'status': 'error:file exist !',
            'name': name
        }

    if code_str is None:
        code_str = "print('" + name + "')"
    if code_str is not None:
        with open(code_path, 'w', encoding='utf-8') as of:
            of.write(code_str)
    if code_md_str is None:
        code_md_str = "# " + name
    if code_md_str is not None:
        with open(code_md_path, 'w', encoding='utf-8') as of:
            of.write(code_md_str)

    code_name_map, code_name_list = utils.load_data()
    return {
        'status': 'success',
        'name': name
    }


@router.get('/md/{name}')
async def view_md(request: Request, name: str = '001_Two_Sum'):
    global code_name_map
    if name not in code_name_map:
        return templates.TemplateResponse("index.html", {"request": request, "message": 'Easy Leetcode'})
    # 代码markdwon路径
    code_md_path = code_name_map[name][2]
    code_md_str = code_util.get_file_read(code_md_path)
    data = {
        'code_md_str': code_md_str,
        'name': name,
    }
    return templates.TemplateResponse("md.html", {"request": request, "data": data, "message": name})
