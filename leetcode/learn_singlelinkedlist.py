# # 设计链表
# # 建立链表结点结构
# class Node(object):
#
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
# # 建立单链表结构
# class MyLinkedList(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.head = Node(None)
#
#     def get(self, index):
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         :type index: int
#         :rtype: int
#         """
#         cur = self.head
#         # 注意列表为空的情形
#         if cur.val is None:
#             return -1
#         for i in range(index):  # index从0开始
#             cur = cur.next
#             if cur is None:
#                 return -1
#         return cur.val
#
#     def addAtHead(self, val):
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         :type val: int
#         :rtype: void
#         """
#         node = Node(val)
#         # 注意列表为空的情形
#         if self.head.val is None:
#             self.head = node
#         else:
#             node.next = self.head
#             self.head = node
#
#     def addAtTail(self, val):
#         """
#         Append a node of value val to the last element of the linked list.
#         :type val: int
#         :rtype: void
#         """
#         node = Node(val)
#         # 注意列表为空的情形
#         if self.head.val is None:
#             self.head = node
#         else:
#             cur = self.head
#             while cur.next is not None:
#                 cur = cur.next
#             cur.next = node
#
#     def addAtIndex(self, index, val):
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         :type index: int
#         :type val: int
#         :rtype: void
#         """
#         cur = self.head
#         if index == 0:  # 无论链表是否为空，都可以对其进行添加
#             self.addAtHead(val)
#         # 注意列表为空的情形
#         if cur.val is None:
#             return
#         elif index == self.countIndex()+1:
#             self.addAtTail(val)
#         elif index > self.countIndex()+1:
#             return
#         else:
#             node = Node(val)
#             for i in range(index-1):
#                 cur = cur.next  # 获得的是该下标的前一结点
#             follow = cur.next  # 获得当前该下标结点
#             cur.next = node
#             node.next = follow
#
#     def deleteAtIndex(self, index):
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         :type index: int
#         :rtype: void
#         """
#         cur = self.head
#         if index == 0:
#             self.head = cur.next
#         elif index == self.countIndex():
#             for i in range(index-1):
#                 cur = cur.next
#             cur.next = None
#         elif index > self.countIndex():
#             return
#         else:
#             for i in range(index-1):
#                 cur = cur.next  # 获得该下标的前一结点
#             follow = cur.next  # 获得当前下标结点
#             cur.next = follow.next
#
#     def countIndex(self):
#         """
#         Count the index of the linked list.
#         :rtype: int
#         """
#         count = 0
#         cur = self.head
#         while cur.next is not None:
#             count += 1
#             cur = cur.next
#         return count  # 获取的刚好是最大的下标，而链表长度为count+1

# # 设计链表优化
# # 建立链表结点结构
# class Node(object):
#
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
# # 建立单链表结构
# class MyLinkedList(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.head = Node(None)  # 哨兵结点
#         self.length = 0
#
#     def get(self, index):
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         :type index: int
#         :rtype: int
#         """
#         # 注意链表为空的情形
#         if self.length == 0:
#             return -1
#         cur = self.head
#         for i in range(index):  # index从0开始,到index-1时指在当前下标上
#             cur = cur.next
#             if cur is None:
#                 return -1
#         return cur.val
#
#     def addAtHead(self, val):
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         :type val: int
#         :rtype: void
#         """
#         node = Node(val)  # 初始化新结点
#         # 注意链表为空的情形
#         if self.length == 0:
#             self.head = node  # 将新结点设置为头结点
#         else:  # 当链表不为空时
#             node.next = self.head  # 将新结点指向头结点
#             self.head = node  # 将新结点设置为头结点
#         self.length += 1
#
#     def addAtTail(self, val):
#         """
#         Append a node of value val to the last element of the linked list.
#         :type val: int
#         :rtype: void
#         """
#         node = Node(val)  # 初始化新结点
#         # 注意列表为空的情形
#         if self.length == 0:
#             self.head = node  # 将新结点设置为头结点
#         else:  # 当链表不为空时
#             cur = self.head  # 对链表进行遍历，直至下一个结点为空时停止
#             while cur.next is not None:
#                 cur = cur.next
#             cur.next = node  # 将下一个结点设置为新结点
#         self.length += 1
#
#     def addAtIndex(self, index, val):
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         :type index: int
#         :type val: int
#         :rtype: void
#         """
#         node = Node(val)  # 初始化新结点
#         if index < 0 or index > self.length:
#             return
#         elif index == self.length:
#             self.addAtTail(val)
#         else:
#             cur = self.head
#             for i in range(index-1):
#                 cur = cur.next  # 给定下标的前一结点
#             node.next = cur.next  # 给定结点的下一结点
#             cur.next = node  # 将新结点连接到前一结点上
#         self.length += 1
#
#
#     def deleteAtIndex(self, index):
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         :type index: int
#         :rtype: void
#         """
#         cur = self.head
#         if index < 0 or index > self.length-1:
#             return
#         elif index == 0:  # 头结点删除
#             self.head = cur.next
#         elif index == self.length-1:  # 尾结点删除
#             for i in range(index-1):
#                 cur = cur.next
#             cur.next = None
#         else:
#             for i in range(index-1):
#                 cur = cur.next  # 获得该下标的前一结点
#             cur.next = cur.next.next
#         self.length -= 1
#

