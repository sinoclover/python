# # 嵌套循环
# for mutiplier in range (5, 8):
#     for i in range (1, 10):
#         print(i, 'x', mutiplier, '=', i * mutiplier)
#     print()

# # 可变循环
# numStars = int(input('How many stars do you want? '))
# for i in range (0, numStars):
#     print('*', end = ' ')

# # 3重深度可变循环
# numBlocks =  int(input('How many blocks of stars do you want? '))
# numLines = int(input('How many lines in each block? '))
# numStars = int(input('How many stars per line? '))
# for block in range(0, numBlocks):
#     for line in range(0, numLines):
#         for star in range(0, numStars):
#             print('*', end = ' ')
#         print()
#     print()

# # 热狗组合
# print('\t\t Dog\t Bun\t Ketchup Mustard Onions')
# count = 1
# for dog in [0, 1]:
#     for bun in [0, 1]:
#         for ketchup in [0, 1]:
#             for mustard in [0, 1]:
#                 for onions in [0, 1]:
#                     print('#', count, '\t', dog, '\t\t', bun, '\t\t', ketchup, '\t\t', mustard, '\t\t', onions)
#                     count += 1

# # 卡路里计算
# dog_cal = 140
# bun_cal = 120
# ket_cal = 80
# mus_cal = 20
# onion_cal = 40
#
# print('\t\t Dog\t Bun\t Ketchup Mustard Onions  Calories')
# count = 1
# for dog in [0, 1]:
#     for bun in [0, 1]:
#         for ketchup in [0, 1]:
#             for mustard in [0, 1]:
#                 for onions in [0, 1]:
#                     total_cal = dog * dog_cal + bun * bun_cal + \
#                         ketchup * ket_cal + mustard * mus_cal + \
#                         onions * onion_cal
#                     print('#', count, '\t', dog, '\t\t', bun, '\t\t', ketchup, '\t\t',
#                           mustard, '\t\t', onions, '\t\t', total_cal)
#                     count += 1

# # 可变计时器
# import time
# total = int(input('How many seconds? '))
# for i in range(total, 0, -1):
#     print(i)
#     time.sleep(1)
# print('BLAST OFF!')

# # 可变计时器2
# import time
# total = int(input('How many seconds? '))
# for i in range(total, 0, -1):
#     print(i, end = ' ')
#     for star in range(i):
#         print('*', end = ' ')
#     print()
#     time.sleep(1)
# print('BLAST OFF!')

# # 名字列表1
# names = []
# print('Enter 5 names: ')
# for i in range(5):
#     name = input()
#     names.append(name)
# print('The names is', names)

# # 名字列表2
# names = []
# print('Enter 5 names: ')
# for i in range(5):
#     name = input()
#     names.append(name)
# names = sorted(names)  # names.sort()
# print('The names is', *names)  # 使用星号获得列表参数

# # 名字列表3
# names = []
# print('Enter 5 names: ')
# for i in range(5):
#     name = input()
#     names.append(name)
# print('The 3rd names is', names[2])

# # 名字列表4
# names = []
# print('Enter 5 names: ')
# for i in range(5):
#     name = input()
#     names.append(name)
# print('The names is', *names)  # 使用星号获得列表参数
# number = int(input('Replace one name. Which one? (1-5): '))
# new_name = input('New name: ')
# del names[number - 1]
# names.insert(number - 1, new_name)
# print('The name is', *names)

