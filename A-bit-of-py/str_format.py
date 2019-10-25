age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

#对于浮点数‘0.333’保留小数点后三位
print('{0:.3f}'.format(1.0/3))
print('{:0.3f}'.format(1.0/3))

#使用下划线填充文本，并保持文字处于中间位置
#使用(^)定义‘_hello_’字符串长度为11
print('{0:_^11}'.format('hello'))
print('{:_^11}'.format('hello'))

#基于关键词输出‘Swaroop wrote A byte of Python’
print('{name} wrote {book}'.format(name = 'Swaroop', book = 'A byte of Python'))

#指定空白结尾
print('a', end='')
print('b')

print('a', end=' ')
print('b', end=' ')
print('c')

#转义序列
print('what\'s your name')
print('This is the first line. \nThis is the second line.')
print('This is the first line.\
 This is the second line. ')

print('This is the first line. This is the second line')
print('This is the first line.'
      ' This is the second line.')
print('''This is the first line.
This is the second line.''')
#原始字符串
print(r'Newlines are indicated by \n')
