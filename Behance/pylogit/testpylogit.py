import numpy as np
import pandas as pd
import pylogit as pl
from numpy.matlib import repmat  # repmat具有矩阵复制的功能
from collections import OrderedDict

# 导入数据及数据处理
# 对于数据而言，每个人都拥有一个选择集，即备选项ALT；而每个个体形成一个选择情境，即GROUP
# 即pylogit要求提供标识选择场景编号的列GROUP和标识备选项编号的列ALT
data = pd.read_excel('data/demoLAB.xlsx')
data['ALT'] = repmat(np.array([1, 2, 3, 4, 5]).reshape(5, 1), 50, 1)
data['GROUP'] = repmat(np.array([x+1 for x in range(50)]).reshape(50, 1), 1, 5).reshape(250, 1)
# data.to_csv('demoLAB.csv')
# print(data)

# # 其他数据
# datar = pd.read_excel('demoR.xlsx', index_col=0)
# print(datar)
# datar.to_csv('demoR.csv')


# 设置模型配置specification
# pylogit通过有序字典来配置
# 每一个key都是要引入的变量，这个变量必须是数据中的一个列名，与key对应的value是一个list，list中的每个元素对应于一个模型系数
# 我们也可以设定一个变量名称字典，与模型匹配字典使用相同的key，其value也是一个list，可以以字符串的形式定义每个模型系数的名称
# 重点是在配置模型的过程中，如果系数是方案系数（系数保持不变），那么要使用一个内层list表示哪些备选项的效用中引入这个系数。
spec = OrderedDict()
var_names = OrderedDict()
vars = ['L', 'A', 'B']
for var in vars:
    spec[var] = [[1, 2, 3, 4, 5]]
    var_names[var] = ['beta of ' + var]

# 建立模型object
# data是数据，alt_id_col是标识备选项名称或编号的列名，obs_id_col是标识选择场景观测编号的列名，choicec_col是标识选择结果0/1的列名
# specification是设定好的模型配置有序字典，model_type选择MNL是一般的logit模型，names是设定好的变量名
model = pl.create_choice_model(data=data, alt_id_col='ALT', obs_id_col='GROUP', choice_col='MODE',
                               specification=spec, model_type='MNL', names=var_names)
# 注意进行估计时需要参数的初始估计值，可以设为0
model.fit_mle(np.zeros(3))
model.print_summaries()
# 结果包括对数似然值、R2、3个参数的估计值、t检验、p值、robust统计量等。
#
# # 通过DIR查看更多信息
print(dir(model))
# print(model.chi_square)
print(model.coefs)
# print(model.cov)
# print(model.params.values)
# print(model.pvalues)

# # 利用模型进行预测，需要输入一个以同样方式组织的数据
# print(model.predict(data.iloc[0:5]))
# print(model.predict(data.iloc[0:5], choice_col='MODE', return_long_probs=False))