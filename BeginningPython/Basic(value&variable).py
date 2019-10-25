# # 关于三引号模式
# print('hello, world')
# print("he said, \"Don't do it\"")
# # 加号串联字符串
# print('John' + 'Everyman')
# print('John' + ' ' + 'Everyman')
# print('John', 'Everyman')
# # 使用格式说明符
# print('John Q. %s' % 'Public')
# print('John %s%s' % ('Every','man'))
# # 在字符串中将%符号转义
# print('The %% behaves differently when combined with other letters, like this: \
# %%d %%s %%f %d' % 10)
# # 将数字格式化为八进制和十六进制
# print('Octal uses the letter "o" lowercase. %d %o' % (10, 10))
# # 打印6-14的八进制形式
# for i in range(6, 15):
#     print('%o' % i, end=' ')
# print()
# # 打印9-19的十六进制形式
# for i in range(9, 20):
#     print('%x' %i, end=' ')
# print()
# # 给名称赋值
# first_string = 'This is a string'
# second_string = 'This is another string'
# first_number = 4
# second_number = 5
# print('The first variables are %s, %s, %d, %d' % (first_string, second_string, first_number, second_number))
# # 更名已命名的值
# proverb = 'A penny saved'
# proverb = proverb + ' is a penny earned'
# print(proverb)
# # 元组
# filler = ('string', 'filled', 'by a', 'tuple')
# print('A %s %s %s %s' % ('string', 'filled', 'by a', 'tuple'))
# print(filler)
# # 使用下标访问元组中的单个值(str类型)
# print(filler[2])
# # 通过一个元组访问另一个元组
# a = ('first', 'second', 'third')
# b = (a, 'b is second element')
# print(b[1])
# print(b[0][0])
# layer2 = b[0]
# print(layer2[1])
# # 元组的创建
# single_element_tuple = ('the sole element',)  # 如果不加，则生成一个str
# print(single_element_tuple)
# # 列表的使用
# breakfast = ['coffee', 'tea', 'toast', 'egg']
# count = 4
# for i in range(count):
#     print("Today's breakfast is %s" % breakfast[i])
# print()
# breakfast.append('waffles')  # 一次增加一个元素
# print(breakfast)
# breakfast.extend(['juice', 'decaf', 'oatmeal'])  # 一次增加多个元素
# print(breakfast)
# # 字典的创建与实例化
# menus_specials = {}  # 初始化后使用赋值方法定义
# menus_specials['breakfast']  = 'Canadian ham'
# menus_specials['lunch']  = 'tuna surprise'
# menus_specials['dinner']  = 'Cheeseburger Deluxe'
# print(menus_specials)
# menus_specials2 = {'breakfast': 'Canadian ham', 'lunch': 'tuna surprise', 'dinner': 'Cheeseburger Deluxe'}  # 一次性定义
# hungry = menus_specials2.keys()
# print(list(hungry))  # 从字典中获取键
# starving = menus_specials2.values()
# print(list(starving))
# # 像列表一样处理字符串
# last_names = ['Douglass', 'Jefferson', 'Williams', 'Frank', 'Thomas']
# print('%s' % last_names[0])
# print('%s' % last_names[0][0])
# len(last_names)
# last_element = len(last_names) - 1  # 引用最后一个元素
# print('%s' %last_names[last_element])
# print('%s' %last_names[-1])  # 快捷引用最后一个元素
# # 对序列分片
# slice_me = ('The', 'next', 'time', 'we', 'meet', 'drinks', 'are', 'on', 'me')
# sliced_tuple = slice_me[5:9]
# print(sliced_tuple)
# slice_this_list = ['The', 'next', 'time', 'we', 'meet', 'drinks', 'are', 'on', 'me']
# sliced_list = slice_this_list[5:9]
# print(sliced_list)
# slice_this_string = 'The next time we meet, drinks are on me'
# sliced_string = slice_this_string[5:9]
# print(sliced_string)
# # 通过附加序列增长列表
# living_room = ('rug', 'table', 'chair', 'TV', 'dustbin', 'shelf')
# apartment = []
# apartment.append(living_room)
# print(apartment)
# apartment.extend(living_room)
# print(apartment)
# # 从列表中弹出元素
# todays_temperatures = [23, 32, 33, 31]
# todays_temperatures.append(29)
# print(todays_temperatures)
# morning = todays_temperatures.pop(0)
# print("This morning's temperature was %.2f" % morning)
# late_morning = todays_temperatures.pop(0)
# print("Today's late morning temperature was %.2f" % late_morning)
# todays_temperatures.pop(0)  # 直接丢弃
# print(todays_temperatures)  # 若是pop()则删除列表中的最后一个元素
# # 处理集合（集合分为可变集合和不可变集合）
# alphabet = ['a', 'b', 'b', 'c', 'a', 'd', 'e']
# print(alphabet)
# alphabet2 = set(alphabet)
# print(alphabet2)  # 通过集合删除重复的元素









