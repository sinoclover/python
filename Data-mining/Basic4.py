# # 面向对象编程，即以功能来划分问题，而非步骤或过程
# class Charmander:
#     def __init__(self, name, gender, level):
#         self.__type = ('fire', None)  # 固定属性，不依赖输入参数
#         self.__gender = gender
#         self.__name = name
#         self.__level = level
#         # 设置怪物状态最大HP，攻击，防御，特攻，特防，速度
#         self.__status = [10+2*level, 5+1*level, 5+1*level, 5+1*level, 5+1*level, 5+1*level]
#         self.__info = [self.__name, self.__type, self.__gender, self.__level, self.__status]
#         self.__index = -1
#     def getName(self):
#         print(self.__name)
#     def getGender(self):
#         print(self.__gender)
#     def getLevel(self):
#         print(self.__level)
#     def getType(self):
#         print(self.__type)
#     def getStatus(self):
#         print(self.__status)
#     def levelUp(self):
#         self.__status = [s+1 for s in self.__status]
#         self.__status[0] += 1  # Hp每级增加2，其余加1，作为接口外部修改数据
#     def __iter__(self):  # 建立迭代器
#         print('Name Type Gender Level Status')
#         return self
#     def __next__(self):  # 建立迭代对象的next方法
#         if self.__index == len(self.__info) - 1:
#             raise StopIteration
#         self.__index += 1
#         return self.__info[self.__index]
#
# # __init__方法在对象实例化时自动执行，用于初始化数据属性
# pokemon = Charmander('faker', 'male', 99)  # 实例化
# pokemon.getName()  # 实例化后显示初始值
#
# # 对象的方法
# getStatus_quote = pokemon.getStatus  # 方法引用
# getStatus_quote()
# # print(pokemon.level)  # 获取对象的数据属性并不需要对象的方法，直接在程序外部就可以调用
# # # 对象的具体数据属性的随意访问，违反了类的封装规则，需要对类的数据属性和方法进行私有化
# pokemon.getType()  # 通过设置的接口访问内部私有数据属性
# print(pokemon._Charmander__type)  # 强行从外部访问内部私有数据属性
# # python迭代器是通过iter()函数，返回定义next()方法的迭代器对象，当终止时抛出StopIteration异常
# for info in pokemon:
#     print(info)

# # 继承可能有一定的弊端，如基类对于子类有一定特殊的地方
# # 在继承中基类初始化方法__init__不会被自动调用，如果希望调用这种方法需要在子类中显示调用
# # 在子类调用基类的方法时，需要加上基类的类名前缀，且带上self参数变量
# # python先查找对应类的方法，如果子类中没有对应方法，才会在继承链的基类中按顺序查找
# # 在python继承中，子类不能方位基类的私有成员
#
# class pokemon:
#     def __init__(self, name, gender, level, type, status):
#         self.__type = type
#         self.__gender = gender
#         self.__name = name
#         self.__level = level
#         # 设置怪物状态最大HP，攻击，防御，特攻，特防，速度
#         self.__status = status
#         self.__info = [self.__name, self.__type, self.__gender, self.__level, self.__status]
#         self.__index = -1
#     def getName(self):
#         print(self.__name)
#     def getGender(self):
#         print(self.__gender)
#     def getLevel(self):
#         print(self.__level)
#     def getType(self):
#         print(self.__type)
#     def getStatus(self):
#         print(self.__status)
#     def levelUp(self):
#         self.__status = [s+1 for s in self.__status]
#         self.__status[0] += 1  # Hp每级增加2，其余加1，作为接口外部修改数据
#     def __iter__(self):  # 建立迭代器
#         print('Name Type Gender Level Status')
#         return self
#     def __next__(self):  # 建立迭代对象的next方法
#         if self.__index == len(self.__info) - 1:
#             raise StopIteration
#         self.__index += 1
#         return self.__info[self.__index]
#
# # 子类不能继承基类的私有数据属性，如__init__中的私有属性
# class Charmander(pokemon):
#     def __init__(self, name, gender, level):
#         self.__type = ('fire', None)  # 固定属性，不依赖输入参数
#         self.__gender = gender
#         self.__name = name
#         self.__level = level
#         self.__status = [10+2*level, 5+1*level, 5+1*level, 5+1*level, 5+1*level, 5+1*level]
#         # 向基类传输数据时需要添加self参数
#         pokemon.__init__(self, self.__name, self.__gender, self.__level, self.__type, self.__status)
#
# pokemon1 = Charmander('Bang', 'male', 5)
# pokemon1.getGender()
# for info in pokemon1:
#     print(info)

# 实验1 定义复数类Complex
class Complex:
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im
    def real(self):
        return self.Re
    def imag(self):
        return self.Im
    def add(self, comp):
        self.Re += comp.real()
        self.Im += comp.imag()
    def show(self):
        print('{:-.2f}{:+.2f}j'.format(self.Re, self.Im))  # +实时显示正负号，-只有负数显示正负号

c1 = Complex(2, 3)
c1.show()
c2 = Complex(8, -1)
print(c2.imag())
c1.add(c2)
c1.show()

# 实验2 定义Shape框架
import math
class Shape:
    pass

class Rectangle(Shape):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    def getCircumFerence(self):
        return 2 * self.__a + 2 * self.__b
    def getArea(self):
        return self.__a * self.__b

class Square(Rectangle, Shape):
    def __init__(self, a):
        self.__a = a
    def getCircumFerence(self):
        return 4 * self.__a
    def getArea(self):
        return self.__a ** 2

class Circle(Shape):
    def __init__(self, r):
        self.__r = r
    def getCircumFerence(self):
        return 2 * math.pi * self.__r
    def getArea(self):
        return math.pi * self.__r * self.__r

c = Circle(10)
print(c.getArea())
s = Square(5)
print(s.getCircumFerence())
r = Rectangle(7, 8)
print(r.getArea())