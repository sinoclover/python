# 反转链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def reverseList(head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
#     pre = head
#     while head and head.next is not None:
#         cur = head.next
#         head.next = head.next.next  # 按原顺序先跳过下一个结点，再将其连接到头部
#         cur.next = pre
#         pre = cur
#     return pre

# # 优化
# def reverseList(head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
#     pre, cur = None, head
#     while cur:
#         cur.next, pre, cur = pre, cur, cur.next  # 双指针反向链接处理，多变量赋值的表达式是先计算右边的值，在赋给左边的变量
#     return pre

# # 移除链表元素
# def removeElements(head, val):
#     """
#     :type head: ListNode
#     :type val: int
#     :rtype: ListNode
#     """
#     dummy = ListNode(0)  # 注意哑结点的使用
#     dummy.next = head
#     pre, cur = dummy, head
#     while cur:
#         if cur.val == val:
#             pre.next = cur.next
#         else:
#             pre = cur
#         cur = cur.next
#     return dummy.next

# # 奇偶链表
# def oddEvenList(head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
#     if head and head.next:
#         odd, even = head, head.next
#         tag = even
#     else:
#         return head
#     while odd.next and even.next:
#         odd.next = even.next
#         odd = odd.next
#         even.next = odd.next
#         even = even.next
#     odd.next = tag
#     return head

# 回文链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def isPalindrome(head):
#     """
#     :type head: ListNode
#     :rtype: bool
#     """
#     # 先找到链表中点
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     # 翻转后半部,将中点作为交叉出口点
#     pre = None
#     while slow:
#         slow.next, pre, slow = pre, slow, slow.next
#     while pre and head:
#         if head.val != pre.val:
#             return False
#         head = head.next
#         pre = pre.next
#     return True

# 优化
def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    pre = None
    slow = fast = head
    # 直接翻转前半部分
    while fast and fast.next:
        fast = fast.next.next
        slow.next, pre, slow = pre, slow, slow.next
    # 通过fast的情况可以判断链表是奇数还是偶数，跳过奇数链表的中间点
    if fast:
        slow = slow.next
    while pre and slow:
        if slow.val != pre.val:
            return False
        slow = slow.next
        pre = pre.next
    return True

