string=input("enter the string :")

digit=apha=space=0

for i in string:
    if i.isdigit():
        digit=digit+1

    elif i.isalpha():
        apha=apha+1
    elif i == "":
        space=space+1
    else:
        pass
print("the digitis is :",digit)
print("the uppercase is :",apha)
print("the space is :",space)