# # 直接使用列表模拟链表
# class MyLinkedList(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.list = []
#
#     def get(self, index):
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         :type index: int
#         :rtype: int
#         """
#         if index < 0 or index > len(self.list) - 1:
#             return -1
#         return self.list[index]
#
#     def addAtHead(self, val):
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         :type val: int
#         :rtype: void
#         """
#         self.list.insert(0, val)
#
#     def addAtTail(self, val):
#         """
#         Append a node of value val to the last element of the linked list.
#         :type val: int
#         :rtype: void
#         """
#         self.list.append(val)
#
#     def addAtIndex(self, index, val):
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         :type index: int
#         :type val: int
#         :rtype: void
#         """
#         if index > len(self.list) or index < 0:
#             return
#         elif index == len(self.list):
#             self.list.append(val)
#         else:
#             self.list.insert(index, val)
#
#     def deleteAtIndex(self, index):
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         :type index: int
#         :rtype: void
#         """
#         if index > len(self.list)-1 or index < 0:
#             return
#         self.list.pop(index)

# 设计双链表
# 建立链表结点结构
class Node(object):

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

# 建立单链表结构
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(None)  # 哨兵结点
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        # 注意链表为空的情形
        if self.length == 0:
            return -1
        cur = self.head
        for i in range(index):  # index从0开始,到index-1时指在当前下标上
            cur = cur.next
            if cur is None:
                return -1
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)  # 初始化新结点
        # 注意链表为空的情形
        if self.length == 0:
            self.head = node  # 将新结点设置为头结点
        else:  # 当链表不为空时
            node.next = self.head  # 将新结点指向头结点
            node.prev = None
            self.head.prev = node
            self.head = node  # 将新结点设置为头结点
        self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)  # 初始化新结点
        # 注意列表为空的情形
        if self.length == 0:
            self.head = node  # 将新结点设置为头结点
        else:  # 当链表不为空时
            cur = self.head  # 对链表进行遍历，直至下一个结点为空时停止
            while cur.next:
                cur = cur.next
            node.prev = cur  # 将尾结点连接至当前结点
            node.next = None
            cur.next = node  # 将下一个结点设置为新结点
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        node = Node(val)  # 初始化新结点
        if index < 0 or index > self.length:
            return
        elif index == self.length:
            # print('sssssss')
            return self.addAtTail(val)
        elif index == 0:
            return self.addAtHead(val)
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next  # 给定下标的结点
            node.prev = cur.prev  # 将要添加的结点的prev连接到前一个结点上
            node.next = cur  # 将要添加的结点的next连接到当前结点上
            cur.prev.next = node  # 将前一个结点连接到给定结点上
            cur.prev = node  # 将当前结点连接到给定结点上
        self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        cur = self.head
        if index < 0 or index > self.length-1:
            return
        elif index == 0:  # 头结点删除
            self.head = cur.next
            self.head.prev = None
        elif index == self.length-1:  # 尾结点删除
            for i in range(index-1):
                cur = cur.next
            cur.next = None
        else:
            for i in range(index):
                cur = cur.next  # 获得该下标的当前结点
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        self.length -= 1

l = MyLinkedList()
# l.addAtHead(0)
# l.addAtTail(1)
# l.addAtTail(2)
l.addAtIndex(0, 0)
print(l.length)
l.addAtIndex(1, 1)
l.addAtIndex(2, 2)
print(l.get(0))
print(l.get(1))
print(l.get(2))