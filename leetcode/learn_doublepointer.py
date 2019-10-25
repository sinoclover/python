# 反转字符串
# # 翻转字符串，直接反序
# def reverseString(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     return s[::-1]

# # 使用双指针
# def reverseString(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     s = list(s)  # 由于字符串不可变，则转换为字符数组
#     i = len(s)-1  # 获取尾部下标
#     for j in range(len(s)):
#         if i > j:
#             s[i], s[j] = s[j], s[i]
#             # temp = s[j]
#             # s[j] = s[i]
#             # s[i] = temp
#             i -= 1
#     return ''.join(s)
#
# s = 'hello'
# print(s)
# print(reverseString(s))

# # 数组拆分1
# def arrayPairSum(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     res = 0
#     nums = sorted(nums)
#     i = 0
#     while i < len(nums):
#         res += nums[i]
#         i += 2
#     return res

# # 代码优化
# def arrayPairSum(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     nums.sort()
#     return sum(nums[::2])
#
# s = [1, 4, 3, 2]
# print(arrayPairSum(s))

# # 两数之和2
# # 超出时间限制
# def twoSum(numbers, target):
#     """
#     :type numbers: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     res = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 res.append(i+1)
#                 res.append(j+1)
#                 return res
#     return res

# # 使用双指针
# # 由于是排序数组，则可以使用首尾双指针进行类似二分法的操作
# def twoSum(numbers, target):
#     """
#     :type numbers: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     i = 0
#     j = len(numbers)-1
#     while i < j:
#         if numbers[i] + numbers[j] == target:
#             return [i+1, j+1]
#         elif numbers[i] + numbers[j] > target:
#             j -= 1
#         else:
#             i += 1
#     return []
#
# numbers = [1, 2, 3, 4]
# target = 10
# print(twoSum(numbers, target))

# # 移除元素
# # 使用双指针，并原地修改数组
# def removeElement(nums, val):
#     """
#     :type nums: List[int]
#     :type val: int
#     :rtype: int
#     """
#     i = 0
#     if nums:
#         for j in range(len(nums)):
#             if nums[j] != val:
#                 nums[i] = nums[j]
#                 i += 1
#     return i
#
# nums = [3,2,2,3]
# val = 3
# print(removeElement(nums, val))

# # 最大连续1的个数
# # 建立一个个数列表和计数器，当列表中的值为1时计数器加一，不为一时则将个数加入到个数列表中，并将计数器清零。
# # 最后不要忘记结束时也要将计数器添加进列表一次
# def findMaxConsecutiveOnes(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     stack = []
#     count = 0
#     for i in range(len(nums)):
#         if nums[i] == 1:
#             count += 1
#         else:
#             stack.append(count)
#             count = 0
#     stack.append(count)
#     return max(stack)
#
# s = [1,1,0,1,1,1]
# print(findMaxConsecutiveOnes(s))

# # 长度最小的子数组
# # 超出时间限制
# def minSubArrayLen(s, nums):
#     """
#     :type s: int
#     :type nums: List[int]
#     :rtype: int
#     """
#     stack = []
#     if nums:
#         for i in range(len(nums)):
#             value = 0
#             j = i
#             while j < len(nums):
#                 value += nums[j]
#                 j += 1
#                 if value >= s:
#                     stack.append(j - i)
#                     break
#     if stack:
#         return min(stack)
#     return 0

# # 利用双指针构成滑动窗口，非快慢双指针
# # 因是计算长度，则通过规则变化左右指针来获取。
# def minSubArrayLen(s, nums):
#     """
#     :type s: int
#     :type nums: List[int]
#     :rtype: int
#     """
#     stack = []
#     value = 0
#     i = j = 0
#     while i < len(nums):
#         if value <= s and j < len(nums):
#             value += nums[j]
#             j += 1
#         else:
#             value -= nums[i]
#             i += 1
#         if value >= s:
#             stack.append(j - i)
#     if stack:
#         return min(stack)
#     return 0
#
# nums = [2,3,1,2,4,3]
# s = 7
# print(minSubArrayLen(s, nums))
