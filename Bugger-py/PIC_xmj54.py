#coding:UTF-8
import requests, bs4, os, random, re

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
        'Referer': 'https://www.meituri.com/t/298/',
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
    pic_url = soup.find('div', attrs={'class': 'hezi'})
    all_a = pic_url.find_all('a', {'href': re.compile(r'https://www.meituri.com/a/.*?/')})
    for a in all_a:
        try:
            href = a.attrs['href']
            listPicurl.append(href)
        except:
            continue

def getPicInfo(listPicurl):
    counter = 0
    for url in listPicurl:
        listPicInfo = []
        html = getHTMLText(url)
        soup = bs4.BeautifulSoup(html, 'html.parser')
        picInfo = soup.find('div', attrs={'class': 'content'})
        all_a = picInfo.find_all('img')
        for a in all_a:
            try:
                href = a.attrs['src']
                listPicInfo.append(href)
            except:
                continue
        for page in range(2, 20):
            try:
                urls = url + str(page) + '.html'
                htmls = getHTMLText(urls)
                soups = bs4.BeautifulSoup(htmls, 'html.parser')
                picInfos = soups.find('div', attrs={'class': 'content'})
                all_as = picInfos.find_all('img')
                for a in all_as:
                    try:
                        href = a.attrs['src']
                        listPicInfo.append(href)
                    except:
                        continue
            except:
                break
        storePic(url, listPicInfo)
        counter += 1
        print(counter)

def storePic(url, listPicInfo):
    root = 'F://pic//1//'
    file_name = url.split('/')[-2]
    print(file_name)
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
                f = open(path_pic, 'wb')
                f.write(r.content)
                f.close()
            else:
                continue
        except:
            print('Error')

def main():
    urls = ['https://www.meituri.com/t/298/', 'https://www.meituri.com/t/298/index_1.html']
    for url in urls:
        listPicurl = []
        html = getHTMLText(url)
        getListOfPic_url(listPicurl, html)
        listPicurl = list(set(listPicurl))
        getPicInfo(listPicurl)

main()