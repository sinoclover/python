# 通过互联网的采集，不同类型的网络爬虫
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# 获取页面内所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme + '://' + urlparse(includeUrl).netloc
    internalLinks = []
    # 找出所有以'/'开头的链接
    for link in bsObj.findAll('a', href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if link.attrs['href'].startswith('/'):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    try:
        # 找出所有以'http'或'www'开头且不包含当前URL的链接
        for link in bsObj.findAll('a', href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in externalLinks:
                    externalLinks.append(link.attrs['href'])
    except AttributeError as e:
        return None
    return externalLinks

# 获取任意外链
def getRandomExternalLink(startingPage):
    try:
        html = urlopen(startingPage, timeout=1)
    except (HTTPError, URLError) as e:
        print('Can not request this site, trace back to the index')
        return getRandomExternalLink('http://sina.com.cn')
    try:
        bsObj = BeautifulSoup(html, 'html.parser', from_encoding="utf-8")
    except AttributeError as e:
        return None

    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    # 没有找到外链的情况
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        domain = urlparse(startingPage).scheme + '://' + urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        if len(internalLinks) == 0:
            print('No internal links, trace back to the index')
            return getRandomExternalLink('http://sina.com.cn')
        else:
            return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExteralOnly(startingSite):
    global pages
    externalLink = getRandomExternalLink(startingSite)
    if externalLink not in pages:
        pages.add(externalLink)
        print('Random external link is: ' + externalLink)
        followExteralOnly(externalLink)
    else:
        followExteralOnly(startingSite)

followExteralOnly('http://sina.com.cn')
