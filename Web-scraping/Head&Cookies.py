# # 通过requests模块自定义请求头和cookie设置
# import requests
# from bs4 import BeautifulSoup
#
# session = requests.Session()
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
#            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
# url = 'https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending'
# req = session.get(url, headers=headers)
#
# bsObj = BeautifulSoup(req.text, 'html.parser')
# print(bsObj.find('table',{'class': 'table-striped'}).get_text)

# 网站会通过cookie跟踪访问过程，如果发现爬虫的异常行为就会中断访问
# 检查网站生成的cookie，考虑那些cookie是爬虫需要处理的

# 查看并获取网站中的cookie保存到变量中
from selenium import webdriver
driver = webdriver.PhantomJS(executable_path='D:/Ide/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get('http://pythonscraping.com')
driver.implicitly_wait(1)
print(driver.get_cookies())

savedCookies = driver.get_cookies()

# 加载相同网站，删除所有cookie，替换成之前获取的cookie
driver2 = webdriver.PhantomJS(executable_path='D:/Ide/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs')
driver2.get('http://pythonscraping.com')
driver2.delete_all_cookies()
for cookie in savedCookies:
    driver2.add_cookie(cookie)

driver2.get('http://pythonscraping.com')
driver2.implicitly_wait(1)
print(driver2.get_cookies())
