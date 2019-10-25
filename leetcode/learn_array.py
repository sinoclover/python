# 寻找数组的中心索引
# 112ms
# 通过一次遍历，分别计算左右两侧的大小进行对比
# def pivotIndex(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     sum_left = 0
#     sum_right = sum(nums)
#     if nums:
#         for i in range(len(nums)):
#             sum_right -= nums[i]
#             if sum_left  == sum_right:
#                 return i
#             else:
#                 sum_left += nums[i]
#     else:
#         return -1
#     return -1

# 直接计算左侧累加和，判断条件为左侧的两倍加上中间元素
# def pivotIndex(nums):
#     """
#     :type nums: List[int]
#     rtype: int
#     """
#     count = 0
#     sum_all = sum(nums)
#     for index, value in enumerate(nums):
#         if 2 * count + value == sum_all:
#             return index
#         count += value
#     return -1
#
# s = [1, 7, 3, 6, 5, 6]
# print(pivotIndex(s))

# 至少是其他数字两倍的最大数
# 在遍历时用continue跳过自身
# def dominantIndex(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     max_value = max(nums)
#     max_index = nums.index(max_value)
#     for i in range(len(nums)):
#         if i == max_index:
#             continue
#         elif max_value < 2 * nums[i]:
#             return -1
#     return max_index

# # 直接在nums中remove最大值即可
# def dominantIndex(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     max_value = max(nums)
#     max_index = nums.index(max_value)
#     nums.remove(max_value)
#     for i in range(len(nums)):
#         if max_value < 2 * nums[i]:
#             return -1
#     return max_index
#
# s = [0, 0, 0, 4]
# print(dominantIndex(s))

# # 加一
# # 通过数学计算先将列表中的数字整合为一个数再加一
# # 再通过取余和整除循环获取加一后的数字添加进一个列表，最后对列表反向即可
# def plusOne(digits):
#     """
#     :type digits: List[int]
#     :rtype: List[int]
#     """
#     num = 0
#     output_digits = []
#     for i in range(len(digits)):
#         num = num * 10 + digits[i]
#     num += 1
#     while num > 0:
#         digit = num % 10
#         output_digits.append(digit)
#         num = num // 10
#     return output_digits[::-1]
#
# s = [1, 2, 3]
# print(plusOne(s))

# # 对角线遍历
# # 超出时间限制，应该是对下标的遍历时间过长
# def findDiagonalOrder(matrix):
#     """
#     :type matrix: List[List[int]]
#     :rtype: List[int]
#     """
#     li = len(matrix)
#     if li == 0:
#         return matrix
#     lj = len(matrix[0])
#     output_list = []
#     for floor in range(li+lj-1):
#         for i in range(floor+1):
#             j = floor - i
#             if floor % 2 == 0:
#                 if i < lj and j < li:
#                     output_list.append(matrix[j][i])
#             else:
#                 if i < li and j < lj:
#                     output_list.append(matrix[i][j])
#     return output_list

# def findDiagonalOrder(matrix):
#     """
#     :type matrix: List[List[int]]
#     :rtype: List[int]
#     """
#     if matrix:
#         row = len(matrix)
#         col = len(matrix[0])
#         lens = row * col
#         res = []
#         r = c = 0
#         for i in range(lens):
#             res.append(matrix[r][c])
#             floor = r + c
#             if floor % 2 == 0:  # 偶数层
#                 if r == 0 and c != col - 1:
#                     c += 1
#                 elif c == col - 1:
#                     r += 1
#                 else:
#                     c += 1
#                     r -= 1
#             else:  # 奇数层
#                 if c == 0 and r != row - 1:
#                     r += 1
#                 elif r == row - 1:
#                     c += 1
#                 else:
#                     c -= 1
#                     r += 1
#     else:
#         return matrix
#     return res

# s = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ]
# ]
# s1 = []
# print(findDiagonalOrder(s))

# # 螺旋矩阵
# def findDiagonalOrder(matrix):
#     """
#     :type matrix: List[List[int]]
#     :rtype: List[int]
#     """
#     if matrix:
#         row = len(matrix)
#         col = len(matrix[0])
#         lens = row * col
#         res = []
#         r = c = 0
#         vecr = 0
#         vecc = 1
#         for i in range(lens):
#             res.append(matrix[r][c])
#             matrix[r][c] = 'x'
#             if matrix[(r + vecr) % row][(c + vecc) % col] == 'x':
#                 vecr, vecc = vecc, -vecr
#             r += vecr
#             c += vecc
#     else:
#         return matrix
#     return res
#
# s = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ],
# ]
# s1 = []
# print(findDiagonalOrder(s))

# 杨辉三角
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    temp = []
    res = [[1]]
    if numRows == 0:
        return temp
    elif numRows == 1:
        return res
    else:
        for row in range(2, numRows+1):
            temp.append(1)
            for i in range(len(res[-1]) - 1):
                num = res[-1][i] + res[-1][i+1]
                temp.append(num)
            temp.append(1)
            res.append(temp)
            temp = []
        return res

print(generate(5))
