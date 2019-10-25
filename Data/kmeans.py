# # 简单k均值聚类算法
# import numpy as np
# from scipy.cluster.vq import vq, kmeans, whiten
#
# list1 = [88.0, 74.0, 96.0, 85.0]
# list2 = [92.0, 99.0, 95.0, 94.0]
# list3 = [91.0, 87.0, 99.0, 95.0]
# list4 = [78.0, 99.0, 97.0, 81.0]
# list5 = [88.0, 78.0, 98.0, 84.0]
# list6 = [100.0, 95.0, 100.0, 92.0]
#
# data = np.array([list1, list2, list3, list4, list5, list6])  # 创建数组
# whiten = whiten(data)  # 使用whiten函数计算各列的标准差，形成一个新的数组
# centroids,_ =  kmeans(whiten, 2)  # kmeans对数据进行聚类，并将数据分为2类，返回一个元组，只需要用到第一个值，即聚类中心数组
# result,_ = vq(whiten, centroids)  # vq是矢量量化函数，对每一个数据进行归类
# print(result)

# 使用scikit-learn解决上述问题
import numpy as np
from sklearn.cluster import KMeans

list1 = [88.0, 74.0, 96.0, 85.0]
list2 = [92.0, 99.0, 95.0, 94.0]
list3 = [91.0, 87.0, 99.0, 95.0]
list4 = [78.0, 99.0, 97.0, 81.0]
list5 = [88.0, 78.0, 98.0, 84.0]
list6 = [100.0, 95.0, 100.0, 92.0]

X = np.array([list1, list2, list3, list4, list5, list6])
kmeans = KMeans(n_clusters=2).fit(X)  # fit方法进行聚类
pred = kmeans.predict(X)  # predict根据聚类结果确定数据所属类别
print(pred)
