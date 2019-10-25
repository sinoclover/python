# from tvtk.api import tvtk
# # 立方体数据源
# s = tvtk.CubeSource(x_length = 1.0, y_length = 2.0, z_length = 3.0)
# print(s)
# print(s.x_length)
# print(s.center)
# print(s.output_points_precision)
# # 圆锥体数据源
# p = tvtk.ConeSource(height = 3.0, radius = 1.0, resolution = 36)  # 底面圆分辨率
# print(p)
# print(p.height)
# print(p.radius)
# print(p.resolution)
# print(p.center)

# # 显示一个三维对象
# from tvtk.api import tvtk
#
# # 创建长方体数据源
# s = tvtk.CubeSource(x_length = 1.0, y_length = 2.0, z_length = 3.0)
# # 使用PolyDataMapper将数据输出并连接到映射器上转换为图形数据
# m = tvtk.PolyDataMapper(input_connection = s.output_port)
# # 使用图形数据m创建一个活动对象a
# a = tvtk.Actor(mapper = m)
# # 创建渲染器r并将对象a添加进去
# r = tvtk.Renderer(background = (0, 0, 0))
# r.add_actor(a)
# # 创建一个渲染窗口w，并将渲染器r+a添加进去
# w = tvtk.RenderWindow(size = (300, 300))
# w.add_renderer(r)
# # 创建一个交互窗口i，将完整的渲染窗口与对象w+r+a添加进去
# i = tvtk.RenderWindowInteractor(render_window = w)
# # 开启交互
# i.initialize()
# i.start()

# # 使用IVTK观察TVTK管线
# from tvtk.api import tvtk
# from tvtk.tools import ivtk
# from pyface.api import GUI
#
# s = tvtk.CubeSource(x_length = 1.0, y_length = 2.0, z_length = 3.0)
# m = tvtk.PolyDataMapper(input_connection = s.output_port)
# a = tvtk.Actor(mapper = m)
#
# # 创建一个带有Crust(Python shell)的窗口
# gui = GUI()
# win = ivtk.IVTKWithCrustAndBrowser()
# win.open()
# win.scene.add_actor(a)
# # # 修正错误
# # dialog = win.control.centralWidget().widget(0).widget(0)
# # from pyface.qt import QtCore
# # dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
# # dialog.show()
# # 开启界面消息循环
# gui.start_event_loop()

# # 使用IVTK观察TVTK管线的函数封装
# from tvtk.api import tvtk
#
# def ivtk_scene(actors):
#     from tvtk.tools import ivtk
#     # 创建一个带有Crust(Python shell)的窗口
#     win = ivtk.IVTKWithCrustAndBrowser()
#     win.open()
#     # 将对象实例置入窗口中
#     win.scene.add_actor(actors)
#     # 修正窗口错误
#     # dialog = win.control.centralWidget().widget(0).widget(0)
#     # from pyface.qt import QtCore
#     # dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
#     # dialog.show()
#
# def event_loop():
#     from pyface.api import GUI
#     gui = GUI()
#     gui.start_event_loop()
#
# s = tvtk.CubeSource(x_length = 1.0, y_length = 2.0, z_length = 3.0)
# m = tvtk.PolyDataMapper(input_connection = s.output_port)
# a = tvtk.Actor(mapper = m)
# win = ivtk_scene(a)
# event_loop()

# # 通过tvtkfunc.py导入IVTK工具
# from tvtk.api import tvtk
# from tvtkfunc import ivtk_scene, event_loop
#
# s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
# m = tvtk.PolyDataMapper(input_connection=s.output_port)
# a = tvtk.Actor(mapper=m)
# win = ivtk_scene(a)
# event_loop()

# # RectilinearGrid数据集
# from tvtk.api import tvtk
# import numpy as np
#
# x = np.array([0, 3, 9, 15])
# y = np.array([0, 1, 5])
# z = np.array([0, 2, 3])
# r = tvtk.RectilinearGrid()
# r.x_coordinates = x
# r.y_coordinates = y
# r.z_coordinates = z
# r.dimensions = len(x), len(y), len(z)

# # 读取STL模型数据
# from tvtk.api import tvtk
# from tvtkfunc import ivtk_scene, event_loop
#
# s = tvtk.STLReader(file_name="data/python.stl")
# m = tvtk.PolyDataMapper(input_connection=s.output_port)
# a = tvtk.Actor(mapper=m)
#
# win = ivtk_scene(a)
# event_loop()

