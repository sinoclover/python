# # 采集整个网站
# # 为了避免一个页面被采集多次，需要对链接进行去重
# from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
# from bs4 import BeautifulSoup
# import re
#
# pages = set()
#
# def getLinks(pageUrl):
#     global pages
#     try:
#         html = urlopen('http://baike.baidu.com' + pageUrl)
#     except (HTTPError, URLError) as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html, 'html.parser')
#     except AttributeError as e:
#         return None
#
#     for link in bsObj.findAll('a', target='_blank', href=re.compile('^(/item/)')):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 newPage = link.attrs['href']
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
#
# getLinks('') # 即从主页进行爬取链接
#
# # 默认的递归限制是1000次

# 完善收集整个百度百科网站数据
from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import re

pages  = set()

def getLinks(pageUrl):
    global pages
    try:
        html = urlopen('http://baike.baidu.com' + pageUrl)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html, 'html.parser')
    except AttributeError as e:
        return None
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find('div', {'class': 'lemma-summary'}).find('div', {'class': 'para'}).get_text())
    except AttributeError as e:
        print('页面缺失一些属性！不过不用担心!')

    for link in bsObj.findAll('a', target='_blank', href=re.compile('^(/item/)((?!=).)*$')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('----------------\n' + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')