# import numpy as np
# # 存储CSV文件
# a = np.arange(100).reshape(5, 20)
# # np.savetxt('../Data-sci/data/a.csv', a, fmt='%d', delimiter=',')
# b = np.loadtxt('../Data-sci/data/a.csv', dtype=int, delimiter=',', unpack=False)  # unpack如果为TRUE读入属性将分别写入不同变量
# print(b)
# # csv的局限性在于其只能存储一维和二维数组，而多维数组的存取使用tofile存储为dat，使用fromfile还原
# # 这两种方法应配合使用，需要知道存入文件时数组的维度和元素类型，可以通过元数据文件来存储额外信息
# c = np.arange(100).reshape(5, 10, 2)
# c.tofile('../Data-sci/data/b.bat', sep=',', format='%d')   # 没有指定分隔符则数据为二进制文件
# d = np.fromfile('../Data-sci/data/b.bat', dtype=int, sep=',', count=-1)  # count指读入元素的个数，-1表示整个文件
# print(d)
# d = d.reshape(5,10,2)
# print(d)
# # numpy的便捷文件存取，save和load函数
# e = np.arange(100).reshape(5, 10, 2)
# np.save('../Data-sci/data/c.npy', e)
# f = np.load('../Data-sci/data/c.npy')
# print(f)

# # python自带的随机数random是针对标量使用的，numpy的random子库为数组类型的提供随机数相关功能
# import numpy as np
# a = np.random.rand(3, 4, 5)  # 默认情况下符合元素选取符合均匀分布
# print(a)
# sn = np.random.randn(3, 4, 5)  # 根据正态分布选取元素
# print(sn)
# b = np.random.randint(100, 200, (3,4))
# print(b)
# # 随机种子设定，使之形成相同的随机数
# np.random.seed(10)
# b1 = np.random.randint(100, 200, (3,4))
# print(b1)
# np.random.seed(10)
# b2 = np.random.randint(100, 200, (3,4))
# print(b2)
# # 高级随机函数
# # shuffle函数
# c = np.random.randint(100, 200, (3, 4))
# print(c)
# np.random.shuffle(c)  # 改变原数组中第一维数组的顺序
# print(c)
# # permutation函数
# d = np.random.randint(100, 200, (3, 4))
# print(d)
# print(np.random.permutation(d))  # 与shuffle功能一致，但其是可迭代的
# # choice函数
# e = np.random.randint(100, 200, (8, ))
# print(e)
# e1 = np.random.choice(e, (3, 2))  # 随机从8个元素中提取，并且可以重复
# print(e1)
# e2 = np.random.choice(e, (3, 2), replace=False)  # 不重复选取
# print(e2)
# e3 = np.random.choice(e, (3, 2), p=e/np.sum(e))  # 通过p设置概率
# print(e3)
# # 产生均匀分布数组uniform
# u = np.random.uniform(0, 10, (3, 4))
# print(u)
# # 产生正态分布数组normal，其中loc是均值，scale为标准差
# n = np.random.normal(10, 5, (3, 4))
# print(n)
# # 产生泊松分布数组poisson，其中lam为随机事件发生率

# # numpy的统计函数
# import numpy as np
# a = np.arange(15).reshape(3, 5)
# print(a)
# print(np.sum(a))  # 求和
# print(np.mean(a, axis=1))  # 对第二维进行求均值
# print(np.mean(a, axis=0))  # 对第一维进行求均值
# print(np.average(a, axis=0, weights=[10, 5, 1]))  # 对第一维进行加权平均
# b = np.arange(15, 0, -1).reshape(3, 5)
# print(np.max(b))  # 求最大值
# print(np.argmax(b))  # 最大值下标，即降维扁平化后的下标
# print(np.unravel_index(np.argmax(b), b.shape))  # 重塑为多维下标
# print(np.ptp(b))  # 求最大值与最小值之差
# print(np.median(b))  # 求中位数

# numpy的梯度函数gradient，计算数组中元素的梯度，当数组为多维时，返回每个维度的梯度
# 梯度即连续值之间的变化率，即斜率
import numpy as np
a = np.random.randint(0, 20, (5))
print(a)
print(np.gradient(a))
# 梯度存在两侧值(c-a)/2，梯度只有右侧值(c-b)/1,只有左侧值(b-a)/1
b = np.random.randint(0, 20, (5))
print(b)
print(np.gradient(b))
c = np.random.randint(0, 50, (3, 5))
print(c)
print(np.gradient(c))  # 二维数组返回两个梯度数组表示两个方向上的梯度，第一个为最外层维度的梯度，依次类推。