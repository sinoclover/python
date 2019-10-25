# 自然语言处理概况数据
from urllib.request import urlopen
import re
import string  # 获取所有的标点符号
import operator

# 单词清洗
def isCommon(ngram):
    ngrams = ngram.split(' ')  # 先将2-gram拆开
    # 清洗以下没有意义的单词
    commonWords=['the', 'be', 'and', 'of', 'a', 'in', 'to', 'have', 'it', 'i', 'for', 'you', 'he',
                 'with', 'on', 'do', 'say', 'this', 'they', 'is', 'an', 'at', 'but', 'we', 'his',
                 'from', 'that', 'not', 'by', 'she', 'or', 'what', 'go', 'their', 'can', 'who',
                 'get', 'if', 'would', 'her', 'all', 'my', 'make', 'about', 'know', 'will', 'as',
                 'up', 'one', 'time', 'has', 'been', 'there', 'year', 'so', 'think', 'when', 'which',
                 'them', 'some', 'me', 'people', 'take', 'out', 'into', 'just', 'see', 'him', 'your',
                 'come', 'could', 'now', 'than', 'like', 'other', 'how', 'then', 'its', 'our', 'two',
                 'more', 'these', 'want', 'way', 'look', 'first', 'also', 'new', 'because', 'day', 'use',
                 'no', 'man', 'find', 'here', 'thing', 'give', 'many', 'well']
    # 判断2-gram中是否存在要清洗的单词
    for word in ngrams:
        if word.lower() in commonWords:
            return False
    return True

# 输入清洗
def cleanInput(input):
    input = re.sub('\n+', ' ', input).lower()
    input = re.sub('\[[0-9]*\]', '', input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'UTF-8')  # 将输入转换为bytes对象，默认编码为utf8
    input = input.decode('ascii', 'ignore')  # 对bytes对象进行解码，解码为ascii,并忽略错误处理方案
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)  # strip移除字符串收尾指定的字符
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

# n-gram模型
def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = ' '.join(input[i:i+n])
        # 对词组进行判断
        if isCommon(ngramTemp):
            if ngramTemp not in output:
                output[ngramTemp] = 0
            output[ngramTemp] += 1
    return output


content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
ngrams = ngrams(content, 2)  # 生成字典的形式，键是2-gram序列，值是出现的次数
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sortedNGrams)

# 获取keywords
keywords = []  # 获取高频关键词列表
hqngrams = []  # 获取与高频关键词有关的NGRAMS模型列表
for i in range(0, len(sortedNGrams)):
    if sortedNGrams[i][1] > 2:
        keywords.append(sortedNGrams[i][0])
for i in range(0, len(keywords)):
    if sortedNGrams[i][0] == keywords[i]:
        hqngrams.append(sortedNGrams[i])
print(keywords)

# 获取含有关键词的第一个句子
sentences = set()  # 存储文章所有句子
main_sentences = set()  # 存储关键句

content = content.lower()
for i in content.split('. '):
    sentences.add(i)

for keyword in keywords:
    for sentence in sentences:
        b = sentence.find(keyword)
        if b != -1:
            sentence = re.sub('\n+', '', sentence)
            sentence = re.sub(' +', ' ', sentence)
            main_sentences.add(sentence)
            break
for i in main_sentences:
    print(i)

