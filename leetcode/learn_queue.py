# # 84
# class MyCircularQueue:
#
#     def __init__(self, k):
#         """
#         Initialize your data structure here. Set the size of the queue to be k.
#         :type k: int
#         """
#         self.data = [None] * k
#         self.size = k
#         self.head = -1
#         self.tail = -1
#
#     def enQueue(self, value):
#         """
#         Insert an element into the circular queue. Return true if the operation is successful.
#         :type value: int
#         :rtype: bool
#         """
#         if self.isFull() == True:
#             return False
#         # 中继状态
#         if self.isEmpty() == True:
#             self.head = 0  # 当队列为空时，入队操作将head放置在首位
#         self.tail = (self.tail + 1) % self.size  # 通过取余进行尾部下标的不断循环
#         self.data[self.tail] = value
#         return True
#
#     def deQueue(self):
#         """
#         Delete an element from the circular queue. Return true if the operation is successful.
#         :rtype: bool
#         """
#         if self.isEmpty() == True:
#             return False
#         # 中继状态
#         if self.head == self.tail:
#             # 当首位下标相等时，进行出队操作即使得队列为空，将首位下标返回至初始状态即可。
#             # 注意，出队操作移动下标即可。队列不关注内部情况，只关注首尾状态，即内部数字被隐藏。
#             self.head = -1
#             self.tail = -1
#             return True
#         self.head = (self.head + 1) % self.size  # 通过取余进行头部下标的不断循环
#         return True
#
#     def Front(self):
#         """
#         Get the front item from the queue.
#         :rtype: int
#         """
#         if self.isEmpty() == True:
#             return -1
#         return self.data[self.head]
#
#     def Rear(self):
#         """
#         Get the last item from the queue.
#         :rtype: int
#         """
#         if self.isEmpty() == True:
#             return -1
#         return self.data[self.tail]
#
#     def isEmpty(self):
#         """
#         Checks whether the circular queue is empty or not.
#         :rtype: bool
#         """
#         # 判断队列头部下标是否在初始位置
#         return self.head == -1
#
#     def isFull(self):
#         """
#         Checks whether the circular queue is full or not.
#         :rtype: bool
#         """
#         # 判断尾部下标的下一位是否为头部下标
#         return (self.tail + 1) % self.size == self.head

#
class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.data = []
        self.size = k
        self.count = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull() == True:
            return False
        self.data.append(value)
        self.count += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty() == True:
            return False
        self.data = self.data[1:]
        self.count -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty() == True:
            return -1
        return self.data[0]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty() == True:
            return -1
        return self.data[-1]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        # 判断队列头部下标是否在初始位置
        return self.count <= 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        # 判断尾部下标的下一位是否为头部下标
        return self.count >= self.size

q = MyCircularQueue(3)  # 初始化循环队列
print(q.isEmpty())  #  判断队列是否为空
print(q.enQueue(1))  # 入队1
print(q.enQueue(2))  # 入队2
print(q.enQueue(3))  # 入队3
print(q.enQueue(4))  # 入队4，队列已满返回False
print(q.Front())  # 队列第一位为1
print(q.Rear())  # 队列最后一位为3
print(q.isFull())  # 判断队列是否已满
print(q.deQueue())  # 出队1
print(q.enQueue(4))  # 入队4
print(q.Front())  # 队列第一位为2
print(q.Rear())  # 队列最后一位为4
print(q)