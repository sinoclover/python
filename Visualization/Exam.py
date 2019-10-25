# # 1请用tvtk绘制一个圆锥，圆锥的数据源对象为ConeSource(),圆锥高度为6.0，圆锥半径为2.0，背景色为红色。
# from tvtk.api import tvtk
#
# p = tvtk.ConeSource(height = 6.0, radius = 2.0, resolution = 36)
# m = tvtk.PolyDataMapper(input_connection = p.output_port)
# a = tvtk.Actor(mapper = m)
#
# r = tvtk.Renderer(background = (1, 0, 0))
# r.add_actor(a)
# w = tvtk.RenderWindow(size = (300, 300))
# w.add_renderer(r)
#
# i = tvtk.RenderWindowInteractor(render_window = w)
# i.initialize()
# i.start()

# # 使用IVTK观察TVTK管线
# from tvtk.api import tvtk
# from tvtk.tools import ivtk
# from pyface.api import GUI
#
# p = tvtk.ConeSource(height = 6.0, radius = 2.0, resolution = 36)
# m = tvtk.PolyDataMapper(input_connection = p.output_port)
# a = tvtk.Actor(mapper = m)
#
# win = ivtk.IVTKWithCrustAndBrowser()
# win.open()
# win.scene.add_actor(a)
#
# gui = GUI()
# gui.start_event_loop()
#
# # 2请自行从网络上下载一个obj模型文件，使用tvtk读取该文件并显示出来。
# from tvtk.api import tvtk
# from tvtkfunc import ivtk_scene, event_loop
#
# s = tvtk.OBJReader(file_name = 'data/Box.obj')
# m = tvtk.PolyDataMapper(input_connection=s.output_port)
# a = tvtk.Actor(mapper=m)
#
# win = ivtk_scene(a)
# event_loop()

# # 3改写课程中标量等值面绘制的实例，通过get_value()和set_value()设定第1个等值面的值为原来的2倍。
# from tvtk.api import tvtk
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
# con = tvtk.ContourFilter()  # 创建等值面对象
# con.set_input_data(grid)  # 使用数据集对象创建等值面
# con.generate_values(10, grid.point_data.scalars.range)  # 指定轮廓数和标量数据范围
# value = 2 * con.get_value(0)
# con.set_value(0, value)
#
# # 设定映射器的变量范围属性
# m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range,
#                         input_connection=con.output_port)
# # 设置对象
# a = tvtk.Actor(mapper=m)
# a.property.opacity = 0.5  # 设定对象透明度为0.5
#
# # 窗口绘制tvtkfunc功能
# win = ivtk_scene(a)
# event_loop()