# # excel工作簿的内省
# import sys
# from xlrd import open_workbook
#
# input_file = sys.argv[1]
# workbook = open_workbook(input_file)  # 读取和分析excel文件
# print('Number of worksheets:', workbook.nsheets)
# for worksheet in workbook.sheets():
#     print('Worksheet name:', worksheet.name, '\tRows:', worksheet.nrows, '\tColumns:', worksheet.ncols)

# # 读写Excel文件
# import sys
# from xlrd import open_workbook
# from xlwt import Workbook
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# # 建立excel文件以及工作表以便写入数据
# output_workbook = Workbook()  # 建立工作簿
# output_worksheet = output_workbook.add_sheet('jan_2013_output')  # 建立工作表
# # 打开原始数据
# with open_workbook(input_file) as workbook:
#     worksheet = workbook.sheet_by_name('january_2013')
#     for row_index in range(worksheet.nrows):
#         for column_index in range(worksheet.ncols):
#             # 根据行列索引将每个单元格的值写入输出文件
#             output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
# output_workbook.save(output_file)

# # 修改日期格式
# import sys
# from xlrd import open_workbook, xldate_as_tuple
# from xlwt import Workbook
# from datetime import date
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet('jan_2013_output')
# with open_workbook(input_file) as workbook:
#     worksheet = workbook.sheet_by_name('january_2013')
#     for row_index in range(worksheet.nrows):
#         for col_index in range(worksheet.ncols):
#             if worksheet.cell_type(row_index, col_index) == 3:
#                 # 将数值转换为元组中的代表日期的浮点数，datamode使函数确定日期的基准
#                 date_cell = xldate_as_tuple(worksheet.cell_value(row_index, col_index), workbook.datemode)
#                 date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                 output_worksheet.write(row_index, col_index, date_cell)
#             else:
#                 non_date_cell = worksheet.cell_value(row_index, col_index)
#                 output_worksheet.write(row_index, col_index, non_date_cell)
# output_workbook.save(output_file)

# 读写excel文件的pd方法
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheetname='january_2013')
writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_outout', index=False)
writer.save()