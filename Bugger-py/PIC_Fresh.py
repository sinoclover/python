#coding:UTF-8
import requests, bs4, os, random

def getHeader():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    ua = random.choice(user_agent_list)
    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'https://gupiao.baidu.com/',
        'User-Agent': ua
    }
    return headers

def getHTMLText(url):
    try:
        r = requests.get(url, headers=getHeader())
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def getListOfPic_url(listPicurl, html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    pic_url = soup.find('ul', attrs={'class': 'item_list'})
    all_a = pic_url.find_all('a', attrs={'target': '_blank', 'title': ''})
    for a in all_a:
        try:
            href = a.attrs['href']
            listPicurl.append(href)
        except:
            continue

def getPicInfo(listPicurl):
    counter = 0
    for url in listPicurl:
        html = getHTMLText(url)
        listPicInfo = []
        soup = bs4.BeautifulSoup(html, 'html.parser')
        pic_info = soup.find('div', attrs={'class': 'content-c'})
        all_a = pic_info.find_all('a')
        for a in all_a:
            try:
                href = a.attrs['href']
                listPicInfo.append(href)
            except:
                continue
        storePic(url, listPicInfo)
        counter += 1
        print('\r {:.2f}% of this page has been done.'.format(counter * 100 / 36), end='')

def storePic(url, listPicInfo):
    root = 'F://pic//1//'
    file_name = url.split('/')[-1]
    path = root + file_name
    if not os.path.exists(root):
        os.mkdir(root)
    for pic in listPicInfo:
        try:
            pic_name = pic.split('/')[-1]
            path_pic = path + '//' + pic_name
            if not os.path.exists(path):
                os.makedirs(path)
            if not os.path.exists(path_pic):
                r = requests.get(pic, headers=getHeader())
                with open(path_pic, 'wb') as f:
                    f.write(r.content)
                    f.close()
            else:
                continue
        except:
            print('Error')

def main():
    for counter in range(1, 3):
        url = 'http://wmtp.net/tupian/qingxin/page/' + str(counter)
        listPicurl = []
        html = getHTMLText(url)
        getListOfPic_url(listPicurl, html)
        getPicInfo(listPicurl)
        print('Page {} has already done.'.format(counter))

main()