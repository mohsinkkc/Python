a=[]
num = int(input("enter the numbers :"))

for i in range (num):
    b=int(input('enter the number:'))
    a.append(b)
print("the largest number is :",max(a))
print("the smallest number is :",min(a))
