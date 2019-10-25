# 通过pandas中的plot函数，用于序列和数据框的数据创建图表
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# # 设置R语言绘图风格
# plt.style.use('ggplot')
# # 面向对象的绘图方式
# fig, axes = plt.subplots(nrows=1, ncols=2)
# ax1, ax2 = axes.ravel()  # 通过ravel函数将两个子图分别赋给两个变量
# # 设置数据
# index = ['Customer1', 'Customer2', 'Customer3', 'Customer4', 'Customer5']
# columns = pd.Index(['Metric1', 'Metric2', 'Metric3'], name='Metrics')
# data_frame = pd.DataFrame(np.random.rand(5, 3), index=index, columns=columns)
# data_frame.plot(kind='bar', ax=ax1, alpha=0.75, title='Bar Plot')
# plt.setp(ax1.get_xticklabels(), rotation=45, fontsize=10)  # 设置坐标轴标签的旋转角度和字体大小
# plt.setp(ax1.get_yticklabels(), rotation=0, fontsize=10)
# ax1.set_xlabel('Customer')
# ax1.set_ylabel('Value')
# ax1.xaxis.set_ticks_position('bottom')
# ax1.yaxis.set_ticks_position('left')
#
# colors = dict(boxes='DarkBlue', whiskers='Gray', medians='Red', caps='Black')
# data_frame.plot(kind='box', ax=ax2, color=colors, sym='r.', title='Box Plot')
# plt.setp(ax2.get_xticklabels(), rotation=45, fontsize=10)  # 设置坐标轴标签的旋转角度和字体大小
# plt.setp(ax2.get_yticklabels(), rotation=0, fontsize=10)
# ax2.set_xlabel('Metric')
# ax2.set_ylabel('Value')
# ax2.xaxis.set_ticks_position('bottom')
# ax2.yaxis.set_ticks_position('left')
# plt.savefig('fig/pandas_plots', dpi=300, bbox_inches='tight')
# plt.show()

# 通过seaborn创建统计图表
sns.set(color_codes=True)
# # 直方图
# x = np.random.normal(size=100)
# sns.distplot(x, bins=20, kde=False, rug=True, label='Histogram w/o Density', axlabel=('Value', 'Frequency'))
# plt.title('Histogram of a Random Sample from a Normal Distribution')
# plt.legend()
# plt.savefig('fig/seaborn_histogram', dpi=300, bbox_inches='tight')
# plt.show()
# # 带有回归直线的散点图与单变量直方图
# mean, cov = [5, 10], [(1, 0.5), (0.5, 1)]
# data = np.random.multivariate_normal(mean, cov, 200)  # 从多元正态分布矩阵中随机抽取数据
# data_frame = pd.DataFrame(data, columns=['x', 'y'])
# sns.jointplot(x='x', y='y', data=data_frame, kind='reg').set_axis_labels('x', 'y')
# plt.title('Joint Plot of Two Variables with Bivariate and Univariate Graphs')
# plt.savefig('fig/seaborn_joint', dpi=300, bbox_inches='tight')
# plt.show()
# # 成对变量之间的散点图和单变量直方图
# iris = sns.load_dataset('iris')
# sns.pairplot(iris)
# plt.savefig('fig/seaborn_iris', dpi=300, bbox_inches='tight')
# plt.show()
# # 按照某几个变量生成的箱线图
# tips = sns.load_dataset('tips')
# sns.factorplot(x='time', y='total_bill', hue='smoker', col='day', data=tips, kind='box', size=4, aspect=0.5)
# plt.savefig('fig/seaborn_tips', dpi=300, bbox_inches='tight')
# plt.show()
# # 带有bootstrap置信区间的线性回归模型
# tips = sns.load_dataset('tips')
# sns.lmplot(x='total_bill', y='tip', data=tips)
# plt.savefig('fig/seaborn_tips2', dpi=300, bbox_inches='tight')
# plt.show()
# 带有bootstrap置信区间的逻辑斯蒂回归模型
tips = sns.load_dataset('tips')
tips['big_tip'] = (tips.tip / tips.total_bill) > .15
sns.lmplot(x='total_bill', y='big_tip', data=tips, logistic=True, y_jitter=0.03).set_axis_labels('Total Bill', 'Big Tip')
plt.title('Logistic Regression of Big Tip vs. Total Bill')
plt.savefig('fig/seaborn_tip3', dpi=300, bbox_inches='tight')
plt.show()