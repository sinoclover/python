import requests
import re
import json
import time
import numpy as np
import pandas as pd
from datetime import date

# 获取30家公司的股票价格示范
def retrieve_dji_list():
    r = requests.get('https://money.cnn.com/data/dow30/')
    search_pattern = re.compile(
        'class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    dji_list = []
    for item in dji_list_in_text:
        dji_list.append([item[0], item[1], float(item[2])])
    return dji_list

dji_list = retrieve_dji_list()
djidf = pd.DataFrame(dji_list)
# print(djidf)

# dataframe数据整理
# 添加行列索引
cols = ['code', 'name', 'lasttrade']
djidf.columns = cols
djidf.index = range(1, len(djidf)+1)
# print(djidf)

# # 数据显示
# print(list(djidf.index))
# print(list(djidf.columns))
# print(djidf.values)
# print(djidf.describe)
# print(djidf.lasttrade)
# print(djidf.head(5))
# print(djidf.tail(5))
# print(djidf[5:15])
# print(djidf.shape)
# print(djidf.size)

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
# quotesdf = pd.DataFrame(quotes)
# print(quotesdf)

# 将时间戳改为合适的时间序列作为index
list_timeIndex = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    y = date.strftime(x, '%Y-%m-%d')
    list_timeIndex.append(y)
quotesdf_ori = pd.DataFrame(quotes, index=list_timeIndex)
quotesdf = quotesdf_ori.drop(['date'], axis=1)
# quotesdf = quotesdf_ori.drop(['unadjclose'], axis = 1)  原先的网站数据有unadjclose列，目前已删除
# print(quotesdf)

# 数据选择
# print(quotesdf['2018-05-07':'2018-05-11'])
# print(djidf['code'])
# print(djidf.code)
# print(djidf.loc[1:5, ])  # 第一维是1到5，第二维为空即全选
# print(djidf.loc[:, ['code','lasttrade']])  # 第一维为空即全选，第二维选择相应两列
# print(djidf.loc[1:5, ['code', 'lasttrade']])  # 通过index参数和colunms参数控制
# print(djidf.iloc[0:5, [0, 2]])  # 通过物理位置参数控制，选择第0列和第2列
# print(djidf.iloc[0:5, 0:2])  # 选择第0列和第1列
# print(quotesdf[(quotesdf.index >= '2018-05-01') & (quotesdf.index <= '2018-05-31')])
# print(quotesdf[(quotesdf.index >= '2018-05-01') & (quotesdf.index <= '2018-05-31') & (quotesdf.close >= 100)])

# 简单数据统计
# print(djidf.lasttrade.mean())  # TOP30道指平均值
# print(djidf[djidf.lasttrade >= 180].name)  # TOP30道指成交价高于180的公司
# print(len(quotesdf[quotesdf.close > quotesdf.open]))  # AXP上涨天数
# # diff计算相邻的两个数据是增加还是减少
# status = np.sign(np.diff(quotesdf.close))
# print(status)
# print(status.size)
# print(status[np.where(status == 1)].size)
# print(status[np.where(status == -1)].size)
# # 排序
# sortdf = djidf.sort_values(by='lasttrade', ascending=False)  # 逆序排列
# print(sortdf[:3])
# # 计算每月的开盘天数
# listtemp = []
# for i in range(len(quotesdf)):
#     temp = time.strptime(quotesdf.index[i], '%Y-%m-%d')
#     listtemp.append(temp.tm_mon)
# tempdf = quotesdf.copy()
# tempdf['month'] = listtemp
# print(tempdf['month'].value_counts())
#
# # 利用分组思想计算每月开盘天数
# a = tempdf.groupby('month').count()
# print(a.close)
# # 计算每月的总成交量
# b = tempdf.groupby('month').sum()
# print(b.volume)
# c = tempdf.groupby('month').volume.sum()
# print(c)

# 数据合并操作
# append方法
p = quotesdf[:2]
q = quotesdf['2018-05-07':'2018-05-11']
print(p.append(q))
# concat方法
pieces = [quotesdf[:5], quotesdf[len(quotesdf)-5:]]
print(pd.concat(pieces))
