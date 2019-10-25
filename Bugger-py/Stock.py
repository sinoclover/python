import requests, re, traceback, bs4

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)  # 获取股票列表的网页页面
    soup = bs4.BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')  # 寻找a标签并返回列表
    for i in a:  # 遍历每一个a标签
        try:
            href = i.attrs['href']  # 查找每个a标签的href属性并将字符串赋给href
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0]) # 将href中匹配正则表达式的所有字符串返回一个列表，并将列表中的第一个元素（即股票代码）添加至数据列表中
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    count = 0  # 设置计数器
    for stock in lst:  # 遍历数据列表中的所有股票代码
        url = stockURL + stock + '.html'  # 根据股票代码生成URL链接
        html = getHTMLText(url)  # 获取个股信息网页页面
        try:
            if html == '':
                continue
            infoDict = {}
            soup = bs4.BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})  # 查找页面中一个带有相关个股属性的DIV标签

            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0] # 查找该标签中的带有所有个股名称属性的标签并返回列表,并将第一个标签返回name
            infoDict.update({'股票名称': name.text.split()[0]})  # 更新字典，将name标签中的文本赋值给键值对中的值

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print('\r当前速度: {:.2f}%'.format(count * 100 / len(lst)), end = '')  # 在with结构中相当于try...except结构
        except:
            count = count + 1
            print('\r当前速度: {:.2f}%'.format(count * 100 / len(lst)), end='')
            traceback.print_exc()
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'F://Coding/PYTHON/Bugger-py/info/baidu_stock.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()
