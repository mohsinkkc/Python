l2=[45,35,45,23,56,65,65,48,35]

odd,even=0,0

for i in l2:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("the even number is :",even)
print("the odd nnumber is :",odd)
