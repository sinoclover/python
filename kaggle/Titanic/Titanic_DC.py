# 导入数据包和数据集
import numpy as np
import pandas as pd
import re
import warnings
warnings.filterwarnings('ignore')  # 过滤忽略警告信息

# 导入数据集
train = pd.read_csv('dataset/train.csv')
test = pd.read_csv('dataset/test.csv')
full_data = [train, test]
# 存储测试集中的乘客ID信息
output_Id = test['PassengerId']
# # 总览原始数据
# print(train.head())
# print(test.head())
# print(train.info())
# print(test.info())
# print(train.describe())

# 数据预处理之清洗
# 姓名处理
# 提取姓名中的称谓
def get_title(name):
    title_search = re.search('([A-Za-z]+)\.', name)
    if title_search:
        return title_search.group(1)
    return ''

for dataset in full_data:
    dataset['Title'] = dataset['Name'].apply(get_title)
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col',
                        'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')

# 根据称谓填补年龄缺失值
for dataset in full_data:
    age_mr = int(dataset.Age[dataset.Title == 'Mr'].dropna().mean())
    dataset.Age[dataset.Title == 'Mr'] = dataset.Age[dataset.Title == 'Mr'].fillna(age_mr)
    age_mrs = int(dataset.Age[dataset.Title == 'Mrs'].dropna().mean())
    dataset.Age[dataset.Title == 'Mrs'] = dataset.Age[dataset.Title == 'Mrs'].fillna(age_mrs)
    age_miss = int(dataset.Age[dataset.Title == 'Miss'].dropna().mean())
    dataset.Age[dataset.Title == 'Miss'] = dataset.Age[dataset.Title == 'Miss'].fillna(age_miss)
    age_master = int(dataset.Age[dataset.Title == 'Master'].dropna().mean())
    dataset.Age[dataset.Title == 'Master'] = dataset.Age[dataset.Title == 'Master'].fillna(age_master)
    age_rare = int(dataset.Age[dataset.Title == 'Rare'].dropna().mean())
    dataset.Age[dataset.Title == 'Rare'] = dataset.Age[dataset.Title == 'Rare'].fillna(age_rare)
# 家庭情况处理
for dataset in full_data:
    dataset['Family'] = dataset['SibSp'] + dataset['Parch'] + 1
for dataset in full_data:
    dataset['IsAlone'] = 0
    dataset.loc[dataset['Family'] == 1, 'IsAlone'] = 1
# 票价处理
# 鉴于缺失值较少，采用中位数填补
for dataset in full_data:
    dataset['Fare'] = dataset['Fare'].fillna(train['Fare'].median())
# 港口处理
# 鉴于缺失值较少，采用众数填补
for dataset in full_data:
    dataset['Embarked']  = dataset['Embarked'].fillna('S')
# 船舱处理
for dataset in full_data:
    dataset['Has_cabin'] = dataset['Cabin'].apply(lambda x: 0 if type(x)==float else 1)
# print(train.info())

# 数据预处理之集成规约
for dataset in full_data:
    # 对性别进行规约
    dataset['Sex'] = dataset['Sex'].map({'female': 0, 'male': 1}).astype(int)
    # 对称谓进行规约
    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0)
    # 对港口进行规约
    dataset['Embarked'] = dataset['Embarked'].map({'S': 0, 'C': 1, 'Q': 2}).astype(int)
    # 对票价进行规约
    dataset.loc[ dataset['Fare'] <= 7.91, 'Fare'] = 0
    dataset.loc[(dataset['Fare'] > 7.91) & (dataset['Fare'] <= 14.454), 'Fare'] = 1
    dataset.loc[(dataset['Fare'] > 14.454) & (dataset['Fare'] <= 31), 'Fare'] = 2
    dataset.loc[ dataset['Fare'] > 31, 'Fare'] = 3
    dataset['Fare'] = dataset['Fare'].astype(int)
    # 对年龄进行规约
    dataset.loc[dataset['Age'] <= 16, 'Age'] = 0
    dataset.loc[(dataset['Age'] > 16) & (dataset['Age'] <= 32), 'Age'] = 1
    dataset.loc[(dataset['Age'] > 32) & (dataset['Age'] <= 48), 'Age'] = 2
    dataset.loc[(dataset['Age'] > 48) & (dataset['Age'] <= 64), 'Age'] = 3
    dataset.loc[dataset['Age'] > 64, 'Age'] = 4

# 特征筛选
drop_elements = ['PassengerId', 'Name', 'Ticket', 'Cabin', 'SibSp', 'Parch', 'Family']
train = train.drop(drop_elements, axis=1)
test = test.drop(drop_elements, axis=1)
print(train.head())
print(test.head())
# 保存特征
train.to_csv('dataset/train_handle.csv', index=False)
test.to_csv('dataset/test_handle.csv', index=False)
