# # 字典的比较
# tuesday_breakfast_sold = {'pancakes':10, 'french toast':4, 'bagels':32}
# wednesday_breakfast_sold = {'pancakes':10, 'bagels':32, 'french toast':4}
# print(tuesday_breakfast_sold == wednesday_breakfast_sold)
# # 字符串的lower()和upper()方法更改字符串中字母的大小写
# word = 'PUMPKIN'.lower()
# print(word)
# word2 = word.upper()
# print(word2)

# # 创建异常以及对异常的说明
# fridge_contents = {'egg':8, 'mushroom':20, 'pepper':3, 'cheese':2, 'tomato':4, 'milk':13}
# try:
#     if fridge_contents['orange juice'] > 3:
#         print('Sure, we have some orange juice.')
# except (KeyError) as error:
#     print('Woah! There is no %s' % error)
# # 通过pass忽略不严重的故障,同时可以添加else以便灵活处理各种情况
# try:
#     if fridge_contents['orange juice'] > 3:
#         print('Sure, we have some orange juice.')
# except (KeyError) as error:
#     print('Woah! There is no %s' % error)
# except (TypeError):
#     pass

# 在函数中描述函数
# def in_fridge():
#     """This is a function to see if the fridge has a food.  # 需要缩进？
# Fridge has to be a dictionary defined outside of the function.
# The food to be searched for is in the string wanted_food."""
#     try:
#         count = 1
#     except KeyError:
#         count = 0
#     return count
# print('%s' % in_fridge.__doc__)

# 函数练习
# def do_plus(a, b):
#     if type(a) == type(b):
#         for param in (a, b):
#             if (type(param) != type("")) and (type(param) != type(1)):
#                 raise TypeError('This function needs a string or an integer')
#         return a + b
#     else:
#         raise TypeError('The type of two params is different')

# def do_plus(a, b):
#     try:
#         for param in (a, b):
#             if (type(param) != type("")) and (type(param) != type(1)):
#                 return 'This function needs a string or an integer'
#         return a + b
#     except TypeError:
#         return 'The type of two params is different'
# print(do_plus(1, 3))
# print(do_plus("a", "c"))
# print(do_plus(1, "c"))
# print(do_plus([1], [2]))

# # python中的任何一条数据都是对象，每个对象由3部分组成，标识、类型和值
# # 将关系紧密的对象整合在一起通过类进行封装
# # 通过dir函数列举一个对象的所有属性和方法
# a = 'abcdefg'
# print(dir(a))  # 以下划线开头的名称是对象的私有属性，它们是不可见的，即不能直接使用它们

