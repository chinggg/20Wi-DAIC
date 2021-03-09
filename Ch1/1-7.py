dic={'zhang':180, 'wang':160, 'Li':175, 'zhao':170, 'ding':165}
for name in dic:
    print(name, dic[name])
query_name=input()
for name in dic:
    if dic[name]>dic[query_name]:
        print(name, dic[name])
