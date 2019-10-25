# # lambda和filter：简单匿名函数
# # lambda使Python创建一个函数并在适当的位置使用它，而不是通过一个名称引用它
# # filter函数接受一个列表基于函数中定义的标准移除元素
# filter_me = [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 14, 15, 19, 22]
# result = filter(lambda x: x % 2 == 0, filter_me)
# print(*result)
# # filter在python2中返回一个列表，在python3中返回一个filter对象
# # 通过*获取filter对象的值
# # 由于缺少名称，lambda创建的函数被称为匿名函数，可以使用lambda语句的结果给函数绑定名称
# func = lambda x: x % 2 == 0
# result2 = filter(func, filter_me)
# print(*result2)
#
# # Map:短路循环
# # map用于需要对列表中的每个元素执行一个指定的操作的情形
# map_me = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# result = map(lambda x: "The letter is %s" % x, map_me)
# print(*result)
# # map可以接受任何类型的序列作为参数
# map_me_again = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result2 = map(lambda list: [list[1], list[0], list[2]], map_me_again)
# print(*result2)

# # 在列表中做出决策——列表解析
# # 可以用来在列表接触引用操作符（方括号）中编写小的循环和判定
# # 以此来定义用以限制被访问元素范围的参数
# everything = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print([x for x in everything if x % 2 == 0])
# # 列表解析将比其他方式运行的更快
#
# # 为循环生成迭代器
# f = range(10, 20)
# print(*f)
# # 在Python3中range不再创建一个列表而是改为一个迭代器xrange
#
# # 使用字典的特殊字符串替换
# person = {'name': 'James', 'camera': 'nikon', 'handedness': 'lefty',
#           'baseball_team': 'angles', 'instrument': 'guitar'}
# print('%(name)s, %(camera)s, %(baseball_team)s' % person)
# person['height'] = 188
# person['weight'] = 75
# print('%(name)s, %(camera)s, %(baseball_team)s, %(height)2.2f, '
#       '%(weight)2.2f' % person)
# # string模块中增加了新的字符串替换的形式
# import string
#
# t = string.Template('$name is $height cm high and $weight kilos')
# print(t.substitute(person))

# # 重要模块
# # getopt——从命令行中得到选项
# import sys, getopt
# # Remember, the first thing in the sys.argv list is the name of the command
# # You don't need that.
# cmdline_params = sys.argv[1:]
#
# opts, args = getopt.getopt(cmdline_params, 'hc:', ['help', 'config='])
#
# for option, parameter in opts:
#     if option == '-h' or option == '--help':
#         print('This program can be run with either -h or --help for this message,')
#         print('or with -c or --config=<file> to specify a different configuration file')
#     if option in ('-c', '--config'):  # this means the same as the above
#         print('Using configuration file %s' % parameter)

# 使用一个以上的进程
import os
pid = os.fork()
if pid == 0:  # This is the child
    print('This is the child')
else:
    print("The child is pid %d" % pid)
