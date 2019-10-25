from rpy2 import robjects
from rpy2.robjects.packages import importr
import numpy as np
from numpy.matlib import repmat
import pandas as pd
import pylogit as pl
from collections import OrderedDict

# data = pd.read_csv('data/demoR.csv')
# print(data)

# 设置R语言控制台
r = robjects.r
splines = importr('splines')

# data2 = r['read.csv']('F://Coding/python/Behance/pylogit/data/demoR.csv')
# print(data2)

x = [1,2,3]
ns = r['ns'](x, df = 3)
print(ns)