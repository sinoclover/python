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
def getFrontground(img_path):
    # 1.1 载入图像
    img = cv2.imread(img_path)
    height, width = img.shape[:2]  # 获取图像的高和宽
    print(height, width)
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
    # 注意，contours[0]表示外轮廓，contours[1]表示内轮廓
    # 1.10 绘制轮廓
    draw_img = cv2.drawContours(img.copy(), contours, -1, (0, 0, 255), 3)
    cv2.imshow('result', draw_img)
    # 1.11 遍历像素点是否在轮廓内，改变轮廓外的像素点
    color = (255, 255, 255)
    for h in range(height):
        for w in range(width):
            try:
                test = cv2.pointPolygonTest(contours[1], (w, h), False)
                if test == -1 or test == 0:
                    img[h, w] = color
            except:
                test = cv2.pointPolygonTest(contours[0], (w, h), False)
                if test == 1:
                    img[h, w] = color
    cv2.imshow('handle', img)
    # 1.12 使用轮廓建立最小矩形区域
    for c in contours:
        # 计算包围目标的最小矩形区域
        rect = cv2.minAreaRect(c)
        # 计算矩形的 4 点坐标，返回结果为float数据类型
        points = cv2.boxPoints(rect)
        # 转换为int类型
        box = np.int0(points)
    # 1.13 根据box将对图片进行裁剪
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

# 2 使用haishoku
def haishokuColor(img):
    dominant = Haishoku.getDominant(img)
    print(dominant)
    palette = Haishoku.getPalette(img)
    print(palette)

def main():
    i = 3
    img_path = str(i) + '.jpg'
    img = getFrontground(img_path)
    img_path2 = 'temp_pic/' + str(i) + '.jpg'
    cv2.imwrite(img_path2, img)
    haishokuColor(img_path2)

main()