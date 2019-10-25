# # mayavi库的使用
# from mayavi import mlab
# import numpy
#
# x = [[-1, 1, 1, -1, -1], [-1, 1, 1,  -1, -1]]
# y = [[-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
# z = [[1, 1, -1, -1, 1], [1, 1, -1, -1, 1]]
#
# s = mlab.mesh(x, y, z)
# mlab.show()

# # 三维可视化实例
# from numpy import pi, sin, cos, mgrid
# from mayavi import mlab
#
# # 建立数据
# dphi, dtheta = pi / 250.0, pi / 250.0
# [phi, theta] = mgrid[0:pi + dphi * 1.5:dphi, 0:2 * pi + dtheta * 1.5:dtheta]
# m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
# r = sin(m0 * phi) ** m1 + cos(m2 * phi) ** m3 + sin(m4 * theta) ** m5 + cos(m6 * theta) ** m7
# x = r * sin(phi) * cos(theta)
# y = r * cos(phi)
# z = r * sin(phi) * sin(theta)
#
# # 对该数据进行三维可视化
# s = mlab.mesh(x, y, z, representation = 'wireframe', line_width = 1.0)
# mlab.show()

# # 0维绘图points3d函数使用
# import numpy as np
# from mayavi import mlab
#
# t = np.linspace(0, 4 * np.pi, 20)
# x = np.sin(2 * t)
# y = np.cos(t)
# z = np.cos(2 * t)
# s = np.sin(t) + 2
#
# points = mlab.points3d(x, y, z, s, colormap = 'Reds', scale_factor = 0.25, resolution = 32)
# mlab.show()

# # 一维绘图plot3d函数使用
# import numpy as np
# from mayavi import mlab

# import numpy as np
# from mayavi import mlab
#
# # 建立数据
# n_mer, n_long = 6, 11
# dphi = np.pi / 1000.0
# phi = np.arange(0.0, 2 * np.pi + 0.5 * dphi, dphi)
# mu = phi * n_mer
# x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
# y = np.sin(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
# z = np.sin(n_long * mu / n_mer) * 0.5
#
# # 对数据进行可视化
# l = mlab.plot3d(x, y, z, np.sin(mu), tube_radius=0.025, colormap='Spectral')
# mlab.show()

# # 二维绘图imshow函数使用
# import numpy
# from mayavi import mlab
#
# s = numpy.random.random((10,10))
#
# img = mlab.imshow(s, colormap = 'gist_earth')
# mlab.show()

# # 二维绘图surf函数使用
# import numpy as np
# from mayavi import mlab
#
# def f(x, y):
#     return np.sin(x - y) + np.cos(x + y)
#
# x, y = np.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
# #s = mlab.surf(x, y, f)
# con_s = mlab.contour_surf(x, y, f)
# mlab.show()

# # 三维绘图contour3d函数使用
# import numpy
# from mayavi import mlab
#
# x, y, z = numpy.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
# scalars = x * x + y * y + z * z
# obj = mlab.contour3d(scalars, contours=8, transparent=True)
# mlab.show()

# # 三维绘图quiver3d函数使用
# import numpy as np
# from mayavi import mlab
#
# x, y, z = np.mgrid[-2:3, -2:3, -2:3]
# r = np.sqrt(x ** 2 + y ** 2 + z ** 4)
# u = y * np.sin(r) / (r + 0.001)
# v = -x * np.sin(r) / (r + 0.001)
# w = np.zeros_like(z)
#
# obj = mlab.quiver3d(x, y, z, u, v, w, line_width=3, scale_factor=1)
# mlab.show()

# # 改变物体颜色
# import numpy as np
# from mayavi import mlab
# # 建立数据
# x, y = np.mgrid[-10:10:200j, -10:10:200j]
# z = 100 * np.sin(x * y) / (x * y)
# # 对数据进行可视化
# mlab.figure(bgcolor=(1, 1, 1))
# surf = mlab.surf(z, colormap = 'cool')
# # 访问surf对象的LUT
# # LUT是一个255*4的数组，列向量表示RGBA，每个值的范围从0-255
# lut = surf.module_manager.scalar_lut_manager.lut.table.to_array()
# # 增加透明梯度，修改alpha通道
# lut[:, -1] = np.linspace(0, 255, 256)
# surf.module_manager.scalar_lut_manager.lut.table = lut
# mlab.show()

# # 鼠标选取交互操作
# import numpy as np
# from mayavi import mlab
#
# ######场景初始化######
# figure = mlab.gcf()
# figure.scene.disable_render = True
#
# # 用mlab.points3d建立红色和白色小球的集合
# x1, y1, z1 = np.random.random((3, 10))
# red_glyphs = mlab.points3d(x1, y1, z1, color=(1, 0, 0),
#                            resolution=10)
# x2, y2, z2 = np.random.random((3, 10))
# white_glyphs = mlab.points3d(x2, y2, z2, color=(0.9, 0.9, 0.9),
#                              resolution=10)
# figure.scene.disable_render = False
# # 绘制选取框，并放在第一个小球上
# outline = mlab.outline(line_width=3)
# outline.outline_mode = 'cornered'
# outline.bounds = (x1[0] - 0.1, x1[0] + 0.1,
#                   y1[0] - 0.1, y1[0] + 0.1,
#                   z1[0] - 0.1, z1[0] + 0.1)
#
# ######处理选取事件#####
# # 获取构成一个红色小球的顶点列表
# glyph_points = red_glyphs.glyph.glyph_source.glyph_source.output.points.to_array()
#
#
# # 当选取事件发生时调用此函数
# def picker_callback(picker):
#     if picker.actor in red_glyphs.actor.actors:
#         # 计算哪个小球被选取
#         point_id = int(picker.point_id / glyph_points.shape[0])  # int向下取整
#         if point_id != -1:  # 如果没有小球被选取，则point_id = -1
#             # 找到与此红色小球相关的坐标
#             x, y, z = x1[point_id], y1[point_id], z1[point_id]
#             # 将外框移到小球上
#             outline.bounds = (x - 0.1, x + 0.1,
#                               y - 0.1, y + 0.1,
#                               z - 0.1, z + 0.1)
#
#
# picker = figure.on_mouse_pick(picker_callback)
# picker.tolerance = 0.01
# mlab.title('Click on red balls')
# mlab.show()

# 标量数据可视化
import numpy as np

x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
s = np.sin(x * y * z) / (x * y * z)

from mayavi import mlab

src = mlab.pipeline.scalar_field(s)
mlab.pipeline.iso_surface(src, contours=[s.min() + 0.1 * s.ptp(), ], opacity=0.1)
mlab.pipeline.iso_surface(src, contours=[s.max() - 0.1 * s.ptp(), ])
mlab.pipeline.image_plane_widget(src,
                                 plane_orientation='z_axes',
                                 slice_index=10,
                                 )
mlab.show()

# # 矢量数据可视化
# import numpy as np
#
# x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
# u = np.sin(np.pi * x) * np.cos(np.pi * z)
# v = -2 * np.sin(np.pi * y) * np.cos(2 * np.pi * z)
# w = np.cos(np.pi * x) * np.sin(np.pi * z) + np.cos(np.pi * y) * np.sin(2 * np.pi * z)
#
# from mayavi import mlab
#
# # mlab.quiver3d(u, v, w)
# # mlab.outline()
# # 降采样
# src = mlab.pipeline.vector_field(u, v, w)
# mlab.pipeline.vectors(src, mask_points=10, scale_factor = 2.0)
#
# mlab.show()