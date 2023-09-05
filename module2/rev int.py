def rev():
    x=int(input("enter the number:"))
    rem=0
    rev1=0
    while x!=0:
        rem=x%10
        rev1=rev1*10+rem
        x//=10
    print(rev1)
rev()
        
