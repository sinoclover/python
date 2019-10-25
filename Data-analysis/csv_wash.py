# # 选取连续的行，清洗掉不需要的行
# import csv
# import sys
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# row_counter = 0
#
# with open(input_file, 'r', newline='') as csv_in_file:
#     with open(output_file, 'w', newline='') as csv_out_file:
#         filereader = csv.reader(csv_in_file)
#         filewriter = csv.writer(csv_out_file)
#         for row in filereader:
#             if row_counter >= 3 and row_counter <= 15:
#                 filewriter.writerow([value.strip() for value in row])
#             row_counter += 1

# # pandas方法清洗掉不需要的行
# import sys
# import pandas as pd
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# data_frame = pd.read_csv(input_file, header=None)
# data_frame = data_frame.drop([0, 1, 2, 16, 17, 18])
# data_frame.columns = data_frame.iloc[0]
# data_frame = data_frame.reindex(data_frame.index.drop(3))
# data_frame.to_csv(output_file, index=False)

# # 添加标题行
# import sys
# import csv
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# with open(input_file, 'r', newline='') as csv_in_file:
#     with open(output_file, 'w', newline='') as csv_out_file:
#         filereader = csv.reader(csv_in_file)
#         filewriter = csv.writer(csv_out_file)
#         header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
#         filewriter.writerow(header_list)
#         for row in filereader:
#             filewriter.writerow(row)

# # pandas方法添加标题行
# import sys
# import pandas as pd
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
# data_frame = pd.read_csv(input_file, header=None, names=header_list)  # 指定输入文件不包含标题行，自行提供列标题列表
# data_frame.to_csv(output_file, index=False)
