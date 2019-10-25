# # 44ms
# # 用栈实现队列
# # 可以使用两个栈，其中一个栈作为中转栈，将入栈的元素反序出栈
# class MyQueue:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.stack = []  # 中转栈
#         self.queue = []  # 输出栈，模拟队列
#
#     def push(self, x):
#         """
#         Push element x to the back of queue.
#         :type x: int
#         :rtype: void
#         """
#         self.stack.append(x)
#
#     def pop(self):
#         """
#         Removes the element from in front of queue and returns that element.
#         :rtype: int
#         """
#         if not self.queue:
#             while self.stack:
#                 self.queue.append(self.stack.pop())
#         return self.queue.pop()
#
#     def peek(self):
#         """
#         Get the front element.
#         :rtype: int
#         """
#         if not self.queue:
#             while self.stack:
#                 self.queue.append(self.stack.pop())
#         return self.queue[-1]
#
#     def empty(self):
#         """
#         Returns whether the queue is empty.
#         :rtype: bool
#         """
#         if self.queue or self.stack:
#             return False
#         else:
#             return True

# # 违法做法
# class MyQueue:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.queue = []
#
#     def push(self, x):
#         """
#         Push element x to the back of queue.
#         :type x: int
#         :rtype: void
#         """
#         self.queue.append(x)
#
#     def pop(self):
#         """
#         Removes the element from in front of queue and returns that element.
#         :rtype: int
#         """
#         return self.queue.pop(0)  # 由题意在栈中pop(0)是违法的，只有pop(-1)合法
#
#     def peek(self):
#         """
#         Get the front element.
#         :rtype: int
#         """
#         return self.queue[0]  # 同样栈中取[0]也是违法的，只有[-1]合法
#
#     def empty(self):
#         """
#         Returns whether the queue is empty.
#         :rtype: bool
#         """
#         return not self.queue
#
# q = MyQueue()
# print(q.empty())
# q.push(1)
# q.push(2)
# print(q.peek())
# q.pop()
# print(q.empty())

# # 用队列实现栈
# # 使用两个队列，相互循环使用。
# # 入栈即将元素入队至非空队列，注意若两者皆为空队列，进入队列1
# # 出栈即将非空队列中出队至最后一位即栈顶元素，将出队元素置于另一个空队列中，如此反复。
# class MyStack:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         # 队列只支持pop(0)和切片[0]操作
#         self.queue1 = []  # 队列1
#         self.queue2 = []  # 队列2
#         self.t = None
#
#     def push(self, x):
#         """
#         Push element x onto stack.
#         :type x: int
#         :rtype: void
#         """
#         # 如果队列2不空，将元素压入队列2
#         if self.queue2:
#             self.queue2.append(x)
#         # 其他情况，队列1不为空或队列1队列2都为空将元素压入队列1
#         else:
#             self.queue1.append(x)
#
#     def pop(self):
#         """
#         Removes the element on top of the stack and returns that element.
#         :rtype: int
#         """
#         # 如果队列1不为空
#         if self.queue1:
#             while len(self.queue1) > 1:
#                 self.queue2.append(self.queue1.pop(0))
#             return self.queue1.pop(0)
#         else:
#             while len(self.queue2) > 1:
#                 self.queue1.append(self.queue2.pop(0))
#             return self.queue2.pop(0)
#
#
#     def top(self):
#         """
#         Get the top element.
#         :rtype: int
#         """
#         if self.queue1:
#             while len(self.queue1) > 1:
#                 self.queue2.append(self.queue1.pop(0))
#             self.t = self.queue1.pop(0)
#             self.queue2.append(self.t)
#             return self.t
#         else:
#             while len(self.queue2) > 1:
#                 self.queue1.append(self.queue2.pop(0))
#             self.t = self.queue2.pop(0)
#             self.queue1.append(self.t)
#             return self.t
#
#     def empty(self):
#         """
#         Returns whether the stack is empty.
#         :rtype: bool
#         """
#         if self.queue1 or self.queue2:
#             return False
#         else:
#             return True

# # 违法做法
# class MyStack:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.stack = []
#
#     def push(self, x):
#         """
#         Push element x onto stack.
#         :type x: int
#         :rtype: void
#         """
#         self.stack.append(x)
#
#     def pop(self):
#         """
#         Removes the element on top of the stack and returns that element.
#         :rtype: int
#         """
#         return self.stack.pop(-1)  # 由题意在队列里pop(-1)是违法的，只有pop(0)合法
#
#     def top(self):
#         """
#         Get the top element.
#         :rtype: int
#         """
#         return self.stack[-1]  # 同样队列中取[-1]也是违法的，只有[0]合法
#
#     def empty(self):
#         """
#         Returns whether the stack is empty.
#         :rtype: bool
#         """
#         return not self.stack
#
# q = MyStack()
# q.push(1)
# q.push(2)
# q.push(3)
# print(q.pop())
# print(q.top())
# q.pop()
# print(q.top())

# # 字符串解码
# def decodeString(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     list = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     stack_k = []  # 数字栈
#     stack_s = []  # 字符栈
#     str = ''
#     for ch in s:
#         if ch in list:  # 根据定义的哈希表将字符串转换为数字压入数字栈
#             stack_k.append(list[ch])
#         elif ch == '[':  # 将[作为分隔符分别压入两个栈，分隔符必在数字后出现
#             stack_k.append(ch)
#             stack_s.append(ch)
#         elif ch == ']':  # 将]作为解码符进行解码运算
#             i = 1 # 初始化参数
#             k = 0
#             res = ''  # 设置字符串变量
#             stack_k.pop()  # 去除k中的'['
#             while stack_k:  # 当数字栈不为空时一直循环
#                 if stack_k[-1] != '[':  # 没有遇到分隔符
#                     k += stack_k.pop() * i # 循环计算当前k值
#                     i *= 10
#                 else:  # 遇到分隔符退出循环
#                     break
#             while stack_s:  # 当字符栈不为空时一直循环
#                 if stack_s[-1] != '[':  # 没有遇到分隔符
#                     res += stack_s.pop()  # 反向连接字符串
#                 else:  # 遇到分隔符退出循环
#                     break
#             stack_s.pop()  # 字符串出栈后再去除s中的'['
#             stack_s.append(k * res)  # 将倍数重复后的字符串压入字符栈
#
#         else:
#             stack_s.append(ch)  # 遇到字符压入字符栈
#     while stack_s:
#         str += stack_s.pop()  # 最后将字符栈中的字符串起来
#     str = str[::-1]  # 将字符反向
#     return str

# 上述算法太过于繁琐，其中对于倍数的计算有些冗杂，可以进行优化
def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    stack_k = []  # 数字栈
    stack_l = []  # 字符长度栈
    string = ''
    k = 0
    l = 0
    for ch in s:
        if '0' <= ch <= '9':
            k = k * 10 + int(ch)  # 由此可以简化数字系数的解码
        elif ch == '[':
            stack_k.append(k - 1)  # 因为string里已经包含一次
            stack_l.append(l)  # 遇到[记录一次字符串长度位置
            k = 0  # 当遇到[时，k复位
        elif ch == ']':
            string += string[stack_l.pop():len(string)] * stack_k.pop()
            l = len(string)  # 实时记录字符串长度位置
        else:
            string += ch  # 遇到字符将其加入字符串
            l = len(string)  # 实时记录字符串长度位置
    return string

s = '3[a]2[bc]'
print(decodeString(s))