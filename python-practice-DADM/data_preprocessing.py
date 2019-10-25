                                                                          # # 数据预处理
# # 数据清洗之缺失值处理——插值方法
# # 用拉格朗日插值法进行插补
# import pandas as pd
# from scipy.interpolate import lagrange  # 导入拉格朗日插值函数
#
# input_file = 'data/chapter4/catering_sale.xls'
# output_file = 'tmp/sales.xls'
# data = pd.read_excel(input_file)
# # data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None # 过滤异常值，将其变为空值
# # data.loc[data[(data[u'销量'] < 400) | (data[u'销量'] > 5000)].index, u'销量'] = None
# outliers = data[(data[u'销量'] < 400) | (data[u'销量'] > 5000)]  # 找出异常值
# data.loc[outliers.index, u'销量'] = None  # 将异常值赋予空值
# # 自定义列向量插值函数
# # s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
# # 对于该数据的插值而言，x与y不具有函数关系，同时该函数方法相当于切片，那么x值应统一而非线性递增
# def ployinterp_column(s, n, k=5):
#     y = s.reindex(list(range(n-k, n)) + list(range(n+1, n+1+k)))  # 去除列向量里n以外的数
#     y.index = list([0, 1, 2, 3, 4, 6, 7, 8, 9, 10])
#     y = y.fillna(y.mean())
#     print(y)
#     return lagrange(y.index, list(y))(5)
#
# # 逐个元素判断是否需要插值
# for i in data.columns:
#     for j in range(len(data)):
#         if (data[i].isnull())[j]:
#             data.loc[j, i] = ployinterp_column(data[i], j)
#             print(data.loc[j, i])
#
# data.to_excel(output_file)

# # 数据变换之数据规范化
# import pandas as pd
# import numpy as np
#
# datafile = 'data/chapter4/normalization_data.xls'
# data = pd.read_excel(datafile, header=None)
# print(data)
#
# # 最小-最大规范化，即离差标准化
# print((data - data.min()) / (data.max() - data.min()))
# # 零-均值规范化，即标准差规范化
# print((data - data.mean()) / data.std())
# # 小数定标规范化
# # ceil()计算大于等于该值的最小整数
# # log10()计算以10为底的自然对数
# # 以x=100为例，np.log10(100)=2, np.ceil(2)=2, 即x/10**2=x/100=1，则将值映射到[-1,1]上
# print(data / 10**np.ceil(np.log10(data.abs().max())) )

# # 数据变换之数据离散化
# import pandas as pd
#
# datafile = 'data/chapter4/discretization_data.xls'
# data = pd.read_excel(datafile)
# data = data[u'肝气郁结证型系数']  # 转化为Series
# k = 4  # 人为分配区间个数
#
# # 等宽离散化，根据值域进行分区，每个区间中值的个数可能不一致。受离群点影响较大。
# d1 = pd.cut(data, k, labels=range(k))  # 各个类别依次命名为0123
#
# # 等频率离散化，每个区间个数一致
# w = [1.0*i/k for i in range(k+1)]
# w = data.describe(percentiles=w)[4:4+k+1]
# d2 = pd.cut(data, w, labels=range(k))
#
# # 聚类
# from sklearn.cluster import KMeans
# kmodel = KMeans(n_clusters=k)  # 建立模型
# kmodel.fit(data.values.reshape(len(data), 1))  # 训练模型
# c = pd.DataFrame(kmodel.cluster_centers_).sort_values(0)  # 输出聚类中心，并且排序（默认是无序的）
# w = c.rolling(window=2).mean().iloc[1:]  # 相邻两项求终点，作为边界点
# w = [0] + list(w[0]) + [data.max()]
# d3 = pd.cut(data, w, labels=range(k))
#
# # 自定义作图函数来显示聚类结果
# def cluster_plot(d, k):
#     import matplotlib.pyplot as plt
#     plt.rcParams['font.sans-serif'] = ['SimHei']
#     plt.rcParams['axes.unicode_minus'] = False
#
#     plt.figure()
#     for j in range(k):
#         plt.plot(data[d==j], [i for i in d[d==j]], 'o')
#     plt.ylim(-0.5, k-0.5)
#     return plt
#
# cluster_plot(d1, k).show()
# cluster_plot(d2, k).show()
# cluster_plot(d3, k).show()

# # 数据变换之属性构造
# # 线损率属性构造
# import pandas as pd
#
# input_file = 'data/chapter4/electricity_data.xls'
# output_file = 'tmp/electricity_data_new.xls'
#
# data = pd.read_excel(input_file)
# data[u'线损率'] = (data[u'供入电量'] - data[u'供出电量']) / data[u'供入电量']
#
# data.to_excel(output_file, index=False)

# # 数据规约之主成分分析PCA
# # 主成分分析降维
# import pandas as pd
# from sklearn.decomposition import PCA
#
# input_file = 'data/chapter4/principal_component.xls'
# output_file = 'tmp/dimention_reducted.xls'
# data = pd.read_excel(input_file, header=None)
#
# # pca = PCA()
# # pca.fit(data)
# # print(pca.components_)  # 返回模型的各个特征向量
# # print(pca.explained_variance_ratio_)  # 返回各个成分各自的方差百分比
#
# # 可以看出8个特征根对应的各个成分的方差百分比（贡献率），方差百分比越大说明向量的权重越大
# # 前4个主成分累计贡献率已经很高，可以选择3个主成分进行计算，即重新建立PCA模型
# pca1 = PCA(3)
# pca1.fit(data)
# print(pca1.components_)  # 返回模型的各个特征向量
# print(pca1.explained_variance_ratio_)  # 返回各个成分各自的方差百分比
#
# # 用该pca1模型来降低data维度
# low_d = pca1.transform(data)
# pd.DataFrame(low_d).to_excel(output_file)
# pca1.inverse_transform(low_d)  # 必要时可以复原数据
# print(low_d)
