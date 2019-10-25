import requests, bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def fillUnivList(ulist, html):
    soup = bs4.BeautifulSoup(html, 'html.parser')  # 将网页解析为bs4类
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')  # 将tr标签中的td标签存入一个列表
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
    tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'
    tplt2 = '{0:^10}\t{1:{3}^10}\t{2:^10}\n'
    new_file = open('info/University_Rank.txt', 'w')
    print(tplt.format("排名","学校名称","总分", chr(12288)))
    new_file.write(tplt2.format("排名","学校名称","总分", chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2], chr(12288)))
        new_file.write(tplt2.format(u[0],u[1],u[2], chr(12288)))
    new_file.close()

uinfo = []
url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
html = getHTMLText(url)
fillUnivList(uinfo, html)
printUnivList(uinfo, 20)
