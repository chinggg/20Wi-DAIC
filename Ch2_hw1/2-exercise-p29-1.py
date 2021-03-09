import numpy as np
# "大润发"、"沃尔玛"、"好德"和"农工商"四个超市都卖苹果、香蕉、橘子和芒果四种水果。使用NumPy的ndarray实现以下功能。
# 创建两个一维数组分别存储超市名称和水果名称
supermarkets = np.array(['大润发', '沃尔玛', '好德', '农工商'])
fruits = np.array(['苹果', '香蕉', '橘子', '芒果'])
# 创建一个4×4的二维数组存储不同超市的水果价格，其中价格由4~10范围内的随机数生成
prices = np.random.randint(4, 10, size = (4,4))
print("初始水果价格")
print(prices)
# 选择"大润发"的苹果和"好德"的香蕉，并将价格增加1元
prices[supermarkets == '大润发', fruits == '苹果'] += 1
prices[supermarkets == '好德', fruits == '香蕉'] += 1
print("\n选择'大润发'的苹果和'好德'的香蕉，并将价格增加1元")
print(prices)
# "农工商"水果大减价，所有水果价格减2元
prices[supermarkets == '农工商'] -= 2
print("\n'农工商'水果大减价，所有水果价格减2元")
print(prices)
# 统计四个超市苹果和芒果的销售均价
mapple = prices[fruits == '苹果'].mean()
print("\n苹果均价", mapple)
mmango = prices[fruits == '芒果'].mean()
print("芒果均价", mmango)
# 找出橘子价格最贵的超市名称（不是编号）
print("\n橘子价格最贵的超市名称：", supermarkets[prices[ :, fruits == '橘子' ].argmax()])
