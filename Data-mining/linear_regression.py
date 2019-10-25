import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
print(boston.keys())  # 查看数据集的相关信息
print(boston.feature_names)  # 查看数据集的自变量因素

# 设置自变量与因变量
# x = boston.data[:, 5].reshape(-1, 1)  # 选取RM即住宅平均房间数作为自变量，通过reshape或np.newaxis的方式将数据单独提出
x = boston.data[:, np.newaxis, 5]
y = boston.target

# 建立线性回归模型
lm = LinearRegression()  # 声明并初始化一个线性回归模型
lm.fit(x, y)  # 拟合训练模型
r2 = lm.score(x, y)  # 返回回归方程的系数
print(u'the coefficient of determination (R^2) of the prediction is: {0:.2f}'.format(r2))

# 回归方程数据可视化
plt.scatter(x, y, color='green', marker='x')  # 显示数据点
plt.plot(x, lm.predict(x), color='blue', linewidth=3, linestyle='-')  # 得到预测的回归模型
plt.xlabel('Average Number of Rooms per Dwelling(RM)')
plt.ylabel('Housing Price')
plt.title('2D demo of linear regression')
plt.grid(True)
plt.savefig('fig/boston', dpi=300)
plt.show()
