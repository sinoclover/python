# # 读取工作簿中的所有工作表
# # 在所有工作表中筛选特定行
# import sys
# from datetime import date
# from xlrd import open_workbook, xldate_as_tuple
# from xlwt import Workbook
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet('filtered_rows_all_worksheets')
#
# sales_column_index = 3
# threshold = 2000.0
# first_worksheet = True
# with open_workbook(input_file) as workbook:
#     data = []
#     for worksheet in workbook.sheets():
#         # 如果是第一个工作表，则将抬头标题存储下来
#         if first_worksheet:
#             header_row = worksheet.row_values(0)
#             data.append(header_row)
#             first_worksheet = False
#         for row_index in range(1, worksheet.nrows):
#             row_list = []
#             sale_amount = worksheet.cell_value(row_index, sales_column_index)
#             if sale_amount > threshold:
#                 for column_index in range(worksheet.ncols):
#                     cell_value = worksheet.cell_value(row_index, column_index)
#                     cell_type = worksheet.cell_type(row_index, column_index)
#                     if cell_type == 3:
#                         date_cell = xldate_as_tuple(cell_value, workbook.datemode)
#                         date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                         row_list.append(date_cell)
#                     else:
#                         row_list.append(cell_value)
#             if row_list:
#                 data.append(row_list)
#     for list_index, output_list in enumerate(data):
#         for element_index, element in enumerate(output_list):
#             output_worksheet.write(list_index, element_index, element)
# output_workbook.save(output_file)

# # 在所有工作表中筛选特定行的PD方法
# import sys
# import pandas as pd
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# date_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)
# row_output = []
#
# for worksheet_name, data in date_frame.items():
#     row_output.append(data[data['Sale Amount'].astype(float) > 2000.0])
# filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)  # 按列组合，将表格数据转化为数据框
# writer = pd.ExcelWriter(output_file)
# filtered_rows.to_excel(writer, sheet_name='sale_amount_gt2000', index=False)
# writer.save()

# # 在所有工作表中选取特定列
# import sys
# from datetime import date
# from xlrd import open_workbook, xldate_as_tuple
# from xlwt import Workbook
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet('selected_columns_all_worksheets')
#
# my_columns = ['Customer Name', 'Sale Amount']
# first_worksheet = True
# with open_workbook(input_file) as workbook:
#     data = [my_columns]
#     index_of_cols_to_keep = []
#     for worksheet in workbook.sheets():
#         if first_worksheet:
#             header = worksheet.row_values(0)
#             for column_index in range(len(header)):
#                 if header[column_index] in my_columns:
#                     index_of_cols_to_keep.append(column_index)
#             first_worksheet = False
#         for row_index in range(1, worksheet.nrows):
#             row_list = []
#             for column_index in index_of_cols_to_keep:
#                 cell_value = worksheet.cell_value(row_index, column_index)
#                 cell_type = worksheet.cell_type(row_index, column_index)
#                 if cell_type == 3:
#                     date_cell = xldate_as_tuple(cell_value, workbook.datemode)
#                     date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                     row_list.append(date_cell)
#                 else:
#                     row_list.append(cell_value)
#             if row_list:
#                 data.append(row_list)
#     for list_index, output_list in enumerate(data):
#         for element_index, element in enumerate(output_list):
#             output_worksheet.write(list_index, element_index, element)
# output_workbook.save(output_file)

# # 在所有工作表中选取特定列的PD方法
# import sys
# import pandas as pd
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)
# column_output = []
#
# for worksheet, data in data_frame.items():
#     column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])
# selected_columns = pd.concat(column_output, axis=0, ignore_index=True)
# writer = pd.ExcelWriter(output_file)
# selected_columns.to_excel(writer, sheet_name='selected_columns_all_worksheets', index=False)
# writer.save()

# 在一组工作表中筛选特定行
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('set_of_worksheets')

my_sheets = [0, 1]
threshold = 1900.0
sales_column_index = 3
first_worksheet = True

with open_workbook(input_file) as workbook:
    data = []
    for sheet_index in range(workbook.nsheets):
        if sheet_index in my_sheets:
            worksheet = workbook.sheet_by_index(sheet_index)
            if first_worksheet:
                header_row = worksheet.row_values(0)
                data.append(header_row)
                first_worksheet = False
            for row_index in range(1, worksheet.nrows):
                row_list = []
                sale_amount = worksheet.cell_value(row_index, sales_column_index)
                if sale_amount > threshold:
                    for column_index in range(worksheet.ncols):
                        cell_value = worksheet.cell_value(row_index, column_index)
                        cell_type = worksheet.cell_type(row_index, column_index)
                        if cell_type == 3:
                            date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                            date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                            row_list.append(date_cell)
                        else:
                            row_list.append(cell_value)
                if row_list:
                    data.append(row_list)
    print(data)
    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)

# # 在一组工作表中筛选特定行的PD方法
# import sys
# import pandas as pd
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# my_sheets = [0, 1]
# threshold = 1900.0
#
# data_frame = pd.read_excel(input_file, sheet_name=my_sheets, index_col=None)
# row_list = []
# for worksheet_name, data in data_frame.items():
#     row_list.append(data[data['Sale Amount'].astype(float) > threshold])
# filtered_rows = pd.concat(row_list, axis=0, ignore_index=True)
# writer = pd.ExcelWriter(output_file)
# filtered_rows.to_excel(writer, sheet_name='set_of_worksheets', index=False)
# writer.save()