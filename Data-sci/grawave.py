import requests
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

# # 下载模板数据
# url = 'https://python123.io/dv/wf_template.txt'
# path = 'data/' + url.split('/')[-1]
# r = requests.get(url)
# with open(path, 'wb') as f:
#     f.write(r.content)

# 从配置文档中读取时间相关数据
rate_h, hstrain = wavfile.read(r'data/H1_Strain.wav', 'rb')  # 分别赋给音频采样率和相应的数据
rate_l, lstrain = wavfile.read(r'data/L1_Strain.wav', 'rb')
reftime, ref_H1 = np.genfromtxt('data/wf_template.txt').transpose() # 通过模板数据的引力波模型，读取时间序列和完整的数据并进行转置

# 读取应变数据建立时间序列
# 音频采样率是一秒钟内声音信号的采样次数
htime_interval = 1 / rate_h  # 则1秒除以采样次数则是1秒内采样时间间隔
ltime_interval = 1 / rate_l

htime_len = hstrain.shape[0] / rate_h  # 数据第一维度即数据点的个数除以速率则是时长，即函数在坐标轴上的总长度
htime = np.arange(-htime_len/2, htime_len/2, htime_interval)  # 根据时间间隔设置时间序列
ltime_len = lstrain.shape[0] / rate_l
ltime = np.arange(-ltime_len/2, htime_len/2, ltime_interval)

# 绘制H1探测器的数据
fig = plt.figure(figsize=(12, 6))
plth = fig.add_subplot(221)
plth.plot(htime, hstrain, 'y')
plth.set_xlabel('Time(s)')
plth.set_ylabel('H1 Strain')
plth.set_title('H1 Strain')

pltl = fig.add_subplot(222)
pltl.plot(ltime, lstrain, 'g')
pltl.set_xlabel('Time(s)')
pltl.set_ylabel('L1 Strain')
pltl.set_title('L1 Strain')

pltref = fig.add_subplot(212)
pltref.plot(reftime, ref_H1)
pltref.set_xlabel('Time(s)')
pltref.set_ylabel('Tamplate')
pltref.set_title('Tamplate')

fig.tight_layout()  # 自动调整图像边缘
plt.savefig('fig/grawave', dpi=300)
plt.show()