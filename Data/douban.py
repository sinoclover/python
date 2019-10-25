# 豆瓣书评爬取
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

# # 爬取过程
# def getHtmlText(url):
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except Exception as e:
#         print(e)
#
# def getInfoList(userList, scoreList, commentList, html):
#     try:
#         bsObj = BeautifulSoup(html, 'html.parser')
#         allInfo = bsObj.findAll('li', attrs={'class':'comment-item'})
#         for info in allInfo:
#             comment = info.find('span', attrs={'class':'short'})
#             commentList.append(comment.string)
#             user_pattern = re.compile(r'<a href="https://www.douban.com/people/.*?/">(.*?)</a>')
#             user = re.findall(user_pattern, str(info))
#             userList.append(user[0])
#             try:
#                 score_pattern = re.compile(r'<span class="user-stars allstar(.*?) rating"')
#                 score = re.findall(score_pattern, str(info))
#                 scoreList.append(float(score[0]))
#             except IndexError as e:
#                 scoreList.append(float(0))
#     except AttributeError as e:
#         print(e)
#
# page = 0
# userList = []
# scoreList = []
# commentList = []
# while(page < 3):
#     url = 'https://book.douban.com/subject/1770782/comments/hot?p=' + str(page+1)
#     html = getHtmlText(url)
#     getInfoList(userList, scoreList, commentList, html)
#     page += 1
#
# # 数据整理
# data = []
# for i in range(0, len(userList)):
#     data.append([userList[i], scoreList[i], commentList[i]])
# douban_frame = pd.DataFrame(data)
#
# douban_frame.index = range(1, len(data)+1)
# cols = ['name', 'score', 'comment']
# douban_frame.columns = cols
# douban_frame.to_csv('../Data/data/douban.csv', encoding='utf_8_sig')

# 数据库数据存储
import pymysql

# from sqlalchemy import create_engine # 通过sqlalchemy.create_engine建立连接
# pymysql.install_as_MySQLdb()  # 建立MYSQL接口程序
# result = pd.read_csv('../Data/data/douban.csv', index_col=0)
# engine = create_engine('mysql+mysqldb://root:1205@localhost:3306/scraping?charset=utf8')
# pd.io.sql.to_sql(result, 'douban', con=engine, schema='scraping', if_exists='append', index=False)

# 数据库数据调取
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1205', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('use scraping')
sql_cmd = 'select * from douban'
try:
    table = pd.read_sql(sql_cmd, con=conn, index_col='id')
    table = table.drop(['time'], axis=1)
finally:
    cur.close()
    conn.close()

# 数据基本分析及可视化
import matplotlib.pyplot as plt

print('The mean score is {:.2f}'.format(table.score.mean()))
score_count = table.groupby('score').score.count()
x = score_count.index
y = score_count.values
f = plt.pie(y, labels=x, startangle=90, shadow=False, autopct='%1.1f%%',
              textprops={'fontsize':10}, labeldistance=1.1, explode=(0, 0, 0, 0, 0.05))

plt.axis('equal')
plt.title("Score distribution map")
plt.legend()
plt.show(f)








