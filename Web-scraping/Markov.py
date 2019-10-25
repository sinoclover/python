from urllib.request import urlopen
from random import randint

# 处理文本，建立基于出现次数的字典
def buildWordDict(text):
    # 删除换行符和引号
    text = text.replace('\n', ' ')
    text = text.replace('\"', '')
    # 保证每个标点都和前面的单词在一起，这样不会被剔除，保留在马尔科夫链中
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, ' '+symbol+' ')  # 给其他标点两侧添加空格
    # 分割并过滤空单词
    words = text.split(' ')
    words = [word for word in words if word != '']
    # 建立文本词典
    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            # 为单词新建一个字典
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] += 1  # 分析每个相邻词出现的次数
    return wordDict

# 计算某个单词之后下一个单词可能性的总权重
def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum

def retrieveRandomWord(wordList):
    # 随机选取单词在总权重中的某个权值
    randIndex = randint(1, wordListSum(wordList))  # 包括两端数字
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
wordDict = buildWordDict(content)
print(wordDict)

# 生成链长为100的马尔科夫链
length = 100
chain = ''
# 确定随机的开始值
currentWord = 'I'
for i in range(0, length):
    chain += currentWord + ' '
    currentWord = retrieveRandomWord(wordDict[currentWord])
print(chain)