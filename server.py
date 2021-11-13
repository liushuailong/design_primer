# -*- coding: utf-8 -*-
# @Author: liushuailong
# @Create:  2021/11/12 上午11:31
# @describe: Primer design tools
from pathlib import Path
from sanic import Sanic
from sanic import Blueprint
import multiprocessing
from settings import BASE_DIR, STATIC_DIR, TEMPLATES_DIR, MEDIA_DIR
from sanic.response import json
from sanic.response import html
from sqlalchemy import select
from sqlalchemy.orm import selectinload

app = Sanic(__name__)
workers = multiprocessing.cpu_count()
app.static("/static", STATIC_DIR)
app.static("/media", MEDIA_DIR)

from sqlalchemy.ext.asyncio import create_async_engine

# bind = create_async_engine("mysql+aiomysql://root:root@localhost/test", echo=True)

def rander(template_path):
    with open(template_path, "r") as f:
        response = f.read()
    return html(response)

@app.route("/")
async def dashboard(request):
    return rander(TEMPLATES_DIR / "dashboard.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, workers=workers)

