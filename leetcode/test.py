# # 有效的括号
# def isValid(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     #
#     # 使用栈的思想
#     brackets = {'(': 0, ')': 1, '[': 10, ']': 11, '{': 20, '}': 21}
#     stack = []
#     if len(s) > 0:
#         for i in range(0, len(s)):
#             if len(stack) == 0 or brackets[s[i]] - 1 != brackets[stack[-1]]:
#                 stack.append(s[i])
#             elif brackets[s[i]] - 1 == brackets[stack[-1]]:
#                 stack.pop()
#     else:
#         return False
#     if len(stack) == 0:
#         return True
#     else:
#         return False
# print(isValid(''))

# # 实现strstr()
# def strStr(haystack, needle):
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     if len(needle) == 0:
#         return 0
#     if len(haystack) == 0:
#         return -1
#     i = 0
#     n = len(needle)
#     for i in range(0, len(haystack)):
#         if  needle == haystack[i:i+n]:
#             return i
#     return -1

# def strStr(haystack, needle):
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     return haystack.find(needle)

# print(strStr('mississippi', 'issip'))

# # 报数
# def countAndSay(n):
#     """
#     :type n: int
#     :rtype: str
#     """
#     if n == 0:
#         return ''
#     if n == 1:
#         return '1'
#     res = ''
#     i = 0
#     pre_value = countAndSay(n-1)
#     for j in range(len(pre_value)):
#         if pre_value[j] != pre_value[i]:
#             res += str(j-i) + pre_value[i]
#             i = j
#     res += str(len(pre_value) - i) + pre_value[i]
#     return res
#
# print(countAndSay(0))