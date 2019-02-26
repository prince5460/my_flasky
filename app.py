# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-2-26 下午2:36
@Desc :
'''
from flask import Flask, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello,Flask!</h1>"


# 动态路由
@app.route('/user/<name>')
def user(name):
    return "<h1>Hello,{}</h1>".format(name)


'''
，获取应用上下文的方法是在应用实例上调用 app.app_context()
'''


# 响应
# @app.route('/')
# def index():
#     return '<h1>Bad Request</h1>', 400
#
#
# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response
