# 用户行为数据探索框架
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
# 载入原始数据
rawdata = pd.read_csv('data/data_for_useractID.csv')
print(rawdata.head(5))
# 选取用户行为数据
tempdata = rawdata.loc[:, ['duration', 'views', 'appreciations', 'comments', 'ownerDuration', 'ownerFollowings',
                           'ownerFollowers', 'ownerViews', 'ownerAppreciations', 'ownerComments']]
# tempdata['views'] = tempdata['views'] / tempdata['duration']
# tempdata['appreciations'] = tempdata['appreciations'] / tempdata['duration']
# tempdata['comments'] = tempdata['comments'] / tempdata['duration']
# tempdata['ownerFollowings'] = tempdata['ownerFollowings'] / tempdata['ownerDuration']
# tempdata['ownerFollowers'] = tempdata['ownerFollowers'] / tempdata['ownerDuration']
# tempdata['ownerViews'] = tempdata['ownerViews'] / tempdata['ownerDuration']
# tempdata['ownerAppreciations'] = tempdata['ownerAppreciations'] / tempdata['ownerDuration']
# tempdata['ownerComments'] = tempdata['ownerComments'] / tempdata['ownerDuration']
# tempdata = tempdata.loc[:, ['views', 'appreciations', 'comments', 'ownerFollowings',
#                            'ownerFollowers', 'ownerViews', 'ownerAppreciations', 'ownerComments']]
print(tempdata.head(5))
tempdata.to_csv('data/data_useractID.csv', index=None)

# # 数据分析及可视化
# # 载入用户行为数据
# data_user = pd.read_csv('data/data_useractall.csv', index_col=None)
# # print(data_user.head(5))
#
# # 基础统计量分析
# statistics = data_user.describe()
# print('The basic statistics:\n', statistics)
#
# # 数据规范化（归一化）
# # 采用零-均值规范化
# data_user = (data_user - data_user.mean()) / data_user.std()
# # print(data_user.head(5))
#
# # # 模拟R语言中ggplot2风格图形
# # plt.style.use('ggplot')
# # # 相关性分析
# # correlation = data_user.corr()
# # print('The variables corr:\n', correlation)
# # # 总览数据相关性热力图
# # fig = plt.figure()
# # fig.set(alpha=0.2)
# # sns.heatmap(correlation, vmin=-1, vmax=1, annot=True, square=True)
# # plt.savefig('fig/Corr_200user1', dpi=300, bbox_inches='tight')
# # # 成对变量之间的散点图和单变量直方图
# # sns.pairplot(data_user)
# # plt.savefig('fig/Corr_200user2', dpi=300, bbox_inches='tight')
#
# # PCA数据规约
# pca = PCA()
# pca.fit(data_user)
# # 协方差矩阵
# M = pca.get_covariance()
# print('协方差矩阵：\n', M)
# # 模型各个特征向量
# V = pca.components_
# print('各个特征向量:\n',V)
# # 特征值
# N = pca.explained_variance_
# print('各个特征值:\n', N)
# # 各个成分各自的方差百分比（贡献率）
# R = pca.explained_variance_ratio_
# print('查看主成分贡献率以选择主成分个数：\n', R)
#
# # PCA降维
# pca = PCA(2)
# pca.fit(data_user)
# # 查看降维后的主成分贡献率
# r = pca.explained_variance_ratio_
# print('主成分贡献率：\n', r)  # 主成分的方差百分比（贡献率）
# # 主成分的特征向量v
# v = pca.components_
# print('主成分特征向量：\n', v)
# n = pca.explained_variance_
# print('主成分特征值：\n', n)
# # # 降维数据
# # z = pca.transform(data_user)
# # print('pca(X):\n', z)
# # # 验证，Z（降维数据）= X（原数据data_user）* V（特征向量）
# # z1 = np.dot(data_user, v.T)
# # print('验证降维数据z:\n', z1)
# # 计算主成分矩阵
# load = np.array([math.sqrt(n[0]) * v[0], math.sqrt(n[1]) * v[1]])
# print('主成分矩阵：\n', load)
# # 计算主成分得分矩阵
# score = np.array([v[0] / math.sqrt(n[0]), v[1] / math.sqrt(n[1])])  # 根据情况翻转向量方向
# print('主成分得分矩阵：\n', score)
#
# # 根据主成分得分矩阵，结合方差贡献率建立综合模型系数
# sum_r = sum(r)
# print('总方差贡献率：\n', sum_r)
# coef = np.array((score[0]*r[0] + score[1]*r[1]) / sum_r)
# print(coef)
# # 系数归一化
# sum_coef = sum(coef)
# coef = coef / sum_coef
# print('模型系数：\n', coef)



