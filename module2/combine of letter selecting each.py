dict= {'1':['a', 'b'], '2':['c', 'd']}
list= list(dict.values())
for i in list[0]:
    for j in list[1]:
        print(i+j)
