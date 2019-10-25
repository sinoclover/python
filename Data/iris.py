# 鸢尾花数据集
from sklearn import datasets

# 数据存储于.data中，150个数据分别包括萼片长度、萼片宽度、花瓣长度和花瓣宽度四个特征值
# .target中保存数据所属种类，包括山鸢尾、变色鸢尾和弗吉尼亚鸢尾
iris = datasets.load_iris()

# KNN最邻近分类算法，对于新的观测值，确定其N维空间最靠近它的训练样本确定其所属类别
from sklearn import neighbors

knn = neighbors.KNeighborsClassifier()  # 构建KNN分类算法对象
knn.fit(iris.data[:-1], iris.target[:-1])  # 将训练集传递给fit方法来实现，传入除了最后一个数据的所有样本作为训练集
print(knn.predict(iris.data[-1].reshape(1, -1)))  # 对最后一个数据进行预测
print(knn.predict([[4.0, 3.0, 5.0, 2.0]]))  # 预测未知数据

# K-MEANS方法进行聚类
from  sklearn import cluster

kmeans = cluster.KMeans(n_clusters=3)  # 构建K-MEANS聚类算法对象，其中聚类中心为3
kmeans.fit(iris.data)  # 将训练集传递给K-MEANS算法对象
pred = kmeans.predict(iris.data)  # 分类预测值
count = 0
print(pred)
print(iris.target)

# 支持向量机分类方法SVM
from sklearn import svm

svc = svm.LinearSVC()  # 构建线性支持向量机
svc.fit(iris.data[:-1], iris.target[:-1])  # 将训练集传递给fit方法来实现，传入除了最后一个数据的所有样本作为训练集
print(svc.predict(iris.data[-1].reshape(1, -1)))
print(svc.predict([[5.0, 3.0, 5.0, 2.0]]))

clf = svm.SVC(gamma=0.0001, C=100)  # 选择模型参数构建分类预测器clf,实现了支持向量机分类
clf.fit(iris.data[:-1], iris.target[:-1])
print(clf.predict(iris.data[-1].reshape(1, -1)))
print(clf.predict([[5.0, 3.0, 5.0, 2.0]]))