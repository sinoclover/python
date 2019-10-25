# 用户行为数据探索框架（暂时使用小样本进行测试）
import numpy as np
import pandas as pd
import time, datetime
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# 载入原始数据
rawdata = pd.read_csv('project/data_helmet.csv')
# print(rawdata)
# 选取用户行为数据
tempdata = rawdata.loc[:, ['ID', 'publishedTime', 'views', 'appreciations', 'comments', 'followers']]
# print(tempdata)

# 将发布时间转换为发布时长并加入数据框中
now = datetime.date(2019,5,1)
duration = []
pbtime = tempdata['publishedTime']
for t in pbtime:
    timearray = time.strptime(str(t), '%Y%m%d')
    pre = datetime.date(timearray.tm_year, timearray.tm_mon, timearray.tm_mday)
    delta_t = now - pre
    duration.append(delta_t.days)
dur = {'duration': duration}
dur = pd.DataFrame(dur)
frames = [tempdata, dur]
data = pd.concat(frames, axis=1)
data = data.drop('publishedTime', axis=1)
print(data)

# 统计量分析
statistics = data.describe()
print('The basic statistics:\n', statistics)

# 相关性分析
correlation = data.corr()
print('The variables corr:\n', correlation)
# 总览数据相关性热力图
fig = plt.figure()
fig.set(alpha=0.2)
sns.heatmap(correlation, vmin=-1, vmax=1, annot=True, square=True)
plt.savefig('fig/Corr', dpi=300, bbox_inches='tight')
