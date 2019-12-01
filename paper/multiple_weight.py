import pandas as pd

# 读取AHP和FA的权重数据
data = pd.read_excel('data/weight.xlsx')
print(data)
AHP = data['AHP']
FA = data['FA']

# 计算综合权重值
product = AHP * FA
METHOD = product / sum(product)
print('\n主客观综合权重：')
print(METHOD)
data['METHOD'] = METHOD
print(data)

# 输出综合权重
data.to_csv('data/multiple_weight.csv', index=None)
