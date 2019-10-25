# # 存在重复元素
# def containsDuplicate(nums):
#     """
#     :type nums: List[int]
#     :rtype: bool
#     """
#     hashset = set()
#     for i in nums:
#         if i not in hashset:
#             hashset.add(i)
#         else:
#             return True
#     return False

# # 存在重复元素简化
# def containsDuplicate(nums):
#     """
#     :type nums: List[int]
#     :rtype: bool
#     """
#     if len(nums) == len(set(nums)):
#         return False
#     else:
#         return True
#
# s = [1,2,3,4]
# print(containsDuplicate(s))

# # 只出现一次的数字
# def singleNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     nums = sorted(nums)
#     for i in range(0,len(nums),2):
#         try:
#             if nums[i] != nums[i+1]:
#                 return nums[i]
#         except:
#             return nums[i]

# # 只出现一次的数字，通过按位异或
# def singleNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     res = 0
#     for i in nums:
#         res ^= i
#     return res
#
# s = [2,2,1]
# print(singleNumber(s))

# # 两个数组的交集
# def intersection(nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: List[int]
#     """
#     res = set()
#     if len(nums1) <= len(nums2):
#         short = nums1
#         long = nums2
#     else:
#         short = nums2
#         long = nums1
#     for num in short:
#         if num in long:
#             res.add(num)
#     return list(res)
#
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# print(intersection(nums1, nums2))

# # 快乐数
# def isHappy(n):
#     """
#     :type n: int
#     :rtype: bool
#     """
#     sum = 0
#     for i in str(n):
#         sum += int(i)**2
#     if sum == 4:
#         return False
#     elif sum == 1:
#         return True
#     else:
#         return isHappy(sum)
#
# print(isHappy(19))

# # 同构字符串
# def isIsomorphic(s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     hashmap_s = {}
#     hashmap_t = {}
#     temp = ''
#     for index, char in enumerate(s):
#         if char in hashmap_s:
#             temp += hashmap_s[char]
#         elif t[index] in hashmap_t:
#             return False
#         else:
#             temp += t[index]
#             hashmap_s[char] = t[index]
#             hashmap_t[t[index]] = 0
#     return temp == t

# # 同构字符串优化
# def isIsomorphic(s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     if len(set(s)) != len(set(t)):
#         return False
#     hashmap = {}
#     for index, char in enumerate(s):
#         if char in hashmap:
#             if hashmap[char] != t[index]:
#                 return False
#         else:
#             hashmap[char] = t[index]
#     return True
#
# s = "ab"
# t = "aa"
# print(isIsomorphic(s, t))

# # 两个列表的最小索引总和
# def findRestaurant(list1, list2):
#     """
#     :type list1: List[str]
#     :type list2: List[str]
#     :rtype: List[str]
#     """
#     hashmap = {}
#     res = []
#     for index, value in enumerate(list1):
#         if value in list2:
#             sum = index + list2.index(value)
#             hashmap[value] = sum
#     target = min(hashmap.values())
#     for i in hashmap:
#         if hashmap[i] == target:
#             res.append(i)
#     return res

# # 两个列表的最小索引总和优化
# def findRestaurant(list1, list2):
#     """
#     :type list1: List[str]
#     :type list2: List[str]
#     :rtype: List[str]
#     """
#     hashmap = {}
#     temp = 10000
#     res = []
#     for index, value in enumerate(list1):
#         hashmap[value] = index
#     for index, value in enumerate(list2):
#         if value in hashmap:
#             count = index + hashmap[value]
#             if count == temp:
#                 res.append(value)
#             elif count < temp:
#                 temp = count
#                 res = [value]
#     return res
#
# a = ["Shogun", "KFC", "Burger King", "Tapioca Express"]
# b = ["KFC", "Shogun", "Burger King"]
# print(findRestaurant(a, b))

# # 字符串中的第一个唯一字符
# def firstUniqChar(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     hashmap = {}
#     for ch in s:
#         if ch in hashmap:
#             hashmap[ch] += 1
#         else:
#             hashmap[ch] = 1
#     for index, ch in enumerate(s):
#         if hashmap[ch] == 1:
#             return index
#     return -1
#
# s = "leetcode"
# print(firstUniqChar(s))

# # 两个数组的交集2
# def intersect(nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: List[int]
#     """
#     hashmap = {}
#     res = []
#     if len(nums1) >= len(nums2):
#         long = nums1
#         short = nums2
#     else:
#         long = nums2
#         short = nums1
#     for num in long:
#         if num in hashmap:
#             hashmap[num] += 1
#         else:
#             hashmap[num] = 1
#     for num in short:
#         if num in hashmap and hashmap[num] >= 1:
#             res.append(num)
#             hashmap[num] -= 1
#     return res

# def intersect(nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: List[int]
#     """
#     res = []
#     union = set(nums1) & set(nums2)
#     for i in union:
#         res += [i] * min(nums1.count(i), nums2.count(i))
#     return res
#
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# print(intersect(nums1, nums2))

# 存在重复元素2
def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    hashmap = {}
    for index, num in enumerate(nums):
        if num not in hashmap:
            hashmap[num] = index
        else:
            if index - hashmap[num] <= k:
                return True
            else:
                hashmap[num] = index
    return False

s = [4, 5, 6, 4]
print(containsNearbyDuplicate(s, 3))