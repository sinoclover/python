# # Numpy
# import numpy as np
# # 创建数组
# print('创建数组')
# arr1 = np.array([2, 3, 4])  # 通过列表创建数组
# print(arr1)
# arr2 = np.array([(1.3, 9, 2.0), (7, 6, 1)])  # 通过元组创建数组
# print(arr2)
# arr3 = np.zeros((2, 3))  # 通过元组创建零矩阵
# print(arr3)
# arr4 = np.identity(3)  # 生成单位阵
# print(arr4)
# arr5 = np.random.random(size=(2, 3))  # 生成随机矩阵
# print(arr5)
# arr6 = np.arange(5, 20, 3)
# print(arr6)
# arr7 = np.arange(0., 2.25, 0.25)
# print(arr7)
#
# # 查看数组属性
# print(arr2.shape)  # 返回矩阵规格
# print(arr2.ndim)  # 返回矩阵的秩
# print(arr2.size)  # 返回矩阵元素总数
# print(arr2.dtype.name)  # 返回矩阵元素的数据类型
# print(type(arr2))  # 返回整个数组对象的类型
#
# # 通过索引和切片访问数组元素
# # 根据函数建立数组
# def f(x, y):
#     return 10*x+y  # 其中x,y分别为行列序号
# arr8 = np.fromfunction(f, (4, 3), dtype=int)
# print(arr8)
# print(arr8[1, 2])  # 返回第一行第二列的元素
# print(arr8[0:2, :])  # 返回前两行元素
# print(arr8[:, 1])  # 返回第一列
# print(arr8[-1])  # 返回最后一行
# # 通过迭代器访问数组
# for row in arr8:
#     print(row)
# for element in arr8.flat:  # 输出矩阵全部元素
#     print(element)
#
# # 数组的运算
# print('数组的运算')
# arr9 = np.array([[2, 1], [1, 2]])
# arr10 = np.array([[1, 2], [3, 4]])
# print(arr9 - arr10)  # 减法
# print(arr9**2)  # 幂
# print(3 * arr10)  # 数乘
# print(arr9 * arr10)  # 普通乘法
# print(np.dot(arr9, arr10))  # 点乘
# print(arr10.T)  # 转置
# print(np.linalg.inv(arr10))  # 逆矩阵
# print(arr10.sum())  # 数组元素求和
# print(arr10.max())  # 返回数组最大元素
# print(arr10.cumsum(axis=1))  # 按行累积总和
#
# # numpy通用函数
# print('numpy通用函数')
# print(np.exp(arr9))  # 指数函数
# print(np.sin(arr9))  # 正弦函数
# print(np.sqrt(arr9))  # 开方
# print(np.add(arr9, arr10))  # 求和
#
# # 数组的分割与合并
# print('数组的分隔与合并')
# arr11 = np.vstack((arr9, arr10))  # 纵向合并数组
# print(arr11)
# arr12 = np.hstack((arr9, arr10))  # 横向合并数组
# print(arr12)
# print(np.hsplit(arr12, 2))  # 将数组横向分为两部分
# print(np.vsplit(arr12, 2))  # 将数组纵向分为两部分

# # Pandas
# import pandas as pd
#
# # 创建数据框
# data = {'id':  ['Jack', 'Sarah', 'Mike'],
#         'age': [18, 35, 20],
#         'cash': [10.53, 500.7, 13.6]}
# df = pd.DataFrame(data, index=None)
# print(df)
# df2 = pd.DataFrame(data, index=['a', 'b', 'c'], columns=['id', 'age', 'cash'])
# print(df2)
# # 数据框的增删改
# print(df2['id'])  # 按列名访问
# df2['rich'] = df2['cash'] > 200.0
# print(df2)
# # del df2['rich']
# df3 = df2.drop(['rich'], axis=1)
# print(df3)
#
# # 创建系列, 系列可以被认为是退化的数据框，或者说是一个子集。同时也可以认为它是广义的一维数组
# data2 = {'a': 4, 'b': 9, 'c': 16}
# s = pd.Series(data2, name='number')
# print(s)
# # 按下标访问系列
# print(s[0])
# print(s[:2])
# # 按索引访问系列
# print(s['a'])
# s['d'] = 25
# print(s)
# # 系列的向量化操作
# import numpy as np
# print(np.sqrt(s))
# print(s*s)