# # 定义类并创建对象
# class Fridge:
#     """
#     This class implements a fridge where ingredients can be
#     added and removed individually, or in groups.
#     The fridge will retain a count of every ingredient added or removed,
#     and will raise an error if a sufficient quantity of an ingredient
#     is not present.
#     Methods:
#     has(food_name [, quantity]) - checks if the string food_name is in the
# fridge. Quantity will be set to 1 if you don't specify a number.
#     has_various(foods) - checks if enough of every food in the dictionary is
# in the fridge.
#     add_one(food_name) - adds a single food_name to the fridge.
#     add_many(food_dict) - adds a whole dictionary filled with foods.
#     get_one(food_name) - takes out a single food_name from the fridge.
#     get_many(food_dict) - takes out a whole dictionary worth of food.
#     get_ingredients(food) - if passed an object that has the __ingredients__
# method, get_many will invoke this to get the list of ingredients.
#     """
#     def __init__(self, items = {}):
#         """Optionally pass in an initial dictionary of items"""
#         if type(items) != type({}):
#             raise TypeError('Fridge requires a dictionary but was given %s'
#                             % type(items))
#         self.items = items
#         return
#
#     # 置入的内部方法
#     def __add_multi(self, food_name, quantity):
#         """
#         __add_multi(food_name, quantity) - adds more than one fo a food
#         item. Returns the number of items added.
#         This should only be used internally, after the type checking has
#         been done.
#         """
#         if (not food_name in self.items):
#             self.items[food_name] = 0
#         self.items[food_name] = self.items[food_name] + quantity
#
#     # 取出的内部方法
#     def __get_multi(self, food_name, quantity):
#         """
#         __get_multi(food_name, quantity) - removes more than one of a food item.
#         :param food_name:
#         :param quantity:
#         :return: The number of items removed, False if there is not enough
#     food_name in the fridge.
#         This should only be used internally, after the type checking has
#         been done.
#         """
#         try:
#             if (self.items[food_name] is None):
#                 return False
#             if (quantity > self.items[food_name]):
#                 return False
#             self.items[food_name] = self.items[food_name] - quantity
#         except KeyError:
#             return False
#         return quantity
#
#     def add_one(self, food_name):
#         """
#         add_one(food_name) - adds a single food_name to the fridge
#         :param food_name:
#         :return: True
#         :raise: a TypeError if food_name is not a string
#         """
#         if type(food_name) != type(""):
#             raise TypeError('add_one requires a string, but given a %s'
#                             % type(food_name))
#         else:
#             self.__add_multi(food_name, 1)
#         return True
#
#     def add_many(self, food_dict):
#         """
#         add_many(food_dict) - adds a whole dictionary filled with food as
#         keys and quantities as values.
#         :param food_dict:
#         :return: a dictionary with the removed food,
#     False if there is not enough food in fridge
#         :raise: a TypeError if food_dict is not a dictionary
#         """
#         if type(food_dict) != type({}):
#             raise TypeError('add_many requires a dictionaty, but give a %s'
#                             % food_dict)
#         for item in food_dict.keys():
#             self.__add_multi(item, food_dict[item])
#         return
#
#     def has(self, food_name, quantity = 1):
#         """
#         has(food_name, [quantity]) - checks if the string food_name is in the
#     fridge. Quantity defaults to 1.
#         :param food_name:
#         :param quantity:
#         :return: True if there is enough, False otherwise.
#         """
#         return self.has_various({food_name: quantity})
#
#     def has_various(self, foods):
#         """
#         has_various(foods) - determines if the dictionary food_name
#     has enough of every element to stisfy a request.
#         :param foods:
#         :return: True if there is enough, False if there is not or if an
#     element does not exist.
#         """
#         try:
#             for food in foods.keys():
#                 if self.items[food] < foods[food]:
#                     return False
#             return True
#         except KeyError:  # if an element does not exist
#             return False
#
#     def get_one(self, food_name):
#         """
#         get_one(food_name) - takes out a single food_name from the fridge
#         :param food_name:
#         :return: a dictionary with the food: 1 as a result, or False if there
#     wasn't enough in the fridge.
#         """
#         # 在__get_multi()的内置方法中定义了异常抛出
#         if type(food_name) != type(""):
#             raise TypeError('get_one requires a string, given a %s'
#                             % type(food_name))
#         else:
#             result = self.__get_multi(food_name, 1)
#         return result
#
#     def get_many(self, food_dict):
#         """
#         get_many(food_dict) - takes out a whole dictionary worth of food.
#         :param food_dict:
#         :return: a dictionary with all of the ingredients, False if there are
#     not enough ingredients or if a dictionary is not provided.
#         """
#         if self.has_various(food_dict):
#             foods_removed = {}
#             for item in food_dict.keys():
#                 foods_removed[item] = self.__get_multi(item, food_dict[item])
#             return foods_removed
#
#     # ??????????????????????????????????
#     def get_ingredients(self, food):
#         """
#         get_ingredients(food) - if passed an object that has the __ingredients__
#     method, get_many will invoke this to get the list of ingredients.
#         :param food:
#         :return:
#         """
#         try:
#             ingredients = self.get_many(food.__ingredients__())
#         except AttributeError:
#             return False
#         if ingredients != False:
#             return ingredients
#
# f = Fridge({'eggs': 6, 'milk': 4, 'cheese': 3})
# print(f.__doc__)
# print(f.items)
# print(f.add_one('grape'))
# f.add_many({'mushroom': 5, 'tomato': 3})
# print(f.items)
# if f.has('cheese', 2):
#     print('it is time to make an omelet!')
# print(f.get_one('eggs'))
# f.get_many({'milk': 3, 'tomato': 2})
# print(f.items)
# f.get_many({'mushroom': 5})  # 当全部取出某一物品时，并未将其删除
# print(f.items)

import sys
print(sys.path)
# 在Run->Edit Configurations->Parameters中设置命令行参数
print('This was given the command line parameters: %s' % sys.argv)



