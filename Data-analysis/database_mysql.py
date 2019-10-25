# import csv
# import pymysql
# import sys
# from datetime import datetime
#
# # CSV输入文件
# # input_file = sys.argv[1]
# input_file = 'data/supplier_data.csv'
# # 连接mysql数据库
# con = pymysql.connect(host='localhost', port=3306, user='root', passwd='1205', db='data_analysis', charset='utf8')
# c = con.cursor()
#
# # 向suppliers中添加数据
# file_reader = csv.reader(open(input_file, 'r', newline=''))
# header = next(file_reader)
# for row in file_reader:
#     data = []
#     for column_index in range(len(header)):
#         if column_index < 4:
#             data.append(str(row[column_index]).lstrip('$').replace(',', '').strip())
#         else:
#             # strptime()函数根据指定的格式把一个时间字符串解析为时间元组
#             a_date = datetime.date(datetime.strptime(str(row[column_index]), '%Y/%m/%d'))
#             a_date = a_date.strftime('%Y-%m-%d')
#             data.append(a_date)
#     print(data)
#     c.execute('INSERT INTO suppliers VALUES (%s, %s, %s, %s, %s);', data)
# con.commit()
# print('\n')
#
# # 查询数据表
# c.execute('SELECT * FROM suppliers')
# rows = c.fetchall()
# for row in rows:
#     row_list_output = []
#     for column_index in range(len(row)):
#         row_list_output.append(str(row[column_index]))
#     print(row_list_output)

# # 使用pandas的数据框方法向suppliers中添加数据
# import pandas as pd
# import pymysql
# import sys
# from sqlalchemy import create_engine  # 通过sqlalchemy.create_engine建立连接
#
# # CSV输入文件
# # input_file = sys.argv[1]
# input_file = 'data/supplier_data2.csv'
#
# pymysql.install_as_MySQLdb()  # 建立MYSQL接口程序
# engine = create_engine('mysql+mysqldb://root:1205@localhost:3306/data_analysis?charset=utf8')
#
# # 获取数据
# file_reader = pd.read_csv(open(input_file), index_col=None)
# # 清洗数据
# # 在数据库中列名不能有空格
# cols = ['Supplier_Name', 'Invoice_Number', 'Part_Number', 'Cost', 'Purchase_Date']
# file_reader.columns = cols
# # 修改价格格式
# file_reader['Cost'] = file_reader['Cost'].str.lstrip('$').str.replace(',', '').astype(float)
# print(file_reader)
# pd.io.sql.to_sql(file_reader, 'suppliers2', con=engine, schema='data_analysis', if_exists='append', index=False)

# # 查询表中相关数据并写入CSV
# import csv
# import pymysql
# import sys
#
# # csv输出文件
# output_file = sys.argv[1]
# # 连接数据库
# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1205', db='data_analysis', charset='utf8')
# cur = conn.cursor()
# # 查询符合相关条件的数据
# cur.execute('select * from suppliers where Cost > 700')
# rows = cur.fetchall()
#
# # 创建写入CSV对象
# file_writer = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
# header = ['Supplier_Name', 'Invoice_Number', 'Part_Number', 'Cost', 'Purchase_Date']
# file_writer.writerow(header)
# for row in rows:
#     file_writer.writerow(row)

# 根据新的csv文件更新数据库
import csv
import pymysql

# csv输入文件
input_file = 'data/database_update.csv'
# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1205', db='data_analysis', charset='utf8')
cur = conn.cursor()

# 读取CSV文件并更新特定的行
file_reader = csv.reader(open(input_file, 'r', newline=''), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(str(row[column_index]).strip())
    print(data)
    cur.execute('update suppliers set Cost=%s, Purchase_Date=%s where Supplier_Name=%s;', data)
conn.commit()

# 查询数据表
cur.execute('select * from suppliers')
rows = cur.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
