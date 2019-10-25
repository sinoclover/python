# # 1 删除字符串中不需要的字符
# # 利用strip()方法删除开始或结尾的字符，其中lstrip()和rstrip()分别是从左和右执行
# s = ' hello world \n'
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
# t = '-----hello====='
# print(t.lstrip('-'))
# print(t.strip('-='))
# # strip()无法处理字符串中间的文本
# k = ' hello     world \n'
# print(k.strip())
# print(k.replace(' ', ''))
# import re
# print(re.sub('\s+', ' ', k))

# 2 审查清理文本字符串
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
a = s.translate(remap)
print(a)