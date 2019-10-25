# # 11 命名切片
# record = '864513654132654136161326165165498645684516543166514564'
# SHARES = slice(20, 23)
# PRICE = slice(31, 37)
# cost = int(record[SHARES]) * int(record[PRICE])
# print(cost)
# # slice()函数的操作与运用
# items = [0, 1, 2, 3, 4, 5, 6]
# a = slice(2, 4)
# print(items[a])
# items[a] = [10, 11]
# print(items)
# del items[a]
# print(items)
# # 对切片对象调用start, stop, step方法
# b = slice(5, 50, 2)
# print(b.start, b.stop, b.step)
# # 调用切片的indices(size)方法返回三元组，并映射到一个确定大小的序列
# s = 'helloworld'
# print(b.indices(len(s)))
# for i in range(*b.indices(len(s))):  # 调用元组信息
#     print(s[i])

# # 12 找出一个序列中出现次数最多的元素
# # 应用collections.Counter类中的most_common()方法
# words = [
# 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
# 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
# 'my', 'eyes', "you're", 'under'
# ]
# from collections import Counter
# word_counts = Counter(words)
# top_three = word_counts.most_common(3)
# print(top_three)
# # Counter对象形成一个字典，将元素映射到它出现的次数上
# print(word_counts['not'])
# print(word_counts['eyes'])
# # 更新单词列表时增加次数的方法,包括使用手动计数或update方法
# morewords = ['why','are','you','not','looking','in','my','eyes']
# for word in morewords:
#     word_counts[word] += 1
# print(word_counts['eyes'])
# word_counts.update(morewords)
# print(word_counts['eyes'])
# # Counter实例与数学运算操作
# a = Counter(words)
# b = Counter(morewords)
# print(a)
# print(b)
# c = a + b
# print(c)
# d = a - b
# print(d)

# # 13 通过某个关键字排序一个字典列表
# #　通过operator模块的itemgetter函数，对数据结构进行排序
# rows = [
# {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
# {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
# ]
# # 根据任意字典字段来排序
# from operator import itemgetter
# rows_by_fname = sorted(rows, key=itemgetter('fname'))
# rows_by_uid = sorted(rows, key=itemgetter('uid'))
# print(rows_by_fname)
# print(rows_by_uid)
# # itemgetter函数支持多个key值，代表关键字排序顺序
# rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
# print(rows_by_lfname)
# # itemgetter()有时可以用lambda表达式代替
# rows_by_fname1 = sorted(rows, key=lambda r: r['fname'])
# rows_by_lfname1 = sorted(rows, key=lambda r: (r['lname'], r['fname']))
# print(rows_by_fname1)
# print(rows_by_lfname1)
# # 这种sorted接受的关键字参数也适用于min和max函数
# print(min(rows, key=itemgetter('uid')))
# print(max(rows, key=itemgetter('uid')))

# # 14 排序不支持原生比较的对象
# # 对关键字参数key可以传入一个callable对象，对每个传入的对象返回一个值，用来进行排序等操作
# class User:
#     def __init__(self, user_id):
#         self.user_id = user_id
#
#     def __repr__(self):
#         return 'User({})'.format(self.user_id)
#
# def sort_compare():
#     users = [User(23), User(3), User(99)]
#     print(users)
#     print(sorted(users, key=lambda u: u.user_id))
#
# sort_compare()
# # 或使用operator.attrgetter()来代替lamdba函数
# from operator import attrgetter
# users = [User(23), User(3), User(99)]
# print(sorted(users, key=attrgetter('user_id')))
# # 同样可以应用于min, max函数
# print(min(users, key=attrgetter('user_id')))
# print(max(users, key=attrgetter('user_id')))

# # 15 通过某个字段将记录分组
# # 使用itertools.groupby()函数对分组操作十分使用
# rows = [
# {'address': '5412 N CLARK', 'date': '07/01/2012'},
# {'address': '5148 N CLARK', 'date': '07/04/2012'},
# {'address': '5800 E 58TH', 'date': '07/02/2012'},
# {'address': '2122 N CLARK', 'date': '07/03/2012'},
# {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
# {'address': '1060 W ADDISON', 'date': '07/02/2012'},
# {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
# {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
# ]
# from operator import itemgetter
# from itertools import groupby
# # groupby()函数扫描整个序列并查找连续相同值（或根据key函数返回值相同）的元素序列
# # 先对列表中的date字段进行排序
# rows.sort(key=itemgetter('date'))
# # 使用itertools进行分组
# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items:
#         print(i)
# print()
# # 多值字典的构建
# from collections import defaultdict
# rows_by_date = defaultdict(list)
# for row in rows:
#     rows_by_date[row['date']].append(row)
# for r in rows_by_date['07/01/2012']:
#     print(r)

