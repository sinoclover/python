import pandas as pd
import numpy as np

# # pandas提供了高性能易用数据类型和分析工具
# # pandas主要提供了series和dataframe两种数据类型
#
# # series类型由一组数据与之相关的数据索引构成
# a = pd.Series([9, 8, 7, 6])
# print(a)  # dtype沿用了numpy库中的数据扩展类型
# b = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
# print(b)  # 自定义索引
#
# # 创建series类型的方法包括列表、标量值、字典、ndarray以及其他函数
# # 通过标量值创建
# s = pd.Series(25, index=[1, 2, 3])
# print(s)
# # 从字典创建
# d = pd.Series({'a': 9, 'b': 8, 'c': 7})
# print(d)
# e = pd.Series({'a': 9, 'b': 8, 'c':7}, index=['c', 'a', 'b', 'd'])
# print(e)  # 通过index调整顺序，即从字典中进行选择操作
# # 从ndarray创建
# n = pd.Series(np.arange(5))
# print(n)
# m = pd.Series(np.arange(5), index=np.arange(9, 4, -1))
# print(m)

# # series类型包括index和value两部分
# b = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
# print(b.index)
# print(b.values)
# # series类型的切片、运算仍是生成series类型，而选择其中的一个值则返回一个值
# print(b.get('f', 100))  # 查找f索引，若没有则返回默认值100
# # series类型的对齐
# a = pd.Series([1, 2, 3], ['c', 'd', 'e'])
# print(a+b)  # 求并集，自动对齐不同索引的数据
# # 定义series类型的name
# b.name = 'Series'
# b.index.name = 'Column'
# print(b)

# # dataframe类型是由共用相同索引的一组列组成，每列的值类型可以不同
# # dataframe可以由二维ndarray对象，由一维ndarray、列表、字典、元组或series构成的字典、由series类型或其他dataframe类型创建
# # 从二维ndarray对象创建
# d = pd.DataFrame(np.arange(10).reshape(2, 5))
# print(d)
# # 从一维ndarray对象字典创建
# dt = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#       'two': pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])}
# df1 = pd.DataFrame(dt)
# print(df1)
# df2 = pd.DataFrame(dt, index=['b', 'c', 'd'], columns=['two', 'three'])
# print(df2)
# # 从列表类型的字典创建
# dl = {'one': [1, 2, 3, 4], 'two': [9, 8, 7, 6]}
# df3 = pd.DataFrame(dl, index=['a', 'b', 'c', 'd'])
# print(df3)

# # dataframe实例的数据表达与获取
# d1 = {'城市': ['北京', '上海', '广州', '深圳', '沈阳'],
#       '环比': [101.5, 101.2, 101.3, 102.0, 100.1],
#       '同比': [120.7, 127.3, 119.4, 140.9, 101.4],
#       '定基': [121.4, 127.8, 120.0, 145.5, 101.6]}
# df = pd.DataFrame(d1, index=['c1', 'c2', 'c3', 'c4', 'c5'])
# # 获取数据框类型的相关属性，包括行列索引以及数据值
# print(df)
# print(df.index)
# print(df.columns)
# print(df.values)
# # 获取所需数据
# print(df['同比'])
# print(df.ix[2])  # 使用ix获取行元素
# print(df['同比'][2])  # 联合索引获取一个元素
#
# # 如何改变series和dataframe对象？对于增加或重排进行重新索引，对于删除进行drop
# # reindex改变或重排series和dataframe索引
# df = df.reindex(index=['c5', 'c4', 'c3', 'c2', 'c1'])
# print(df)
# df = df.reindex(columns=['城市', '同比', '环比', '定基'])
# print(df)
# new_col = df.columns.insert(4, '新增')
# new_df = df.reindex(columns=new_col, fill_value=200)
# print(new_df)  # series和dataframe的索引是Index类型，是不可修改的
# nc = df.columns.delete(2)
# ni = df.index.insert(5, 'c0')
# nd = df.reindex(index=ni, columns=nc).ffill()  # 将method单独使用
# print(nd)
# # 使用drop删除series和dataframe指定的行列索引
# print(nd.drop('c0'))
# print(nd.drop('同比', axis=1))
# a = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
# print(a)
# print(a.drop(['b', 'c']))

# pandas库数据类型的运算
# 算术运算根据行列索引，补齐后(NaN)运算，运算默认产生浮点数
a = pd.DataFrame(np.arange(12).reshape(3, 4))
print(a)
b = pd.DataFrame(np.arange(20).reshape(4, 5))
print(b)
print(a+b)
print(a*b)
print(b.add(a, fill_value=100))  # 将a与b之间缺少的数值用100来补齐
print(a.mul(b, fill_value=0))
c = pd.Series(np.arange(4))
print(c)
print(b-c)  # 不同维度间进行广播运算，一维series默认在轴1参与运算
print(b.sub(c, axis=0))
