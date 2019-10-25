# # 30家公司的道指数据
import requests
import re
import pandas as pd
import pymysql
import matplotlib.pyplot as plt

# # 爬取框架
#
# # 获取网页页面信息
# def getHtmlText(url):
#     try:
#         r = requests.get(url, timeout = 30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except Exception as e:
#         print(e)
# # 获取需求数据放入列表中
# def getInfoList(html):
#     search_pattern = re.compile(r'class="wsod_symbol">(.*?)</a>.*?<span.*?>(.*?)</span>.*?\n'
#                                 r'.*?class="wsod_stream">(.*?)</span>')
#     items = re.findall(search_pattern, html)
#     data = []
#     for item in items:
#         data.append([item[0], item[1], float(item[2])])
#     return data
#
# # 爬取主程序
# data = []
# url = "https://money.cnn.com/data/dow30/"
# html = getHtmlText(url)
# data = getInfoList(html)
# print(data)
#
# # 基于pandas的数据处理并存储数据
#
# # data_frame = pd.DataFrame(data)
# # cols = ['code', 'name', 'price']
# # data_frame.columns = cols
# # data_frame.index = range(1, len(data_frame)+1)
# # data_frame.to_csv('data/dow.csv')
#
# # 写入数据库
# from sqlalchemy import create_engine
#
# pymysql.install_as_MySQLdb()
# result = pd.read_csv('data/dow.csv', index_col=0)
# engine = create_engine('mysql+mysqldb://root:1205@localhost:3306/scraping?charset=utf8')
# pd.io.sql.to_sql(result, 'dow', con=engine, schema='scraping', if_exists='append', index=False)  # replace将原表删除重建, fail不操作

# 数据库数据调取
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1205', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('use scraping')
sql_cmd = 'select * from dow'
try:
    table = pd.read_sql(sql_cmd, con=conn, index_col='id')
    table = table.drop(['time'], axis=1)
finally:
    cur.close()
    conn.close()

# 数据基本分析及可视化
new_table = table.sort_values(by=['price'], ascending=False)
new_table.index = range(1, len(new_table)+1)

x = new_table.code
y = new_table.price

plt.figure(figsize=(18, 12))
plt.title('Companies in the Dow Jones Industrial Average.')
plt.xlabel('Code')
plt.ylabel('Price')

# 在绘图时将xy轴分开绘制
plt.xticks(range(len(new_table)),new_table['code'])
fig = plt.bar(range(len(new_table)), y)
plt.savefig('fig/dow.jpg', dpi=300)
plt.show(fig)