# # 16 过滤序列元素提取所需要的值或缩短序列
# # 使用列表推导较为简单，但是占用大量内存
# mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# print([n for n in mylist if n > 0])
# print([n for n in mylist if n < 0])
# # 如果对内存敏感可以使用生成器表达式迭代产生过滤的元素
# pos = (n for n in mylist if n > 0)
# print(pos)
# for x in pos:
#     print(x, end=' ')
# print()
# # 当过滤规则复杂时，可以将过滤代码放入函数中，使用内建的filter函数
# values = ['1', '2', '-3', '-', '4', 'N/A', '5']
# def is_int(val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False
# ivals = list(filter(is_int, values))
# print(ivals)
# # 列表推导和生成器在过滤时可以进行数据的转换
# import math
# print([math.sqrt(n) for n in mylist if n > 0])
# # 过滤操作的变种即将过滤掉的值用新值代替
# clip_neg = [n if n > 0 else 0 for n in mylist]
# print(clip_neg)
# clip_pos = [n if n < 0 else 0 for n in mylist]
# print(clip_pos)
# # 过滤工具itertools.compress()
# # 以一个iterable对象和一个相对应的Boolean选择器序列作为参数，输出iterable对象中对应选择器为True的元素
# # filter和compress都返回一个迭代器
# addresses = [
#     '5412 N CLARK',
#     '5148 N CLARK',
#     '5800 E 58TH',
#     '2122 N CLARK'
#     '5645 N RAVENSWOOD',
#     '1060 W ADDISON',
#     '4801 N BROADWAY',
#     '1039 W GRANVILLE'
# ]
# counts = [0, 3, 10, 4, 1, 7, 6, 1]
# from itertools import compress
# more5 = [n > 5 for n in counts]
# print(more5)
# print(list(compress(addresses, more5)))

# # 17 从字典中提取子集
# # 使用字典推导较为简单
# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
# # 构建价格超过200的子字典
# p1 = {key: value for key, value in prices.items() if value > 200}
# # 构建包含元素名称的子集
# tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# p2 = {key: value for key, value in prices.items() if key in tech_names}
# print(p1)
# print(p2)
# # 通过构建元组序列然后传递给dict()函数
# p3 = dict((key, value) for key, value in prices.items() if value > 200)
# print(p3)
# p4 = {key: prices[key] for key in prices.keys() if key in tech_names}
# print(p4)
# p5 = {key: prices[key] for key in prices.keys() & tech_names}  # 此处的&不知何意
# print(p5)

# # 18 映射名称到序列元素
# # 通过下标访问列表或元组中元素可能难以阅读，想通过名称来访问元素
# # 使用collections.namedtuple()以返回标准元组类型子类
# from collections import namedtuple
# Subscriber = namedtuple('Subscriber', ['addr', 'joined'])  # 初始化类，为字段传递值
# sub = Subscriber('jonesy@example.com', '2018-5-29')
# print(sub)
# print(sub.addr)
# print(sub.joined)
# # namedtuple实例和元组类型是可交换的，支持所有普通元组的操作
# print(len(sub))
# addr, joined = sub
# print(addr, joined)
# # 使用命名元组使得数据不必依赖记录的结构
# Stock = namedtuple('Stock', ['name', 'shares', 'price'])
# def compute_cost(records):
#     total = 0.0
#     for rec in records:
#         s = Stock(*rec)  # 调用列表信息生成命名元组结构
#         total += s.shares * s.price
#     return total
# # 命名元组的另一个用途是作为字典的代替，因为字典存储需要更大的内存空间
# # 但是一般情况下命名元组是不可更改的
# s = Stock('ACME', 100, 123.45)
# print(s)
# # 可以使用元组实例的_replace()方法，创建全新的命名元组并将对应的字段用新的值代替
# s = s._replace(shares = 75)
# print(s)
# # _replace()方法另一个特性是当命名元组拥有可选或缺失字段的时候，可以快捷地填充数据
# Stock2 = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# # 创建缺省原型元组
# stock_prototype = Stock2('', 0, 0.0, None, None)
# # 通过调用元组信息建立快速填充函数
# def dict_to_stock(s):
#     return stock_prototype._replace(**s)  # 调用元组內的信息
# a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
# print(dict_to_stock(a))
# b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
# print(dict_to_stock(b))

# # 19 在过滤或转换数据的同时对数据进行计算
# # 使用一个生成器表达式参数来结合数据计算与转换
# nums = [1, 2, 3, 4, 5]
# s = sum(x * x for x in nums)
# print(s)
# # 根据key值查找字典中的最值
# portfolio = [
# {'name':'GOOG', 'shares': 50},
# {'name':'YHOO', 'shares': 75},
# {'name':'AOL', 'shares': 20},
# {'name':'SCOX', 'shares': 65}
# ]
# min_shares = min(s['shares'] for s in portfolio)
# print(min_shares)
# min_shares2 = min(portfolio, key=lambda s: s['shares'])
# print(min_shares2)

# 20 合并多个字典或映射
# 使用collections模块中的ChainMap类将多个字典或映射在逻辑上合并为单一的映射
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
from collections import ChainMap
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])  # 对于重复键会返回第一次出现的映射值
# ChainMap类创建了一个容纳这些字典的列表并重新定义了一些常见的字典操作对字典进行遍历
print(len(c))
print(list(c.keys()))
print(list(c.values()))
# 对于字典的更新或删除操作影响的是列表中的第一个字典
c['z'] = 10
c['w'] = 40
print(a)
print(b)
# 可以使用update()方法替代ChainMap()对字典进行合并
d = {'x': 1, 'z': 3 }
e = {'y': 2, 'z': 4 }
merged = dict(e)
merged.update(d)
print(merged['x'])
print(merged['y'])
print(merged['z'])
# 这种方法创建了一个完全不同的字典对象（或是破坏了现有的字典结构）
# 原字典进行更新不会反映到新字典中去
merged2 = ChainMap(d, e)
print(merged2['x'])
d['x'] = 42
print(merged2['x'])