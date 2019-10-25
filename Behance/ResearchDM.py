# # 建立BehanceAPI框架
import os
import csv
import time
import requests
import numpy as np
import pandas as pd
from behance_python3 import API

# 通过BehanceAPI秘钥创建对象
def getBehanceObj():
    behance = API('mCfVlxzktvga8E0HPEDt1GjzS1943EFp')
    return behance

# 时间戳转换方法
def timeTrans(stamp):
    timeArray = time.localtime(stamp)
    transTime = time.strftime('%Y%m%d', timeArray)
    return transTime

# 数据挖掘并存储CSV
def dataMining(behance):
    count = 0
    data = open('project/data_helmet_all.csv', 'wt', newline='', encoding='utf_8_sig')
    writer = csv.writer(data)
    try:
        writer.writerow(('ID', 'projectID', 'projectName', 'publishedTime', 'field', 'views', 'appreciations',
                         'comments', 'pic', 'colors', 'ownerID', 'ownerName', 'followers'))
        for i in range(1, 10):
            # 第一个参数是自定义搜索项，第二个参数列表是过滤器
            projects = behance.project_search('helmet', page=i, field='49', time='all', sort='appreciations')
            for project in projects:
                try:
                    writer.writerow(
                        (count, project.id, project.name, timeTrans(project.published_on), project.fields[0],
                        project.stats.views, project.stats.appreciations, project.stats.comments,
                        project.covers[404], project.colors,  # 图片质量包括808,404,202，origin等,但有些可能不一定存在
                        project.owners[0].id, project.owners[0].username, project.owners[0].stats.followers))
                    count += 1
                except KeyError as e:
                    print(e)
    finally:
        data.close()

# 下载保存图片并根据ID重命名
def downloadPic(data):
    path_file = 'picture/helmet_all'
    if not os.path.exists(path_file):
        os.mkdir(path_file)

    projectID_list = list(data['ID'])
    pic_list = list(data['pic'])
    for i in range(len(pic_list)):
        pic_name = str(projectID_list[i]) + '.jpg'
        pic_path = path_file + r'/' + pic_name
        try:
            r = requests.get(pic_list[i])
            if not os.path.exists(pic_path):
                f = open(pic_path, 'wb')
                f.write(r.content)
                f.close()
        except:
            pass
        print('\rFinished: {:.2f}%'.format(i * 100 / len(pic_list)), end='')

def main():
    # behance = getBehanceObj()
    # dataMining(behance)
    data = pd.read_csv('project/data_helmet_all.csv')
    print(data)
    downloadPic(data)

main()
