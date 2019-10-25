# 先获取前景矩形框
# grabcut提取图像前景主体物，通过FCM获得主体物主色彩
# 也可以考虑使用Haishoku库获取图像色彩组成
import numpy as np
import pandas as pd
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from haishoku.haishoku import Haishoku
import warnings
warnings.filterwarnings('ignore')

# 1 获取前景
def getFrontground(img):
    # 1.1 载入图像
    h, w = img.shape[:2]  # 获取图像的高和宽
    # cv2.imshow('Origin', img)
    # 1.2 滤波降噪
    blured = cv2.blur(img, (5, 5))  # 进行滤波去掉噪声，参数二为低通滤波器的大小
    # cv2.imshow('Blur', blured)
    # 1.3 mask是掩码图像，用来确定哪些区域是背景，哪些区域是前景
    mask = np.zeros((h+2, w+2), np.uint8)  # 掩码长和宽都比输入图像多两个像素点，满水填充不会超出掩码的非零边缘
    # 为什么要加2可以这么理解：当从0行0列开始泛洪填充扫描时，mask多出来的2可以保证扫描的边界上的像素都会被处理
    # 1.4 进行泛洪填充
    cv2.floodFill(blured, mask, (w-1, h-1), (255, 255, 255), (1, 1, 1), (1, 1, 1), 8)
    # cv2.imshow('floodfill', blured)
    # 1.5 转换为灰度图
    gray = cv2.cvtColor(blured, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', gray)
    # 1.6 定义结构元素
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(50, 50))
    # 1.7 开闭运算，先开运算去除背景噪声，再继续闭运算填充目标内的孔洞
    opened = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow('closed', closed)
    # 1.8 求二值图
    ret, binary = cv2.threshold(closed, 250, 255, cv2.THRESH_BINARY)
    # cv2.imshow('binary', binary)
    # 1.9 找到前景物轮廓，并转换为最小矩形框
    _, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        # 计算包围目标的最小矩形区域
        rect = cv2.minAreaRect(c)
        # 计算矩形的 4 点坐标，返回结果为float数据类型
        points = cv2.boxPoints(rect)
        # 转换为int类型
        box = np.int0(points)
    # 1.10 绘制轮廓
    draw_img = cv2.drawContours(img.copy(), [box], -1, (0, 0, 255), 3)
    # cv2.imshow('result', draw_img)
    # 1.11 根据box将对图片进行裁剪
    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = min(Xs)
    x2 = max(Xs)
    y1 = min(Ys)
    y2 = max(Ys)
    height = y2 - y1
    width = x2 - x1
    crop_img = img[y1:y1+height, x1:x1+width]
    cv2.imshow('crop_img', crop_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return crop_img

# 2 使用grabcut进一步提取主体物
def grabTarget(img):
    # 掩码图像，用来确定前后景
    mask = np.zeros((img.shape[:2]), np.uint8)
    # 前后景模型
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    # 限定图像范围，这里选择全部
    rect = (1, 1, img.shape[1], img.shape[0])
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 20, cv2.GC_INIT_WITH_RECT)
    # 关于where函数第一个参数是条件，满足条件的话赋值为0，否则是1。如果只有第一个参数的话返回满足条件元素的坐标。
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    # 这里的img也是固定的
    img_grab = img * mask2[:, :, np.newaxis]
    # 输出对比图
    plt.subplot(121), plt.imshow(cv2.cvtColor(img_grab, cv2.COLOR_BGR2RGB))
    plt.title("grabcut"), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("original"), plt.xticks([]), plt.yticks([])
    plt.show()
    return img_grab

# # 3 进一步优化色彩
# img_path = 'temp_pic/3.jpg'
# img = Image.open(img_path)
# width, height = img.size
# black = (10, 10, 10)
# white = (250, 250, 250)
# for h in range(height):
#     for w in range(width):
#         dot = (w, h)
#         color = img.getpixel(dot)
#         if color <= black:
#             color = (0, 0, 0)
#             img.putpixel(dot, color)
#         elif color >= white:
#             color = (255, 255, 255)
#             img.putpixel(dot, color)
# img.save('temp_pic/3.jpg')

# 4 利用聚类方法获得图片色彩构成
# 确定聚类中心点
k = 5
# 读取图片
img_path = 'temp_pic/19.jpg'
img_data = cv2.imread(img_path)
print(img_data.shape, img_data.dtype)  # 宽度，高度和像素RGB值，RGB值由uint8类型表示
# 转换数据维度
img_data = img_data.reshape((img_data.shape[0]*img_data.shape[1], img_data.shape[2]))
print(img_data.shape, img_data.dtype)  # 宽度，高度和像素RGB值，RGB值由uint8类型表示
print(img_data)
# 建立聚类器
kmeans = KMeans(n_clusters=k, max_iter=4000, init='k-means++', n_init=50)
# kmeans = KMeans(n_clusters=k)
kmeans.fit(img_data)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
print(centroids)

# # 5 使用haishoku
# img_path2 = 'temp_pic/3.png'
# dominant = Haishoku.getDominant(img_path)
# print(dominant)
# palette = Haishoku.getPalette(img_path)
# print(palette)

# def main():
#     img = cv2.imread('3.jpg')
#     img2 = getFrontground(img)
#     img3 = grabTarget(img2)
#     # cv2.imwrite('temp_pic/3.jpg', img3)
#
# main()