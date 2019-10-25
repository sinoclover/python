import requests, re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def parsePage(ls, html):
    try:
        pls1 = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        pls2 = re.findall(r'\"price\"\:\"[\d\.]*\"', html)
        tls1 = re.findall(r'\"raw_title\"\:\".*?\"', html)
        tls2 = re.findall(r'\"title\"\:\".*?\"', html)
        if len(pls1) == 0:
            for i in range(len(pls2)):
                price = eval(pls2[i].split(':')[1])
                title = eval(tls2[i].split(':')[1])
                ls.append([price, title])
        else:
            for i in range(len(pls1)):
                price = eval(pls1[i].split(':')[1])
                title = eval(tls1[i].split(':')[1])
                ls.append([price, title])


    except:
         print('')

def printGoodsList(ls):
    tplt = '{:4}\t{:8}\t{:16}'
    new_file = open('info/淘宝耳机.txt', 'w')
    new_file.write(tplt.format('序号', '价格', '商品名称') + '\n')
    print(tplt.format('序号', '价格', '商品名称'))
    count = 0
    for i in ls:
        count = count + 1
        print(tplt.format(count, i[0], i[1]))
        new_file.write(tplt.format(count, i[0], i[1]) + '\n')
    new_file.close()

def main():
    goods = '耳机'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()

