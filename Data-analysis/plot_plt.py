import matplotlib.pyplot as plt
import os
import numpy as np

# 模拟R语言中ggplot2风格图形
plt.style.use('ggplot')

# # 绘制条形图
# # 设置数据
# customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
# sale_amount = [127, 90, 201, 111, 232]
# customers_index = range(len(customers))
# # 面向对象的绘图方法
# fig = plt.figure()  # 创建对象
# ax1 = fig.add_subplot(111)  # 实例化子图
# ax1.bar(customers_index, sale_amount, align='center', color='darkblue')  # align设置条形与标签中间对齐
# ax1.xaxis.set_ticks_position('bottom')  # 设置刻度线位置
# ax1.yaxis.set_ticks_position('left')
# # 对图像进行设置
# plt.xticks(customers_index, customers, rotation=0, fontsize='small')  # 将x轴刻度线标签改为客户实际名称
# plt.xlabel('Customer Name')
# plt.ylabel('Sale Amount')
# plt.title('Sale Amount per Customer')
# # 存储和显示图片
# path = 'fig'
# if not os.path.exists(path):
#     os.mkdir(path)
# plt.savefig('fig/bar_plot', dpi=300, bbox_inches='tight')  # 在保存图片时将图形四周的空白去掉
# plt.show()

# # 直方图用来表示数值分布，如频率分布、频率密度分布、概率分布和概率密度分布
# mu1, mu2, sigma = 100, 130, 15  # mu为决定位置的期望，sigma为决定分布幅度的标准差
# x1 = mu1 + sigma * np.random.randn(10000)  # 基于标准正态分布产生10000个数据
# x2 = mu2 + sigma * np.random.randn(10000)
# # 面向对象的绘图方法
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# # 返回值n为直方图向量，bins是返回各个bin的区间范围，patches是返回每个bin里包含的数据list
# n1, bins1, patches1 = ax1.hist(x1, bins=50, normed=False, color='darkgreen', edgecolor='white')  # bins将数据分为50份，normed控制是否将直方图向量归一化
# n2, bins2, patches2 = ax1.hist(x2, bins=50, normed=False, color='orange', alpha=0.5, edgecolor='white')
# ax1.xaxis.set_ticks_position('bottom')
# ax1.yaxis.set_ticks_position('left')
# # 对图像进行设置
# plt.xlabel('Bins')
# plt.ylabel('Number of Values in Bin')
# fig.suptitle('Histograms', fontsize=14, fontweight='bold')
# ax1.set_title('Two Frequency Distributions')
# plt.savefig('fig/histogram', dpi=300, bbox_inches='tight')
# plt.show()

# # 折线图表示数据随时间发生的变化
# plot_data1 = np.random.randn(50).cumsum()  # 正态分布数据的累加值
# plot_data2 = np.random.randn(50).cumsum()
# plot_data3 = np.random.randn(50).cumsum()
# plot_data4 = np.random.randn(50).cumsum()
# # 面向对象的绘图方法
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1.plot(plot_data1, marker=r'o', color=u'blue', linestyle='-', label='Blue Solid')
# ax1.plot(plot_data2, marker=r'+', color=u'red', linestyle='--', label='Red Dashed')
# ax1.plot(plot_data3, marker=r'*', color=u'green', linestyle='-.', label='Green Dash Dot')
# ax1.plot(plot_data4, marker=r's', color=u'orange', linestyle=':', label='Orange Dotted')
# ax1.xaxis.set_ticks_position('bottom')
# ax1.yaxis.set_ticks_position('left')
# ax1.set_title('Line Plots: Markers, Colors and Linestyles')
# # 图像设置
# plt.xlabel('Draw')
# plt.ylabel('Random Number')
# plt.legend(loc='best')  # 根据图中空白部分将图例放在合适的位置
# plt.savefig('fig/line_plot', dpi=300, bbox_inches='tight')
# plt.show()

# # 散点图表示两个数值变量之间的相对关系
# x = np.arange(start=1., stop=15., step=1.)
# y_linear = x + 5. * np.random.randn(14)
# y_quadratic = x**2 + 10. * np.random.randn(14)
# # polyfit来计算某个deg阶数的多项式拟合模型的系数，poly1d来使用这些系数建立实际的多项式方程
# fn_linear = np.poly1d(np.polyfit(x, y_linear, deg=1))
# fn_quadratic = np.poly1d(np.polyfit(x, y_quadratic, deg=2))
# # 面向对象的绘图方式
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1.plot(x, y_linear, 'bo', x, fn_linear(x), 'b-', linewidth=2.)
# ax1.plot(x, y_quadratic, 'go', x, fn_quadratic(x), 'g-', linewidth=2.)
# ax1.xaxis.set_ticks_position('bottom')
# ax1.yaxis.set_ticks_position('left')
# ax1.set_title('Scatter Plots Regression Lines')
# # 图像设置
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.xlim((min(x)-1., max(x)+1.))  # 使用具体的数值设置坐标轴范围
# plt.ylim((min(y_quadratic)-10., max(y_quadratic)+10.))
# plt.savefig('fig/scatter_plot', dpi=300, bbox_inches='tight')
# plt.show()

# 箱线图可以表示数据的最小值、第一四分位数、中位数、第三四分位数和最大值
N = 500
normal = np.random.normal(loc=0.0, scale=1.0, size=N)  # 正态分布
lognormal = np.random.lognormal(mean=0.0, sigma=1.0, size=N)  # 对数正态分布
index_value = np.random.random_integers(low=0, high=N-1, size=N)
normal_sample = normal[index_value]
lognormal_sample = lognormal[index_value]
box_plot_data = [normal, normal_sample, lognormal, lognormal_sample]
# 面向对象的绘图方法
fig = plt.figure()
ax1 = fig.add_subplot(111)
box_labels = ['normal', 'normal_sample', 'lognormal', 'lognormal_sample']
ax1.boxplot(box_plot_data, notch=False, sym='.', vert=True, whis=1.5, showmeans=True, labels=box_labels)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Box Plots: Resampling of Two Distributions')
ax1.set_xlabel('Distribution')
ax1.set_ylabel('Value')
plt.savefig('fig/box_plot', dpi=300, bbox_inches='tight')
plt.show()
