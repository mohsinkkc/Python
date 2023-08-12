l2=[45,35,65,100,45,65,85,98,54,63,54,3,2,3]

uniquelist=[]

for i in l2:
    if i not in uniquelist:
        uniquelist.append(i)
print("the unique list is",uniquelist)
