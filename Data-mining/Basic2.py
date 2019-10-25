# # 工作目录的改变
# import os
# pwd = os.getcwd()
# os.chdir('F:/pic')  # 改变路径至F:\pic，注意命令中不是反斜杠
# print(os.getcwd())
# os.chdir(pwd)
# print(os.getcwd())
# # 文件读写
# data = []
# with open('data/ticdata.txt') as f:
#     for line in f.readlines():
#         line = line.strip()  # 去掉换行符
#         data_line = line.split('\t')  # 根据分隔符分割数据
#         data.append(data_line)
#     print(data[0])

# # 使用JSON处理数据，json通过序列化接受python的数据结构，并将其转换为字符串表示形式。
# # 通过反序列化将字符串表示形式重新构建数据结构
# # 即序列化和反序列化使用dumps()和loads()
# import json
# x = dict(height=176, weight=60)
# print(x)  # 字典原始内容
# y = json.dumps(x)  # 序列化返回字符串
# print(y)  # 序列化的字典
# z = json.loads(y)
# print(z)  # 反序列化
# # 使用dump()和load()存储和加载
# with open('data/bigdata.json', 'w') as f1:
#     json.dump(x, f1)
# with open('data/bigdata.json', 'r') as f2:
#     print(json.load(f2))

# # 实验1冒泡排序
# sList = [5, 6, 3, 4, 8, 1, 9, 0, 2]
# list = sorted(sList, reverse=False)  # 通过sorted方法排序
# print(list)
# def bubble_sort(nums):
#     for i in range(len(nums)-1):
#         for j in range(len(nums)-1-i):
#             if(nums[j] > nums[j+1]):
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums
# print(bubble_sort(sList))

# # 实验2 节假日字典
# import json
# with open('data/holiday.json') as f:
#     holiday = json.load(f)
# print(holiday)

# 实验3 数据读取
data = []
dataArr = []
labelArr = []
with open('data/horseColic.txt') as f:
    for line in f.readlines():
        line = line.strip()
        line = line.replace('\t', ' ')
        data_line = line.split(' ')
        data.append(data_line)
        dataArr.append(data_line[0:len(data_line)-1])
        label = data_line[len(data_line)-1]
        labelArr.append(label)
print(labelArr)
print(dataArr)
