# # 使用dir有助于研究模块，包括自己创建的模块
# print(dir(__builtins__))
# import sys
# print(dir(sys))
#
# # 对于导入的模块，python解释器搜索路径中的目录
# print(sys.path)
#
# # 创建一个模块并导入
# import food
# print(dir(food))
# food.favoriteFood()
#
# from food import favoriteFood
# favoriteFood()

# # 面向对象编程的封装、继承和多态
# # 建立meal模块
# """
# Module for making meals in Python.
#
# Import this moudle and then call
# makeBreakfast(), makeDinner() or makeLunch().
# """
# __all__ = ['Meal', 'AngryChefException', 'makeBreakfast', 'makeLunch',
#            'makeDinner', 'Breakfast', 'Lunch', 'Dinner']
#
# # Helper functions.
# def makeBreakfast():
#     """Creates a Breakfast object."""
#     return Breakfast()
# def makeLunch():
#     """Creates a Lunch object."""
#     return Lunch()
# def makeDinner():
#     """Creates a Dinner object."""
#     return Dinner()
#
# # Exception classess.
# class SensitiveArtistException(Exception):
#     """
#     Exception raised by an overly-sensitive artist.
#     Base class for artistic types.
#     """
#     pass
#
# class AngryChefException(SensitiveArtistException):
#     """Exception that indicates the chef is unhappy."""
#     pass
#
# class Meal:
#     """
#     Holds the food and drink used in a meal.
#     In true object-oriented tradition, this class
#     includes setter methods for the food and drink.
#
#     Call printIt to pretty-print the values.
#     """
#     def __init__(self, food='omelet', drink='coffee'):
#         """Initialize to default values."""
#         self.name = 'generic meal'
#         self.food = food
#         self.drink = drink
#
#     def printIt(self, prefix=''):
#         """Print the data nicely."""
#         print(prefix, 'A fine', self.name, 'with', self.food, 'and', self.drink)
#
#
#     def setFood(self, food='omelet'):
#         """Setter for the food."""
#         self.food = food
#     def setDrink(self, drink='coffee'):
#         """Setter for the drink."""
#         self.drink = drink
#     def setName(self, name=''):
#         """Setter for the name."""
#         self.name = name
#
# class Breakfast(Meal):
#     """Holds the food and drink for breakfast."""
#     def __init__(self):
#         """Initialize with an omelet and coffee."""
#         Meal.__init__(self, 'omelet', 'coffee')
#         self.setName('breakfast')
#
# class Lunch(Meal):
#     """Holds the food and drinks for lunch."""
#     def __init__(self):
#         """Initialize with a sandwich and a gin and tonic."""
#         Meal.__init__(self, 'sandwich', 'gin and tonic')
#         self.setName('midday meal')
#
#     # Override setFood()
#     def setFood(self, food='sandwich'):
#         if food != 'sandwith' and food != 'omelet':
#             raise AngryChefException
#         Meal.setFood(self, food)
#
# class Dinner(Meal):
#     """Holds the food and drink for dinner."""
#     def __init__(self):
#         """Initialize with steak and merlot."""
#         Meal.__init__(self, 'steak', 'merlot')
#         self.setName('dinner')
#
#     def printIt(self, prefix=''):
#         """Print even more nicely."""
#         print(prefix, 'A gourmet', self.name, 'with', self.food, 'and', self.drink)
#
# def test():
#     """Test function."""
#     print('Moudle meal test.')
#     # Generic no arguments.
#     print('Testing Meal class.')
#     m = Meal()
#     m.printIt('\t')
#     m = Meal('green eggs and ham', 'tea')
#     m.printIt('\t')
#     # Test breakfast
#     print('Testing Breakfast class.')
#     b = Breakfast()
#     b.printIt('\t')
#
#     b.setName('breaking of the fast')
#     b.printIt('\t')
#     # Test lunch
#     print('Testing Lunch class.')
#     l = Lunch()
#     l.printIt('\t')
#     print('Calling Lunch.setFood().')
#     try:
#         l.setFood('hotdog')
#     except AngryChefException:
#         print('\t', 'The chef is angry. Pick an omelet.')
# # Run test if this moudle is run as a program.
# if __name__ == '__main__':
#     test()

import meal
print('Making a Breakfast')
breakfast = meal.makeBreakfast()

breakfast.printIt('\t')

print('Making a Lunch')
lunch = meal.makeLunch()

try:
    lunch.setFood('pancakes')
except meal.AngryChefException:
    print('\t', 'Cannot make a lunch of pancakes.')
    print('\t', 'The chef is angry. Pick an omelet.')