# #读取PLOT3D数据
# from tvtk.api import tvtk
#
# def read_data():  # 读入数据
#     plot3d = tvtk.MultiBlockPLOT3DReader(
#         xyz_file_name="data/combxyz.bin",  # 网格文件
#         q_file_name="data/combq.bin",  # 空气动力学结果文件
#         scalar_function_number=100,  # 设置标量数据数量
#         vector_function_number=200  # 设置矢量数据数量
#     )
#     plot3d.update()
#     return plot3d
#
# plot3d = read_data()
# grid = plot3d.output.get_block(0)

# PLOT3D标量数据可视化
from tvtk.api import tvtk
from tvtkfunc import ivtk_scene, event_loop

plot3d = tvtk.MultiBlockPLOT3DReader(
    xyz_file_name="data/combxyz.bin",
    q_file_name="data/combq.bin",
    scalar_function_number=100, vector_function_number=200
)  # 读入Plot3D数据
plot3d.update()  # 让plot3D计算其输出数据
grid = plot3d.output.get_block(0)  # 获取读入的数据集对象

con = tvtk.ContourFilter()  # 创建等值面对象
con.set_input_data(grid)  # 使用数据集对象创建等值面
con.generate_values(10, grid.point_data.scalars.range)  # 指定轮廓数和标量数据范围

# 设定映射器的变量范围属性
m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range,
                        input_connection=con.output_port)
# 设置对象
a = tvtk.Actor(mapper=m)
a.property.opacity = 0.5  # 设定对象透明度为0.5

# 窗口绘制tvtkfunc功能
win = ivtk_scene(a)
event_loop()

# # POLT3D矢量数据可视化
# from tvtk.api import tvtk
# from tvtkfunc import ivtk_scene, event_loop
#
# # 读入PLot3D数据
# plot3d = tvtk.MultiBlockPLOT3DReader(
#     xyz_file_name="data/combxyz.bin",
#     q_file_name="data/combq.bin",
#     scalar_function_number=100, vector_function_number=200
# )
# plot3d.update()
# grid = plot3d.output.get_block(0)
#
# # 对数据集中的数据进行随机选取，每50个点选择一个点
# mask = tvtk.MaskPoints(random_mode=True, on_ratio=50)  # 降采样处理减少数据点
# mask.set_input_data(grid)  # 将数据与MASK对象绑定
#
# # 创建表示箭头的PolyData数据集
# glyph_source = tvtk.ArrowSource() # 使用箭头或圆锥作为符号化技术的应用
# # 在Mask采样后的PolyData数据集每个点上放置一个箭头
# # 箭头的方向、长度和颜色由于点对应的矢量和标量数据决定
# glyph = tvtk.Glyph3D(input_connection=mask.output_port,  # 将MASK对象的输出数据进行符号化处理
#                      scale_factor=2)  # 放缩系数为2
# glyph.set_source_connection(glyph_source.output_port)  # 设置符号化处理中的圆锥数据源形式
#
# m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range,
#                         input_connection=glyph.output_port)  # 将GLYPH对象的输出数据进行图形数据的映射
# a = tvtk.Actor(mapper=m)
#
# # 窗口绘制
# win = ivtk_scene(a)
# event_loop()

# # PLOT3D空间轮廓线 可视化
# from tvtk.api import tvtk
# from tvtk.common import configure_input
# from tvtkfunc import ivtk_scene, event_loop
#
# plot3d = tvtk.MultiBlockPLOT3DReader(
#     xyz_file_name="data/combxyz.bin",
#     q_file_name="data/combq.bin",
#     scalar_function_number=100, vector_function_number=200
# )  # 读入Plot3D数据
# plot3d.update()  # 让plot3D计算其输出数据
# grid = plot3d.output.get_block(0)  # 获取读入的数据集对象
#
# outline = tvtk.StructuredGridOutlineFilter()  # 计算表示外边框的PolyData对象
# configure_input(outline, grid)  # 调用tvtk.common.configure_input()将外框计算和数据集产生关联
# m = tvtk.PolyDataMapper(input_connection=outline.output_port)
# a = tvtk.Actor(mapper=m)
# a.property.color = 0.3, 0.3, 0.3
#
# # 窗口绘制
# win = ivtk_scene(a)
# event_loop()