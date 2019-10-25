import pandas as pd
from pandas import Series

aSer = Series([1, 2.0, 'a'])
print(aSer)
bSer = Series(['apple', 'peach', 'lemon'], index=[1,2,3])
print(bSer)
print(bSer.index, bSer.values)

# series的数据对齐
data = {'AXP':'86.40', 'CSCO':'122.64', 'BA':'99.44'}
sindex = ['AXP', 'CSCO', 'BA', 'AAPL']
cSer = Series(data, index=sindex)
print(cSer)
print(pd.isnull(cSer)) # 判断字典内那些为空

# series的name属性
cSer.name = 'cnames'
cSer.index.name = 'volume'
print(cSer)
