# # 筛选特定行满足某个条件
# import sys
# from datetime import date
# from xlrd import open_workbook, xldate_as_tuple
# from xlwt import Workbook
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet('jan_2013_output')
#
# sale_amount_index = 3
# with open_workbook(input_file) as workbook:
#     worksheet = workbook.sheet_by_name('january_2013')
#     data = []
#     header = worksheet.row_values(0)
#     data.append(header)
#     for row_index in range(1, worksheet.nrows):
#         row_list = []
#         sale_amount = worksheet.cell_value(row_index, sale_amount_index)
#         if sale_amount > 1400.0:  # 只需要大于1400的行
#             for column_index in range(worksheet.ncols):
#                 cell_value = worksheet.cell_value(row_index, column_index)
#                 cell_type = worksheet.cell_type(row_index, column_index)
#                 if cell_type == 3:
#                     date_cell = xldate_as_tuple(cell_value, workbook.datemode)
#                     date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')  # 将转换的元组作为参数传递给date函数
#                     row_list.append(date_cell)
#                 else:
#                     row_list.append(cell_value)
#         if row_list:
#             data.append(row_list)  # 检测该行是否为空
#     # 保证将各行作为一个连续整体写入输出文件，行与行之间不出现缺口
#     for list_index, output_list in enumerate(data):
#         for element_index, element in enumerate(output_list):
#             output_worksheet.write(list_index, element_index, element)
# output_workbook.save(output_file)

# # 筛选特定行的值满足条件的PD方法
# import sys
# import pandas as pd
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
# data_frame_find = data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]
# writer = pd.ExcelWriter(output_file)
# data_frame_find.to_excel(writer, sheet_name='jan_2013_output', index=False)
# writer.save()

# # 行中的值属于某个集合，如日期属于一个特定日期集合
# import sys
# from datetime import date
# from xlrd import open_workbook, xldate_as_tuple
# from xlwt import Workbook
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet('jan_2013_output')
#
# important_dates = ['01/24/2014', '01/31/2014']
# purchase_date_column_index = 4
# with open_workbook(input_file) as workbook:
#     worksheet = workbook.sheet_by_name('january_2013')
#     data = []
#     header = worksheet.row_values(0)
#     data.append(header)
#     for row_index in range(1, worksheet.nrows):
#         purchase_datetime = xldate_as_tuple(worksheet.cell_value(row_index, purchase_date_column_index), workbook.datemode)
#         purchase_date = date(*purchase_datetime[0:3]).strftime('%m/%d/%Y')
#         row_list = []
#         if purchase_date in important_dates:
#             for colume_index in range(worksheet.ncols):
#                 cell_value = worksheet.cell_value(row_index, colume_index)
#                 cell_type = worksheet.cell_type(row_index, colume_index)
#                 if cell_type == 3:
#                     date_cell = purchase_date
#                     # date_cell = xldate_as_tuple(cell_value, workbook.datemode)
#                     # date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                     row_list.append(date_cell)
#                 else:
#                     row_list.append(cell_value)
#         if row_list:
#             data.append(row_list)
#     for list_index, output_list in enumerate(data):
#         for element_index, element in enumerate(output_list):
#             output_worksheet.write(list_index, element_index, element)
# output_workbook.save(output_file)

# # 行中的值属于某个集合查找的PD方法
# import sys
# import pandas as pd
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# important_dates = ['01/24/2014', '01/31/2014']
# data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
# data_frame_valueinset = data_frame[data_frame['Purchase Date'].isin(important_dates)]
# writer = pd.ExcelWriter(output_file)
# data_frame_valueinset.to_excel(writer, sheet_name='jan_13_output', index=False)
# writer.save()

# # 行中的值匹配于某个特定模式
# import sys
# import re
# from datetime import date
# from xlrd import open_workbook, xldate_as_tuple
# from xlwt import Workbook
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet('jan_2013_output')
#
# pattern = re.compile(r'^J.*')
# customer_name_colunmn_index = 1
# with open_workbook(input_file) as workbook:
#     worksheet = workbook.sheet_by_name('january_2013')
#     data = []
#     header = worksheet.row_values(0)
#     data.append(header)
#     for row_index in range(1, worksheet.nrows):
#         row_list = []
#         if pattern.search(worksheet.cell_value(row_index, customer_name_colunmn_index)):
#             for column_index in range(worksheet.ncols):
#                 cell_value = worksheet.cell_value(row_index, column_index)
#                 cell_type = worksheet.cell_type(row_index, column_index)
#                 if cell_type == 3:
#                     date_cell = xldate_as_tuple(cell_value, workbook.datemode)
#                     date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                     row_list.append(date_cell)
#                 else:
#                     row_list.append(cell_value)
#         if row_list:
#             data.append(row_list)
#     for list_index, output_list in enumerate(data):
#         for element_index, element in enumerate(output_list):
#             output_worksheet.write(list_index, element_index, element)
# output_workbook.save(output_file)

# # 行中的值匹配特定模式的PD方法
# import sys
# import pandas as pd
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
# data_frame_pattern = data_frame[data_frame['Customer Name'].str.startswith('J')]
# writer = pd.ExcelWriter(output_file)
# data_frame_pattern.to_excel(writer, 'jan_2013_output', index=False)
# writer.save()

# # 使用列索引值选取特定列
# import sys
# from datetime import date
# from xlrd import open_workbook, xldate_as_tuple
# from xlwt import Workbook
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# output_workbook = Workbook()
# output_sheet = output_workbook.add_sheet('jan_2013_output')
#
# my_columns = [1, 4]
# with open_workbook(input_file) as workbook:
#     worksheet = workbook.sheet_by_name('january_2013')
#     data = []
#     for row_index in range(worksheet.nrows):
#         row_list = []
#         for columns_index in my_columns:
#             cell_value = worksheet.cell_value(row_index, columns_index)
#             cell_type = worksheet.cell_type(row_index, columns_index)
#             if cell_type == 3:
#                 date_cell = xldate_as_tuple(cell_value, workbook.datemode)
#                 date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                 row_list.append(date_cell)
#             else:
#                 row_list.append(cell_value)
#         data.append(row_list)
#     for list_index, output_list in enumerate(data):
#         for element_index, element in enumerate(output_list):
#             output_sheet.write(list_index, element_index, element)
# output_workbook.save(output_file)

# 使用列索引值选取特定列的PD方法
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_column = data_frame.iloc[:, [1, 4]]
writer = pd.ExcelWriter(output_file)
data_frame_column.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()

# 使用列标题选取特定列
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

my_columns = ['Customer Name', 'Purchase Date']
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = [my_columns]
    # 获取列标题的索引值
    header_list = worksheet.row_values(0)
    header_index_list = []
    for header_index in range(len(header_list)):
        if header_list[header_index] in my_columns:
            header_index_list.append(header_index)

    for row_index in range(1, worksheet.nrows):
        row_list = []
        for column_index in header_index_list:
            cell_value = worksheet.cell_value(row_index, column_index)
            cell_type = worksheet.cell_type(row_index, column_index)
            if cell_type == 3:
                date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list.append(date_cell)
            else:
                row_list.append(cell_value)
        data.append(row_list)
    # 保证将各行作为一个连续整体写入输出文件，行与行之间不出现缺口
    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)

# # 使用列标题选取特定列的PD方法
# import sys
# import pandas as pd
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
# data_frame_column = data_frame.loc[:, ['Customer Name', 'Purchase Date']]
# writer = pd.ExcelWriter(output_file)
# data_frame_column.to_excel(writer, sheet_name='jan_13_output', index=False)
# writer.save()
