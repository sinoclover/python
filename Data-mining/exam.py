import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import spline

data = pd.read_excel('data/a.xlsx')
print(data)
x = data['R']
y = data['V']

# sns.jointplot(x, y, kind='reg').set_axis_labels('x', 'y')
# plt.scatter(x, y, color='green', marker='x')  # 显示数据点

# 无法进行曲线光滑
# xnew = np.linspace(x.min(), x.max(), 30)
# power_smooth = spline(x, y, xnew)
# plt.plot(xnew,power_smooth)

z1 = np.polyfit(x, y, 8)
p1 = np.poly1d(z1)
print(z1)
print(p1)

plt.rcParams['font.sans-serif']=['SimHei']
xnew = np.linspace(x.min(), x.max(), 100)
ynew = p1(xnew)
plt.scatter(x, y, color='green', marker='x')  # 显示数据点
plt.plot(xnew, ynew, color='b', label='拟合图')

plt.xlabel('R')
plt.ylabel('values')
plt.title('R-V')
plt.legend(loc='best')
plt.grid(True)
plt.show()

