# 使用NLTK做统计分析
# 下载NLTK数据包
# import nltk
# nltk.download()

# from nltk import word_tokenize
# from nltk import Text
#
# tokens = word_tokenize('Here is some not very interesting text')
# text = Text(tokens)  # 通过字符串建立Text对象

# from nltk.book import *
# print(len(text6))
# fdist = FreqDist(text6)  # 选取'Monty Python and the Holy Grail'剧本生成频率分布对象
# print(fdist.most_common(10))  # 查看常用单词以及单词的频率
# print(fdist['Grail'])  # 查看特定单词的频率
#
# # 通过nltk创建n-gram模型
# # 或使用bigrams创建2-gram模型或用trigram创建3-gram模型
# from nltk import ngrams
#
# fourgrams = ngrams(text6, 4)
# fourgramsDist = FreqDist(fourgrams)
# print(fourgramsDist.most_common(2))

# NLTK的词性分析
from nltk import word_tokenize
from nltk import pos_tag

text = word_tokenize('Strange women lying in ponds distributing swords is no basisi for a system of government. Supreme'
                     ' executive power derives from a mandate from the masses, not from some farcical aquatic ceremony.')
print(pos_tag(text))
text2 = word_tokenize('He was objective in achieving his objective of writing an objective philosophy, primarily'
                      'using verbs in the objective case.')
print(pos_tag(text2))  # 即根据英文的上下文无关文法识别词性

# 处理搜索单词问题，如要采集作为专有名词的Google，而非动词的google
from nltk import sent_tokenize

sentences = sent_tokenize("Google is one of the best companies in the world. I constantly google myself to see what"
                          " I'am up to.")
nonus = ['NN', 'NNS', 'NNP', 'NNPS']

for sentence in sentences:
    if 'google' in sentence.lower():
        taggedWords = pos_tag(word_tokenize(sentence))
        for word in taggedWords:
            if word[0].lower() == 'google' and word[1] in nonus:
                print(sentence)
