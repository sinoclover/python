# # 打开和读文件
# my_file = open('notes.txt', 'r')
# lines = my_file.readlines()  # 读取多行
# print(lines)
# my_file.close()

# # 多次使用读取一行
# my_file = open('notes.txt', 'r')
# first_line = my_file.readline()
# second_line = my_file.readline()
# print(first_line, end = '')  # 自带换行符
# print(second_line, end = '')  # 自带换行符
# my_file.seek(0)  # readline函数回到起始位置
# first_line_again = my_file.readline()
# print(first_line_again, end = '')
# my_file.close()

# # 追加到文件
# todo_list = open('notes.txt', 'a')
# todo_list.write('\nSpend allowance')
# todo_list.close()

# # 新文件的写入
# new_file = open('my_new_notes.txt', 'w')
# new_file.write('Eat supper\n')
# new_file.write('Play soccer\n')
# new_file.write('Go to bed')
# new_file.close()

# # 对现有文件的写入
# the_file = open('notes.txt', 'w')
# the_file.write('Wake up\n')
# the_file.write('Watch cartoons')
# the_file.close()

# # 使用print重定向写入
# my_file = open('new_file.txt', 'w')
# print('Hello there, neighbor!', file = my_file) # 重定向
# my_file.close()

# # 使用pickle封装
# import pickle
# my_list = ['Fred', 73, 'Hello there', 81.987e-13]
# pickle_file = open('my_pickled_list.pkl', 'wb')  # 写入二进制模式
# pickle.dump(my_list, pickle_file)
# pickle_file.close()

# # 使用pickle还原
# import pickle
# pickle_file = open('my_pickled_list.pkl', 'rb')
# recover_list = pickle.load(pickle_file)
# pickle_file.close()
# print(recover_list)

# # 滑稽句子
# import random
# wordlist = open('wordlist.txt', 'r')
# adj_list = wordlist.readline().strip().split(',')  # strip函数从行中删除换行符
# n_list = wordlist.readline().strip().split(',')
# v_list = wordlist.readline().strip().split(',')
# adv_list = wordlist.readline().strip().split(',')
# wordlist.close()
# adj = random.choice(adj_list)
# n = random.choice(n_list)
# v = random.choice(v_list)
# adv = random.choice(adv_list)
# print('The', adj, n, v, adv, end='.')

# # 用户信息
# user_info = open('info.txt', 'w')
# user_info.write(input('What is your name?\n') + '\n')
# user_info.write(input('How old are you?\n') + '\n')
# user_info.write(input('What is your favorite color?\n') + '\n')
# user_info.write(input('What is your favorite food?\n') + '\n')
# user_info.close()

# #pickle封装用户信息
# import pickle
#
# name = input('What is your name?\n')
# age = input('How old are you?\n')
# color = input('What is your favorite color?\n')
# food = input('What is your favorite food?\n')
# info_list = [name, age, color, food]
# pickle_file = open('user_info_list.pkl', 'wb')
# pickle.dump(info_list, pickle_file)
# pickle_file.close()

# # pickle调用用户信息
# import pickle
#
# pickle_file = open('user_info_list.pkl', 'rb')
# user_info = pickle.load(pickle_file)
# print(user_info)
