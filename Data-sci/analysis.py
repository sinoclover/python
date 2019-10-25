# 在数据形成特征的过程中，有损地获取相应的结果即数据的摘要
# 包括基本统计、分布/累计特征、相关性周期性等数据特征以及数据挖掘形成的知识
import numpy as np
import pandas as pd

# # pandas库的数据排序
# # 指定轴上根据索引进行排序，默认为升序
# b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])
# print(b)
# print(b.sort_index())
# print(b.sort_index(ascending=False))
# c = b.sort_index(axis=1, ascending=False)  # 横轴降序
# print(c)
# c = c.sort_index()  # 纵轴升序
# print(c)
# # 指定轴上跟根据数值进行排序，默认为升序
# d = b.sort_values(2, ascending=False)  # 根据第二列降序排列所有行
# print(d)
# d = d.sort_values('a', axis=1, ascending=False)  # 根据a行降序排列所有列
# # NaN统一放到排序末尾

# # 基本统计分析
# a = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
# print(a)
# print(a.describe())
# print(type(a.describe()))
# print(a.describe()['count'])
# print(a.describe()['max'])
# b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])
# print(b)
# print(b.describe())
# print(b.describe().ix['max'])  # 返回一行的某个统计数据
# print(b.describe()[2])  # 返回一列的详细统计数据
#
# # 数据的累计统计分析，依次给出前1、2、...、n个数的信息
# print(b.cumsum())  # 累计和
# print(b.cumprod())  # 累计积
# # 滚动计算，依次计算相邻w个元素的信息
# print(b.rolling(2).sum())  # 默认在纵向上相邻2个元素的和

# 数据的相关分析
# 协方差矩阵cov()，即将每一个元素与它的均值和另一个元素的均值之间进行累计乘加操作，若协方差>0则正相关，<0负相关，而=0则无关
# pearson相关系数矩阵corr(),r在[-1,1]范围内，|r|若为0.8-1.0则极强相关，0.6-0.8强相关，0.4-0.6中等相关，0.2-0.4弱相关，0.0-0.2极弱相关或无相关
hprice = pd.Series([3.04, 22.93, 12.75, 22.6, 12.33], index=['2008', '2009', '2010', '2011', '2012'])
m2 = pd.Series([8.18, 18.38, 9.13, 7.83, 6.69], index=['2008', '2009', '2010', '2011', '2012'])
pearson = hprice.corr(m2)
print(pearson)
