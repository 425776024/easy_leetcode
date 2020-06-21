#!/usr/bin/env python
# -*- coding:utf-8 -*-


from setuptools import setup, find_packages

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setup(
    name="easyleetcode",
    version="2.0.4",
    keywords=("easyleetcode", "bilibili", 'youtube', 'leetcode'),
    description="Leetcode easy study use Python on web",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT Licence",
    url="https://github.com/425776024/easy_leetcode",
    author="Jiang.XinFa",
    author_email="425776024@qq.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['uvicorn', 'fastapi', 'pydantic', 'aiofiles', 'jinja2']
)
