# # CSV
# import csv
# import os
#
# path = '../Web-scraping/files'
# if not os.path.exists(path):
#     os.makedirs(path)
# csvFile = open('../Web-scraping/files/test.csv', 'w+', newline='')  # 使用newline解决隔行问题，即不换行
# try:
#     writer = csv.writer(csvFile)
#     writer.writerow(('number', 'number plus 2', 'number times 2'))
#     for i in range(10):
#         writer.writerow((i, i+2, i*2))
#
# finally:
#     csvFile.close()

# # 获取html表格table并写入CSV文件
# import csv
# import os
# from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
# from bs4 import BeautifulSoup
#
# def getHtml(url):
#     try:
#         html = urlopen(url)
#     except (HTTPError, URLError) as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html, 'html.parser')
#     except AttributeError as e:
#         return None
#     return bsObj
#
# url = 'https://baike.baidu.com/'
# bsObj = getHtml(url)
# if bsObj is None:
#     print('This page is not exist.')
#
# table = bsObj.findAll('table', {'class': 'statistics_num'})[0]
# rows = table.findAll('tr')
#
# path = '../Web-scraping/files'
# if not os.path.exists(path):
#     os.makedirs(path)
#
# csvFile = open('../Web-scraping/files/editors.csv', 'wt', newline='', encoding='gbk')
# writer = csv.writer(csvFile)
# try:
#     for row in rows:
#         csvRow = []
#         for cell in row.findAll('td'):
#             csvRow.append(cell.get_text())
#         writer.writerow(csvRow)
# finally:
#     csvFile.close()

# BehanceTest
from behance_python.api import API
import os
import csv
import time
# 时间戳转换
def timeTrans(stamp):
    timeArray = time.localtime(stamp)
    transTime = time.strftime('%Y%m%d', timeArray)
    return transTime

path = '../Behance/files'
if not os.path.exists(path):
    os.makedirs(path)

behance = API('mCfVlxzktvga8E0HPEDt1GjzS1943EFp')

# # 任选一个项目打印存储
# project1 = behance.get_project(project_id='4889175')
# print(project1)
# # 存储文本格式
# f1 = open('../Behance/files/proj1.txt', 'w')
# f1.write(str(project1))
# f1.close()

# # 存储csv,使用get_project
# csv1 = open('../Behance/files/proj1.csv', 'w+', newline='')
# writer = csv.writer(csv1)
# try:
#     writer.writerow(('projectID', 'name', 'publishedTime', 'field1', 'field2', 'field3', 'views', 'appreciations',
#                     'comments', 'owner', 'city', 'country'))
#     writer.writerow((project1.id, project1.name, timeTrans(project1.published_on), project1.fields[0], project1.fields[1],
#                     project1.fields[2], project1.stats.views, project1.stats.appreciations, project1.stats.comments,
#                     project1.owners[0].username, project1.owners[0].city, project1.owners[0].country))
# finally:
#     csv1.close()

# # 存储csv,使用project_search
# project1 = behance.get_project(project_id='4889175')
# csv2 = open('../Behance/files/proj2.csv', 'w+', newline='')
# writer = csv.writer(csv2)
# try:

#     writer.writerow((project1.id, project1.name, timeTrans(project1.published_on), project1.fields[0], project1.fields[1],
#                     project1.fields[2], project1.stats.views, project1.stats.appreciations, project1.stats.comments,
#                     project1.owners[0].username, project1.owners[0].city, project1.owners[0].country))
# finally:
#     csv2.close()

# 项目列表CSV存储
csv3 = open('../Behance/files/proj4.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(csv3)
try:
    writer.writerow(('projectID', 'name', 'publishedTime', 'field', 'views', 'appreciations',
                     'comments', 'owner', 'city', 'country'))
    for i in range(3):
        projects = behance.project_search('', '', page=i)
        for project in projects:
            writer.writerow(
                (project.id, project.name, timeTrans(project.published_on), project.fields[0],
                 project.stats.views, project.stats.appreciations, project.stats.comments,
                 project.owners[0].username, project.owners[0].city, project.owners[0].country))
finally:
    csv3.close()

# 一次最多爬取48个项目
# projects = behance.project_search('', '',time='all')
# print(len(projects))
# project_id = projects[0].id
# print(project_id)
# project2 = behance.get_project(project_id=str(project_id))
# print(project2.owners)
# project3 = behance.get_project(project_id='66058621')
# print(len(project3.owners))


