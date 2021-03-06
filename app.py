#encoding: utf-8

from flask import Flask, render_template
from pyecharts import Scatter3D, Bar
from pyecharts.utils import json_dumps
import random

app = Flask(__name__)

# REMOTE_HOST = "http://echarts.baidu.com/build/dist/echarts.js"
REMOTE_HOST = "https://pyecharts.github.io/assets/js"

@app.route("/")
def hello():
    s3d = scatter3d()
    return render_template('pyecharts.html',
                           myechart=s3d.render_embed(),
                           host=REMOTE_HOST,
                           script_list=s3d.get_js_dependencies())

@app.route("/bar")
def index():
    _bar = bar_chart()
    return render_template('pyecharts2.html',
                           chart_id=_bar.chart_id,
                           host=REMOTE_HOST,
                           my_width="100%",
                           my_height=600,
                           my_option=json_dumps(_bar.options),
                           script_list=_bar.get_js_dependencies())


def bar_chart():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("服装",
            ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
            [5, 20, 36, 10, 75, 90])
    return bar


def scatter3d():
    data = [generate_3d_random_point() for _ in range(80)]
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    scatter3D = Scatter3D("3D scattering plot demo", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    return scatter3D


def generate_3d_random_point():
    return [random.randint(0, 100),
            random.randint(0, 100),
            random.randint(0, 100)]

if __name__ == "__main__":
    app.run(debug=True)
