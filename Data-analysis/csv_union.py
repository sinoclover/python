# # 文件计数与文件中的行列计数
# import csv
# import glob  # 通过glob模块定位匹配于某个特定模式的所有路径名
# import os
# import sys
#
# input_path = sys.argv[1]
# file_counter = 0
#
# for input_file in glob.glob(os.path.join(input_path, 'sales_*')):  # glob创建了输入文件的列表
#     row_counter = 1
#     with open(input_file, 'r', newline='') as csv_in_file:
#         filereader = csv.reader(csv_in_file)
#         header = next(filereader, None)
#         for row in filereader:
#             row_counter += 1
#     print('{0:s}: \t{1:d} rows \t{2:d} columns'.format(os.path.basename(input_file), row_counter, len(header)))
#     file_counter += 1
# print('Number of files: {0:d}'.format(file_counter))

# # 测试
# import csv
#
# input_file = r'F:\Coding\PYTHON\DataAnalysis\data\sales_march.csv'
#
# with open(input_file, 'r', newline='') as csv_in_file:
#     filereader = csv.reader(csv_in_file)
#     row_counter = 0
#     for row in filereader:
#         print(row)
#         row_counter += 1
#     print(row_counter)

# # 从多个文件中连接数据
# import csv
# import glob
# import os
# import sys
#
# input_path = sys.argv[1]
# output_file = sys.argv[2]
#
# first_file = True
# for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
#     print(os.path.basename(input_file)) # 打印文件的基本名
#     with open(input_file, 'r', newline='') as csv_in_file:
#         with open(output_file, 'a', newline='') as csv_out_file:  # 采用追加模式写入，防止覆盖
#             filereader = csv.reader(csv_in_file)
#             filewriter = csv.writer(csv_out_file)
#             # 将标题仅写入一次
#             if first_file:
#                 for row in filereader:
#                     filewriter.writerow(row)
#                 first_file = False
#             else:
#                 header = next(filereader, None)  # 将后续文件的第一行跳过
#                 for row in filereader:
#                     filewriter.writerow(row)

# # pandas方法从多个CSV中连接数据
# import pandas as pd
# import sys
# import os
# import glob
#
# input_path = sys.argv[1]
# output_file = sys.argv[2]
#
# all_files = glob.glob(os.path.join(input_path, 'sales_*'))
# all_data_frames = []
# for file in all_files:
#     data_frames = pd.read_csv(file, index_col=None)
#     all_data_frames.append(data_frames)
# data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True) # 通过concat函数连接数据框，axis为0时垂直连接，为1时水平连接
# data_frame_concat.to_csv(output_file, index=False)

# # 计算每个文件中值的总和与均值
# import csv
# import glob
# import os
# import sys
#
# input_path = sys.argv[1]
# output_file = sys.argv[2]
#
# output_header_list = ['file_name', 'total_sales', 'average_sales']
# csv_out_file = open(output_file, 'a', newline='')
# filewriter = csv.writer(csv_out_file)
# filewriter.writerow(output_header_list)
#
# for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
#     with open(input_file, 'r', newline='') as csv_in_file:
#         filereader = csv.reader(csv_in_file)
#         output_list = []
#         output_list.append(os.path.basename(input_file))
#         header = next(filereader)
#
#         total_sales = 0.0
#         number_of_sales = 0.0
#         for row in filereader:
#             sale_amount = row[3]
#             total_sales += float(str(sale_amount).strip('$').replace(',', ''))
#             number_of_sales += 1
#         average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
#         output_list.append(total_sales)
#         output_list.append(average_sales)
#         filewriter.writerow(output_list)
#
# csv_out_file.close()

# pandas方法计算总和与均值
import pandas as pd
import sys
import os
import glob

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []
for input_file in all_files:
    data_frame = pd.read_csv(input_file, index_col=None)
    total_cost = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in data_frame.loc[:, 'Sale Amount']]).sum()
    average_cost = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in data_frame.loc[:, 'Sale Amount']]).mean()
    data = {'file_name': os.path.basename(input_file),
            'total_sales': total_cost,
            'average_sales': average_cost}
    all_data_frames.append(pd.DataFrame(data, columns=['file_name', 'total_sales', 'average_sales']))

data_frames_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frames_concat.to_csv(output_file, index=False)