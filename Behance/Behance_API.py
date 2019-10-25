# 建立BehanceAPI框架
import os
import time
import requests
import pandas as pd
import pymysql
from behance_python3 import API

# 通过BehanceAPI秘钥创建对象
def getBehanceObj():
    behance = API('mCfVlxzktvga8E0HPEDt1GjzS1943EFp')
    return behance

# 连接mysql数据库
def connetMysql():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1205', db='behance', charset='utf8mb4')
    cur = conn.cursor()
    return conn, cur

# 时间戳转换方法
def timeTrans(stamp):
    timeArray = time.localtime(stamp)
    transTime = time.strftime('%Y%m%d', timeArray)
    return transTime

# 通过API将数据直接存入数据库，自带查重
def dataPush(behance, conn, cur):
    global data
    for i in range(1, 2):
        # 根据需要更改项目查询参数
        projects = behance.project_search('car', page=i, field='130', time='all', sort='featured_date')
        for project in projects:
            try:
                data = [project.id, project.name, timeTrans(project.published_on), project.fields[0],
                        project.stats.views, project.stats.appreciations, project.stats.comments,
                        project.covers[404],  # 图片质量包括808,404,202，origin等,但有些可能不一定存在
                        project.owners[0].username, project.owners[0].city, project.owners[0].country]
            except:
                pass
            cur.execute('INSERT IGNORE INTO automotive_design (projectID, name, publishedTime, '
                        'field, views, appreciations, comments, pic, owner, city, country) '
                        'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', data)
    conn.commit()

# 从数据库调取数据
def dataPop(conn, cur):
    cur.execute('use behance')
    sql_cmd = 'select * from automotive_design'
    try:
        data = pd.read_sql(sql_cmd, con=conn, index_col='id')
    finally:
        cur.close()
        conn.close()
    return data

# 将数据存储为CSV文件备份,
def saveCsv(data):
    path_csv = 'project'
    if not os.path.exists(path_csv):
        os.mkdir(path_csv)
    data.to_csv('project/automotive_design.csv')

# 下载保存图片并根据ID重命名
def downloadPic(data):
    path_file = 'picture/automotive_design'
    if not os.path.exists(path_file):
        os.mkdir(path_file)

    projectID_list = list(data['projectID'])
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
    behance = getBehanceObj()
    conn, cur = connetMysql()
    dataPush(behance, conn, cur)
    data = dataPop(conn, cur)
    saveCsv(data)
    downloadPic(data)

main()
