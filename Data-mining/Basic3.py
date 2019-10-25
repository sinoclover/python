# lambda匿名函数
g = lambda x : x+1
print(g(1))
# lambda定义了单行函数，其参数列表可以有多个，有且只有一个返回值，同时唯一的表达式中不能含有命令
from math import log
# 定义一个函数用于返回一个以base为底匿名对数函数
def make_logarithmic_function(base):
    return lambda x : log(x, base)
My_LF = make_logarithmic_function(3)
print(My_LF(9))

# 深复制与浅复制
import copy
list1 = [1, 2, ['a', 'b']]
list2 = list1
list3 = copy.copy(list1)  # 浅复制仅仅复制父对象，不会复制父对象内部的子对象
list4 = copy.deepcopy(list1)  # 复制父对象和子对象
list1.append(3)
list1[2].append('c')

print('list1', list1)
print('list2', list2)
print('list3', list3)
print('list4', list4)

# 递归算法计算斐波那契数列
def Fibonacci(n):
    if (n <= 2):
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(10))