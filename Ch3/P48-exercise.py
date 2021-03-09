# P48思考与练习
import math
import pandas as pd
from pandas import DataFrame


# 1.数据清洗
print("从studentsInfo.xlsx文件的Group1表单中读取数据")
# xlrd does not work with python>=3.9
dfm = pd.read_excel(r'data/studentsInfo.xlsx','Group1',index_col=0)
print(dfm)
print('将“教学案例”列数据值全改为NaN')
dfm['案例教学']=math.nan
print(dfm)
print("滤除每行缺失3项及以上的行 (当前数据没有缺失3项以上的行)")
dfm.dropna(thresh=3)
print(dfm)
print("滤除值全部为NaN的列")
dfm.dropna(axis=1, how='all', inplace=True)
print(dfm)

# 2.数据填充
print('使用列的平均值填充“体重”和“成绩”列的NaN数据')
dfm.fillna({'体重':dfm['体重'].mean(), '成绩':dfm['成绩'].mean()}, inplace=True)
print(dfm)
print('使用上一行数据填充“年龄”列的NaN数据')
dfm.fillna(method='ffill', inplace=True)
print(dfm)
print('使用中位数填充“生活费用”列的NaN数据')
dfm.fillna({'月生活费':dfm['月生活费'].median()}, inplace=True)
print(dfm)
