# # 字母异位词分组
# def groupAnagrams(strs):
#     """
#     :type strs: List[str]
#     :rtype: List[List[str]]
#     """
#     hashtable = {}
#     res = []
#     for str in strs:
#         sort_str = ''.join(sorted(str))
#         if sort_str not in hashtable:
#             hashtable[sort_str] = [str]
#         else:
#             hashtable[sort_str].append(str)
#     for key in hashtable:
#         res.append(hashtable[key])
#     return res
#
# s = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(groupAnagrams(s))

# # 有效的数独
# def isValidSudoku(board):
#     """
#     :type board: List[List[str]]
#     :rtype: bool
#     """
#     col = {}
#     block  = {}
#     for i, list in enumerate(board):
#         # 列坐标列表
#         for j, value in enumerate(list):
#             if j not in col:
#                 col[j] = [value]
#             else:
#                 col[j].append(value)
#         # 块坐标列表
#         for j, value in enumerate(list):
#             count = int((i//3)*3+j//3)
#             if count not in block:
#                 block[count] = [value]
#             else:
#                 block[count].append(value)
#         # 判断行
#         while '.' in list:
#             list.remove('.')
#         set_list = set(list)
#         if len(list) != len(set_list):
#             return False
#     # 判断列
#     for key in col:
#         list = col[key]
#         while '.' in list:
#             list.remove('.')
#         set_list = set(list)
#         if len(list) != len(set_list):
#             return False
#     # 判断块
#     for key in block:
#         list = block[key]
#         while '.' in list:
#             list.remove('.')
#         set_list = set(list)
#         if len(list) != len(set_list):
#             return False
#     return True

# # 有效的数独优化
# def isValidSudoku(board):
#     """
#     :type board: List[List[str]]
#     :rtype: bool
#     """
#     s = set()
#     for i in range(9):
#         for j in range(9):
#             b = board[i][j]
#             k = (i//3)*3+j//3
#             if b == '.':
#                 continue
#             if (i, b, 0) in s or (j, b, 1) in s or (k, b, 2) in s:
#                 return False
#             s.add((i, b, 0))
#             s.add((j, b, 1))
#             s.add((k, b, 2))
#     return True
#
# s = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# print(isValidSudoku(s))

# # 宝石和石头
# def numJewelsInStones(J, S):
#     """
#     :type J: str
#     :type S: str
#     :rtype: int
#     """
#     res = 0
#     list_j = list(J)
#     list_s = list(S)
#     for stone in list_s:
#         if stone in list_j:
#             res += 1
#     return res
#
# J = "aA"
# S = "aAAbbbb"
# print(numJewelsInStones(J, S))

# # 无重复字符的最长子串
# # 运用双指针建立滑动窗口
# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     res = 0
#     bracket = []
#     i = j = 0
#     while i < len(s):
#         if j < len(s) and s[j] not in bracket:
#             bracket.append(s[j])
#             j += 1
#         else:
#             res = max(res, len(bracket))
#             bracket.remove(s[i])
#             i += 1
#     return res

# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     res = 0
#     bracket = []
#     for ch in s:
#         if ch in bracket:
#             index = bracket.index(ch)
#             bracket = bracket[index+1:]
#             bracket.append(ch)
#         else:
#             bracket.append(ch)
#             res = max(res, len(bracket))
#     return res
#
# s = "aabaab!bb"
# print(lengthOfLongestSubstring(s))

# # 四数相加2
# def fourSumCount(A, B, C, D):
#     """
#     :type A: List[int]
#     :type B: List[int]
#     :type C: List[int]
#     :type D: List[int]
#     :rtype: int
#     """
#     hashmap = {}
#     res = 0
#     for a in A:
#         for b in B:
#             ab = a + b
#             if ab not in hashmap:
#                 hashmap[ab] = 1
#             else:
#                 hashmap[ab] += 1
#     for c in C:
#         for d in D:
#             cd = -(c + d)
#             if cd in hashmap:
#                 res += hashmap[cd]
#     return res
#
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# print(fourSumCount(A,B,C,D))

# # 前K个高频元素
# def topKFrequent(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: List[int]
#     """
#     hashmap = {}
#     for num in nums:
#         if num not in hashmap:
#             hashmap[num] = 1
#         else:
#             hashmap[num] += 1
#     list = sorted(hashmap.items(), key=lambda x:x[1], reverse=True)[:k]
#     return [i[0] for i in list]
#
# # # 使用库函数
# # def topKFrequent(nums, k):
# #     """
# #     :type nums: List[int]
# #     :type k: int
# #     :rtype: List[int]
# #     """
# #     from collections import Counter
# #     c = Counter(nums)
# #     return [i[0] for i in c.most_common(k)]
#
# nums = [1,1,1,2,2,3,3,3,3,3]
# k = 2
# print(topKFrequent(nums, k))

# # 常数时间插入、删除和获取随机元素
# # 非常数时间
# class RandomizedSet:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.hastset = []
#
#     def insert(self, val):
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         :type val: int
#         :rtype: bool
#         """
#         if val not in self.hastset:
#             self.hastset.append(val)
#             return True
#         else:
#             return False
#
#     def remove(self, val):
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         :type val: int
#         :rtype: bool
#         """
#         if val in self.hastset:
#             self.hastset.remove(val)
#             return True
#         else:
#             return False
#
#     def getRandom(self):
#         """
#         Get a random element from the set.
#         :rtype: int
#         """
#         import random
#         return random.choice(self.hastset)

# 优化
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hastmap = {}
        self.list = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hastmap:
            self.list.append(val)
            self.hastmap[val] = len(self.list) - 1  # 即映射中的键是插入的值，值为其下标
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hastmap:
            index = self.hastmap[val]  # 将当前下标与最后一位下标互换，从而不影响字典中的其他下标
            last = self.list[-1]
            self.list[index] = last  # 用最后一位的值覆盖当前值
            self.hastmap[last] = index
            # 删除列表和字典中的值
            self.list.pop()  # 将最后一位重复值删除
            del self.hastmap[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return random.choice(self.list)