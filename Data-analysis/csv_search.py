# # 行中的值满足某个条件
# import csv
# import sys
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# with open(input_file, 'r', newline='') as csv_in_file:
#     with open(output_file, 'w', newline='') as csv_out_file:
#         filereader = csv.reader(csv_in_file)
#         filewriter = csv.writer(csv_out_file)
#         header = next(filereader)  # next函数读取输入文件的第一行
#         filewriter.writerow(header)
#         for row_list in filereader:
#             supplier = str(row_list[0]).strip()
#             cost = str(row_list[3]).strip('$').replace(',', '')
#             if supplier == 'Supplier Z' or float(cost) > 600.0:
#                 filewriter.writerow(row_list)

# # 使用pandas处理行中的值
# import sys
# import pandas as pd
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# data_frame = pd.read_csv(input_file)
# cost_list = data_frame['Cost'].str.strip('$').astype(float)  # astype实现变量类型转换
# name_list = data_frame['Supplier Name']
#
# condition_pattern = data_frame.loc[(name_list.str.contains('Z')) | (cost_list > 600.0), :]
# condition_pattern.to_csv(output_file)

# # 行中的值属于某个集合
# import sys
# import csv
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# important_dates = ['2014/1/20', '2014/1/30']
# with open(input_file, 'r', newline='') as csv_in_file:
#     with open(output_file, 'w', newline='') as csv_out_file:
#         filereader = csv.reader(csv_in_file)
#         filewriter = csv.writer(csv_out_file)
#         header = next(filereader)
#         filewriter.writerow(header)
#         for row_list in filereader:
#             a_date = row_list[4]
#             if a_date in important_dates:
#                 filewriter.writerow(row_list)

# # 使用pandas方法搜索属于某个集合的值
# import sys
# import pandas as pd
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# important_date = ['2014/1/20', '2014/1/30']
# data_frame = pd.read_csv(input_file)
# date_pattern = data_frame.loc[data_frame['Purchase Date'].isin(important_date), :]  # isin()
# date_pattern.to_csv(output_file)

# # 行中的值匹配某个模式
# import csv
# import re
# import sys
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# re_pattern = re.compile(r'^001-.*', re.I)  # re.I进行大小写敏感的匹配
#
# with open(input_file, 'r', newline='') as csv_in_file:
#     with open(output_file, 'w', newline='') as csv_out_file:
#         filereader = csv.reader(csv_in_file)
#         filewriter = csv.writer(csv_out_file)
#         header = next(filereader)
#         filewriter.writerow(header)
#         for row_list in filereader:
#             invoice_number = row_list[1]
#             if re_pattern.search(invoice_number):
#                 filewriter.writerow(row_list)

# # 使用pandas方法匹配某个模式
# import sys
# import pandas as pd
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# data_frame = pd.read_csv(input_file)
# match_pattern = data_frame.loc[data_frame['Invoice Number'].str.startswith('001-'), :]
# match_pattern.to_csv(output_file)

# # 使用列值索引
# import csv
# import sys
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# my_columns = [0, 3]
# with open(input_file, 'r', newline='') as csv_in_file:
#     with open(output_file, 'w', newline='') as csv_out_file:
#         filereader = csv.reader(csv_in_file)
#         filewriter = csv.writer(csv_out_file)
#         for row_list in filereader:
#             row_list_output = []
#             for index_value in my_columns:
#                 row_list_output.append(row_list[index_value])
#             filewriter.writerow(row_list_output)

# # 使用列值索引的pandas方法
# import pandas as pd
# import sys
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# data_frame = pd.read_csv(input_file)
# data_frame_columns = data_frame.iloc[:, [0,3]]  # iloc函数根据索引位置选取列,注意与loc的区别
# data_frame_columns.to_csv(output_file)

# # 使用列标题索引
# import csv
# import sys
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# my_columns = ['Invoice Number', 'Purchase Date']
# my_columns_index = []
#
# with open(input_file, 'r', newline='') as csv_in_file:
#     with open(output_file, 'w', newline='') as csv_out_file:
#         filereader = csv.reader(csv_in_file)
#         filewriter = csv.writer(csv_out_file)
#         header = next(filereader, None)
#         for index_value in range(len(header)):
#             if header[index_value] in my_columns:
#                 my_columns_index.append(index_value)
#         filewriter.writerow(my_columns)
#         for row_list in filereader:
#             row_list_output = []
#             for index_value in my_columns_index:
#                 row_list_output.append(row_list[index_value])
#             filewriter.writerow(row_list_output)

# 使用列标题索引的pandas方法
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]
data_frame_name.to_csv(output_file)