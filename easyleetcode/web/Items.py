#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @File    : Items.py

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    code_str: str = None
    code_md_str: str = None
