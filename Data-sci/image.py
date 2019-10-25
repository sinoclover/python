# # PIL库具有强大的图像处理能力的第三方库(python image library)
# from PIL import Image  # Image类是PIL库中代表图像的类（对象）来表示图像，用数组表示图像中的每个元素
# # 图像是一个由像素组成的二维矩阵构成，每个元素即一个RGB值
# import numpy as np
# im = np.array(Image.open('../Data-sci/data/d.jpg'))
# print(im.shape, im.dtype)  # 宽度，高度和像素RGB值，RGB值由uint8类型表示
#
# # 图像的变换，即读入图像后，获得像素的RGB值，修改后保存为新的文件
# b = [255, 255, 255] - im
# im2 = Image.fromarray(b.astype('uint8'))
# im2.save('../Data-sci/data/d1.jpg')
# # 获取图片的灰度值
# im_gray = np.array(Image.open('../Data-sci/data/d.jpg').convert('L'))
# print(im_gray.shape, im_gray.dtype)  # 降维成只有灰度信息的图片
# c = 255 - im_gray
# im3 = Image.fromarray(c.astype('uint8'))
# im3.save('../Data-sci/data/d2.jpg')
# d = (100/255) * im_gray + 150
# im4 = Image.fromarray(d.astype('uint8'))
# im4.save('../Data-sci/data/d3.jpg')
# e = 255 * (im_gray/255)**2
# im5 = Image.fromarray(e.astype('uint8'))
# im5.save('../Data-sci/data/d4.jpg')

# 手绘风格图像处理
# 利用像素之间的梯度值和虚拟深度值对图像进行重构，即根据灰度变化来模拟人类视觉的明暗程度
# 梯度值代表了灰度变化率，对梯度值进行基于光源的影响，从而反映到灰度上，立体效果通过添加虚拟深度值呈现
from PIL import Image
import numpy as np

im_gray = np.array(Image.open('../Data-sci/data/d.jpg').convert('L'))  # 对图像进行灰度处理，获取图像的灰度值
depth = 1  # 预设深度值为10，取值范围为0-100
grad = np.gradient(im_gray)
grad_x, grad_y = grad  # 图片二维方向上灰度的梯度
grad_x = grad_x * depth / 100  # 深度值与方向梯度值的乘积表示深度对梯度的影响因素，并进行归一化
grad_y = grad_y * depth / 100
A = np.sqrt(grad_x**2 + grad_y**2 + 1)  # 将梯度用单位1表示，构造x,y轴梯度的三维归一化单位坐标系
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1/A

# 模拟光源效果，根据灰度变化来模拟人类视觉的远近程度
vec_el = np.pi/2.2                   # 光源的俯视角度，弧度值
vec_az = np.pi/4.                    # 光源的方位角度，弧度值
dx = np.cos(vec_el)*np.cos(vec_az)   #光源对x 轴的影响
dy = np.cos(vec_el)*np.sin(vec_az)   #光源对y 轴的影响
dz = np.sin(vec_el)              #光源对z 轴的影响

B = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化，梯度与光源的相互作用，并梯度转化为灰度
B = B.clip(0, 255)

im = Image.fromarray(B.astype('uint8'))  # 重构图像
im.save('../Data-sci/data/dX.jpg')
