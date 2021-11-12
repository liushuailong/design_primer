# -*- coding: utf-8 -*-
# @Author: liushuailong
# @Create:  2021/11/12 下午1:55
# @describe: 
from sanic import Blueprint

static = Blueprint("primer_static", url_prefix="/static")
