# 箱型图
import pandas as np
import matplotlib.pyplot as plt

data = np.read_excel('data/score.xlsx', index_col='Name')
# # 使用pandas自动作图
# data.boxplot()
# plt.xlabel('Subject')
# plt.ylabel('Score')
# plt.savefig('fig/score')
# plt.show()

# 使用plt作图
# xticks = data.columns.tolist() # 可以获取列索引的列表
plt.boxplot(x=data.values, labels=data.columns, whis=1.5)
plt.title('Score Report')
plt.xlabel('Subject')
plt.ylabel('Score')
plt.savefig('fig/score2')
plt.show()