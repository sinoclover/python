# import pymysql
#
# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1205', db='mysql', charset='utf8')
# cur = conn.cursor()
# cur.execute('use scraping')
# # execute()方法执行mysql的查询
# cur.execute("select * from pages where id = 1")
# # fetchone()方法获取查询数据
# print(cur.fetchone())
# cur.close()
# conn.close()

# 将百度百科的信息存入数据库
from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1205', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('use scraping')

random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute('insert into pages (title, content) values (\"%s\", \"%s\")', (title, content))
    cur.connection.commit()

def getLinks(articleUrl):
    try:
        html = urlopen('http://baike.baidu.com' + articleUrl)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html, 'html.parser', from_encoding="utf-8")
    except AttributeError as e:
        return None

    innerLinks = []
    for link in bsObj.find('div', {'class': 'body-wrapper'}).findAll('a', target='_blank', href=re.compile('^(/item/)(.)*$')):
        if 'href' in link.attrs:
            if link not in innerLinks:
                innerLinks.append(link.attrs['href'])

    try:
        title = bsObj.find('h1').get_text()
        content = bsObj.find('div', {'class': 'lemma-summary'}).find('div', {'class': 'para'}).get_text()
        store(title, content)
    except AttributeError as e:
        return innerLinks

    return innerLinks

article = '/item/%E8%89%BE%E4%BC%A6%C2%B7%E9%BA%A6%E5%B8%AD%E6%A3%AE%C2%B7%E5%9B%BE%E7%81%B5'
links = getLinks(article)

try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)]
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()




