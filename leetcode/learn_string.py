# # 二进制求和
# def addBinary(a, b):
#     """
#     :type a: str
#     :type b: str
#     :rtype: str
#     """
#     res = ''
#     stack = [0]
#     if len(a) >= len(b):
#         long = a
#         short = b
#     else:
#         long = b
#         short = a
#     while short:
#         c = int(long[-1]) + int(short[-1]) + stack[-1]
#         if c > 1:
#             res += str(c%2)
#             stack.append(1)
#             long = long[:-1]
#             short = short[:-1]
#         else:
#             res += str(c)
#             stack.append(0)
#             long = long[:-1]
#             short = short[:-1]
#     while long:
#         c = int(long[-1]) + stack[-1]
#         if c > 1:
#             res += str(c%2)
#             stack.append(1)
#             long = long[:-1]
#         else:
#             res += str(c)
#             stack.append(0)
#             long = long[:-1]
#     if stack[-1] == 1:
#         res += '1'
#     return res[::-1]

# def addBinary(a, b):
#     """
#     :type a: str
#     :type b: str
#     :rtype: str
#     """
#     return bin(int(a,2)+int(b,2))[2:]
# a = '1111'
# b = '1111'
# print(addBinary(a, b))

# # 实现strStr()
# def strStr(haystack, needle):
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     if needle == '':
#         return -1
#     for i in range(len(haystack)):
#         if needle == haystack[i:i+len(needle)]:
#             return i
#     return -1
#
# haystack = "hello"
# needle = "ll"
# print(strStr(haystack, needle))

# 最长公共字符串
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    res = ''
    if strs:
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i < len(strs[j]) and strs[0][i] == strs[j][i]:
                    continue
                else:
                    return res
            res += strs[0][i]
    return res

s = ["flower","flow","flight"]
s1 = ['aa', 'a']
print(longestCommonPrefix(s))