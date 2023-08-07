a = int(input("enter the number :"))

fact=1

if a<0:
    print("the factorial is not for negative number")
elif a==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,a+1):
        fact=fact*i
        print("the factorial of the number is",fact)
