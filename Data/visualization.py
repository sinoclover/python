import requests
import re
import json
import time
import numpy as np
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import pylab as pl

# matplotlib应用1

# 获取AXP的股票情况
def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return [item for item in quotes if not 'type' in item]

quotes = retrieve_quotes_historical('AXP')

# 数据源处理修改时间戳
list_timeIndex = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    y = date.strftime(x, '%Y-%m-%d')
    list_timeIndex.append(y)
quotesdf_ori = pd.DataFrame(quotes, index=list_timeIndex)
quotesdf = quotesdf_ori.drop(['date'], axis=1)
# 数据源处理通过时间获取月份信息
listtemp = []
for i in range(len(quotesdf)):
    temp = time.strptime(quotesdf.index[i], '%Y-%m-%d')
    listtemp.append(temp.tm_mon)
tempdf = quotesdf.copy()
tempdf['month'] = listtemp
print(tempdf)

# 获取数据源中相关数据进行绘制
closeMeansKO = tempdf.groupby('month').close.mean()
print(closeMeansKO)

x = closeMeansKO.index
y = closeMeansKO.values
# # 使用不同的图形
# fig1 = plt.plot(x, y)
# plt.savefig(r'..\Data\fig\stock_line.jpg')
# fig2 = plt.plot(x, y, 'o')
# plt.savefig('../Data/fig/stock_scatter.jpg')
# fig3 = plt.bar(x, y)
# plt.savefig('../Data/fig/stock_bar.jpg')
#  改变图像属性
# fig4 = plt.plot(x, y, 'g--')
# plt.show(fig4)
# fig5 = plt.plot(x, y, 'rd')
# plt.show(fig5)
# # 对图的横纵坐标或图加文字说明
# plt.title('Stock Statistics of AXP')
# plt.xlabel('Month')
# plt.ylabel('Average Close Price')
# fig6 = plt.plot(x, y)
# plt.show(fig6)
# # 多子图设置
# plt.subplot(211)
# plt.plot(x, y, color='b', marker='o')
# plt.subplot(212)
# plt.plot(x, y, color='r', marker='d')
# plt.show()


# # matplotlib应用2
# t = np.arange(0.0, 4.0, 0.1)
# f1 = plt.plot(t, t, t, t+2, t, t**2)
# plt.savefig('../Data/fig/1.jpg')
# plt.show(f1)
#
# f2 = plt.plot(t, t, 'o', t, t+2, 'o', t, t**2, 'o')  # 绘制散点图scatter
# plt.savefig('../Data/fig/2.jpg')
# plt.show(f2)

# # 使用pylab模块进行绘图
# t = np.arange(0.0, 4.0, 0.1)
# f3 = plt.plot(t,t,t,t+2,t,t**2)
# pl.show(f3)

# 使用pandas作图
# # 在使用plot时也可以将数据直接传递给plot函数
# fig7 = plt.plot(closeMeansKO)
# plt.show(fig7)
# # 那么用pandas是对series或dataframe数据集直接调用plot方法
# closeMeansKO.plot()
# plt.show()

# 绘制AXP一年来的股票收盘价折线图
quotesdf.close.plot()
plt.show()