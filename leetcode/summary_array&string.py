# # 旋转数组
# def rotate(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: void Do not return anything, modify nums in-place instead.
#     """
#     length = len(nums)
#     for i in range(length):
#         nums.append(nums[i])
#     temp = len(nums) - k
#     for j in range(k):
#         nums[j] = nums[temp]
#         temp += 1
#     temp = temp // 2
#     for j in range(k, length):
#         nums[j] = nums[temp]
#         temp += 1
#     for i in range(length):
#         nums.pop()

# # 优化
# def rotate(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: void Do not return anything, modify nums in-place instead.
#     """
#     length = len(nums)
#     nums[0:length] = nums[length-k:] + nums[0:length-k]
#
#
# s = [1,2,3,4,5,6,7]
# k = 3
# rotate(s, k)
# print(s)

# # 杨辉三角2
# # 二项式定理
# def getRow(rowIndex):
#     """
#     :type rowIndex: int
#     :rtype: List[int]
#     """
#     import math
#     res = [0] * (rowIndex+1)
#     for i in range(rowIndex+1):
#         res[i] = math.factorial(rowIndex) // (math.factorial(i) * math.factorial(rowIndex-i))
#     return res
#
# print(getRow(3))

# # 翻转字符串里的单词
# # 使用栈来翻转效率太低
# def reverseWords(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     stack = []
#     word = ''
#     res = ''
#     if s:
#         for i in range(len(s)):
#             if s[i] != ' ':
#                 word += s[i]
#             else:
#                 stack.append(word)
#                 word = ''
#         stack.append(word)
#         while '' in stack:
#             stack.remove('')
#     if stack:
#         for j in range(len(stack)):
#             res += stack.pop()
#             res += ' '
#         res = res.strip()
#     return res
#
# # 直接进行原地的分割和翻转
# def reverseWords(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     return ' '.join(reversed(s.split()))  # split函数默认对所有的空字符进行分割
#
# s = 'the  sky  is blue'
# print(reverseWords(s))

# # 翻转字符串里的单词3
# # 使用栈效率较低，空间复杂度较大
# def reverseWords(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     stack = []
#     word = ''
#     res = ''
#     if s:
#         for i in range(len(s)):
#             if s[i] != ' ':
#                 word += s[i]
#             else:
#                 stack.append(word[::-1])
#                 word = ''
#         stack.append(word[::-1])
#         while '' in stack:
#             stack.remove('')
#     if stack:
#         res = ' '.join(stack)
#     return res

# # 直接进行原地的分割和翻转
# def reverseWords(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     return ' '.join(reversed(s[::-1].split())) # split函数默认对所有的空字符进行分割
#
# s = "Let's take LeetCode contest"
# print(reverseWords(s))

# # 删除排序数组中的重复项
# # 使用set函数
# def removeDuplicates(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     nums[:] = sorted(list(set(nums)))
#     return len(nums)
#
# # 使用双指针
# def removeDuplicates(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     i = 0
#     if not nums:
#         return 0
#     for j in range(1, len(nums)):
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i] = nums[j]
#     i += 1
#     return i

# # 移动零
# # 基本思路先去掉零，再添上零，使用库函数方法效率不高O(n2)
# def moveZeroes(nums):
#     """
#     :type nums: List[int]
#     :rtype: void Do not return anything, modify nums in-place instead.
#     """
#     count = 0
#     while 0 in nums:
#         nums.remove(0)
#         count += 1
#     for i in range(count):
#         nums.append(0)

# 双指针交换位置，O(n)
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

s = [0,1,0,3,12]
moveZeroes(s)
print(s)
