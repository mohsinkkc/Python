len1 = int(input("Enter length of list :"))

len2 = []
a = 0
for k in range(len1):
    n = int(input("Enter  number: "))
    k+1
    len2.append(n)


print("Before sorting: ",len2)


for i in range(0,len(len2)):
    for j in range(0,len(len2)):
        if len2[i]<len2[j]:
            a = len2[i]
            len2[i] = len2[j]
            len2[j] = a

print("After sorting: " , len2)
