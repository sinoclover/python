# 函数式绘图
import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(0,  10, 1000)  # 在指定的间隔内返回均匀间隔的数字
# y = np.sin(x)
# z = np.cos(x**2)
# plt.figure(figsize=(8, 4))
# plt.plot(x, y, label='$sin(x)$', color='red', linewidth=2)
# plt.plot(x, z, 'b--', label='$cos(x^2)$')
# plt.xlabel('Time(s)')
# plt.ylabel('Volt')
# plt.title('PyPlot First Example')
# plt.ylim(-1.2, 1.2)  # 设置y轴刻度
# plt.legend()  # 显示图例
# plt.savefig('fig/1.jpg')
# plt.show()

# # 设置子图
# # 第一部分
# plt.figure(figsize=(8, 4))
# plt.subplot(2,1,1)
# n = 12
# x = np.arange(n)
# y1 = (1-x/float(n)) * np.random.uniform(0.5, 1.0, n)  # uniform随机在范围内生成一个实数
# y2 = (1-x/float(n)) * np.random.uniform(0.5, 1.0, n)
# plt.bar(x, +y1, facecolor='#9999ff', edgecolor='white')
# plt.bar(x, -y2, facecolor='#ff9999', edgecolor='white')
# # 通过zip函数打包x,y1生成一个元组的可迭代列表
# for x, y in zip(x, y1):
#     plt.text(x, y, '{0:.2f}'.format(y), ha='center', va='bottom')
# # 限制图形打印时对应的纵坐标范围
# plt.ylim(-1.25, 1.25)
#
# # 第二部分
# plt.subplot(2,2,3)
# z = np.random.uniform(0, 1, n)
# plt.pie(z)
# plt.axis('equal')  # 使饼图长宽相等
#
# # 第三部分
# plt.subplot(2,2,4)
# x1 = np.linspace(-np.pi, np.pi, num=200, endpoint=True)
# yc = np.cos(x1)
# ys = np.sin(x1)
# plt.plot(x1, yc, color='blue', linewidth=2.5, linestyle='-')
# plt.plot(x1, ys, color='red', linewidth=2.5, linestyle='-')
# # 设置坐标值的刻度文字，以及坐标轴值的限制
# plt.xlim(x1.min()*1.1, x1.max()*1.1)
# # 使用$符号以显示相应的科学符号
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
# plt.ylim(yc.min()*1.1, yc.max()*1.1)
# plt.yticks([-1, 0, +1])
# plt.savefig('fig/2.jpg')
# plt.show()

# 使用bokeh绘制交互式可视化应用
from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# 输出为静态文件
output_file('fig/line.html', title='line plot example')
# 创建一个figure对象，附带标题和坐标轴标记
p = figure(title='simple line example', x_axis_label='x', y_axis_label='y')
# 添加一条线，设置图例
p.line(x, y, legend='Line A.', line_width=2)
show(p)