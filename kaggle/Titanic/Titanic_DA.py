# 导入数据包和数据集
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')  # 过滤忽略警告信息

# 导入数据集
train = pd.read_csv('dataset/train.csv')
test = pd.read_csv('dataset/test.csv')
full_data = [train, test]
# 存储测试集中的乘客ID信息
output_Id = test['PassengerId']
# 总览原始数据
print(train.head())
print(test.head())
print(train.info())
print(test.info())
print(train.describe())

# 对数据的初步认识和分析
# 通过图表的方式探索一个或多个自变量对因变量的影响
fig = plt.figure()
fig.set(alpha=0.2)
# 总览数据相关性热力图
corr = train.drop('PassengerId', axis=1).corr()
print(corr)
sns.heatmap(corr, vmin=-1, vmax=1, annot=True, square=True)
plt.savefig('fig/Corr', dpi=300, bbox_inches='tight')
# 总体生还状况(0/1)
survived = train.Survived.value_counts()
survived.plot(kind='bar')
x = survived.index
y = survived.values
for x,y in zip(x, y):
    plt.text(x, y, '{}'.format(y), ha='center', va='bottom')
plt.xticks([0, 1], ['Died', 'Survived'])
plt.title('Survived')
plt.xlabel('People')
plt.ylabel('Amount')
plt.savefig('fig/survived_rate', dpi=300, bbox_inches='tight')
# 乘客等级(1/2/3)
no_survived_Pclass = train.Pclass[train.Survived == 0].value_counts()
survived_Pclass = train.Pclass[train.Survived == 1].value_counts()
Pclass = pd.DataFrame({'Died': no_survived_Pclass, 'Survived': survived_Pclass})
print(Pclass)
Pclass.plot(kind='bar')
plt.title('Survived-Pclass')
plt.xlabel('Pclass')
plt.ylabel('Amount')
plt.savefig('fig/survived_Pclass', dpi=300, bbox_inches='tight')
# 性别(male/female)
no_survived_Sex = train.Sex[train.Survived == 0].value_counts()
survived_Sex = train.Sex[train.Survived == 1].value_counts()
Sex = pd.DataFrame({'Died': no_survived_Sex, 'Survived': survived_Sex})
print(Sex)
Sex.plot(kind='bar')
plt.title('Survived-Sex')
plt.xlabel('Sex')
plt.ylabel('Amount')
plt.savefig('fig/survived_Sex', dpi=300, bbox_inches = 'tight')
# 港口(C/Q/S)
# 注意缺少数据889/891
no_survived_Embarked = train.Embarked[train.Survived == 0].value_counts()
survived_Embarked = train.Embarked[train.Survived == 1].value_counts()
Embarked = pd.DataFrame({'Died': no_survived_Embarked, 'Survived': survived_Embarked})
print(Embarked)
Embarked.plot(kind='bar')
plt.title('Survived-Embarked')
plt.xlabel('Embarked')
plt.ylabel('Amount')
plt.savefig('fig/survived_Embarked', dpi=300, bbox_inches='tight')
# 票价
# 对连续属性进行等频离散化，观察其特征
train['FareClass'] = pd.qcut(train['Fare'], 4)
no_survived_Fare = train.FareClass[train.Survived == 0].value_counts()
survived_Fare = train.FareClass[train.Survived == 1].value_counts()
Fare = pd.DataFrame({'Died': no_survived_Fare, 'Survived': survived_Fare})
print(Fare)
Fare.plot(kind='bar')
plt.title('Survived-Fare')
plt.xlabel('Fare')
plt.ylabel('Amount')
plt.savefig('fig/survived_Fare', dpi=300, bbox_inches='tight')
# 年龄
# 注意缺少数据714/891
# 对连续属性进行等宽离散化，初步观察其特征
train['AgeClass'] = pd.cut(train['Age'], 5)
no_survived_Age = train.AgeClass[train.Survived == 0].value_counts()
survived_Age = train.AgeClass[train.Survived == 1].value_counts()
Age = pd.DataFrame({'Died': no_survived_Age, 'Survived': survived_Age})
Age = Age.sort_index(axis=0, ascending=True)
print(Age)
Age.plot(kind='bar')
plt.title('Survived-Age')
plt.xlabel('Age')
plt.ylabel('Amount')
plt.savefig('fig/survived-Age', dpi=300, bbox_inches='tight')
# 兄弟姐妹
no_survived_Sibsp = train.SibSp[train.Survived == 0].value_counts()
survived_Sibsp = train.SibSp[train.Survived == 1].value_counts()
Sibsp = pd.DataFrame({'Died': no_survived_Sibsp, 'Survived': survived_Sibsp})
Sibsp = Sibsp.fillna(0).astype(int)
print(Sibsp)
Sibsp.plot(kind='bar')
plt.title('Survived-Sibsp')
plt.xlabel('Sibsp')
plt.ylabel('Amount')
plt.savefig('fig/survived-Sibsp', dpi=300, bbox_inches='tight')
# 父母子女
no_survived_Parch = train.Parch[train.Survived == 0].value_counts()
survived_Parch = train.Parch[train.Survived == 1].value_counts()
Parch = pd.DataFrame({'Died': no_survived_Parch, 'Survived': survived_Parch})
Parch = Parch.fillna(0).astype(int)
print(Parch)
Parch.plot(kind='bar')
plt.title('Survived-Parch')
plt.xlabel('Parch')
plt.ylabel('Amount')
plt.savefig('fig/survived-Parch', dpi=300, bbox_inches='tight')
# 家庭人数
train['Family'] = train['SibSp'] + train['Parch'] + 1
no_survived_Family = train.Family[train.Survived == 0].value_counts()
survived_Family = train.Family[train.Survived == 1].value_counts()
Family = pd.DataFrame({'Died': no_survived_Family, 'Survived': survived_Family})
Family = Family.fillna(0).astype(int)
print(Family)
Family.plot(kind='bar')
plt.title('Survived-Family')
plt.xlabel('FamilySize')
plt.ylabel('Amount')
plt.savefig('fig/survived_Family', dpi=300, bbox_inches = 'tight')
# 是否独身
train['Family'] = train['SibSp'] + train['Parch'] + 1
train['IsAlone'] = 0
train.loc[train['Family'] == 1, 'IsAlone'] = 1
no_survived_IsAlone = train.IsAlone[train.Survived == 0].value_counts()
survived_IsAlone = train.IsAlone[train.Survived == 1].value_counts()
IsAlone = pd.DataFrame({'Died': no_survived_IsAlone, 'Survived': survived_IsAlone})
print(IsAlone)
IsAlone.plot(kind='bar')
plt.title('Survived-IsAlone')
plt.xlabel('IsAlone')
plt.ylabel('Amount')
plt.savefig('fig/survived_IsAlone', dpi=300, bbox_inches='tight')
# 姓名称谓
# 提取姓名中的称谓
def get_title(name):
    title_search = re.search('([A-Za-z]+)\.', name)
    if title_search:
        return title_search.group(1)
    return ''

