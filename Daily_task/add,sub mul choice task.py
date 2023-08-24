def addition(num1,num2):
    return num1+num2
def subraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
def floordivison(num1,num2):
    return num1//num2
def exponent(num1,num2):
    return num1**num2
def menu():
    print("1.Addition")
    print("2.Subraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Floor Division")
    print("6.Exponent")
    print("7.Exit")

menu()
status = True
while status:   
    x=int(input("Enter Choice:"))
    n=int(input("Enter Number1:"))
    n1=int(input("Enter Number2:"))

    if x == 1:
        print("Addition Is ",addition(n,n1))
    elif x == 2:
        print("Subraction Is",subraction(n,n1))
    elif x == 3:
        print("Multiplication Is",multiplication(n,n1))
    elif x == 4:
        print("Divison Is",division(n,n1))
    elif x == 5:
        print("Floor Division Is",floordivison(n,n1))
    elif x == 6:
        print("Exponent Is",exponent(n,n1))
    elif x == 7:
        print("Thank you")
        break
    a=input("Do You Want To Continue?['Y/N']:")
    if a == 'Y':
        menu()
    else:
        print("Thank You")
