import scrapy
from baikeSpider.items import Article
import random

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/XPath/5574064?fr=aladdin', 'https://baike.baidu.com/item/Python/407313']

    # user_agent_list = [ "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    #     "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    #     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    #     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    #     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    #     "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    #     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    #     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    # ]
    # ua = random.choice(user_agent_list)  # 随机抽取User-Agent
    # headers = {
    #     'Accept-Encoding': 'gzip, deflate, sdch, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.8',
    #     'Connection': 'keep-alive',
    #     'Referer': 'https://baike.baidu.com/',
    #     'User-Agent': ua
    # }  # 构造请求头

    custom_settings = headers

    # def start_requests(self):
    #     ua = random.choice(self.user_agent_list)  # 随机抽取User-Agent
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, sdch, br',
    #         'Accept-Language': 'zh-CN,zh;q=0.8',
    #         'Connection': 'keep-alive',
    #         'Referer': 'https://baike.baidu.com/',
    #         'User-Agent': ua
    #     }  # 构造请求头
    #
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, headers=headers)

    def parse(self, response):
        item = Article()
        # title = response.css('.lemmaWgt-lemmaTitle-title h1::text').extract()[0]
        title = response.xpath('//h1/text()')[0].extract()
        print('Title is: ' + title)
        item['title'] = title
        return item
