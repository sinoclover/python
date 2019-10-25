# matplotlib.pyplot是绘制各类可视化图形的命令子库，相当于快捷方式
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 基本操作
# plt.plot([3, 1, 4, 5, 2])  # 只输入一个列表会被当做y值来处理，而x轴则是列表的索引
# plt.ylabel('Grade')
# plt.savefig('fig/test', dpi=600)  # 默认为PNG文件
# plt.show()

# plt.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2])  # 输入两个列表则前者为x轴，后者为y轴
# plt.ylabel('Grade')
# plt.axis([-1, 10, -1, 6])  # 定义x,y轴的范围尺度
# plt.savefig('fig/test1', dpi=600)  # 默认为PNG文件
# plt.show()

# # 绘图区域
# # 使用subplot函数在全局绘图区域中创建一个分区体系
# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)
#
# a = np.arange(0.0, 5.0, 0.02)
# plt.subplot(211)
# plt.plot(a, f(a))
# plt.subplot(212)
# plt.plot(a, np.cos(2 * np.pi * a), 'r--')
# plt.savefig('fig/test2', dpi=300)
# plt.show()

# # 绘制多条曲线函数，控制绘制风格
# a = np.arange(10)
# plt.plot(a, a*1.5, 'go-', a, a*2.5, 'rx', a, a*3.5, '*', a, a*4.5, 'b-.')
# plt.plot(a, a**2, color='black',linewidth=2, marker='o', linestyle='--')
# plt.axis([0, 10, 0, 100])
# plt.savefig('fig/test3', dpi=300)
# plt.show()

# # 绘图时的中文显示
# matplotlib.rcParams['font.family'] = 'SimHei'  # 字体名称
# matplotlib.rcParams['font.style'] = 'italic'  # 字体风格
# matplotlib.rcParams['font.size'] = '10'  # 字体大小
# plt.plot([3,1,4,5,2])
# plt.ylabel('纵轴（值）')
# plt.savefig('fig/test4', dpi=300)
# plt.show()
# # 中文显示实例
# # 这种方式会改变所有的字体，不要轻易改变全局字体
# matplotlib.rcParams['font.family'] ='STSong'
# matplotlib.rcParams['font.size'] = 20
# a = np.arange(0.0, 5.0, 0.02)
# plt.xlabel('横轴：时间')
# plt.ylabel('纵轴：振幅')
# plt.plot(a, np.cos(2*np.pi*a), 'r--')
# plt.savefig('fig/test5', dpi=300)
# plt.show()
# # 在有中文输出的地方，增加属性fontproperties，就可以进行局部的改动
# a = np.arange(0.0, 5.0, 0.02)
# plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=20)
# plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=20)
# plt.plot(a, np.cos(2*np.pi*a), 'r--')
# plt.savefig('fig/test6', dpi=300)
# plt.show()

# # 正弦波实例文本显示函数
# a = np.arange(0.0, 5.0, 0.02)
# plt.plot(a, np.cos(2*np.pi*a), color='red', linestyle='--')
# plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=15, color='green')
# plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=15)
# plt.title(r'正弦波实例 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=25)  # 扩展标识$引入Latex格式文本
# # plt.text(2, 1, r'$\mu=100$', fontsize=15)  # 确定文本显示位置
# plt.annotate(r'$\mu=100$', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.1, width=2))
#
# plt.axis([-1, 6, -2, 2])
# plt.grid(True)  # 加入网格曲线
# plt.savefig('fig/test7', dpi=300)
# plt.show()

# # 子绘图区域辅助设计，即通过subplot2grid()设定网格，选中网格，确定选中行列区域数量，编号从0开始
# plt.subplot2grid((3, 3), (0, 0), colspan=3)
# plt.subplot2grid((3, 3), (1, 0), colspan=2)
# plt.subplot2grid((3, 3), (1, 2), rowspan=2)
# plt.subplot2grid((3, 3), (2, 0))
# plt.subplot2grid((3, 3), (2, 1))
# plt.show()

# # 绘制饼图
# labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
# sizes = [15, 30, 45, 10]
# explode = (0,  0.1, 0, 0)
# plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)  # stratangle起始角度
# plt.axis('equal')  # xy轴相等
# plt.savefig('fig/pie', dpi=300)
# plt.show()
#
# # 绘制直方图，区别柱形图
# np.random.seed(0)
# mu, sigma = 100, 20  # 均值和标准差
# a = np.random.normal(mu, sigma, size=100)
# # 数组在直方图划分的区域中出现的个数即直方图的高度值
# plt.hist(a, 20, normed=1, histtype='stepfilled', facecolor='b', edgecolor='r', alpha=0.75)
# # 第二个参数bin，即直方图的个数；normed=1则进行归一化，normed=0则是其出现的个数
# plt.title('Histogram')
# plt.savefig('fig/hist', dpi=300)
# plt.show()

# # 绘制极坐标图，面向对象的方法
# N = 20  # 绘制数据的个数
# theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
# radii = 10 * np.random.rand(N)  # rand()是生成[0,1)之间的随机数
# width = np.pi / 4 * np.random.rand(N)
# ax = plt.subplot(111, projection='polar')
# bars = ax.bar(theta, radii, width=width, bottom=0.0)
# for r, bar in zip(radii, bars):
#     bar.set_facecolor(plt.cm.viridis(r / 10.))
#     bar.set_alpha(0.5)
# plt.savefig('fig/polar', dpi=300)
# plt.show()

# # 绘制散点图
# a = np.random.randn(100)  # 从标准正态分布中返回一个或多个样本值
# b = np.random.randn(100)
# plt.scatter(a, b, c='r', marker='x')
# plt.savefig('fig/scatter1', dpi=300)
# plt.show()

# 面向对象的方法绘制散点图
ax = plt.subplot()  # ax为一个子图对象
ax.plot(10 * np.random.randn(100), 10 * np.random.randn(100), 'o')
ax.set_title('Simple scatter')
plt.savefig('fig/scatter2', dpi=300)
plt.show()
