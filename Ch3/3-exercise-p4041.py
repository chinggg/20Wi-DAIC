# P40-41思考与练习
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

print("1.创建并访问Series对象")
srs=Series([30,25,27,41,25,34],['a','b','c','d','e','f'])
print(srs)
print("增加数据27,索引为g")
srs=srs.append(Series(27,['g']))
print(srs)

print("修改索引d对应值为40")
srs['d']=40
print(srs)

print("查询值大于27的数据")
print(srs[srs > 27])

print("删除位置为1~3的数据")
# srs.index.delete([1,2,3])
labels=srs.index[1:3]
srs=srs.drop(index=labels)
print(srs)


print("2.创建并访问DataFrame对象")
dfm=DataFrame(np.arange(1,10).reshape(3,3),columns=['one','two','three'],index=['a','b','c'])
print(dfm)

print("查询列索引为two和three的两列数据")
print(dfm[["two","three"]])

print("查询第0、2行，第0、2列数据")
print(dfm.iloc[[0,2],[0,2]])

print("筛选第1列中值大于2的所有行数据，另存为data1对象")
data1= dfm[dfm.iloc[:,1] >2]
print(data1)

print("为data1添加一列数据,列索引为four,值都为10")
data1["four"]=10
print(data1)

print("将data1所有值大于9的数据修改为8")
data1[data1>9]=8
print(data1)

print("删除data1中第0行和第1行数据")
labels=data1.index[0:2]
data1=data1.drop(index=labels)
print(data1)
