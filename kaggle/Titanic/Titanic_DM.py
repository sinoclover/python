import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')  # 过滤忽略警告信息
from sklearn.metrics import accuracy_score

# 导入处理后的数据集
origin = pd.read_csv('dataset/test.csv')
train = pd.read_csv('dataset/train_handle.csv')
test = pd.read_csv('dataset/test_handle.csv')
# print(train.head())
# print(test.head())
output_Id = origin['PassengerId']

# 第一次0.80246，提交0.77033，逻辑回归baseline
# 第二次0.80471，提交0.76555，在baseline的基础上处理cabin数据
# 第三次0.81725，提交0.78468，使用随机森林算法
# 第四次0.82223，提交0.78468，使用决策树算法

# # 建立模型
# # baseline的逻辑回归模型
# import statsmodels.formula.api as sm

#
# logit_model = sm.logit('Survived~Pclass+Sex+Age+Fare+Embarked+Title+IsAlone+Has_cabin', data=train).fit()
# # print(logit_model.summary2())
# # print(logit_model.params)
# # 对测试集进行预测
# predictions_test = np.round(logit_model.predict(test)).astype(int)
# # print(predictions_test)
# # 对训练集进行预测
# predictions_train = np.round(logit_model.predict(train)).astype(int)
# # print(predictions_train)
# # 评价模型准确率
# score = accuracy_score(train['Survived'], predictions_train)
# print(score)  # 0.80471

# 选择最佳模型
# 分割训练集，使用部分训练集数据测试不同模型准确率
from sklearn.model_selection import train_test_split

predictors = train.drop(['Survived'], axis=1)
target = train['Survived']
x_train, x_test, y_train, y_test = train_test_split(predictors, target, test_size=0.22, random_state=0)

# 高斯朴素贝叶斯
from sklearn.naive_bayes import GaussianNB

gaussian = GaussianNB()
gaussian.fit(x_train, y_train)
y_pred = gaussian.predict(x_test)
acc_gaussian = accuracy_score(y_pred, y_test)
print(acc_gaussian)  # 0.77665

# 逻辑回归
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(x_train, y_train)
y_pred = logreg.predict(x_test)
acc_logreg = accuracy_score(y_pred, y_test)
print(acc_logreg)  # 0.80710

# 支持向量机SVC
from sklearn.svm import SVC

svc = SVC()
svc.fit(x_train, y_train)
y_pred = svc.predict(x_test)
acc_svc = accuracy_score(y_pred, y_test)
print(acc_svc)  # 0.81218

# 线性支持向量机SVC
from sklearn.svm import LinearSVC

linear_svc = LinearSVC()
linear_svc.fit(x_train, y_train)
y_pred = linear_svc.predict(x_test)
acc_linear_svc = accuracy_score(y_pred, y_test)
print(acc_linear_svc)  # 0.77157

# 感知机
from sklearn.linear_model.perceptron import Perceptron

perceptron = Perceptron()
perceptron.fit(x_train, y_train)
y_pred = perceptron.predict(x_test)
acc_perceptron = accuracy_score(y_pred, y_test)
print(acc_perceptron)  # 0.77665

# 决策树
from sklearn.tree import DecisionTreeClassifier

decisiontree = DecisionTreeClassifier()
decisiontree.fit(x_train, y_train)
y_pred = decisiontree.predict(x_test)
acc_decisiontree = accuracy_score(y_pred, y_test)
print(acc_decisiontree)  # 0.82233

# 随机森林
from sklearn.ensemble import RandomForestClassifier

randomforest = RandomForestClassifier()
randomforest.fit(x_train, y_train)
y_pred = randomforest.predict(x_test)
acc_randomforest = accuracy_score(y_pred, y_test)
print(acc_randomforest)  # 0.83248

# KNN
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
acc_knn = accuracy_score(y_pred, y_test)
print(acc_knn)  # 0.80710

# 随机梯度下降
from sklearn.linear_model import SGDClassifier

sgd = SGDClassifier()
sgd.fit(x_train, y_train)
y_pred = sgd.predict(x_test)
acc_sgd = accuracy_score(y_pred, y_test)
print(acc_sgd)  # 0.78172

# 梯度提升
from sklearn.ensemble import GradientBoostingClassifier

gbk = GradientBoostingClassifier()
gbk.fit(x_train, y_train)
y_pred = gbk.predict(x_test)
acc_gbk = accuracy_score(y_pred, y_test)
print(acc_gbk)  # 81.22

# 模型得分总览
models = pd.DataFrame({
    'Model': ['Support Vector Machines', 'KNN', 'Logistic Regression',
              'Random Forest', 'Naive Bayes', 'Perceptron', 'Linear SVC',
              'Decision Tree', 'Stochastic Gradient Descent', 'Gradient Boosting Classifier'],
    'Score': [acc_svc, acc_knn, acc_logreg,
              acc_randomforest, acc_gaussian, acc_perceptron,acc_linear_svc, acc_decisiontree,
              acc_sgd, acc_gbk]})
models.set_index(['Model'], inplace=True)
models.plot(kind='bar')
x = np.arange(len(models))
y = list(models.Score)
for x, y in zip(x, y):
    plt.text(x, y, '{:.4f}'.format(y), ha='center', va='bottom')
print(models)
plt.title('Models Score')
plt.xlabel('Model')
plt.ylabel('Score')
plt.savefig('fig/Model_Score', dpi=300, bbox_inches='tight')

# 使用随机森林模型获取结果
predictions_test = randomforest.predict(test)
predictions_test = pd.Series(predictions_test)

# # 使用决策树
# predictions_test = decisiontree.predict(test)
# predictions_test = pd.Series(predictions_test)

# 获取预测结果
output = pd.concat([output_Id, predictions_test], axis=1)
output.columns = ['PassengerId', 'Survived']
print(output)
output.to_csv('result/submission3.csv', index=False)
