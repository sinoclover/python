# # 百度首页爬取
# import requests
#
# r = requests.get('http://www.baidu.com')
#
# print(r.status_code)
# print(type(r.text))
# file = open('info/baidu_index.txt', 'w', encoding = 'utf-8')
# file.write(r.text)
#
# print(r.encoding)
# print(r.apparent_encoding)
# r.encoding = 'utf-8'
# file = open('info/baidu_index.txt', 'a')
# file.write(r.text)
# file.close()

# # 百度首页爬取框架
# import requests
#
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout = 30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return 'Error'
#
# if __name__ == '__main__':
#     url = 'http://www.baidu.com'
#     print(type(getHTMLText(url)))
#     new_file = open('info/baidu_index2.txt', 'w')
#     new_file.write(getHTMLText(url))
#     new_file.close()


# # 京东商品信息爬取
# import requests
#
# url = 'https://item.jd.com/26126724547'
# try:
#     r = requests.get(url)
#     print(r.status_code)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     new_file = open('info/jingdong_item.txt', 'w', encoding = 'utf-8')  # 已经改成了UTF-8为何还要在文本中再改？
#     new_file.write(r.text)
#     new_file.close()
# except:
#     print('Get Error')

# # 亚马逊商品信息爬取
# import requests
#
# url = 'https://www.amazon.cn/dp/B0783MLRN3'
# try:
#     kv = {'user-agent':'Mozilla/5.0'}  # 更改浏览器属性
#     r = requests.get(url, headers = kv)
#     print(r.status_code)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     new_file = open('info/amazon_item.txt', 'w', encoding = 'utf-8')
#     new_file.write(r.text)
#     new_file.close()
# except:
#     print('Get Error')

# # 百度搜索
# import requests
#
# keyword = 'Python'
# try:
#     kv = {'wd' : keyword}
#     r = requests.get('http://www.baidu.com/s', params = kv)
#     print(r.request.url)
#     print(r.status_code)
#     r.raise_for_status()
#     print(len(r.text))
# except:
#     print('Get Error')

# 图片或其他资源爬取框架
import requests
import os
url = 'https://lh3.googleusercontent.com/-gCLkd9ncV8c/VxrkepybvoI/AAAAAAAA8Uo/PIlhS3qdgC8FZ8T_BFgWY3YBhMQeCYLlACHM/w800-o/002.jpg'
root = 'F://Coding//PYTHON//Bugger-py//pics//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        f = open(path, 'wb')
        f.write(r.content)
        f.close()
        print('File saved success')
    else:
        print('File is already existed')
except:
    print('Get Error')

