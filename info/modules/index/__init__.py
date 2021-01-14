# -*- coding: utf-8 -*-
# author:yang  time:19-8-7 上午10:24


from flask import Blueprint


# 创建蓝图对象
index_blu = Blueprint('index', __name__)

from . import views