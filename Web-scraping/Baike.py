# # 百度百科六度分隔理论实验
#
# # 1 获取静态百度百科页面上的词条链接
# from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
# from bs4 import BeautifulSoup
# import re
#
# def getHtml(url):
#     try:
#         html = urlopen(url)
#     except (HTTPError, URLError) as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html, 'html.parser')
#     except AttributeError as e:
#         return None
#     return bsObj
#
# url = 'https://baike.baidu.com/item/%E8%89%BE%E4%BC%A6%C2%B7%E9%BA%A6%E5%B8%AD%E6%A3%AE%C2%B7%E5%9B%BE%E7%81%B5'
# bsObj = getHtml(url)
#
# for link in bsObj.find('div', {'class': 'body-wrapper'}).findAll('a', target='_blank', href=re.compile('^(/item/)(.)*$')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# 2 继续调用百度百科页面上其他词条链接，直到主动停止或新页面上没有新的链接
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import datetime
import random
import re

# 使用系统时间作为随机数序列生产的起点，使之更有随机性
random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    try:
        html = urlopen('http://baike.baidu.com' + articleUrl)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html, 'html.parser', from_encoding="utf-8")
    except AttributeError as e:
        return None
    return bsObj.find('div', {'class': 'body-wrapper'}).findAll('a', target='_blank', href=re.compile('^(/item/)(.)*$'))

article = '/item/%E8%89%BE%E4%BC%A6%C2%B7%E9%BA%A6%E5%B8%AD%E6%A3%AE%C2%B7%E5%9B%BE%E7%81%B5'
links = getLinks(article)
while(len(links) > 0):
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
