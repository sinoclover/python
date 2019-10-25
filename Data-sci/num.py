# 数据的维度从一个数据中的一个含义到一组数据中的一个或多个含义
# 维度是一组数据的组织形式
# 一维数据由对等关系的有序或无序数据构成，采用线性方式组织，通过列表、数组、集合等方式表示
# 其中列表中数据类型可以不同，而数组中的数据类型是相同的，列表是有序的，而集合是无序的
# 二维数据由多个一维数据构成，是一维数据的组合形式，表格是典型的二维数据，常用列表方式进行表示
# 多维数据由一维数据或二维数据在新维度上扩展而成，常用列表的方式进行表示
# 高维数据仅利用最基本的二元关系展示数据间的复杂结构，常用字典或数据表示格式的方式进行表示

# numpy基础库中提供了一个强大的N维数组对象ndarray、广播功能函数、整合C等类似语言代码的工具以及线性代数、傅里叶变换、随机数生成等功能
# 数组对象可以去掉元素间运算所需的循环，使一维向量更像单个数据；设置这种专门的数组对象，经过优化可以提升应用的运算速度；
# 在科学计算中，一个维度的所有数据类型往往相同，那么采用相同的数据类型有助于节省运算和存储空间
# import numpy as np
# a = np.array([0, 1, 2, 3, 4])
# b = np.array([9, 8, 7, 6, 5])
# c = a**2 + b**3
# print(c)
# ndarray是一个多维数组对象，由两部分组成：实际的数据、描述这些数据的元数据（数据维度、数据类型）
# ndarray数组一般要求所有元素类型相同，数组下标从0开始
# 对于ndarray的基本概念有轴axis表示保存数据的维度，秩rank表示轴的数量，通过例子来说明ndarray对象的属性
# import numpy as np
# a = np.array([[0, 1, 2, 3, 4],
#               [9, 8, 7, 6, 5]])
# print(a.ndim)  # 对象的秩,即数组的维度
# print(a.shape)  # 对象的尺度，即n行m列
# print(a.size)  # 对象元素的个数
# print(a.dtype)  # 对象元素的类型
# print(a.itemsize)  # 对象中每个元素的大小

# ndarray数组的创建方式包括从列表、元组等类型中创建；使用NUMPY中的函数创建；通过字节流创建；从文件中读取相关格式创建
# import numpy as np
# x1 = np.array([0, 1, 2, 3])  # 从列表中创建
# print(x1)
# x2 = np.array((4, 5, 6, 7))  # 从元组中创建
# print(x2)
# x3 = np.array([[1, 2], [9, 8], (0.1, 0.2)])  # 元组和列表混合创建
# print(x3)
# y1 = np.arange(10)  # 通过范围函数创建数组序列
# print(y1)
# y2 = np.ones((3, 6))  # 创建全1数组
# print(y2)
# y3 = np.zeros((3, 6), dtype=np.int32)  # 创建全0数组，并设置元素类型为整型
# print(y3)
# y4 = np.eye(5)  # 生成对角阵
# print(y4)
# y5 = np.ones((2, 3, 4))  # 生成多维数组
# print(y5)
# y6 = np.linspace(1, 10, 4)  # 生成间距数组
# print(y6)
# y7 = np.linspace(1, 10, 4, endpoint=False)  # 末尾值不作为数组元素，则将多分出一份
# print(y7)
# y8 = np.concatenate((y6, y7))  # 将两个数组合并起来
# print(y8)
# ndarray数组的维度变换
# import numpy as np
# z1 = np.ones((2, 3, 4), dtype=np.int32)
# print(z1)
# print(z1.reshape((3, 8)))  # 创建副本来改变数组维度
# z1.resize((3, 8))  # 改变了原数组的维度
# print(z1)
# print(z1.flatten())  # 对数组的副本进行降维，不改变原数组
# z2 = np.ones((2, 3, 4), dtype=np.int)
# print(z2)
# z3 = z2.astype(np.float)  # 进行数组的类型改变,该方法一定会创建新的数组，即使两个类型一致
# print(z3)
# # ndarray数组向列表的转变
# z4 = np.full((2, 3, 4), 25, dtype=np.int32)
# print(z4)
# print(z4.tolist())

# 对数组的索引和切片
# 索引是指获取数组中特定位置元素的过程，切片是获取数组元素子集的过程
import numpy as np
a = np.array([9, 8, 7, 6, 5])
print(a[2])  # 一维数组的索引
print(a[1:4:2])  # 一维数组的切片
b = np.arange(24).reshape((2, 3, 4))
print(b)
print(b[1,2,3])  # 多维数组的索引
print(b[0,1,2])
print(b[-1,-2,-3])
print(b[:,1,-3])  # 多维数组的切片
print(b[:,1:3,:])
print(b[:,:,::2])

# ndarray数组的运算
# 数组与标量之间的运算作用于数组的每一个元素
print(b.mean())
c = b / b.mean()
print(c)
# 一元函数实例
print(np.square(b))  # 数组的平方
print(np.sqrt(b))  # 数组的平方根
print(np.modf(c))  # 将小数部分和整数部分分开
