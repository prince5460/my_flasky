# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 2019/2/27 下午10:31
@Desc :
'''
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
