# # 1 使用多个界定符分割字符串
# # 分隔符不固定时使用Re,返回一个列表结构
# line = 'asdf fjdk; afed, fjek,asdf, foo'
# import re
# word_list = re.split(r'[;,\s]\s*', line)
# print(word_list)
# # 通过括号建立捕获分组
# fields = re.split(r'(;|,|\s)\s*', line)
# print(fields)
# value = fields[::2]
# delimiters = fields[1::2]
# print(value)
# print(delimiters)
# print(''.join(v+d for v, d in zip(value, delimiters)))
# # 通过括号建立非捕获分组
# word_list2 = re.split(r'(?:,|;|\s)\s*', line)
# print(word_list2)

# # 2 通过指定的文本模式检查字符串的开头或结尾匹配
# filename = 'spam.txt'
# print(filename.endswith('.txt'))
# print(filename.startswith('file:'))
# url = 'http://www.python.org'
# print(url.startswith('http:'))
# # 将所有的匹配项放入一个元组中检查多种匹配可能
# import os
#
# filenames = os.listdir(".")
# print(filenames)
# py_list = [name for name in filenames if name.endswith('.py')]
# print(py_list)
# print(any(name.endswith('.idea') for name in filenames))
#
# from urllib.request import urlopen
#
# def read_data(name):
#     if name.startswith(('http:', 'https:', 'ftp:')):
#         return urlopen(name).read()
#     else:
#         with open(name) as f:
#             return f.read()
#
# choices = ['http:', 'ftp:']
# print(url.startswith(tuple(choices)))
# # 也可以考虑用切片来对字符串的开头和结尾进行检查，但代码不够优雅
# print(filename[-4:] == '.txt')
# print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')
# # 或者使用正则表达式实现
# import re
#
# print(re.match('http:|https:|ftp:', url))
# # 另外可以检查某个文件夹中是否存在指定的文件类型
# if any(name.endswith(('.jpg', '.png')) for name in os.listdir('.')):
#     print('yes, we have pictrues.')
# else:
#     print(('Oh, we have no pictrues.'))

# # 3 用shell通配符匹配字符串
# from fnmatch import fnmatch, fnmatchcase
#
# print(fnmatch('foo.txt', '*.txt'))
# print(fnmatch('foo.txt', '?oo.txt'))
# print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
# names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
# list_dat = [name for name in names if fnmatch(name, 'Dat*.csv')]
# print(list_dat)
# # 不同的操作系统下fnmatch()对底层操作系统的大小写敏感规则不同，可以使用fnmatchcase()代替
# print(fnmatch('foo.txt', '*.TXT'))
# print(fnmatchcase('foo.txt', '*.TXT'))
# # 同时可以处理非文件名的字符串
# addresses = [
#     '5412 N CLARK ST',
#     '1060 W ADDISON ST',
#     '1039 W GRANVILLE AVE',
#     '2122 N CLARK ST',
#     '4802 N BROADWAY',
# ]
# list_addr = [addr for addr in addresses if fnmatch(addr, '* st')]
# print(list_addr)
# # fnmatch()函数匹配能力介于简单的字符串方法和RE之间。
# # 在数据操作处理中只需要简单的通配符就能完成时，是比较合理的方案
# # 如果代码需要做文件名的匹配，要使用glob模块

# # 4 字符串的匹配和搜索，搜索特定模式的文本
# text = 'yeah, but no, but yeah, but no, but yeah'
# print(text.startswith('yeah'))
# print(text.endswith('no'))
# print(text.find('no'))
#
# import re
#
# text1 = '11/27/2012'
# text2 = 'Nov 27, 2012'
# # match()总是从字符串开始去匹配
# if re.match(r'\d+/\d+/\d+', text1):
#     print('yes')
# else:
#     print('no')
# if re.match(r'\d+/\d+/\d+', text2):
#     print('yes')
# else:
#     print('no')
# # 将正则模式编译为模式对象
# datepat = re.compile(r'\d+/\d+/\d+')
# if datepat.match(text1):
#     print('yes')
# else:
#     print('no')
# if datepat.match(text2):
#     print('yes')
# else:
#     print('no')
# # 想查找字符串任意部分的模式出现的位置，使用findall()方法代替
# text3 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# print(datepat.findall(text3))
# # 在定义正则表达式的时候，通常会利用括号去捕获分组
# datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
# m = datepat2.match('11/27/2012')
# print(m.groups())
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))
# month, day, year = m.groups()
# # findall方法会搜索文本并以列表的形式返回所有的匹配
# for month, day, year in datepat2.findall(text3):
#     print('{}-{}-{}'.format(year, month, day))
# # 通过迭代的方式返回匹配使用finditer方法
# for m in datepat2.finditer(text3):
#     print(m.groups())
# # 仅仅做一次文本匹配好搜索可以略过编译部分，但对于大量的匹配和搜索操作最好先编译re

