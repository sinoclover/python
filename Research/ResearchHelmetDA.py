import numpy as np
import pandas as pd

# # 载入原始数据
# rawdata = pd.read_csv('data/data_for_helmet_clear2.csv')
# # 选取用户行为数据
# tempdata = rawdata.loc[:, ['id', 'publishedtime', 'p_views', 'p_appreciations', 'p_comments', 'createdtime',
#                            'followers', 'u_views', 'u_appreciations', 'R', 'G', 'B', 'alt']]
# print(tempdata.head(5))
# tempdata.to_csv('data/data_final.csv', index=None)

# 载入用户行为数据
data = pd.read_csv('data/data_final.csv', index_col=None)
print(data.head(5))

data_user = data.loc[:, ['publishedtime', 'p_views', 'p_appreciations', 'p_comments', 'createdtime',
                         'followers', 'u_views', 'u_appreciations']]
# 基础统计量分析
statistics = data_user.describe()
print('The basic statistics:\n', statistics)
# # 数据规范化（归一化）
# # 采用01规范化
data_user = data_user / data_user.sum()
print(data_user.head(5))
v = data_user['p_views']*0.125+data_user['p_appreciations']*0.140+data_user['p_comments']*0.130+\
    data_user['followers']*0.098+data_user['u_views']*0.118+data_user['u_appreciations']*0.117+\
    data_user['createdtime']*0.143+data_user['publishedtime']*0.129
v = v / v.sum()
print('项目影响力值：\n', v)
data_user['V']=v
data_user.to_csv('data/data_final2.csv', index=None)