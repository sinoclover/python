# # 建立BehanceAPI框架
import os
import csv
import datetime, time
import requests
import numpy as np
import pandas as pd
from behance_python3 import API

# 通过BehanceAPI秘钥创建对象
def getBehanceObj():
    behance = API('mCfVlxzktvga8E0HPEDt1GjzS1943EFp')
    return behance

# 时间戳转换为时长
def timeTrans(stamp):
    now = datetime.date(2019, 10, 20)
    timeArray = time.localtime(stamp)
    pre = datetime.date(timeArray.tm_year, timeArray.tm_mon, timeArray.tm_mday)
    delta_t = now - pre
    return delta_t.days

# 数据挖掘并存储CSV
def dataMining(behance):
    count = 0
    # 修改文件
    data = open('data/data_for_question.csv', 'wt', newline='', encoding='utf_8_sig')
    writer = csv.writer(data)
    try:
        writer.writerow(('ID', 'projectID', 'projectName', 'duration', 'field', 'views', 'appreciations',
                        'comments', 'pic', 'color', 'ownerID', 'ownerName', 'ownerDuration',
                         'ownerFollowings', 'ownerFollowers', 'ownerViews', 'ownerAppreciations', 'ownerComments'))
        # 修改挖掘数目
        for i in range(1, 10):
            # 第一个参数是自定义搜索项，第二个参数列表是过滤器
            projects = behance.project_search('drill', page=i, field='49', time='all', sort='appreciations')
            for project in projects:
                try:
                    writer.writerow(
                        (count, project.id, project.name, timeTrans(project.published_on), project.fields[0],
                        project.stats.views, project.stats.appreciations, project.stats.comments,
                        project.covers[404], project.colors,  # 图片质量包括808,404,202，origin等,但有些可能不一定存在
                        project.owners[0].id, project.owners[0].username, timeTrans(project.owners[0].created_on),
                        project.owners[0].stats.following, project.owners[0].stats.followers,
                        project.owners[0].stats.views, project.owners[0].stats.appreciations,
                        project.owners[0].stats.comments))
                    count += 1
                except KeyError as e:
                    print(e)
    finally:
        data.close()

# 下载保存图片并根据ID重命名
def downloadPic(data):
    # 修改文件
    path_file = 'pic/question'
    if not os.path.exists(path_file):
        os.mkdir(path_file)

    projectID_list = list(data['ID'])
    pic_list = list(data['pic'])
    for i in range(len(pic_list)):
        pic_name = str(projectID_list[i]) + '.jpg'
        pic_path = path_file + r'/' + pic_name
        try:
            if not os.path.exists(pic_path):
                r = requests.get(pic_list[i])
                f = open(pic_path, 'wb')
                f.write(r.content)
                f.close()
        except:
            pass
        print('\rFinished: {:.2f}%'.format(i * 100 / len(pic_list)), end='')

# 清除无效数据
def cleardata(data):
    for i in range(500):
        img_path = 'pic/question/' + str(i) + '.jpg'
        if not os.path.exists(img_path):
            data.drop(data[data['id'] == i].index, inplace=True)
    return data

def main():
    # behance = getBehanceObj()
    # dataMining(behance)
    # 修改文件
    data = pd.read_csv('data/data_for_question.csv')
    print(data.head(5))
    downloadPic(data)
    # # 清除多余数据
    # data_filter = cleardata(data)
    # data_filter.drop('pic', axis=1, inplace=True)
    # data_filter.to_csv('data/data_for_question_clear.csv', index=None)

main()
