# 建立BehanceAPI框架
import os
import csv
import time
import pandas as pd
import pymysql
from behance_python3 import API

# # 建立数据存储位置
# path = 'project'
# if not os.path.exists(path):
#     os.mkdir(path)
#
# # 通过BehanceAPI秘钥创建对象
# behance = API('mCfVlxzktvga8E0HPEDt1GjzS1943EFp')
#
# # 时间戳转换方法
# def timeTrans(stamp):
#     timeArray = time.localtime(stamp)
#     transTime = time.strftime('%Y%m%d', timeArray)
#     return transTime
#
# # 根据关键字存储CSV项目列表
# data = open('project/data_field.csv', 'wt', newline='', encoding='utf_8_sig')
# writer = csv.writer(data)
# try:
#     writer.writerow(('projectID', 'name', 'publishedTime', 'field', 'views', 'appreciations',
#                      'comments','pic', 'owner', 'city', 'country'))
#     for i in range(1, 6):
#         # 第一个参数是自定义搜索项，第二个参数列表是过滤器
#         projects = behance.project_search('car', page=i, field='130', time='all', sort='featured_date')
#         for project in projects:
#             try:
#                 writer.writerow(
#                     (project.id, project.name, timeTrans(project.published_on), project.fields[0],
#                     project.stats.views, project.stats.appreciations, project.stats.comments,
#                     project.covers[404],  # 图片质量包括808,404,202，origin等,但有些可能不一定存在
#                     project.owners[0].username, project.owners[0].city, project.owners[0].country))
#             except KeyError as e:
#                 print(e)
# finally:
#     data.close()

# # 写入数据库
# from sqlalchemy import create_engine
#
# pymysql.install_as_MySQLdb()
# result = pd.read_csv('project/data_field.csv', index_col=None)
# engine = create_engine('mysql+mysqldb://root:1205@localhost:3306/behance?charset=utf8')
# pd.io.sql.to_sql(result, 'automotive_design', con=engine, schema='behance', if_exists='append', index=False)  # replace将原表删除重建, fail不操作

# # 数据库数据调取
# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1205', db='mysql', charset='utf8')
# cur = conn.cursor()
# cur.execute('use behance')
# sql_cmd = 'select * from automotive_design'
# try:
#     table = pd.read_sql(sql_cmd, con=conn, index_col='id')
# finally:
#     cur.close()
#     conn.close()
