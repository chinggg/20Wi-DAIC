lst=[]
for i in range(5):
    name=input()
    lst.append(name)
for each_name in lst:
    print(each_name)
query_name=input()
if query_name in lst:
    print("yes")
else :
    print("no")
