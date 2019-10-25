import wx

# # 单纯的GUI框架
# app = wx.App()
# frame = wx.Frame(None, title = 'Hello, World!')
# frame.Show(True)
# app.MainLoop()

# # 使用面向对象方法的GUI框架
# class MyApp(wx.App):
#     def Onlnit(self):
#         frame = wx.Frame(None, title = 'Hello, World!')
#         frame.Show()
#         return True
#
# if __name__ == '__main__':
#     app = MyApp()
#     app.MainLoop()

# # GUI组件框架
# class Frame1(wx.Frame):
#     def __init__(self, superior):
#         wx.Frame.__init__(self, parent=superior, title='Example', pos=(100,200), size=(350,200))
#         panel = wx.Panel(self)
#         text1 = wx.TextCtrl(panel, value='Hello, World!', size=(350,200))
# if __name__ == '__main__':
#     app = wx.App()
#     frame = Frame1(None)
#     frame.Show(True)
#     app.MainLoop()

# # GUI事件处理机制
# class Frame1(wx.Frame):
#     def __init__(self, superior):
#         wx.Frame.__init__(self, parent=superior, title='Example', pos=(100,200), size=(350,200))
#         self.panel = wx.Panel(self)
#         self.panel.Bind(wx.EVT_LEFT_UP, self.OnClick) # 鼠标左键抬起事件绑定在PANEL的OnClick方法上
#     def OnClick(self, event):
#         posm = event.GetPosition()
#         wx.StaticText(parent = self.panel, label = 'hello, world!', pos=(posm.x, posm.y))
# if __name__ == '__main__':
#     app = wx.App()
#     frame = Frame1(None)
#     frame.Show(True)
#     app.MainLoop()

# GUI布局管理
class Frame1(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, parent=superior, title='Hello World in wxPython')
        panel = wx.Panel(self)  # 创建自动调用尺寸的容器
        sizer = wx.BoxSizer(wx.VERTICAL)  # 创建SIZER的实例
        # 创建窗口部件,并将每个子窗口添加给sizer
        self.text1 = wx.TextCtrl(panel, value='Hello, World!', size=(200,180), style=wx.TE_MULTILINE)
        sizer.Add(self.text1, 0, wx.ALIGN_TOP | wx.EXPAND)
        button = wx.Button(panel, label='Click Me')
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)  # 调用setsizer方法
        panel.Layout()
        self.Bind(wx.EVT_BUTTON, self.OnClick, button)
    def OnClick(self, text):
        self.text1.AppendText('\nHello, World!')

if __name__ == '__main__':
    app = wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop()