# # 5 字符串的搜索和替换
# # 对于简单的字面模式
# text = 'yeah, but no, but yeah, but no, but yeah'
# print(text.replace('yeah', 'yep'))
# # 对于复杂的模式使用sub，其中第一个参数是被匹配的模式，第二个参数是替换模式
# # 反斜杠数字\3指向前面模式的捕获组号
# import re
#
# text1 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# string = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text1)
# print(string)
# # 对多次替换考虑先编译提升性能
# datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# print(datepat.sub(r'\3-\1-\2', text1))
# # 对于更加复杂的函可以传递一个替换回调寒素来代替
# from calendar import month_abbr
#
# def change_data(m):
#     mon_name = month_abbr[int(m.group(1))]
#     return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
#
# print(datepat.sub(change_data, text1))
# # 统计替换次数
# newtext, n = datepat.subn(r'\3-\1-\2', text1)
# print(newtext)
# print(n)

# # 6 忽略大小写的方式搜索与替换文本字符串
# # 为了在文本操作时忽略大小写，需要在使用re时提供re.IGNORECASE标志参数
# import re
#
# text = 'UPPER PYTHON, lower python, Mixed Python'
# list_py = re.findall('python', text, flags=re.IGNORECASE)
# print(list_py)
# str_snake = re.sub('python', 'snake', text, flags=re.IGNORECASE)
# print(str_snake)
# # 替换字符串不会自动跟被匹配字符串大小写保存一致
# def matchcase(word):
#     def replace(m):
#         text = m.group()
#         if text.isupper():
#             return word.upper()
#         elif text.islower():
#             return word.lower()
#         elif text[0].isupper():
#             return word.capitalize()
#         else:
#             return word
#     return replace
#
# str_snakes = re.sub('python', matchcase('snake'),text, flags=re.IGNORECASE)
# print(str_snakes)

# # 7 最短匹配模式
# # 问题一般出现在需要匹配一对分隔符之间的文本的时候
# import re
#
# str_pat = re.compile(r'\"(.*)\"')
# text1 = 'Computer says "no."'
# print(str_pat.findall(text1))
# text2 = 'Computer says "no." Phone says "yes."'
# print(str_pat.findall(text2))
# # 匹配的非贪婪模式
# str_pat1 = re.compile(r'\"(.*?)\"')
# print(str_pat1.findall(text2))

# # 8 使用RE匹配一块文本，需要跨越多行匹配
# import re
#
# comment = re.compile(r'/\*(.*?)\*/')
# text1 = '/* this is a comment */'
# print(comment.findall(text1))
# # (.)不能匹配换行符
# comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
# text2 = '''/* this is a
#  multiline comment */
# '''
# print(comment2.findall(text2))
# # 定义自己的正则表达式

# # 9 将Unicode文本标准化，确保所有字符串在底层有相同的表示
# s1 = 'Spicy Jalape\u00f1o'
# s2 = 'Spicy Jalapen\u0303o'
# print(s1, s2)
# # 使用unicodedata将文本标准化
# import unicodedata
#
# t1 = unicodedata.normalize('NFC', s1)
# t2 = unicodedata.normalize('NFC', s2)
# print(t1, t2)
# print(ascii(t1), ascii(t2))
# t3 = unicodedata.normalize('NFD', s1)
# t4 = unicodedata.normalize('NFD', s2)
# print(t3, t4)
# print(ascii(t3), ascii(t4))
# # NFC表示字符应该是整体组成，NFD表示字符应分解为多个组合字符表示
# # Python同样支持扩展的标准化形式NFKC和NFKD，它们在处理某些字符的时候增加了额外的兼容属性
# s = '\ufb01'
# print(s)
# print(unicodedata.normalize('NFC', s))
# print(unicodedata.normalize('NFD', s))
# print(unicodedata.normalize('NFKC', s))
# print(unicodedata.normalize('NFKD', s))
# # 标准化对于任何需要一致的方式去处理UNICODE文本的程序都是非常重要的
# # 在清理和过滤文本的时候字符的标准化也是很重要的

# 10 在正则表达式中使用Unicode
import re

num = re.compile('\d+')
print(num.match('123'))
print(num.match('\u0661\u0662\u0663'))

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))
print(s.upper())
