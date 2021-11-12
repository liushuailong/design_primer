# -*- coding: utf-8 -*-
# @Author: liushuailong
# @Create:  2021/11/12 下午1:54
# @describe: 

from sanic import Blueprint
from .static import static

content = Blueprint.group(static, url_prefix="/static")