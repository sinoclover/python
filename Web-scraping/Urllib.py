# # 1 使用urllib、bs4进行对象爬取
# from urllib.request import urlopen
# from urllib.error import URLError, HTTPError
# from bs4 import BeautifulSoup
#
# def getTitle(url):
#     # 针对URL可能出现的异常进行处理
#     try:
#         html = urlopen(url)
#     except (URLError, HTTPError) as e:
#         return None
#     # 解析网页并存储标签，同时针对bs4对象为空的异常进行处理
#     try:
#         bsObj = BeautifulSoup(html, 'html.parser')
#         print(type(bsObj))  # BeautifulSoup对象
#         title = bsObj.title
#     except AttributeError as e:
#         return None
#     return title
#
# title = getTitle('http://news.baidu.com/')
# # 针对标签为空的情况进行处理
# if title is None:
#     print('Title could not be found')
# else:
#     print(title)
#     print(type(title))  # 标签Tag对象
#     print(title.string)
#     print(title.get_text())
#     print(title.text)

# # 根据CSS属性查找标签
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# bsObj = BeautifulSoup(html, 'html.parser')
#
# nameList = bsObj.find_all('span', attrs={'class': 'green'})
# for name in nameList:
#     print(name.string)

# # 处理标签
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bsObj = BeautifulSoup(html, 'html.parser')
# bsObj.prettify()
# # 处理子标签
# for child in bsObj.find('table', attrs={'id':'giftList'}).children:
#     print(child)
# # 处理兄弟标签
# for sibling in bsObj.find('table', attrs={'id':'giftList'}).tr.next_siblings:
#     print(sibling)
# # 处理父标签
# print(bsObj.find('img', attrs={'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())