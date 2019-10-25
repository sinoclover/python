# # 有序数组的平方
# def sortedSquares(A):
#     """
#     :type A: List[int]
#     :rtype: List[int]
#     """
#     return sorted([i**2 for i in A])
#
# s = [-4,-1,0,3,10]
# print(sortedSquares(s))

# # 最长湍流子数组
# # 直接根据规则遍历两遍数组
# def maxTurbulenceSize(A):
#     """
#     :type A: List[int]
#     :rtype: int
#     """
#     length = 0
#     temp = 0
#     for i in range(len(A)):
#         if i == 0 or (i%2==0 and A[i-1]>A[i]) or (i%2==1 and A[i-1]<A[i]):
#             length += 1
#         else:
#             length = 1
#         temp = max(temp, length)
#     length = 0
#     for i in range(len(A)):
#         if i == 0 or (i%2==0 and A[i-1]<A[i]) or (i%2==1 and A[i-1]>A[i]):
#             length += 1
#         else:
#             length = 1
#         temp = max(temp, length)
#     return temp

# 动态规划
def maxTurbulenceSize(A):
    """
    :type A: List[int]
    :rtype: int
    """
    n = len(A)
    bigger, smaller = [1]*n, [1]*n
    for i in range(1, n):
        if A[i] > A[i-1]:
            bigger[i] = smaller[i-1] + 1
        elif A[i] < A[i-1]:
            smaller[i] = bigger[i-1] + 1
    return max(max(bigger), max(smaller))

s = [9,4,2,10,7,8,8,1,9]
print(maxTurbulenceSize(s))