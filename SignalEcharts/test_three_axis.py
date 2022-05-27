import math
import pyecharts.options as opts
from pyecharts.charts import Surface3D


def float_range(start, end, step, round_number=2):
    """
    浮点数 range
    :param start: 起始值
    :param end: 结束值
    :param step: 步长
    :param round_number: 精度
    :return: 返回一个 list
    """
    temp = []
    while True:
        if start < end:
            temp.append(round(start, round_number))
            start += step
        else:
            break
    return temp


def surface3d_data():
    ret = []
    for t0 in float_range(-3, 3, 0.05):
        y = t0
        for t1 in float_range(-3, 3, 0.05):
            x = t1
            z = math.sin(x ** 2 + y ** 2) * x / 3.14
            ret.append([x, y, z])
    return ret


# 3D散点图需要的数据一个二维数组，每一个元素是一个三元素一维数组，分别是x，y，z的坐标

c = (
    Surface3D(init_opts=opts.InitOpts(
        width="1600px",
        height="800px"))
    .add(
        series_name="Scatter3D",
        data=surface3d_data(),
        xaxis3d_opts=opts.Axis3DOpts(type_="value"),
        yaxis3d_opts=opts.Axis3DOpts(type_="value"),
        grid3d_opts=opts.Grid3DOpts(width=100,
                                    height=30,
                                    depth=100),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            dimension=2,
            max_=1,
            min_=-1,
            range_color=[
                'red',
                'orange',
                'yellow',
                'green',
                'blue',
                'purple'
            ],
        )
    )
)

c.render("test_three_axis.html")
