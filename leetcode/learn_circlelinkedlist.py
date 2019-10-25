# 环形链表
# 已经给定链表结点结构，考虑使用双指针
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def hasCycle(head):
#     """
#     :type head: ListNode
#     :rtype: bool
#     """
#     slow = quick = head
#     while slow and quick:
#         try:
#             slow = slow.next
#             quick = quick.next.next
#         except:
#             return False
#         if slow == quick:
#             return True
#     return False
#
# # 考虑使用哈希表
# def hasCycle(head):
#     """
#     :type head: ListNode
#     :rtype: bool
#     """
#     dic = {}
#     while head:
#         if head in dic:
#             return True
#         else:
#             dic[head] = 1
#         head = head.next
#     return False

# # 环形链表2
# # 已经给定链表结点结构，考虑使用双指针
# def detectCycle(head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
#     loop = False
#     slow = quick = head
#     # 判断是否有环
#     while slow and quick:
#         try:
#             slow = slow.next
#             quick = quick.next.next
#         except:
#             return None
#         if slow == quick:
#             loop = True
#     if loop is True:
#         check = head
#         while check != slow:
#             check = check.next
#             slow = slow.next
#         return slow
#     return None

# # 已经给定链表结点结构，考虑使用哈希表
# def detectCycle(head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
#     dic = {}
#     i = 0
#     while head:
#         if head in dic:
#             return head
#         else:
#             dic[head] = 1
#         head = head.next
#     return None

# 相交链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# # 考虑使用哈希表，但使用了额外的空间，不能通过
# def getIntersectionNode(headA, headB):
#     """
#     :type head1, head1: ListNode
#     :rtype: ListNode
#     """
#     dic = {}
#     curA, curB = headA, headB
#     while curA is not None:
#         dic[curA] = 1
#         curA = curA.next
#     while curB is not None:
#         if curB in dic:
#             return curB.val
#     return None

# # 考虑使用指针，双重循环超出时间限制
# def getIntersectionNode(headA, headB):
#     """
#     :type head1, head1: ListNode
#     :rtype: ListNode
#     """
#     curA = headA
#     while curA is not None:
#         curB = headB
#         while curB is not None:
#             if curA == curB:
#                 return curA
#             curB = curB.next
#         curA = curA.next
#     return None

# # 将其中一个链表连成环，那么就回到了环形链表2的问题上去
# def getIntersectionNode(headA, headB):
#     """
#     :type head1, head1: ListNode
#     :rtype: ListNode
#     """
#     if headA and headB:
#         # 将headB成环，注意在返回时解环
#         cur = headB
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = headB
#         # 判断是否相交
#         loop = False
#         slow = quick = headA
#         while quick and quick.next:
#             slow = slow.next
#             quick = quick.next.next
#             if slow == quick:
#                 loop = True
#                 break
#         # 查找交点
#         if loop is True:
#             check = headA
#             while check != slow:
#                 check = check.next
#                 slow = slow.next
#             cur.next = None
#             return slow
#         cur.next = None
#     return None

# # 优化
# def getIntersectionNode(headA, headB):
#     """
#     :type head1, head1: ListNode
#     :rtype: ListNode
#     """
#     p1, p2 = headA, headB
#     while p1 != p2:
#         if p1 is None:
#             p1 = headB
#         else:
#             p1 = p1.next
#         if p2 is None:
#             p2 = headA
#         else:
#             p2 = p2.next
#     return p1

# 删除链表的倒数第N个结点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 注意哑结点的应用
# 遍历两遍
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    length = 0
    first = head
    while first is not None:
        length += 1
        first = first.next
    length -= n
    first = dummy
    while length > 0:
        length -= 1
        first = first.next
    first.next = first.next.next
    return dummy.next

# # 遍历一遍
# def removeNthFromEnd(head, n):
#     """
#     :type head: ListNode
#     :type n: int
#     :rtype: ListNode
#     """
#     dummy = ListNode(0)
#     dummy.next = head
#     slow = fast = dummy
#     for i in range(n):
#         fast = fast.next
#     while fast.next is not None:
#         slow = slow.next
#         fast = fast.next
#     slow.next = slow.next.next
#     return dummy.next