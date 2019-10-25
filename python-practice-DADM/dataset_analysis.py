# # 函数式编程
# # 列表解析，其本质是for循环效率不高
# a = [1, 2, 3]
# b = [i+2 for i in a]
# print(b)
# # map函数，用于逐一遍历效率较高
# # 即首先用lambda定义一个函数，通过map命令将函数逐一应用到列表中的每一个元素
# c = map(lambda x: x+2, a)
# c = list(c)
# print(c)
# # reduce函数，用于递归计算
# from functools import reduce
# d = reduce(lambda x,y: x*y, range(1, 5))
# print(d)
# # filter函数，是一个过滤器，，用来筛选出列表中符合条件的元素
# e = filter(lambda x: 5 < x < 8, range(10))
# e = list(e)
# print(e)

# # 数据质量分析之数据异常值检测
# import pandas as pd
# import matplotlib.pyplot as plt
# # 导入数据并读取
# catering_sale = 'data/catering_sale.xls'
# data = pd.read_excel(catering_sale, index_col=u'日期')  # 指定日期为索引列
# # 简单统计量分析
# print(len(data))
# print(data.describe())
# print('lost data: {0}'.format(len(data) - int(data.count())))
# # 绘制箱线图
# plt.figure()
# plt.rcParams['font.family'] = ['SimHei']  # 设置全局字体
# plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
# p = data.boxplot(return_type='dict')  # 直接使用数据框的方法绘制箱线图
# x = p['fliers'][0].get_xdata()  # 'flies'即异常值的标签
# y = p['fliers'][0].get_ydata()
# y.sort()  # 从大到小排列，该方法直接改变原对象
# # 用annotate添加注释
# # 其中有相近的点，注释会出现重叠，需要进行控制
# for i in range(len(x)):
#     plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i-1]), y[i]), fontproperties='STSong')
# # 可以使用fontproperties局部控制字体
# plt.savefig('fig/catering_sale', dpi=300, bbox_inches='tight')
# plt.show()

# # 数据特征分析之数据统计量分析
# # from __future__ import print_function
# import pandas as pd
#
# catering_sale = 'data/catering_sale.xls'
# data = pd.read_excel(catering_sale, index_col=u'日期')
# data = data[(data[u'销量'] > 400) & (data[u'销量'] < 5000)]  # 过滤异常数据
# statistics = data.describe()  # 保存基本统计量
#
# statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']  # 极差
# statistics.loc['var'] = statistics.loc['std'] / statistics.loc['mean']  # 变异系数
# statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']  # 四分位数间距
# print(statistics)

# # 数据特征分析之数据贡献度分析（帕累托分析）
# # 菜品盈利数据帕累托图
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 初始化参数
# dish_profit = 'data/catering_dish_profit.xls'  # 菜品盈利数据
# data = pd.read_excel(dish_profit, index_col=u'菜品名')
# data = data[u'盈利'].copy()
# data.sort_values(ascending=False)
# print(data)
#
# # 绘制图像
# # plt.rcParams['font.family'] = ['SimHei']
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.figure()
# data.plot(kind='bar')
# plt.ylabel(u'盈利（元）', fontproperties='SimHei')
# p = 1.0 * data.cumsum() / data.sum()  # 通过累加和获取盈利的百分比
# p.plot(color='r', secondary_y=True, style='-o', linewidth=2)  # 实现双坐标轴
# # 添加注释，即在85%处的标记，这里包括了指定箭头样式
# plt.annotate(format(p[6], '.4%'), xy=(6, p[6]), xytext=(6*0.9, p[6]*0.9), arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
# plt.ylabel(u'盈利（比例）', fontproperties='SimHei')
# plt.savefig('fig/pareto', dpi=300, bbox_inches='tight')
# plt.show()

# # 数据特征分析之数据相关性分析
# import pandas as pd
#
# catering_sale = 'data/catering_sale_all.xls' # 餐饮数据，含有其他属性
# data = pd.read_excel(catering_sale, index_col=u'日期')  # 读取数据
#
# print(data.corr())  # 相关系数矩阵
# print(data.corr()[u'百合酱蒸凤爪'])  # 只显示该菜式的与其他菜式的相关系数
# print(data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺']))  # 只计算两个菜式的相关系数

# # 主要的数据探索函数
# # 基本统计特征函数包括sum, mean, var, std等
# # 相关系数矩阵corr
# import pandas as pd
# import numpy as np
# df1 = pd.DataFrame([range(1, 8), range(2, 9)])
# print(df1.corr(method='spearman'))  # 计算相关系数矩阵，默认为pearson,也可以使用kendall或spearman
# s1 = df1.loc[0, :]
# s2 = df1.loc[0, :]
# print(s1.corr(s2, method='pearson'))
# # 协方差矩阵cov
# df2 = pd.DataFrame(np.random.randn(6, 5))
# print(df2.cov())
# print(df2[0].cov(df2[1]))
# # 样本偏度（三阶矩）/峰度（四阶距）skew/kurt
# print(df2.skew())
# print(df2.kurt())
# # describe
# print(df2.describe())
# # 拓展统计特征函数，包括累积计算和滚动计算
# # 累积统计特征有cumsum, cumprod, cummax, cummin
# # 滚动计算rolling_系列，为pandas的函数而非对象的方法
# s = pd.Series(range(20))
# print(s.cumsum())
# print(pd.rolling_sum(s, 2))  # 依次对相邻两项求和

# 统计作图函数
# pandas基于matplotlib简化了某些命令，如plot, pie, hist, boxplot等
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# plot
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
plt.plot(x, y, 'bp--')
plt.show()
# pie
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]  # 每一块的比例
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = [0, 0.1, 0, 0]
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
# hist
m = np.random.randn(1000)  # 1000个服从正态分布的随机数
plt.hist(m, 10, edgecolor='white')
plt.show()
# box
df = pd.DataFrame([m, m+1]).T # 构造两列的数据框
df.plot(kind = 'box')
plt.show()
# pandas对象绘图方法
# plot(logx = True)/plot(logy = True) 绘制x或y轴的对数图形
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
a = pd.Series(np.exp(np.arange(20)))
a.plot(label=u'原始数据图', legend=True)
plt.show()
a.plot(logy=True, label=u'对数数据图', legend=True)
plt.show()
# ploy(yerr = error) 绘制误差条形图
error = np.random.randn(10)
y = pd.Series(np.sin(np.arange(10)))
y.plot(yerr = error)
plt.show()