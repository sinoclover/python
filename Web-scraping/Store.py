# # 下载一个文件
# from urllib.request import urlopen
# from urllib.request import urlretrieve
# from urllib.error import HTTPError, URLError
# from bs4 import BeautifulSoup
# import os
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
# url = 'http://www.pythonscraping.com'
# bsObj = getHtml(url)
# imageLocation = bsObj.find('a', {'id': 'logo'}).find('img')['src']
# print(imageLocation)
#
# path = '../Web-scraping/pic'
# if not os.path.exists(path):
#     os.makedirs(path)
# urlretrieve(imageLocation, '../Web-scraping/pic/logo.jpg')

# # 下载所有SRC属性的文件
# import os
# from urllib.request import urlopen
# from urllib.request import urlretrieve
# from urllib.error import HTTPError, URLError
# from bs4 import BeautifulSoup
#
# # 获取文件绝对路径，即下载路径
# def getAbsoluteUrl(baseUrl, source):
#     if source.startswith('http://www.'):
#         url = 'http://' + source[11:]
#     elif source.startswith('http://'):
#         url = source
#     elif source.startswith('www'):
#         url = 'http://' + source[4:]
#     else:
#         url = baseUrl + '/' + source
#
#     if baseUrl not in url: # 去掉外链
#         return None
#     return url
#
# # 获取存储路径，通过替换掉www和baseUrl，得到的尾链作为存储文件路径
# def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
#     path = absoluteUrl.replace('www', '')
#     path = path.replace(baseUrl, '')
#     path = downloadDirectory + path
#     directory = os.path.dirname(path)
#
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
#     return path
#
# # 获取页面bsObj
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
# downloadDirectory = 'downloaded' # 创建文件夹
# baseUrl = 'http://pythonscraping.com'
# bsObj = getHtml(baseUrl)
# downloadList = bsObj.findAll(src = True) # 获取网页所有SRC资源
#
# for download in downloadList:
#     fileUrl = getAbsoluteUrl(baseUrl, download['src']) # 获取SRC资源的下载路径
#     if fileUrl is not None: # 如果资源路径存在
#         print(fileUrl)
#         urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))

# # CSV
# import csv
# import os
#
# path = '../Web-scraping/files'
# if not os.path.exists(path):
#     os.makedirs(path)
# csvFile = open('../Web-scraping/files/test.csv', 'w+', newline='')  # 使用newline解决隔行问题，即不换行
# try:
#     writer = csv.writer(csvFile)
#     writer.writerow(('number', 'number plus 2', 'number times 2'))
#     for i in range(10):
#         writer.writerow((i, i+2, i*2))
#
# finally:
#     csvFile.close()

# 获取html表格table并写入CSV文件
import csv
import os
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getHtml(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html, 'html.parser')
    except AttributeError as e:
        return None
    return bsObj

url = 'https://baike.baidu.com/'
bsObj = getHtml(url)
if bsObj is None:
    print('This page is not exist.')

table = bsObj.findAll('table', {'class': 'statistics_num'})[0]
rows = table.findAll('tr')

path = '../Web-scraping/files'
if not os.path.exists(path):
    os.makedirs(path)

csvFile = open('../Web-scraping/files/editors.csv', 'wt', newline='', encoding='gbk')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll('td'):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
