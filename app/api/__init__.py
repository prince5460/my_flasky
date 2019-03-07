# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-3-6 下午3:36
@Desc :
'''
from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, posts, users, comments, errors
