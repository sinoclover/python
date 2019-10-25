# bs4获取网页范式
from urllib.request import urlopen
from bs4  import BeautifulSoup
from urllib.error import URLError, HTTPError

def getHtml(url):
    try:
        html = urlopen(url)
    except (URLError, HTTPError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html, 'html.parser')
    except AttributeError as e:
        return None
    return bsObj

url1 = 'http://www.pythonscraping.com/pages/warandpeace.html'
url2 = 'http://www.pythonscraping.com/pages/page3.html'
bsObj1 = getHtml(url1)
bsObj2 = getHtml(url2)

# # find与findAll获取标签Tag对象
#
# # 对于find与findAll一般只使用tag和attributes参数
# nameList1 = bsObj1.findAll('span', {'class': 'green'})
# for name in nameList1:
#     print(name.get_text()) # 在获取数据时使用，一般保留标签结构
#
# # recursive参数是布尔变量，控制抓取层数。默认True抓取所有子标签，而设置为False时则仅查找一级标签
#
# # text参数用标签的文本内容去匹配
# nameList2 = bsObj1.findAll(text='the prince')
# print(len(nameList2))
#
# # keyword参数可以选择具有指定属性的标签
# allText = bsObj1.findAll(id='text')
# print(allText[0].get_text())

# # 处理标签
#
# # 处理子标签
# for child in bsObj2.find('table', {'id': 'giftList'}).children:
#     print(child)

# # 处理兄弟标签
# for sibling in bsObj2.find('table', {'id': 'giftList'}).tr.next_siblings:
#     print(sibling)
#
# # 处理父标签
# print(bsObj2.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())





