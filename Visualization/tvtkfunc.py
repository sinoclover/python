# 使用IVTK观察TVTK管线的函数封装
from tvtk.api import tvtk

def ivtk_scene(actors):
    from tvtk.tools import ivtk
    # 创建一个带有Crust(Python shell)的窗口
    win = ivtk.IVTKWithCrustAndBrowser()
    win.open()
    # 将对象实例置入窗口中
    win.scene.add_actor(actors)
    # 修正窗口错误
    # dialog = win.control.centralWidget().widget(0).widget(0)
    # from pyface.qt import QtCore
    # dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
    # dialog.show()

def event_loop():
    from pyface.api import GUI
    gui = GUI()
    gui.start_event_loop()