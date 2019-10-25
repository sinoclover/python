import requests
import re
import json
import time
import numpy as np
import pandas as pd
from datetime import date

# # 获取AXP的股票情况
# def retrieve_quotes_historical(stock_code):
#     quotes = []
#     url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
#     r = requests.get(url)
#     m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
#     if m:
#         quotes = json.loads(m[0])
#         quotes = quotes[::-1]
#     return [item for item in quotes if not 'type' in item]
#
# quotes = retrieve_quotes_historical('AXP')
#
# # 将时间戳改为合适的时间序列作为index
# list_timeIndex = []
# for i in range(len(quotes)):
#     x = date.fromtimestamp(quotes[i]['date'])
#     y = date.strftime(x, '%Y-%m-%d')
#     list_timeIndex.append(y)
# quotesdf_ori = pd.DataFrame(quotes, index=list_timeIndex)
# quotesdf = quotesdf_ori.drop(['date'], axis=1)

# # 将信息存储到CSV中
# quotesdf.to_csv('../Data/data/stockAXP.csv')
# # 将信息存储到EXCEL中
# quotesdf.to_excel('../Data/data/stockAXP.xlsx', sheet_name = 'AXP')

# # 读取CSV数据，获得一个dataframe
# result = pd.read_csv('../Data/data/stockAXP.csv')
# print(result)
# 读取EXCEL数据，获得一个dataframe
result2 = pd.read_excel('../Data/data/stockAXP.xlsx')
print(result2)
