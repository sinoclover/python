# # 设计哈希集合
# class MyHashSet(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.hashset = []
#
#     def add(self, key):
#         """
#         :type key: int
#         :rtype: void
#         """
#         if self.contains(key):
#             return
#         else:
#             self.hashset.append(key)
#
#     def remove(self, key):
#         """
#         :type key: int
#         :rtype: void
#         """
#         if self.contains(key):
#             self.hashset.remove(key)
#         else:
#             return
#
#     def contains(self, key):
#         """
#         Returns true if this set contains the specified element
#         :type key: int
#         :rtype: bool
#         """
#         if key in self.hashset:
#             return True
#         else:
#             return False

# # 设计哈希集合优化
# class MyHashSet(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.hashset = set()
#
#     def add(self, key):
#         """
#         :type key: int
#         :rtype: void
#         """
#         self.hashset.add(key)
#
#     def remove(self, key):
#         """
#         :type key: int
#         :rtype: void
#         """
#         if self.contains(key):
#             self.hashset.remove(key)
#
#     def contains(self, key):
#         """
#         Returns true if this set contains the specified element
#         :type key: int
#         :rtype: bool
#         """
#         return key in self.hashset

# # 设计哈希映射
# class MyHashMap(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.hashmap = {}
#
#     def put(self, key, value):
#         """
#         value will always be non-negative.
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         self.hashmap[key] = value
#
#     def get(self, key):
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         :type key: int
#         :rtype: int
#         """
#         if key in self.hashmap:
#             return self.hashmap[key]
#         else:
#             return -1
#
#     def remove(self, key):
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         :type key: int
#         :rtype: void
#         """
#         if key in self.hashmap:
#             del self.hashmap[key]
#
# h = MyHashMap()
# h.put(1, 1)
# h.put(2, 2)
# h.get(1)
