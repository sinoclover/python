from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    # 排除URL错误和HTTP未响应的情况，将返回空对象
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    # 排除不存在的标签情况，即调用空对象的标签属性
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.title
    except AttributeError as e:
        return None
    return title

title = getTitle('http://news.baidu.com/')
if title is None:
    print('Title could not be found')
else:
    print(title)

