import pandas as pd
import numpy as np

data = {'name':['Jack','Rose','Jason','Tom'], 'pay':[4000,5000,6000,7000]}
frame = pd.DataFrame(data)
print(frame)

data2 = np.array([('Wangdachui', 4000), ('Linling', 3000), ('Niuyun', 2000)])
frame2 = pd.DataFrame(data2, index=range(1,4), columns=['name', 'pay'])
print(frame2)
print(frame2.index)
print(frame2.columns)
print(frame2.values)

# DataFrame的基本操作
print(frame['name'])
print(frame.pay)
print(frame.iloc[0:2, [0,1]])

# DataFrame的统计功能
print(frame[frame.pay >= 6000])
