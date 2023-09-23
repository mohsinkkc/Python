dict1={'apple':{'qty':'2','price':'120'},'Banana':{'qty':'3','price':'180'}}
print("Welcome to fruit market")
d1={}
dx={}
status=True






def add():
    c=input("enter your fruit name:")
    a=int(input("enter your qty:"))
    b=int(input("enter your price:"))
    print("your fruit name is :",c)
    print("your Qty  is :",a)
    print("your price  is :",b)
    d1={c:{'qty':a,'price':b}}
    dict1.update(d1)
    print(dict1)
print(d1)


while status:
    print("Add Fruit Stock")
    print("view your stock")
    print("update your stock")
    n=int(input("enter your choice 1 to 3:"))
    if n==1:
        print("Add your stock:",add())
    elif n==2:
        print(dict1)
    elif n==3:
        dict1.update(dx)
        print(dict1)
    else:
        break
    print("===============================================================")
    z=input("do you want to continue:y/n:")
    if z=='y':
        continue
    else:
        break
