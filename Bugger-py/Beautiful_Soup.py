# # 网页解析前的状态
# import requests
#
# url = 'https://python123.io/ws/demo.html'
# try:
#     r = requests.get(url)
#     print(r.status_code)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     demo = r.text
#     new_file = open('info/demo_origin.txt', 'w')
#     new_file.write(demo)
#     new_file.close()
# except:
#     print('Get Error')

# # BeautifulSoup类的使用对网页进行解析
# import requests, bs4
#
# url = 'https://python123.io/ws/demo.html'
# try:
#     r = requests.get(url)
#     print(r.status_code)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     demo = r.text
#     soup = bs4.BeautifulSoup(demo, 'html.parser')
#     new_file = open('info/demo.txt', 'w')
#     new_file.write(soup.prettify())
#     new_file.close()
# except:
#     print('Get Error')

# # BeautifulSoup库的基本元素
# import requests, bs4
#
# url = 'http://python123.io/ws/demo.html'
# r = requests.get(url)
# demo = r.text
# soup = bs4.BeautifulSoup(demo, 'html.parser')
# print(soup.title)
# print(soup.p)
# tag1 = soup.p
# print(tag1.attrs)
# print(tag1.string)
# print(soup.a)
# tag2 = soup.a
# print(tag2.attrs)
# print(tag2.string)

# # 内容遍历方法
# import requests, bs4
#
# url = 'http://python123.io/ws/demo.html'
# r = requests.get(url)
# demo = r.text
# soup = bs4.BeautifulSoup(demo, 'html.parser')
# # 下行遍历
# print(soup.head)
# print(soup.head.contents)  # 返回子节点的列表
# print(soup.body.contents)
# print(len(soup.body.contents))
# print(soup.body.contents[1])
# # 上行遍历
# print(soup.title.parent)
# print(soup.html.parent)
# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)
# # 平行遍历
# print(soup.a.next_sibling)
# print(soup.a.previous_sibling)

# # prettify方法
# import requests, bs4
#
# url = 'http://python123.io/ws/demo.html'
# r = requests.get(url)
# demo = r.text
# soup = bs4.BeautifulSoup(demo, 'html.parser')
# print(soup.prettify())

# # 搜索与解析融合方法提取关键信息
# import requests, bs4
#
# url = 'http://python123.io/ws/demo.html'
# r = requests.get(url)
# demo = r.text
# soup = bs4.BeautifulSoup(demo, 'html.parser')  # 使用bs4解析HTML页面
# for link in soup.find_all('a'):  # find_all搜索所有<a>标签
#     print(link.get('href'))

# 基于bs4库的HTML内容查找方法
import requests, bs4, re

url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
soup = bs4.BeautifulSoup(demo, 'html.parser')
print(soup.find_all('a'))
print(soup.find_all(['a', 'b']))  # 返回列表形式存储查找到的数据
for tag in soup.find_all(True):  # True表示查找所有标签信息
    print(tag.name)
for tag in soup.find_all(re.compile('b')):
    print(tag.name)  # 使用正则表达式查找以b开头的标签信息
print(soup.find_all('p', 'course'))  # 对标签属性进行查找
print(soup.find_all(id = 'link1'))
print(soup.find_all(id = 'link'))
print(soup.find_all(id = re.compile('link')))  # 使用正则表达式查找所有link相关的属性信息
print(soup.find_all('a', recursive = False))
print(soup.find_all(string = 'Basic Python'))
print(soup.find_all(string = re.compile('python')))
