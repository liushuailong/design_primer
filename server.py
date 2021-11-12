# -*- coding: utf-8 -*-
# @Author: liushuailong
# @Create:  2021/11/12 上午11:31
# @describe:
from pathlib import Path
from sanic import Sanic
from sanic.response import json
from sanic.response import html
from sanic import Blueprint
import multiprocessing

BASE_DIR = Path(__file__).parent.resolve()
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
app = Sanic(__name__)
app.static("/static", STATIC_DIR)
workers = multiprocessing.cpu_count()

def rander(template_path):
    with open(template_path, "r") as f:
        response = f.read()
    return html(response)

@app.route("/")
async def dashboard(request):
    return rander(TEMPLATES_DIR / "dashboard.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, workers=workers)

