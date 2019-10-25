# # 打印字符
# print('hi', end=' ')
# print('there')
#
# print('hi there')
#
# print('hi' + 'there')
#
# # 打印换行符
# print('hello')
# print()
# print('world')
#
# print('hello \nworld')
# # 水平制表符
# print('abc\txyz')  # IDE里与实际不符，实际8个字符之后有一个制表点
# # 打印反斜线
# print('hi\\there')

# # 打印正方体
# print('Number \tSquare \tCube')
# for i in range(1, 11):
#     print(i, '\t', i**2, '\t', i**3)  # ???

# # 在字符串中插入变量
# name = 'Warren Sande'
# print('My name is', name, 'and i wrote this book')
# print('My name is %s and i wrote this book' % name)
# print('My name is {} and i wrote this book'.format(name))
# age = 13
# print('i am %i years old' % age)
# average = 75.6
# print('The average on our math test was %f percent' % average)
# dec = 12.3456
# print('it is %.2f degrees today.' % dec)  # 浮点数格式化时数字自动四舍五入
# number = 12.67
# print('%i' % number)  # 整数格式化时数字被截断
# print('%f' % dec)
# print('%.2f' % dec)
# print('%.8f' % dec)
# number2 = -98.76
# # 正负号的使用
# print('%+f' % number)
# print('% f' % number)
# print('%f' % number2)
# # E记法
# print('%e' % dec)
# print('%.3e' % dec)
# print('%.8e' % dec)
# # 自动选择E记法或浮点数
# number3 = 12.3
# number4 = 456712345.6
# print('%g' % number3)
# print('%g' % number4)
# # 打印%号
# print('i got 90% on my math test!')

# # 存储格式化数字
# my_string = '%.2f' % 12.3456
# print(my_string)
# print('The answer is', my_string)
# # 分解字符串
# name_string = 'Sam,Brad,Alex,Cameron,Toby,Gwen,Connor'
# names = name_string.split(',')
# print(names)
# for name in names:
#     print(name, end = ' ')
# print()
# names2 = name_string.split('Toby,')  # 分解记号会消失
# print(names2)
# for name2 in names2:
#     print(name2, end = ' ')
# print()
# names3 = name_string.split()  # 按空白符分解
# print(names3)
# # 联结字符串
# print('cat' + 'dog') # 称为拼接
# word_list = ['My', 'name', 'is', 'Warren']
# long_string = '*'.join(word_list)  # 引号内表示联结时的间隔，或者说是粘合剂
# print(long_string)

# # 搜索字符串
# name = 'Frankenstein'
# print(name.startswith('F'))
# print(name.startswith('Frank'))
# print(name.startswith('Flop'))
# print(name.endswith('n'))
# print(name.endswith('stein'))
# print(name.endswith('stone'))
# # in 与 index
# addr1 = '657 Maple Lane'
# if 'Maple' in addr1:
#     print("That address has 'Maple' in it.")
#     position = addr1.index('Maple')
#     print("found 'Maple' at index", position)

# # 删除字符串的一部分strip()
# name = 'Warren Sande'
# short_name = name.strip('de')
# print(short_name)
# name2 = 'Warren Sande   '
# short_name2 = name.strip()
# print(short_name2)
#
# # 改变大小写
# string1 = 'Hello'
# string2 = string1.lower()
# string3 = string1.upper()
# print(string2)
# print(string3)

# # 打印一句话
# name = input('What is your name?')
# age = input('How old are you?')
# color = input('What is your favorite color?')
# print('Your name is {0} you are {1} years old and you like {2}'.format(name, age, color))

# # 使用制表符打印乘法表
# for looper in range(1, 11):
#     print(looper, '\ttimes 8 =\t', looper * 8)

# # 计算8的所有分数
# for i in range(1, 9):
#     print(i,'/ 8 = %.3f' % (i / 8.0))
