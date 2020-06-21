#!/usr/bin/env python
# -*- coding: utf-8 -*-


import uvicorn
from fastapi import FastAPI

import easyleetcode.config as config
import easyleetcode.web.server as a_server
import easyleetcode.web.simple_server as a_simple_server
import easyleetcode.web.utils as utils

app = FastAPI()
app.mount("/static", config.statics, name="static")
app.mount("/python_static", config.python_statics, name="python_files")
app.mount("/Skulpt", config.python_rstatics, name="pythonr_static")

app.include_router(a_server.router)
app.include_router(a_simple_server.simple_router)


def run(host="127.0.0.1", port=8080):
    '''

    :param host: host
    :param port: port
    :return:
    '''
    print('your host is :', host)
    print('your port is :', port)

    config.templates.env.variable_start_string = '{['
    config.templates.env.variable_end_string = ']}'

    # every times running,path config.count_day 's count +=1 (running count log)
    utils.add_file_txt_count(config.count_day)
    print('_____running:____')
    print('please web browser', 'http://%s:%s' % (str(host), str(port)))
    uvicorn.run(app=app, host=host, port=port, log_level="error")
    # uvicorn.run(app=app, host=host, port=port)


if __name__ == '__main__':
    run()
