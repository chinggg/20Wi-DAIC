import numpy as np

print("一维数组访问")
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳', '钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese', 'Art', 'Database', 'Physics'])
print("subjects数组中选择并显示序号1、2、4门课的名称")
print(subjects[ [1, 2, 4] ])
print("使用倒序索引选择并显示names数组中'方绮雯'")
print(names[-3])
print("选择并显示names数组从2到最后的数组元素")
print(names[ 2: : ])
print("选择并显示subjects数组正序2~4的数组元素")
print(subjects[ 2:5 ])
print("使用布尔条件选择并显示subjects数组中的英语和物理科目名称")
print(subjects[ (subjects == 'English') | (subjects == 'Physics')])

print("\n二维数组访问")
scores = np.array([[70, 85, 77, 90, 82, 84, 89],
[60, 64, 80, 75, 80, 92, 90],
[90, 93, 88, 87, 86, 90, 91],
[80, 82, 91, 88, 83, 86, 80],
[88, 72, 78, 90, 91, 73, 80]])
print("选择并显示scores数组的1、4行(首行为第0行)")
print(scores[[1,4]])
print("选择并显示scores数组中行序2、4学生的数学和Python成绩")
print(scores[[2,4]][:,(subjects == 'Math') | (subjects == 'Python')])
print("选择并显示scores数组中所有学生的数学和艺术成绩")
print(scores[:,(subjects == 'Math') | (subjects == 'Art')])
print("选择并显示scores数组中“王微”和“刘旭阳”的英语和艺术课程成绩")
print(scores[ (names == '王微') | (names == '刘旭阳')]
        [:,(subjects == 'English') | (subjects == 'Art')])

print("\n生成由整数10~19组成的2×5的二维数组")
print(np.arange(10,20).reshape(2,5))
