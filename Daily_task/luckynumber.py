luck= 55

status= True

while status:
    num=int(input("enter your lucky number :"))
    if num==luck:
        print("your a lucky man")
    else:
        print("unlucky !")
    choice=input("would you like to continue ? ['y/n']")
    if choice == 'y':
        status=True
    else:
        status=False
