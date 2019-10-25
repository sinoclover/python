# # 工作表计数以及每个工作表中的行列计数
# import glob
# import os
# import sys
# from xlrd import open_workbook
#
# input_path = sys.argv[1]  # 路径必须为双引号
# workbook_counter = 0
#
# for input_file in glob.glob(os.path.join(input_path, '*.xls*')):
#     workbook = open_workbook(input_file)
#     print('Workbook: {:s}'.format(os.path.basename(input_file)))
#     print('Number of worksheets: {:d}'.format(workbook.nsheets))
#     for worksheet in workbook.sheets():
#         print('Worksheet name:', worksheet.name, '\tRows:', worksheet.nrows, '\tColumns:', worksheet.ncols)
#     workbook_counter += 1
# print('Number of Excel workbooks: {:d}'.format(workbook_counter))

# # 从多个工作簿中链接数据
# import glob
# import os
# import sys
# from xlrd import open_workbook, xldate_as_tuple
# from xlwt import Workbook
# from datetime import date
#
# input_folder = sys.argv[1]
# output_file = sys.argv[2]
# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet('all_data_all_workbooks')
#
# data = []
# first_worksheet = True
# for input_file in glob.glob(os.path.join(input_folder, '*.xls*')):
#     print(os.path.basename(input_file))
#     with open_workbook(input_file) as workbook:
#         for worksheet in workbook.sheets():
#             if first_worksheet:
#                 header_row = worksheet.row_values(0)
#                 data.append(header_row)
#                 first_worksheet = False
#             for row_index in range(1, worksheet.nrows):
#                 row_list = []
#                 for column_index in range(worksheet.ncols):
#                     cell_value = worksheet.cell_value(row_index, column_index)
#                     cell_type = worksheet.cell_type(row_index, column_index)
#                     if cell_type == 3:
#                         date_cell = xldate_as_tuple(cell_value, workbook.datemode)
#                         date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                         row_list.append(date_cell)
#                     else:
#                         row_list.append(cell_value)
#                 if row_list:
#                     data.append(row_list)
# for list_index, output_list in enumerate(data):
#     for element_index, element in enumerate(output_list):
#         output_worksheet.write(list_index, element_index, element)
# output_workbook.save(output_file)

# # 从多个工作簿中链接数据的PD方法
# import glob
# import os
# import sys
# import pandas as pd
#
# input_path = sys.argv[1]
# output_file = sys.argv[2]
# all_workbooks = glob.glob(os.path.join(input_path, '*.xls*'))  # 生成文件路径的列表
# data_frames = []
# print(all_workbooks)
#
# for workbook in all_workbooks:
#     all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
#     for worksheet_name, data in all_worksheets.items():
#         data_frames.append(data)
# all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)
# writer = pd.ExcelWriter(output_file)
# all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)
# writer.save()

# # 为每个工作簿和工作表计算总数和均值
# import glob
# import sys
# import os
# from xlrd import open_workbook
# from xlwt import Workbook
#
# input_folder = sys.argv[1]
# output_file = sys.argv[2]
# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet('sums_and_averages')
#
# all_data = []
# sales_column_index = 3
# header = ['workbook', 'worksheet', 'worksheet_total', 'worksheet_average', 'workbook_total', 'workbook_average']
# all_data.append(header)
#
# for input_file in glob.glob(os.path.join(input_folder, '*.xls*')):
#     # 每次打开一个工作簿进行重置
#     with open_workbook(input_file) as workbook:
#         list_of_totals = []
#         list_of_numbers = []
#         workbook_output = []
#         # 处理工作簿中的所有单个工作表
#         for worksheet in workbook.sheets():
#             total_sales = 0
#             number_of_sales = 0
#             worksheet_list = [os.path.basename(input_file), worksheet.name]
#             for row_index in range(1, worksheet.nrows):
#                 try:
#                     total_sales += float(str(worksheet.cell_value(row_index, sales_column_index)).strip('$').replace(',', ''))
#                     number_of_sales += 1.
#                 except:
#                     total_sales += 0.
#                     number_of_sales += 0.
#             average_sales = '{:.2f}'.format(total_sales / number_of_sales)  # 计算单个工作表中的平均值
#             worksheet_list.append(total_sales)
#             worksheet_list.append(float(average_sales))  # 将数据添加到工作表信息的列表中
#             workbook_output.append(worksheet_list)  # 将单个工作表的信息添加到输出文件列表中
#             list_of_totals.append(total_sales)
#             list_of_numbers.append(float(number_of_sales))
#         # 将该工作簿的数据进行计算
#         workbook_total = sum(list_of_totals)
#         workbook_average = sum(list_of_totals) / sum(list_of_numbers)
#         # 将所有输出文件列表中的数据都添加上工作簿的总体数据信息
#         for list_element in workbook_output:
#             list_element.append(workbook_total)
#             list_element.append(workbook_average)
#         # 扩展而非追加
#         all_data.extend(workbook_output)
# for list_index, output_list in enumerate(all_data):
#     for element_index, element in enumerate(output_list):
#         output_worksheet.write(list_index, element_index, element)
# output_workbook.save(output_file)

# 为每个工作簿和工作表计算总数和均值的PD方法



