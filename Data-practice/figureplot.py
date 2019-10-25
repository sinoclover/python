import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

data1 = pd.read_excel('file/check4.xlsx')
print(data1)

matplotlib.rcParams['font.family'] = 'SimHei'  # 字体名称
matplotlib.rcParams['font.style'] = 'italic'  # 字体风格
matplotlib.rcParams['font.size'] = '10'  # 字体大小
fig = plt.figure()
fig.set(alpha=0.2)

# 全勤率
# data1.plot(kind='bar')
# plt.show()

# x = data1.index
# y1 = data1['全勤']
# y2 = data1['有缺席']
# y3 = data1['全勤率']
# width = 0.35
#
# p1 = plt.bar(x, y1, width)
# p2 = plt.bar(x, y2, width, bottom=y1)
# for x, y in zip(x, y3):
#     plt.text(x, y, '{0:.2f}'.format(y), ha='center', va='bottom')
#
# plt.title('全勤情况')
# plt.ylabel('人数')
# plt.legend((p1[0], p2[0]), ('全勤', '有缺席'))
# plt.savefig('fig/1', dpi=300, bbox_inches='tight')
# plt.show()

# # 回收率
# x = data1.index
# y1 = data1['有效']
# y2 = data1['无效']
# y3 = data1['有效率']
# width = 0.35
#
# p1 = plt.bar(x, y1, width)
# p2 = plt.bar(x, y2, width, bottom=y1)
# for x, y in zip(x, y3):
#     plt.text(x, y, '{0:.2f}'.format(y), ha='center', va='bottom')
#
# plt.title('问卷回收情况')
# plt.ylabel('人数')
# plt.legend((p1[0], p2[0]), ('有效', '无效'))
# plt.savefig('fig/2', dpi=300, bbox_inches='tight')
# plt.show()

# 答题得分
data1.plot(kind='bar')
plt.title('调查问卷题目得分情况')
plt.xlabel('题目')
plt.ylabel('得分')
plt.savefig('fig/3', dpi=300, bbox_inches='tight')
plt.show()
