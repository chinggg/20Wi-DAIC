import numpy as np
import pandas as pd
from pandas import Series, DataFrame

print("创建50*7的DataFrame对象,数据为[10,99]之间的随机整数,columns为字符a~g")
df1 = DataFrame(np.random.randint(low=10, high=100, size=[50,7]), 
            columns=['a','b','c','d','e','f','g'])
print(df1)
df1.to_csv('p45.csv',mode='w')

colNames=['flymiles','videogame','icecream','type']
df2 = DataFrame.read_excel("data/datingTestSet.xls","Group1",col_name=colNames)
print(df2.head(5))
print(df2[ df2.type == "largeDoses" ])


