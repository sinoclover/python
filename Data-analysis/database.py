# # 创建SQLite3内存的数据库
# import sqlite3
#
# # 创建带有4个属性的sales表
# con = sqlite3.connect(':memory:')  # 使用内存创建数据库
# query = 'CREATE TABLE sales (customer VARCHAR(20), product VARCHAR(40), amount FLOAT, date DATE);'  # 定义数据表
# con.execute(query)  # 执行创建数据表
# con.commit()  # 将修改提交保存到数据库
#
# # 在表中插入数据
# data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
#         ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
#         ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
#         ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]
# statement = 'INSERT INTO sales VALUES(?, ?, ?, ?)'  # ?作为占位符，表示在命令中使用的值
# con.executemany(statement, data)  # 多次执行SQL命令
# con.commit()
#
# # 查询sales表
# cursor = con.execute('SELECT * FROM sales')
# rows = cursor.fetchall()  # 使光标对象返回SQL选择命令的所有行
#
# # 计算查询结果中的行的数量
# row_counter = 0
# for row in rows:
#     print(row)
#     row_counter += 1
# print('Number of rows: {:d}'.format(row_counter))

# # 向表中插入记录
# import csv
# import sqlite3
# import sys
#
# # CSV输入文件的路径和文件名
# input_file = sys.argv[1]
#
# # 创建内存数据库
# # 创建带有5个属性的Suppliers.db
# con = sqlite3.connect('Suppliers.db')
# create_table = 'CREATE TABLE IF NOT EXISTS Suppliers (Supplier_Name VARCHAR(20), ' \
#                'Invoice_Number VARCHAR(20), Part_Number VARCHAR(20), Cost FLOAT, Purchase_Date DATE);'
# con.execute(create_table)
# con.commit()
#
# # 读取CSV文件
# # 向数据表中插入数据
# c = con.cursor()
# file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
# header = next(file_reader, None)  # 去掉index行
# for row in file_reader:
#     data = []
#     for column_index in range(len(header)):
#         data.append(row[column_index])
#     print(data)
#     c.execute('INSERT INTO Suppliers VALUES (?, ?, ?, ?, ?);', data)
# con.commit()
#
# # 查询Suppliers表
# output = c.execute('SELECT * FROM Suppliers')
# rows = output.fetchall()
# for row in rows:
#     output = []
#     for column_index in range(len(row)):
#         output.append(str(row[column_index]))
#     print(output)

# 更新表中记录
import csv
import sqlite3
import sys

# csv输入文件的路径和文件名
input_file = sys.argv[1]

# 创建内存数据库
# 创建带有4个属性的sales表

con = sqlite3.connect(':memory:')
query = '''CREATE TABLE IF NOT EXISTS sales
            (customer VARCHAR(20), 
            product VARCHAR(20), 
            amount FLOAT, 
            date DATE);'''
con.execute(query)
con.commit()

# 向表中插入数据
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
        ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
        ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
        ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]
for tu in data:
    print(tu)
statement = 'INSERT INTO sales VALUES(?, ?, ?, ?)'
con.executemany(statement, data)
con.commit()

# 读取CSV文件并更新特定的行
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    con.execute('UPDATE sales SET amount=?, date=? WHERE customer=?;', data)
con.commit()

# 查询sales表
cursor = con.execute('SELECT * FROM sales')
rows = cursor.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)