# # Scipy
# # scipy是基于numpy的高级模块，在符号计算、信号处理和数值优化上有着突出作用
# # scipy的向量化思想
# # 符号计算
# from scipy import poly1d
#
# p = poly1d([3, 4, 5])
# print(p)
# print(p*p)
# print(p.integ(k=6))  # 求p(x)的不定积分，指定常数项为6
# print(p.deriv())  # 求p(x)的一阶导数
# print(p([4, 5]))   # 计算每个值带入p(x)的结果
#
# # 函数向量化
# # 为了增强程序的健壮性，matlab通常使函数接受向量形式的参数
# # 而在scipy中，将函数本身作为参数，传递给vectorize()函数作为参数，从而处理后返回一个能接受向量化输入的函数
# import numpy as np
#
# def addsubtract(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
# vec_addsubtract = np.vectorize(addsubtract)
# print(vec_addsubtract([0, 3, 6, 9], [1, 3, 5, 7]))

# # scikit-learn
# # scikit-learn是基于numpy, scipy和matplotlib的数据挖掘和数据分析的工具
# # scikit的六大功能包括分类(classification)，回归(regression)，聚类(clustering)，降维(dimensionality reduction)，
# # 模型选择(model selection)和预处理(preprocessing)
# # scikit的机器学习分为有监督学习(supervised learning)和无监督学习(unsupervised learning)
# # 监督学习分为两类，即分类和回归，分类是指样本属于两个或多个类别，我们希望通过从已经标记类别的数据学习，来预测未标记数据的分类；
# # 而回归是指输出一个或多个连续的变量
# # 无监督学习的训练数据包括输入向量，但没有相应的目标变量。这类问题的目标是发掘数据中相似样本的分组，即聚类；
# # 也可以是确定输入样本空间中的数据分布，即密度估计；还可以是将数据从高维空间投射到二维或三维空间，进行数据可视化
#
# # scikit-learn的数据集
# from  sklearn import datasets
# # 数据集类似字典对象，包括所有数据和关于数据的元数据
# # 数据被存储在.data成员内，是一个n_samples*n_features的数组
# # 在有监督问题的情形下，一个或多个因变量被存储在.target成员中
#
# digits = datasets.load_digits()
# # 如在digits数据集中，data是可以用来分类数字样本的特征
# print(digits.data)
# # target给出了digits数据集的目标变量，即每个数字图案对应的我们想预测的真实数字
# print(digits.target)
#
# # scikit-learn的训练和预测
# # 训练一个预测器(estimator)来预测(predict)未知样本所属分类，分类的预测器是一个python对象，具有fit(X, y)方法和predict(test)方法
# from sklearn import svm
#
# # 选择模型参数构建分类预测器clf,实现了支持向量机分类
# clf = svm.SVC(gamma=0.0001, C=100)
# # 将训练集传递给fit方法来实现，传入除了最后一个数据的所有样本作为训练集
# clf.fit(digits.data[:-1], digits.target[:-1])
# # 调用predict方法进行预测
# # 如果数据具有单个特性，则使用reshape(-1,1)重塑数据；如果数据包含单个示例，则使用reshape(1,-1)重塑数据。
# print(clf.predict(digits.data[-1].reshape(1, -1)))  # 将单一特征值的一维数组转为二维
# # reshape(1, -1),将数组转为1行，列数未知；reshape(-1, 1)，将数组转为1列，行数未知。

# 实验
import pandas as pd

score = pd.read_csv('data/data.csv', index_col=None)
# 判断第一列是否有缺失值
score['Id'] = score['Id'].interpolate()  # 判断缺省值进行补充，默认线性顺序补充
score = score.fillna(0)  # 成绩空缺为0
score['Chinese'] = score['Chinese'].astype('int64')  # 将成绩设置为整数
# 判断是否有重复记录，如果有，则删除至唯一,并重置索引
score = score.drop_duplicates(subset=('Chinese', 'Math', 'English'))
score['Id'] = list(range(1, len(score)+1))
score = score.set_index('Id')
# 计算成绩的平均值，作为新的一列加入到原数据框中
average = score.mean(axis=1)  # 求平均值后生成了系列
score['Average'] = average
# 寻找平均分最高的记录,对平均值系列进行操作
print('The best average grade is: {0:.2f}, and the id is: '.format(average.max()), end='')
while True:
    average_max = score['Average'].max()
    print(average.idxmax(), end=' ')
    average = average.drop(index=average.index[average.values.argmax()])
    if not average_max == average.max():
        print('\n')
        break
# 统计每个科目及格的人数
print('Chinese pass number: {0}'.format(score[(score['Chinese'] >= 60)]['Chinese'].count()))
print('Math pass number: {0}'.format(score[(score['Math'] >= 60)]['Math'].count()))
print('English pass number: {0}'.format(score[(score['English'] >= 60)]['English'].count()))
print(score)