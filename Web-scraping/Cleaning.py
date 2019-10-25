# 脏数据的清理
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re

# 清理所有半角全角符号，留下字母、数字和中文
def remove_punctuation(input):
  rule = re.compile(u'[^a-zA-Z0-9\u4e00-\u9fa5]')
  input = rule.sub('', input)
  return input

# 文本清理
def cleanInput(input):
    input = re.sub('\n+', '', input)
    input = re.sub('[0-9]*', '', input)
    input = re.sub(' +', '', input)
    input = bytes(input, 'UTF-8')
    input = input.decode('UTF-8', 'ignore')
    input = remove_punctuation(input)
    cleanInput = []
    for item in input:
        cleanInput.append(item)
    return cleanInput
# n-gram模型
def ngrams(input, n):
    input = cleanInput(input)  # 对输入进行清理
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

try:
    html = urlopen("https://baike.baidu.com/item/%E9%80%BB%E8%BE%91/543")
    bsObj = BeautifulSoup(html, 'html.parser')
    context = bsObj.find('div', {'class':'lemma-summary'}).get_text()
except Exception as e:
    print(e)

ngrams = ngrams(context, 2)
ngrams = OrderedDict(ngrams)
ngrams = sorted(ngrams.items(), key=lambda t: t[0], reverse=True)
print(ngrams)
print('2-grams count is: ' + str(len(ngrams)))