train['Title'] = train['Name'].apply(get_title)
train['Title'] = train['Title'].replace(['Lady', 'Countess','Capt', 'Col',
                'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
train['Title'] = train['Title'].replace('Mme', 'Mrs')
train['Title'] = train['Title'].replace('Mlle', 'Miss')
train['Title'] = train['Title'].replace('Ms', 'Miss')
no_survived_title = train.Title[train.Survived == 0].value_counts()
survived_title = train.Title[train.Survived == 1].value_counts()
Title = pd.DataFrame({'Died': no_survived_title, 'Survived': survived_title})
Title = Title.fillna(0).astype(int)
print(Title)
Title.plot(kind='bar')
plt.title('Survive-Title')
plt.xlabel('Title')
plt.ylabel('Amount')
plt.savefig('fig/survived_Title', dpi=300, bbox_inches='tight')
# 客舱信息
# 由于缺失较多，先从粗粒度观察
train['Has_cabin'] = train['Cabin'].apply(lambda x: 0 if type(x) == float else 1)
no_survived_cabin = train.Has_cabin[train.Survived == 0].value_counts()
survived_cabin = train.Has_cabin[train.Survived == 1].value_counts()
Cabin = pd.DataFrame({'Died': no_survived_cabin, 'Survived': survived_cabin})
print(Cabin)
Cabin.plot(kind='bar')
plt.title('Survive-Cabin')
plt.xlabel('Has Cabin or not')
plt.ylabel('Amount')
plt.savefig('fig/survived_Cabin', dpi=300, bbox_inches='tight')
# 乘客等级与船舱信息遗失的关系
train['Has_cabin'] = train['Cabin'].apply(lambda x: 0 if type(x) == float else 1)
no_cabin_pclass = train.Pclass[train.Has_cabin == 0].value_counts()
cabin_pclass = train.Pclass[train.Has_cabin == 1].value_counts()
Pclass_Cabin = pd.DataFrame({'No Cabin': no_cabin_pclass, 'Has Cabin': cabin_pclass})
print(Pclass_Cabin)
Pclass_Cabin.plot(kind='bar')
plt.title('Cabin-Pclass')
plt.xlabel('Pclass')
plt.ylabel('Amount')
plt.savefig('fig/Cabin-Pclass', dpi=300, bbox_inches='tight')
# 乘客等级与票价的关系
# # 对连续属性进行等频离散化，观察其特征
train['FareClass'] = pd.qcut(train['Fare'], 4)
pclass1 = train.FareClass[train.Pclass == 1].value_counts()
pclass2 = train.FareClass[train.Pclass == 2].value_counts()
pclass3 = train.FareClass[train.Pclass == 3].value_counts()
Pclass_Fare = pd.DataFrame({'Pclass1': pclass1, 'Pclass2': pclass2, 'Pclass3': pclass3})
print(Pclass_Fare)
Pclass_Fare.plot(kind='bar')
plt.title('Pclass-Fare')
plt.xlabel('Fare')
plt.ylabel('Amount')
plt.savefig('fig/Pclass-Fare', dpi=300, bbox_inches='tight')

