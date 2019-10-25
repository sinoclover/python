from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import re

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

url = 'http://www.pythonscraping.com/pages/page3.html'
bsObj = getHtml(url)

images = bsObj.findAll('img', {'src': re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
for image in images:
    print(image.attrs['src']) # 获取标签属性的内容
