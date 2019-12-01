import pandas as pd

# # 1调查问卷案例影响力计算
# # 读取问卷案例数据
# raw_data = pd.read_excel('data/question_sample.xlsx')
# # 选择相关用户行为数据
# data = raw_data.loc[:, ['ID', 'duration', 'views', 'appreciations', 'comments', 'ownerDuration',
#                          'ownerFollowers', 'ownerViews', 'ownerAppreciations']]
# data_user = raw_data.loc[:, ['duration', 'views', 'appreciations', 'comments', 'ownerDuration',
#                          'ownerFollowers', 'ownerViews', 'ownerAppreciations']]
# print(data_user.head(5))
# # 基础统计量分析
# statistics = data_user.describe()
# print('The basic statistics:\n', statistics)
# # # 数据规范化（采用01规范化)
# # data_user = data_user / data_user.sum()
# # print(data_user.head(5))
# # 计算案例影响力
# v = data_user['views']*0.0564+data_user['appreciations']*0.1890+data_user['comments']*0.4513 +\
#     data_user['ownerViews']*0.0282+data_user['ownerAppreciations']*0.0782+data_user['ownerFollowers']*0.1061 +\
#     data_user['duration']*0.0493+data_user['ownerDuration']*0.0415
# # v = v / v.sum()
# print('项目影响力值：\n', v)
# data['V'] = v
# print(data)
# data.to_csv('data/question_effect.csv', index=None)

# 2色彩设计应用案例影响力计算
# 读取案例数据
data = pd.read_csv('data/helmet_sample.csv')
# 选择用户行为数据
data_user = data.loc[:, ['duration', 'views', 'appreciations', 'comments', 'ownerDuration',
                      'ownerFollowers', 'ownerViews', 'ownerAppreciations']]
print(data_user.head(5))
# 基础统计量分析
statistics = data_user.describe()
print('The basic statistics:\n', statistics)
# 计算案例影响力
v = data_user['views']*0.0564+data_user['appreciations']*0.1890+data_user['comments']*0.4513 +\
    data_user['ownerViews']*0.0282+data_user['ownerAppreciations']*0.0782+data_user['ownerFollowers']*0.1061 +\
    data_user['duration']*0.0493+data_user['ownerDuration']*0.0415
# v = v / v.sum()
print('项目影响力值：\n', v)
data['V'] = v
print(data.head(5))
data.to_csv('data/helmet_effect.csv', index=None)

