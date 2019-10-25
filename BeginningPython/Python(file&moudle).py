# # 文件问题
# # 较大的程序都要使用文件来读取输入或存储输出
# # Windows环境中的路径里反斜杠\是Python中的特殊字符，因此需要对反斜杠转义\\
# # 或在路径前加r
# import os
#
# def make_text_file():
#     a = open('text.txt', 'w')
#     a.write('This is how you create a new text file\n')
#     a.close()
#
# def make_another_file():
#     if os.path.isfile('text.txt'):
#         print('You are trying to create a file that already exists!\n')
#     else:
#         f = open('text.txt', 'w')
#         f.write('This is how you create a new text file\n')
#
# def add_some_text():
#     a = open('text.txt', 'a')
#     a.write('Here is some additional text!\n')
#
# def even_more_text():
#     a = open('text.txt', 'a')
#     a.write("""
#     here
#     is
#     more
#     text
#     """)
#
# def print_line_lengths():
#     a = open('text.txt', 'r')
#     text = a.readlines()
#     for line in text:
#         print(len(line))
#
# make_text_file()
# make_another_file()
# add_some_text()
# even_more_text()
# a = open('text.txt', 'r')
# print(a.readline())  # 使用了print打印文本，Python将换行符看作真正的换行符而不是\n
# text = a.read()
# print(text)
# print_line_lengths()

# # 路径问题
# import os
#
# def split_fully(path):
#     parent_path, name = os.path.split(path)
#     if name == "":
#         return (parent_path, )
#     else:
#         return split_fully(parent_path) + (name, )
#
# print(os.path.join('snakes', 'Python'))  # 路径组合
# print(os.path.split('c:\\Program Files\\Python36\\Lib'))  # 路径分割
# parent_path, name = os.path.split('c:\\Program Files\\Python36\\Lib')
# print(parent_path)
# print(name)
# print(split_fully('c:\\Program Files\\Python36\\Lib'))  # 路径全分割
# print(os.path.splitext('image.jpg'))
# extension = os.path.splitext('image.jpg')[1]
# print(extension)  # 提取扩展名
# print(os.path.normpath(r'C:\\Program Files\Perl\..\Python36'))
# print(os.path.abspath('other_stuff'))  # 规范化路径
# print(os.path.exists('C:\\Windows'))
# print(os.path.exists('C:\\windows\\reptiles'))  # 判断路径是否存在

# # 目录问题
# # 找出硬盘上实际存在的内容从而对路径或文件进行操作
# import os, time
#
# def print_dir(dir_path):
#     for name in os.listdir(dir_path):
#         print(os.path.join(dir_path, name))
# # 打印目录树
# def print_tree(dir_path):
#     for name in os.listdir((dir_path)):
#         full_path = os.path.join(dir_path, name)
#         print_dir(full_path)
#         if os.path.isdir(full_path):
#             print_tree(full_path)
#
# print(os.listdir("C:\\"))  # listdir返回一个列表
# print(os.listdir("."))  # 使用"."来列出当前目录列表
# print_dir('C:\\Users\\Administrator\\Desktop')  # 打印目录中内容的完整路径
# print(os.path.isfile('C:\\Windows'))
# print(os.path.isdir('C:\\Windows'))  # 判断一个路径是指向一个文件还是一个目录
#
# mod_time = os.path.getmtime('C:\\Windows')
# print(time.ctime(mod_time))  # 输出某个目录上次被修改的时间

# # 文件操作
# import os, shutil
#
# f = open('test.txt', 'w')
# f.write('Hacker!')
# f.close()
# shutil.copy('test.txt', 'test_copy.txt')  # 文件复制并能够重命名
# shutil.copy('test.txt', 'C:\\Users\\Administrator\\Desktop')  # 文件复制并移动位置
# os.remove('C:\\Users\\Administrator\\Desktop\\test.txt')  # 文件删除
# shutil.move('test.txt', 'test_new.txt')  # 文件重命名
# shutil.move('test_new.txt', 'C:\\Users\\Administrator\\Desktop')  # 文件移动
# os.remove('C:\\Users\\Administrator\\Desktop\\test_new.txt')

# # 轮换文件
# import os
# import shutil
#
# def make_version_path(path, version):
#     if version == 0:
#         # No suffix for version 0, the current version.
#         return path
#     else:
#         # Append a suffix to indicate the older version.
#         return path + "." + str(version)
#
# def rotate(path, version = 0):
#     # Construt the name of the version we're rotating.
#     old_path = make_version_path(path, version)
#     if not os.path.exists(old_path):
#         # it does not exist, so complain.
#         raise IOError("'%s' does not exist" % path)
#     # Construct the new version name for this file.
#     new_path = make_version_path(path, version + 1)
#     # Is there already a version with this name?
#     if os.path.exists(new_path):
#         # Yes. Rotate it out of the way first!
#         rotate(path, version + 1)
#     # Now we can rename the version safely.
#     shutil.move(old_path, new_path)
#
# def rotae_log_file(path):
#     if not os.path.exists(path):
#         # The file is missing, so create it.
#         new_file = open(path, 'w')
#         # Close the new file immediately, which leaves it empty.
#         del new_file
#     # Now rotate it.
#     rotate(path)

# # 目录操作
# import os
#
# # mkdir创建的目录的父目录要先存在，而makedirs则可以创建不存在的父目录
# # os.makedirs('C:\\Users\\Administrator\\Desktop\\test_file')
# os.rmdir('C:\\Users\\Administrator\\Desktop\\test_file')
# #shutil.rmtree()函数会删除一整组文件

# 通配globbing，用来表示在文件名称模式中展开通配符
# 通配和大小写区分
import glob

print(glob.glob('C:\\Program Files\\M*'))
# 通配语法与正则表达式类似但不相同
# glob比os.listdir强大，因为可以在目录或子目录名称中指定通配符。






