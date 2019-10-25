# 用Selenium执行JS
# Selenium是强大的网络数据采集工具，可以让浏览器自动加载页面，获取需要的数据，甚至页面截屏，或者判断网站上某些动作的是否发生
# Selenium自己不带浏览器，需要与第三方浏览器结合，如phantomJS无头浏览器。
# 常规采集带有Ajax的页面信息

# import requests
#
# r = requests.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
# print(r.text)  # 得不到JS脚本生成的页面信息

# # 通过phantomJS获取Ajax后的数据
# from selenium import webdriver
# import time
#
# driver = webdriver.PhantomJS(executable_path='D:/Ide/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs')
# driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
# time.sleep(3)   # 延迟3秒加载时间，即显式等待，但很多网站的页面加载速度是不确定的
# print(driver.find_element_by_id('content').text)
# driver.close()

# # 检查页面是否已经完全加载，通过检查某个元素是否存在
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.PhantomJS(executable_path='D:/Ide/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs')
# driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
# try:
#     # 隐式等待，即等DOM中某个状态发生后再继续运行代码
#     # 通过定位器查找ID为loadedButton的按钮元素
#     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'loadedButton')))
# finally:
#     print(driver.find_element_by_id('content').text)
#     driver.close()

# 处理重定向
# 客户端重定向是在服务器将页面内容发送到浏览器之前，由浏览器执行JS完成的页面跳转，而非服务器完成的跳转。
# 当使用浏览器方位页面时，很难区分这两种重定向，但进行网络数据采集时，则差异非常明显。
# 检测客户端重定向，通过从页面开始加载监视DOM中一个元素，并重复调用，知道Selenium抛出StaleElementReferenceException异常，即元素不在页面DOM中，这表示网站已经跳转
from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def waitForLoad(driver):
    elem = driver.find_element_by_tag_name('html')
    count = 0
    while True:
        count += 1
        if count > 20:
            print('Timing out after 10 seconds and returning')
            return
        time.sleep(.5)
        try:
            elem = driver.find_element_by_tag_name('html')
        except StaleElementReferenceException:
            return

driver = webdriver.PhantomJS(executable_path='D:/Ide/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/redirectDemo1.html')
waitForLoad(driver)
print(driver.page_source)
