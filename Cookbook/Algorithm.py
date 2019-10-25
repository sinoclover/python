# # 1 将序列分解为单独的变量
# # 元组
# p = (4, 5)
# x, y = p
# print('{0}, {1}'.format(x, y))
# print('%d' %x, ' %d' %y)
# # 列表
# data = ['ACME', 50, 91.1, (2012, 12, 21)]
# name, shares, price, date = data
# print('{0}, {1}'.format(name, date))
# name2, shares2, price2, (year, month, day) = data
# print('{0} {1}/{2}/{3}'.format(name, year, month, day))
# # 字符串、文件、迭代器、生成器等，只要对象可以迭代就可以执行分解操作
# s = 'hello'
# a, b, c, d, e = s
# print('{0},{1},{2},{3},{4}'.format(a,b,c,d,e))
# # 可以通过使用用不到的变量名来丢弃值

# # 2 从任意长度的可迭代对象中分解元素（使用*表达式分解）
# record = ('Dave', 'dave@example.com', '779-555-1212', '847-555-1212')
# name, email, *phone_numbers = record
# print('{0}, {1}'.format(name, email))
# print('{0}'.format(phone_numbers))
# # 迭代一个变长的元组序列
# records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4)]
# def do_foo(x, y):
#     print('foo', x, y)
# def do_bar(s):
#     print('bar', s)
# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     else:
#         do_bar(*args)
# # 和某些特定的字符串处理操作相结合，做拆分操作
# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(uname, homedir, sh)
# print(fields)
# # *表达式分解操作和各种函数式语言中的列表处理功能有着一定的相似性
# items = [1, 10, 7, 4, 5, 9]
# head, *tail = items
# print(head)
# print(tail)

# # 3 保存最后N个元素(保存有限的历史记录collections.deque)
# # deque的特性
# from collections import deque
# q = deque(maxlen = 3)
# q.append(1)
# q.append(2)
# q.append(3)
# print(q)
# q.append(4)
# print(q)
# q.append(5)
# print(q)
# # 无界限队列
# q2 = deque()
# q2.append(1)
# q2.append(2)
# q2.append(3)
# print(q2)
# q2.appendleft(4)
# print(q2)
# print(q2.pop())
# print(q2)
# print(q2.popleft())
# print(q2)

# # 4 查找最大或最小的N个元素
# # 使用heapq模块中的nlargest()和nsmallest()函数
# import heapq
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(nums)
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))
# # lambda
# portfolio = [
# {'name': 'IBM', 'shares': 100, 'price': 91.1},
# {'name': 'APL', 'shares': 50, 'price': 543.22},
# {'name': 'FB', 'shares': 200, 'price': 21.09},
# {'name': 'HPQ', 'shares': 35, 'price': 31.75},
# {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# print(cheap)
# print(expensive)
# # 堆数据结构（最上方永远是最小的元素）
# # 将集合数据进行堆排序后放入一个列表
# heapq.heapify(nums)
# print(nums)
# print(heapq.heappop(nums))
# print(nums)

# # 5 实现一个优先级队列
# import heapq
# class PriorityQueue:
#     def __init__(self):
#         self._queue = []
#         self._index = 0
#     def push(self, item, priority):
#         heapq.heappush(self._queue, (-priority, self._index, item))
#         # -priority使优先级从高到低， index保证同等优先级元素的正确排列，保证元素的插入顺序排序
#         # 即Item实例不支持排序，priority实现不同优先级的排序，Index实现相同优先级的排序，即使用三元组结构
#         self._index += 1
#     def pop(self):
#         return heapq.heappop(self._queue)[-1]
# class Item:
#     def __init__(self, name):
#         self.name = name
#     def __repr__(self):
#         return 'Item({!r})'.format(self.name)
#
# q = PriorityQueue()
# q.push(Item('foo'), 1)
# q.push(Item('bar'), 5)
# q.push(Item('spam'), 4)
# q.push(Item('grok'), 1)
# print(q.pop())
# print(q.pop())
# print(q.pop())  # 若优先级相同则按照插入队列的顺序返回

# # 6 字典中的键映射多个值(multidict)
# a = {'a':[1, 2, 3], 'b':[4, 5]}  # 使用列表作为多个值的容器，保持元素的插入顺序
# b = {'a':{1, 2, 3}, 'b':{4, 5}}  # 使用集合作为多个值的容器，去掉重复的元素
# # 通过collections模块中的defaultdict构造这样的字典,自动创建实体
# from collections import defaultdict
# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)
# print(d)
# print(d['a'], d['b'])
# e = defaultdict(set)
# e['a'].add(1)
# e['a'].add(2)
# e['b'].add(4)
# print(e)
# print(e['a'], e['b'])
# # 使用setdefault不自动创建映射实体
# c = {}
# c.setdefault('a', []).append(1)
# c.setdefault('a', []).append(2)
# c.setdefault('b', []).append(4)
# print(c)
# print(c['a'], c['b'])
# # 常规方法
# pairs = []
# f = {}
# for key, value in pairs:
#     if key not in f:
#         f[key] = []
#     f[key].append(value)

# # 7 字典排序问题
# # 使用collections模块中的OrderedDict类在迭代或序列化字典时能够控制元素的顺序
# from collections import OrderedDict
# d = OrderedDict()
# d['foo'] = 1
# d['bar'] = 2
# d['spam'] = 3
# d['grok'] = 4
# for key in d:
#     print(key, d[key])
# print(d)
# # 希望构建需要序列化或编码成其他格式的映射时使用OrderedDict,但要注意其内部维护了根据键插入顺序排序的双向链表(消耗内存)
# import json
# print(json.dumps(d))

# # 8 字典的运算
# # 在数据字典中执行如求最值、排序等计算操作
# prices = {'ACME': 45.23, 'APL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
# # 使用zip函数将键值对翻转
# min_price = min(zip(prices.values(), prices.keys()))
# max_price = max(zip(prices.values(), prices.keys()))
# print(min_price, max_price)
# # 使用sorted函数来排列字典数据
# price_sorted = sorted(zip(prices.values(), prices.keys()))
# print(price_sorted)
# # zip函数是一个只能访问一次的迭代器, 同时若value值相同则会参考key值比较大小或排序
# # 常规方式先获取最值的key，再获取其value
# min_key = min(prices, key=lambda k: prices[k])
# min_value = prices[min_key]
# print(min_key, min_value)

# # 9 查找两个字典中的相同点
# a = {'x': 1, 'y': 2, 'z': 3}
# b = {'w': 10, 'x': 11, 'y': 2}
# # 可以在两字典的keys()或者items()方法返回结果上执行集合操作
# # 字典的keys()方法返回一个展现键集合的键视图对象，item()方法返回一个包含键值对的元素视图对象
# # 也可以将字典转换为set后进行操作
# print(a.keys() & b.keys())  # 查找keys中的共同点
# print(a.keys() - b.keys())  # 查找a中的特有keys
# print(a.items() & b.items())  # 查找键值对中的共同点
# # 也可以进行对字典的修改或过滤字典元素
# c = {key: a[key] for key in a.keys() - {'z', 'w'}}
# print(c)

# 10 删除序列相同元素的同时保持元素顺序
# 序列上的值若都是hashable则可以利用集合或生成器解决
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
# 不可哈希的如dict类型
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)  # key参数指定了一个函数，将序列元素转换成hashable类型
        if val not in seen:
            yield item
            seen.add(val)
b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe2(b, key=lambda d: (d['x'], d['y']))))
# set函数只能消除重复元素，但不能维护顺序
print(set(a))




