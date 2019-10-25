import pandas as pd
import numpy as np

# 读入数据
unames = ['user id', 'age', 'gender', 'occupation', 'zip code']
users = pd.read_table('data/ml-100k/u.user', sep=r'|', names=unames, engine='python')
rnames = ['user id', 'item id', 'rating', 'timestamp']
ratings = pd.read_table('data/ml-100k/u.data', sep='\t', names=rnames, engine='python')

# 为了判断性别与评分的关系，则将相关数据提取出来
users_df = pd.DataFrame()
users_df['user id'] = users['user id']
users_df['gender'] = users['gender']
ratings_df = pd.DataFrame()
ratings_df['user id'] = ratings['user id']
ratings_df['rating'] = ratings['rating']

# 合并数据
data_df = pd.merge(users_df, ratings_df)
gender_table = pd.pivot_table(data_df, index=['gender', 'user id'], values='rating')  # 得到的透明数据表仍是数据框

# 根据性别分离数据
Female_df = gender_table.query("gender=='F'")
Male_df = gender_table.query("gender=='M'")  # query方法使用布尔表达式查询相关列

# 按照性别计算标准差
Female_std = np.std(Female_df)
Male_std = np.std(Male_df)
print('Gender\nF\t{0:.6f}\nM\t{1:.6f}'.format(Female_std['rating'], Male_std['rating']))