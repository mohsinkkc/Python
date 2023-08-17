#set
l1=[1,2,3,4,5,6]

print("before chnage:",l1)
print(id(l1))

l1[3]=8
print("after changing:",l1)
print(id(l1))

#tuple
l1=(6,7,8,9,4,3,2)
print(l1)
print("before change:",id(l1))

l1=(6,1,8,9,4,3,2)
print(l1)
print("after change:",id(l1))
