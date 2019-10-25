# # for循环1
# for looper in [1, 2, 3, 4, 5]:
#     print('hello')

# # for循环2
# for looper in [1, 2, 3, 4, 5]:
#     print(looper, 'time 8 =', looper * 8)

# # for循环3
# for looper in range(1, 11):
#     print(looper, 'time 8 =', looper * 8)

# # 倒计时
# import time
# for i in range (10, 0, -1):
#     print(i)
#     time.sleep(1)
# print('BLAST OFF!')

# # while循环
# print('Type 3 to continue, anything else to quit.')
# someInput = input()
# while someInput == '3':
#     print('Thank you for the 3. Very kind of you.')
#     print('Type 3 to continue, anything else to quit.')
#     someInput = input()
# print('That is not 3, so I am quitting now.')

# # continue
# for i in range (1, 6):
#     print()
#     print('i =', i, end = ' ')
#     print('Hello, how', end = ' ')
#     if i == 3:
#         continue
#     print('are you today.')

# # 乘法表1
# print('Which multiplication table would you like? ')
# number = int(input())
# print('Here is your table: ')
# for i in range (1, 11):
#     print(number, 'x',i,'=', number * i)

# # 乘法表2
# print('Which multiplication table would you like? ')
# number = int(input())
# i = 1
# while i < 11:
#     print(number, 'x', i, '=', number * i)
#     i += 1

# # 乘法表3
# print('Which multiplication table would you like? ')
# number = int(input())
# print('How high do you want to go?')
# high = int(input())
# print('Here is your table: ')
# for i in range(1, high + 1):
#     print(number, 'x', i, '=', number * i)

