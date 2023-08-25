def circle(radius):
    return 3.14 * radius * radius

def triangle(base, height):
    return base * height / 2

def rectangle(height, width):
    return height * width

status=True

while status:
    n=int(input("enter your choice(1 to 3):"))
    if n==1:
        a=int(input("enter your radius:"))
        print("circle radius is:",circle(a))
    elif n==2:
        n1=int(input("enter the base of triangle:"))
        n2=int(input("enter the height of triangle:"))
        print("the area of tringle is:",triangle(n1,n2))
    elif n==3:
        a=int(input("enter the height of rectangle:"))
        b=int(input("enter the width of rectangle:"))
        print("the area of rectangle is :",rectangle(a,b))
    else:
        break
    z=input("do you want to continue [y/n]:")
    if z=='y':
        continue
    else:
        print("thank you")
        break
        
    
