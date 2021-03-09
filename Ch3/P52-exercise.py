import pandas as pd
from pandas import DataFrame


data1 = pd.read_excel("data/studentsInfo.xlsx", "Group3", usecols=["序号","性别","年龄"])
print(data1)
data2 = pd.read_excel("data/studentsInfo.xlsx", "Group3", usecols=["序号","身高","体重","成绩"])
print(data2)
print("将data2合并到data1,连接方式为内连接")
data1 = pd.merge(data1, data2, how='inner')
print(data1)

print("按成绩排名")
data1.sort_values(by='成绩', inplace=True)
print(data1)
print("身高降序排名")
pm = data1['身高'].rank(method='min',ascending=False)
print(pm)

