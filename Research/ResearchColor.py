# 先获取前景矩形框
# grabcut提取图像前景主体物，通过FCM获得主体物主色彩
# 也可以考虑使用Haishoku库获取图像色彩组成
import numpy as np
import pandas as pd
import math
import cv2
from sklearn.cluster import KMeans
from haishoku.haishoku import Haishoku

# 1 获取前景
def getFrontground(img_path):
    # 1.1 载入图像
    img = cv2.imread(img_path)
    height, width = img.shape[:2]  # 获取图像的高和宽
    # cv2.imshow('Origin', img)
    # 1.2 滤波降噪
    blured = cv2.blur(img, (5, 5))  # 进行滤波去掉噪声，参数二为低通滤波器的大小
    # cv2.imshow('Blur', blured)
    # 1.3 mask是掩码图像，用来确定哪些区域是背景，哪些区域是前景
    mask = np.zeros((height+2, width+2), np.uint8)  # 掩码长和宽都比输入图像多两个像素点，满水填充不会超出掩码的非零边缘
    # 为什么要加2可以这么理解：当从0行0列开始泛洪填充扫描时，mask多出来的2可以保证扫描的边界上的像素都会被处理
    # 1.4 进行泛洪填充
    cv2.floodFill(blured, mask, (width-1, height-1), (255, 255, 255), (1, 1, 1), (1, 1, 1), 8)
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
    # 1.9 找到前景物轮廓
    _, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 1.10 绘制轮廓
    draw_img = cv2.drawContours(img.copy(), contours, -1, (0, 0, 255), 3)
    cv2.imshow('result', draw_img)
    # 保存轮廓图
    cv2.imwrite('107.png', draw_img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 1.11 遍历像素点是否在轮廓内，存储在轮廓内的像素
    color = []
    for h in range(height):
        for w in range(width):
            if len(contours) == 2:
                # 此时两个轮廓并列，将不在任何轮廓的像素点进行存储
                if hierarchy[0][0][0] == 1:
                    test1 = cv2.pointPolygonTest(contours[0], (w, h), False)
                    test2 = cv2.pointPolygonTest(contours[1], (w, h), False)
                    if test1 == -1 and test2 == -1:
                        color.append(img[h, w])
                # 此时两个轮廓嵌套，将在内轮廓的像素点进行存储
                elif hierarchy[0][0][2] == 1:
                    test = cv2.pointPolygonTest(contours[1], (w, h), False)
                    if test == 1 or test == 0:
                        color.append(img[h, w])
            elif len(contours) == 1:
                # 此时仅有一个轮廓，将轮廓外的像素点进行存储
                test = cv2.pointPolygonTest(contours[0], (w, h), False)
                if test == -1:
                    color.append(img[h, w])
            else:
                color.append(img[h, w])
    color = np.array(color)
    # 1.12 根据色彩长度重塑为图片
    l = len(color)
    side = int(math.sqrt(l))
    l2 = side * side
    color = color[:l2]
    color = color.reshape(side, side, 3)
    return color

# 2 使用haishoku
def haishokuColor(img):
    # dominant = Haishoku.getDominant(img)
    # Haishoku.showDominant(img)
    # print(dominant)
    palette = Haishoku.getPalette(img)
    x = []
    y = []
    for per, color in palette:
        x.append(per)
        y.append(color)
    print('调色盘色彩比例：\n', palette)
    Haishoku.showPalette(img)

# 3 使用Kmeans聚类
def kmeansColor(img_path):
    # 确定聚类中心点
    k = 5
    # 读取图片
    img_data = cv2.imread(img_path)
    # print(img_data.shape, img_data.dtype)  # 宽度，高度和像素RGB值，RGB值由uint8类型表示
    # 转换数据维度
    img_data = img_data.reshape((img_data.shape[0]*img_data.shape[1], img_data.shape[2]))
    # print(img_data.shape, img_data.dtype)  # 宽度，高度和像素RGB值，RGB值由uint8类型表示
    # print(img_data)
    # 建立聚类器
    # kmeans = KMeans(n_clusters=k, max_iter=4000, init='k-means++', n_init=50)
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(img_data)
    centroids = kmeans.cluster_centers_
    # labels = kmeans.labels_
    print('聚类中心：\n', centroids)

def main():
    i = 107
    img_path = 'pic/' + str(i) + '.jpg'
    img = getFrontground(img_path)
    img_path2 = 'temp_pic/' + str(i) + '.jpg'
    cv2.imwrite(img_path2, img)
    kmeansColor(img_path2)
    haishokuColor(img_path2)

main()