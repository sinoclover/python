import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

churn = pd.read_csv('data_model/churn.csv', sep=',', header=0)
# 格式化列标题
churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ', '_').str.replace('\'', '').str.strip('?')]
# 创建新的数值型二值变量
churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
# 检查数据框的前几行数据
# print(churn.head())

# # 通过计算流失客户和未流失客户的描述性统计量，来找出区别。即将数据分为两组，并为每个分组中的特定的列计算总数、均值和标准差
# # 为分组数据计算描述性统计量
# print(churn.groupby(['churn'])[['day_charge', 'eve_charge', 'night_charge', 'intl_charge', 'account_length',
#                                 'custserv_calls']].agg(['count', 'mean', 'std']))
# # 为不同的变量计算不同类型的多个统计量
# print(churn.groupby(['churn']).agg({'day_charge': ['mean', 'std'], 'eve_charge': ['mean', 'std'],
#                                     'night_charge': ['mean', 'std'], 'intl_charge': ['mean', 'std'],
#                                     'account_length': ['count', 'min', 'max'], 'custserv_calls': ['count', 'min', 'max']}))

# 创建total_charges，将其分为5组，并为每一组计算统计量
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + churn['night_charge'] + churn['intl_charge']

# # 使用等宽分箱法将数据分为5组
# factor_cut = pd.cut(churn.total_charges, 5, precision=2)
# # 创建函数为每个分组返回一个统计量字典
# def get_stats(group):
#     return {'min': group.min(), 'max': group.max(), 'count': group.count(), 'mean': group.mean(), 'std': group.std()}
# # 将客户服务通话次数也分成5组
# grouped = churn.custserv_calls.groupby(factor_cut)
# print(grouped.apply(get_stats).unstack())
# # 将客户服务通话数据按照分位数进行分组，即使用等深分箱法将数据分为5组，并为每个分组计算统计量
# factor_qcut = pd.qcut(churn.account_length, [0., 0.25, 0.5, 0.75, 1.])
# grouped = churn.custserv_calls.groupby(factor_qcut)
# print(grouped.apply(get_stats).unstack())
#
# # 创建二值指标变量
# # 为intl_plan和vmail_plan创建二值虚拟指标变量
# intl_dummies = pd.get_dummies(churn['intl_plan'], prefix='intl_plan')
# vmail_dummies = pd.get_dummies(churn['vmail_plan'], prefix='vmail_plan')
# churn_with_dummies = churn[['churn']].join([intl_dummies, vmail_dummies])
# print(churn_with_dummies.head())
#
# # 将total_charge列按照四分位数进行划分，并使用qcut_names中的名称对四分位数进行标记
# qcut_names = ['1st', '2nd', '3rd', '4th']
# total_charges_quartiles = pd.qcut(churn.total_charges, 4, labels=qcut_names)
# dummies = pd.get_dummies(total_charges_quartiles, prefix='total_charges')
# churn_with_dummies = churn.join(dummies)
# print(churn_with_dummies.head())

# # 创建透视表
# print(churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))
# print(churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))
# print(churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'],
#                         aggfunc='mean', fill_value='NaN', margins=True))

# 因为因变量为一个二值变量，因此要将预测值限制在0,1之间，通过逻辑斯蒂回归进行预测
# 通过使用逻辑函数的反函数估计改了的方式，来测量自变量和二值型因变量之间的关系。该函数可以将连续的值转换为0,1之间的值，以表示某种结果的概率。
dependent_variable = churn['churn01']
independent_variable = churn[['account_length', 'custserv_calls', 'total_charges']]  # 设置3列自变量
independent_variable_with_constant = sm.add_constant(independent_variable, prepend=True)  # 通过add_constant向输入变量中加入一列1
logit_model = sm.Logit(dependent_variable, independent_variable_with_constant).fit()

print(logit_model.summary2())  # 打印模型摘要信息
print('\nQuantities you can extract from the result:\n{0}'.format(dir(logit_model)))
print('\nCoefficients:\n{0}'.format(logit_model.params))  # 以序列的形式返回模型系数
print('\nCoefficient Std Errors:\n{0}'.format(logit_model.bse))  # 以序列的形式返回系数标准差


# 系数解释
# 逻辑斯蒂函数的反函数是曲线，这说明自变量一个单位的变化所造成的因变量变化不是一个常数，必须选择使用哪个函数值来评价自变量对成功概率的影响
# 和线性回归一样，截距系数的意义是当所有自变量为0时成功的概率，有些时候0是没有意义的，所以另外一种方式是当自变量都取均值时，看看函数的值有何意义
# 函数将线性模型得出的连续预测值转换为0和1之间的概率值
def inverse_logit(model_value):
    from math import exp
    return (1.0 / (1.0 + exp(-model_value)))


# 计算所有自变量取均值时观测的预测值
at_means = float(logit_model.params[0]) + float(logit_model.params[1]) * float(churn['account_length'].mean()) + \
           float(logit_model.params[2]) * float(churn['custserv_calls'].mean()) + float(logit_model.params[3]) * \
           float(churn['total_charges'].mean())
print('Probability of churn at mean values: {0:.2f}'.format(inverse_logit(at_means)))

# 当客户服务通话次数在均值的基础上发生一个单位的变化时，对客户流失概率造成的影响
cust_serv_mean = float(logit_model.params[0]) + float(logit_model.params[1]) * float(churn['account_length'].mean()) + \
                 float(logit_model.params[2]) * float(churn['custserv_calls'].mean()) + float(logit_model.params[3]) * \
                 float(churn['total_charges'].mean())
cust_serv_mean_minus_one = float(logit_model.params[0]) + float(logit_model.params[1]) * float(churn['account_length'].mean()) + \
                           float(logit_model.params[2]) * float(churn['custserv_calls'].mean() - 1) + float(logit_model.params[3]) * \
                           float(churn['total_charges'].mean())
print('Probability of churn when account length changes by 1: {0:.2f}'.format(inverse_logit(cust_serv_mean) -
                                                                              inverse_logit(cust_serv_mean_minus_one)))

# 预测
# 在数据集中创建10个‘新’观测
new_observations = churn.ix[churn.index.isin(range(10)), independent_variable.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
# 基于新观测的账户特性，预测客户流失可能性
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)