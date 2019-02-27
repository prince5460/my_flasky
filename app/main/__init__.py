# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-2-27 下午4:46
@Desc :
'''
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
