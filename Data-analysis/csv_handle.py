# # 使用python方法处理CSV
# import sys
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# with open(input_file, 'r', newline='') as filereader:
#     with open(output_file, 'w', newline='') as filewriter:
#         header = filereader.readline()
#         header = header.strip()
#         header_list = header.split(',')
#         print(header_list)
#         filewriter.write(','.join(map(str, header_list)) + '\n')
#         for row in filereader:
#             row = row.strip()
#             row_list = row.split(',')
#             print(row_list)
#             filewriter.write(','.join(map(str, row_list)) + '\n')

# # 使用pandas方法处理CSV
# import sys
# import pandas as pd
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# data_frame = pd.read_csv(input_file)
# print(data_frame)
# data_frame.to_csv(output_file)

# # 使用Python方法中的csv模块处理CSV
# import csv
# import sys
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# with open(input_file, 'r', newline='') as csv_in_file:
#     with open(output_file, 'w', newline='') as csv_out_file:
#         filereader = csv.reader(csv_in_file, delimiter=',')
#         filewriter = csv.writer(csv_out_file, delimiter=',')  # delimiter是默认分隔符
#         for row_list in filereader:
#             print(row_list)
#             filewriter.writerow(row_list)
