# BehanceTest
from behance_python3.api import API
import os
import csv
import time

# # 时间戳转换
# def timeTrans(stamp):
#     timeArray = time.localtime(stamp)
#     transTime = time.strftime('%Y%m%d', timeArray)
#     return transTime
#
# path = 'files'
# if not os.path.exists(path):
#     os.makedirs(path)

behance = API('mCfVlxzktvga8E0HPEDt1GjzS1943EFp')

# # 任选一个项目打印存储
# project1 = behance.get_project(project_id='4889175')
project1 = behance.get_project(project_id='69010049')
print(project1)
# # print(project1.modules[0])
# # print(project1.modules[0].sizes.original)
# project_image = [module.src for module in project1.modules if module.type == 'image']
# print(project_image[0])

# # 查找某个用户
user1 = project1.owners
# print(user1)
print(project1.stats)
print(user1[0].stats)

# # 项目列表CSV存储
# csv3 = open('../Behance/files/proj4.csv', 'wt', newline='', encoding='utf-8')
# writer = csv.writer(csv3)
# try:
#     writer.writerow(('projectID', 'name', 'publishedTime', 'field', 'views', 'appreciations',
#                      'comments', 'owner', 'city', 'country'))
#     for i in range(3):
#         projects = behance.project_search('', '', page=i)
#         for project in projects:
#             writer.writerow(
#                 (project.id, project.name, timeTrans(project.published_on), project.fields[0],
#                  project.stats.views, project.stats.appreciations, project.stats.comments,
#                  project.owners[0].username, project.owners[0].city, project.owners[0].country))
# finally:
#     csv3.close()
