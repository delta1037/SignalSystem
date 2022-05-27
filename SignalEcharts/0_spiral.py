import math
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Line3D


def spiral_line_data(omega_0=4):
    xyz = []
    x_o_y = []
    y_o_z = []
    for t in np.arange(-3, 3, 0.01):
        y = t
        z = math.cos(omega_0 * y)
        x = math.sin(omega_0 * y)
        xyz.append([x, y, z])
        x_o_y.append([x, y, 0])
        y_o_z.append([0, y, z])
    return [xyz, x_o_y, y_o_z]


data = spiral_line_data()

c = (
    Line3D(init_opts=opts.InitOpts(
        width="1080px",
        height="720px")
    )
    .add(
        series_name="XYZ",
        data=data[0],
        xaxis3d_opts=opts.Axis3DOpts(type_="value"),
        yaxis3d_opts=opts.Axis3DOpts(type_="value"),
        grid3d_opts=opts.Grid3DOpts(width=100,
                                    height=100,
                                    depth=100),
    )
    .add(
        series_name="XOY",
        data=data[1],
        xaxis3d_opts=opts.Axis3DOpts(type_="value"),
        yaxis3d_opts=opts.Axis3DOpts(type_="value"),
        grid3d_opts=opts.Grid3DOpts(width=100,
                                    height=100,
                                    depth=100),
    )
    .add(
        series_name="YOZ",
        data=data[2],
        xaxis3d_opts=opts.Axis3DOpts(type_="value"),
        yaxis3d_opts=opts.Axis3DOpts(type_="value"),
        grid3d_opts=opts.Grid3DOpts(width=100,
                                    height=100,
                                    depth=100),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="周期圆可视化"),
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
        ),
    )
)

c.render("0_spiral.html")
