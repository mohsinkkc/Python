even=0
odd=0

for i in range(1,10):
    num=int(input(f "enter the nuber [i] :"))

    if num%2==0 :
        even +=1
    else:
        odd +=1

print("the count of even is :",even)
print("the count of odd is :",odd)
