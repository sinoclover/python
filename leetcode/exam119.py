# 最接近原点的K个点
# def kClosest(points, K):
#     """
#     :type points: List[List[int]]
#     :type K: int
#     :rtype: List[List[int]]
#     """
#     if points:
#         import math
#         res = []
#         distance = []
#         for i in range(len(points)):
#             d = math.sqrt(points[i][0]**2 + points[i][1]**2)
#             distance.append(d)
#         print(distance)
#         for j in range(K):
#             min_distance = min(distance)
#             min_index = distance.index(min_distance)
#             res.append(points[min_index])
#             distance[min_index] = 10000
#             print(distance)
#         return res
#     else:
#         return points

# def kClosest(points, K):
#     """
#     :type points: List[List[int]]
#     :type K: int
#     :rtype: List[List[int]]
#     """
#     if points:
#         import math
#         res = []
#         distance = {}
#         for i in range(len(points)):
#             d = math.sqrt(points[i][0]**2 + points[i][1]**2)
#             distance[d] = i
#         for j in range(K):
#             min_distance = min(distance)
#             res.append(points[distance[min_distance]])
#             distance.pop(min_distance)
#         return res
#     else:
#         return points
#
# points = [[3,3],[5,-1],[-2,4]]
# K = 2
# print(kClosest(points, K))

# # 三角形最大周长
# # 超出时长
# def largestPerimeter(A):
#     """
#     :type A: List[int]
#     :rtype: int
#     """
#     stack = []
#     for i in range(len(A)):
#         a = A[i]
#         for j in range(i + 1, len(A)):
#             b = A[j]
#             for k in range(j + 1, len(A)):
#                 c = A[k]
#                 if a + b > c and a + c > b and b + c > a:
#                     d = a + b + c
#                     stack.append(d)
#     if stack:
#         return max(stack)
#     else:
#         return 0

# 考虑的重心错误，一直考虑的是对边长进行遍历，而应该放在最大的边长上
# 即只判断最长的和其余两个即可
def largestPerimeter(A):
    """
    :type A: List[int]
    :rtype: int
    """
    A = sorted(A, reverse=True)  # 先对边长进行有小到大的排序
    print(A)
    for i in range(len(A) - 2):
        if A[i] < A[i+1] + A[i+2]:
            return A[i]+A[i+1]+A[i+2]
    return 0

s = [3,2,3,4]
print(largestPerimeter(s))

