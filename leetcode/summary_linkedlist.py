# # 两数相加
# def addTwoNumbers(l1, l2):
#     """
#     :type l1: ListNode
#     :type l2: ListNode
#     :rtype: ListNode
#     """
#     stack = [0]
#     dummy = ListNode(0)
#     cur = dummy
#     while l1 and l2:
#         value = l1.val + l2.val + stack[-1]
#         if value >= 10:
#             value = value % 10
#             cur.next = ListNode(value)
#             stack.append(1)
#         else:
#             cur.next = ListNode(value)
#             stack.append(0)
#         l1 = l1.next
#         l2 = l2.next
#         cur = cur.next
#     while l1:
#         value = l1.val + stack[-1]
#         if value >= 10:
#             value = value % 10
#             cur.next = ListNode(value)
#             stack.append(1)
#         else:
#             cur.next = ListNode(value)
#             stack.append(0)
#         l1 = l1.next
#         cur = cur.next
#     while l2:
#         value = l2.val + stack[-1]
#         if value >= 10:
#             value = value % 10
#             cur.next = ListNode(value)
#             stack.append(1)
#         else:
#             cur.next = ListNode(value)
#             stack.append(0)
#         l2 = l2.next
#         cur = cur.next
#     if stack[-1] != 0:
#         tail = ListNode(1)
#         cur.next = tail
#     return dummy.next

# 旋转链表
def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    length = 0
    dummy = ListNode(0)
    dummy.next = head
    cur = dummy
    while cur.next:
        cur = cur.next
        length += 1
    cur.next = head
    count = length - k % length
    for i in range(count):
        cur = cur.next
    head = cur.next
    cur.next = None
    return head