import numpy as np

# 数组的创建
x = np.array([(1,2,3),(4,5,6)])
print(x)
y = np.arange(1,10,0.5)
print(y)

# 数组的属性
print(x.ndim) # 数组的秩
print(x.shape) # 数组的维度
print(x.size) # 数组的元素个数

# ndarray的操作
print(x[1])
print(x[0:2])
print(x[:,[0,1]])
for row in x:
    print(row)

a = x.reshape(3,2) # 改变数组结构形式，但不改变原有数组
print(a)
x.resize(3,2)  # 改变数据原有结构
print(x)

b = np.array([1,3,7])
c = np.array([3,5,8])
bc1 = np.vstack((b, c))  # 竖直方向拼接数组
print(bc1)
bc2 = np.hstack((b, c))  # 水平方向拼接数组
print(bc2)

# ndarray的运算
aArray = np.array([(5,5,5),(5,5,5)])
bArray = np.array([(2,2,2),(2,2,2)])
cArray = aArray *  bArray
print(cArray)
aArray += bArray
print(aArray)

print(aArray.sum()) # 数组元素求和
print(aArray.sum(axis=0)) # 数组元素按列求和
print(aArray.sum(axis=1)) # 数组元素按行求和

print(b.min()) # 返回最小值
print(b.argmax()) # 返回最大值的索引
print(b.mean())  # 返回数组元素平均值
print(b.var()) # 返回方差
print(b.std()) # 返回标准差