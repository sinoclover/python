# # 820ms
# # 最小栈，由于最后对栈进行遍历，造成效率低
# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.data = []
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.data.append(x)
#
#     def pop(self):
#         """
#         :rtype: void
#         """
#         self.data.pop()
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.data[-1]
#
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return min(self.data)
#
# # 84ms
# # 考虑使用双栈思想以提高效率
# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.data = []
#         self.min = []
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.data.append(x)  # 压入数据栈
#         if not self.min or self.min[-1] >= x:  # 当最小值栈为空或最小值栈顶大于数据时压入最小值栈
#             self.min.append(x)
#
#     def pop(self):
#         """
#         :rtype: void
#         """
#         a = self.data.pop()  # 顶层数值退栈
#         if a == self.min[-1]:  # 若退栈的数值与最小值栈顶相同，则最小值栈顶也退栈
#             self.min.pop()
#
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.data[-1]
#
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.min[-1]
#
# stack = MinStack()
# stack.push(-2)
# stack.push(0)
# stack.push(-3)
# print(stack.getMin())
# stack.pop()
# print(stack.top())
# print(stack.getMin())

# 40ms
# # 有效的括号
# def isValid(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     # 使用栈的思想，根据括号规则进行入栈退栈，最后判断栈是否为空来衡量是否合法
#     stack = []
#     brackets = {'(': ')', '[': ']', '{': '}'}
#     if len(s) > 0:
#         for i in range(len(s)):
#             if s[i] in brackets:
#                 stack.append(s[i])
#             elif len(stack) > 0 and s[i] == brackets[stack[-1]]:
#                 stack.pop()
#             else:
#                 return False
#     else:
#         return True
#     return len(stack) == 0
#
# print(isValid(']'))

# # 每日温度
# # 嵌套循环超出时间限制
# def dailyTemperatures(T):
#     """
#     :type T: List[int]
#     :rtype: List[int]
#     """
#     stack = []
#     for i in range(len(T)):
#         for j in range(i+1, len(T)):
#             if T[i] < T[j]:
#                 stack.append(j-i)
#                 break
#             if j >= len(T) - 1:
#                 stack.append(0)
#     stack.append(0)
#     return stack

# # 328ms
# def dailyTemperatures(T):
#     """
#     :type T: List[int]
#     :rtype: List[int]
#     """
#     # 构建递减栈，栈作为一个下标的存储器，对尚未满足条件的下标进行暂存
#     # 一但满足条件，递减栈则进行出栈操作，从而对上一个未满足条件的下标进行判断
#     stack = []
#     res = [0] * len(T)  # 初始化返回值0
#     # 获取列表下标及值
#     for key, value in enumerate(T):
#         # 当栈不为空时
#         if stack:
#             # 栈不为空以及栈顶代表的元素值小于当前元素值时保持循环，对栈进行递减
#             while stack and T[stack[-1]] < value:
#                 res[stack[-1]] = key - stack[-1]
#                 stack.pop()
#         # 当栈为空以及栈顶代表的值大于等于当前元素值时，将当前下标入栈
#         stack.append(key)
#     return res
#
# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# print(dailyTemperatures(temperatures))

# # 逆波兰表达式求值
# # 68ms
# def evalRPN(tokens):
#     """
#     :type tokens: List[str]
#     :rtype: int
#     """
#     stack = []
#     for ch in tokens:
#         if ch not in '+-*/':
#             stack.append(int(ch))
#         elif ch == '+':
#             num1 = stack.pop()
#             num2 = stack.pop()
#             stack.append((num2 + num1))
#         elif ch == '-':
#             num1 = stack.pop()
#             num2 = stack.pop()
#             stack.append((num2 - num1))
#         elif ch == '*':
#             num1 = stack.pop()
#             num2 = stack.pop()
#             stack.append((num2 * num1))
#         elif ch == '/':
#             num1 = stack.pop()
#             num2 = stack.pop()
#             stack.append(int(num2 / num1))
#     return stack[-1]

# 44ms 优化
def evalRPN(tokens):
    stack = []
    cal = {"+": lambda x, y: x+y, "-": lambda x, y: x-y, "*": lambda x, y: x*y, "/": lambda x, y: int(x/y)}

    for i in tokens:
        if i not in ["+", "-", "*", "/"]:
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(cal[i](a, b))
    return stack[0]

l1 = ["4", "13", "5", "/", "+"]
l2 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(l1))
print(evalRPN(l2))
