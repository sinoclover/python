import numpy as np
import pandas as pd
import pylogit as pl
from collections import OrderedDict
import math
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('data/demoR.csv')
print(data)

# # 使用pylogit中的MNL进行验证R中multinom()方法
# spec = OrderedDict()
# var_names = OrderedDict()
# vars = ['l', 'a', 'b']
# for var in vars:
#     spec[var] = [[1, 2, 3, 4, 5]]
#     var_names[var] = ['beta of ' + var]
# model = pl.create_choice_model(data=data, alt_id_col='alt', obs_id_col='chid', choice_col='choice',
#                                specification=spec, model_type='MNL', names=var_names)
# model.fit_mle(np.zeros(3))
# model.print_summaries()

# 利用基线logit进行线性计算
data2 = data[data.choice == True]
data2.reset_index(drop=True, inplace=True)
print(data2)

# 计算概率
# 计算总数
total = len(data2.alt)
print(total)
# 选择概率
dic = {}
for i in data2.alt:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
key = sorted(dic)
print(key)
print(dic)

# logit计算
p = []
for i in key:
    pr = dic[i] / 10
    p.append(pr)
print(p)
# 以方案5的概率p5 = 0.2为标准
p = [i / 0.2 for i in p]
print(p)
logitp = [math.log(i, math.e) for i in p]
print(logitp)

# 存储色彩变量
data3 = data2.drop('chid', axis=1)
data3 = data3.drop('choice', axis=1)
data3 = data3.drop_duplicates()
data3.reset_index(drop=True, inplace=True)
print(data3)
dl = [i - 94 for i in data3.l]
da = [i - -6 for i in data3.a]
db = [i - 2 for i in data3.b]
dlab = {'dl': dl, 'da': da, 'db':db}
frames_lab = pd.DataFrame(dlab)
print(frames_lab)
add_dlab = [data3, frames_lab]
add_dlab = pd.concat(add_dlab, axis=1)
print(add_dlab)

# 组合数据
logit = {'logit_value': logitp}
logit_value = pd.DataFrame(logit)
frames = [add_dlab, logit_value]
frames = pd.concat(frames, axis=1)
print(frames)
frames.to_csv('data/demolm.csv')

# 多元线性回归
x = frames[['dl', 'da', 'db']]
y = frames['logit_value']
print(x)
print(y)
lm = LinearRegression()
lm.fit(x, y)
# 预测及预测后的均方误差和R2评估

# 回归结果
# 系数
print('Cofficients: \n', lm.coef_)


