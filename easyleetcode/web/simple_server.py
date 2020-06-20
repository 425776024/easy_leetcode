#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @File    : simple_server.py

from fastapi import APIRouter
from fastapi import Request
from easyleetcode.config import templates

simple_router = APIRouter()


@simple_router.get('/')
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": 'Easy Leetcode'})


@simple_router.get('/help')
async def help(request: Request):
    return templates.TemplateResponse("help.html", {"request": request, "message": 'Easy Leetcode'})


@simple_router.get('/about')
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "message": 'Easy Leetcode'})

@simple_router.get('/addview')
async def index(request: Request):
    return templates.TemplateResponse("add_file.html", {"request": request, "message": 'Easy Leetcode'})
