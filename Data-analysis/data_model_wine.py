# 葡萄酒质量
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

# 将数据集读入到pandas数据框中
wine = pd.read_csv('data_model/winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')  # 将列名中的空格替换为下划线

# # 描述性统计
# # 显示所有变量的描述性统计量
# print(wine.describe())
# # 找出唯一值
# print(sorted(wine.quality.unique()))
# # 计算值的频率
# print(wine.quality.value_counts())
# # 分组、直方图和T检验
# # 按照葡萄酒类型显示质量的描述性统计量
# print(wine.groupby('type')[['quality']].describe().unstack('type'))
# # print(wine.groupby('type')[['quality']].describe())  # unstack将结果重新排列，显示在并排的两列中
# # 按照葡萄酒类型显示质量的特定分位数值
# print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))
# # 按照葡萄酒类型查看质量分布
# red_wine = wine.loc[wine['type'] == 'red', 'quality']
# white_wine = wine.loc[wine['type'] == 'white', 'quality']
# sns.set_style('dark')
# sns.distplot(red_wine, norm_hist=True, kde=False, color='red', label='Red wine')
# sns.distplot(white_wine, norm_hist=True, kde=False, color='white', label='White wine')
# plt.title('Distribution of Quality by wine Type')
# plt.xlabel('Quality Score')
# plt.ylabel('Density')
# plt.legend()
# plt.savefig('data_model/wine_dist', dpi=300, bbox_inches='tight')
# plt.show()
# # T检验两者的平均质量是否有所不同
# print(wine.groupby('type')[['quality']].agg('std'))  # agg()是横向的列之间的聚合
# tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
# print('tstat: {0:.3f} pvalue: {1:.4f}'.format(tstat, pvalue))

# 计算所有变量的相关矩阵
print(wine.corr())  # 通过corr()计算出数据集中所有变量两两之间的线性相关性
# 从数据中取出一个小样本来进行绘图
# 使用数据框索引和随机函数随机选择
def take_sample(data_frame, replace=False, n=200):
    return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]
reds_sample = take_sample(wine.loc[wine['type'] == 'red', :])
whites_sample = take_sample(wine.loc[wine['type'] == 'white', :])
wine_sample = pd.concat([reds_sample, whites_sample])
# 在wine数据框中创建新列，并对新列进行填充，根据此行的索引值是否在抽样数据的索引值中分别设为1和0
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1., 0.)
print(pd.crosstab(wine.in_sample, wine.type, margins=True))  # 使用crosstab进行确认

# 成对变量之间的关系和相关性
# # 查看成对变量之间的关系
# sns.set_style('dark')
# g = sns.pairplot(wine_sample, kind='reg', plot_kws={'ci': False, 'x_jitter': 0.25, 'y_jitter': 0.25}, hue='type',
#                  diag_kind='hist', diag_kws={'bins': 10, 'alpha': 1.0}, palette=dict(red='red', white='white'),
#                  markers=['o', 's'], vars=['quality', 'alcohol', 'residual_sugar'])
# print(g)
# plt.suptitle('Histograms and Scatter Plots of Quality, Alcohol, and Residual Sugar', fontsize=14,
#              horizontalalignment='center', verticalalignment='top', x=0.5, y=0.999)
# plt.savefig('data_model/wine_corr', dpi=300, bbox_inches='tight')
# plt.show()

# 使用最小二乘估计进行线性回归
# 相关系数和两两变量之间的统计图有助于对两个变量之间的关系进行量化和可视化，但不能测量出每个自变量在其他自变量不变时与因变量之间的关系。
# 线性回归模型表示观测y服从均值为μ方差为σ2的正态分布（高斯分布），其中μ依赖于自变量，σ2为一个常数，即根据一个自变量的值可以得到一个具体的质量评分
# 类似R语言的回归公式定义
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + ' \
             'residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'

# # 拟合一个普通最小二乘回归模型
# lm = ols(my_formula, data=wine).fit()
# # 或者使用广义线性模型(glm)语法进行线性回归
# # lm = glm(my_formula, data=wine, family=sm.families.Gaussian()).fit()
# print(lm.summary())  # 打印结果的摘要信息
# print('\nQuantities you can extract from the result:\n{0}'.format(dir(lm)))  # 打印一个列表包含从对象中提取出的所有数值信息
# print('\Coefficients:\n{0}'.format(lm.params))  # 以序列的形式返回模型系数
# print('\nCoefficient Std Errors:\n{0}'.format(lm.bse))  # 以序列的形式返回模型系数的标准差
# print('\nAdj. R-squared:\n{:.2f}'.format(lm.rsquared_adj))  # 返回修正R方
# print('\nF-statistic: {0:.1f}   P-value: {1:.2f}'.format(lm.fvalue, lm.f_pvalue))  # 分别返回F统计量和它的p值
# print('\nNumber of obs: {0}   Number of fitted values: {1}'.format(lm.nobs, len(lm.fittedvalues)))  # 返回拟合值

# 对自变量进行标准化后再进行最小二乘回归
# 最小二乘回归是通过使残差平方和最小化来估计位置参数值的，残差指的是自变量观测值和拟合值之间的差别
# 残差的大小是依赖于自变量的测量单位的，所以如果自变量的测量单位相差很大的话，将自变量标准化后，就可以更容易对模型进行解释了
# 先从自变量的每个观测值中减去均值，然后再除以这个自变量的标准差。自变量标准化后其均值为0，标准差为1，即标准化为z-scores
# print(wine) # 确认是否包括in_sample
# 创建一个序列来保存质量数据
dependent_variables = wine['quality']
# 创建数据框来保存初始数据集中处理quanlity,type和in_sample之外的所有变量
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
# 对自变量进行标准化
# 对每个变量在每个观测中减去变量的均值，并且使用结果除以变量的标准差
independent_variables_standardized = (independent_variables - independent_variables.mean()) / independent_variables.std()
# 将因变量quality作为一列添加到自变量数据框中
# 创建一个带有标准化自变量的新数据集
wine_standardized = pd.concat([dependent_variables, independent_variables_standardized], axis=1)
# 重新进行线性回归
lm_standardized = ols(my_formula, data=wine_standardized).fit()
print(lm_standardized.summary())

# 预测
# 即使用没有用来拟合的新数据进行预测，在此使用数据集中的前10个观测创建10个新观测，其中只包括模型中使用的自变量
new_observations = wine.ix[wine.index.isin(range(10)), independent_variables.columns]
print(new_observations)
# 基于新观测中的葡萄酒特性预测质量评分
y_predicted = lm_standardized.predict(new_observations)
# 打印预测值
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)
