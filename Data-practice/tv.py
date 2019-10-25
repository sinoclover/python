import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 数据导入
quarter3 = pd.read_csv('file/tv_quarter3.csv', index_col=None)
quarter3.index = range(1, len(quarter3)+1)
quarter4 = pd.read_csv('file/tv_quarter4.csv', index_col=None)
quarter4.index = range(1, len(quarter4)+1)
print(quarter3)

# # 面向对象的绘图方式
# # 散点图以及回归线
# r3 = quarter3['收视率']
# s3 = quarter3['收视份额']
# r4 = quarter4['收视率']
# s4 = quarter4['收视份额']
# fn_linear3 = np.poly1d(np.polyfit(s3, r3, deg=1))
# fn_linear4 = np.poly1d(np.polyfit(s4, r4, deg=1))

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1.plot(s3, r3, 'bo', s3, fn_linear3(s3), 'b-', linewidth=2., label='quarter3')
# ax1.plot(s4, r4, 'go', s4, fn_linear4(s4), 'g-', linewidth=2., label='quarter4')
# ax1.xaxis.set_ticks_position('bottom')
# ax1.yaxis.set_ticks_position('left')
# ax1.set_title('Scatter Plots Regression Lines')
# # 图像设置
# plt.ylabel('rating')
# plt.xlabel('share')
# plt.legend(loc='best')
# plt.savefig('fig/scatter_plot', dpi=300, bbox_inches='tight')
# plt.show()

# 柱状图
name3 = quarter3['节目名称']
r3 = quarter3['收视率']
s3 = quarter3['收视份额']
# 根据name3排序第四季度数据进行比较
quarter4['节目名称'] = quarter4['节目名称'].astype('category')
quarter4['节目名称'].cat.reorder_categories(name3, inplace=True)
quarter4.sort_values('节目名称', inplace=True)
quarter4.index = range(1, len(quarter4)+1)
print(quarter4)
r4 = quarter4['收视率']
s4 = quarter4['收视份额']

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# width = 0.35
# ax1.bar(quarter3.index - width/2, r3, width, align='center', color='SkyBlue', label='quarter3')
# ax1.bar(quarter4.index + width/2, r4, width, align='center', color='IndianRed', label='quarter4')
# ax1.xaxis.set_ticks_position('bottom')  # 设置刻度线位置
# ax1.yaxis.set_ticks_position('left')
# plt.xticks(quarter3.index, name3, rotation=45, fontsize=5, fontproperties='SimHei')  # 将x轴刻度线标签改为客户实际名称
# plt.xlabel('Program Name')
# plt.ylabel('Rating')
# plt.title('Program rating')
# plt.legend(loc='best')
# plt.savefig('fig/bar', dpi=300, bbox_inches='tight')
# plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111)
width = 0.35
ax1.bar(quarter3.index - width/2, s3, width, align='center', color='SkyBlue', label='quarter3')
ax1.bar(quarter4.index + width/2, s4, width, align='center', color='IndianRed', label='quarter4')
ax1.xaxis.set_ticks_position('bottom')  # 设置刻度线位置
ax1.yaxis.set_ticks_position('left')
plt.xticks(quarter3.index, name3, rotation=45, fontsize=5, fontproperties='SimHei')  # 将x轴刻度线标签改为客户实际名称
plt.xlabel('Program Name')
plt.ylabel('Share')
plt.title('Program share')
plt.legend(loc='best')
plt.savefig('fig/bar2', dpi=300, bbox_inches='tight')
plt.show()
