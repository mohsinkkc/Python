d1={'email':'abcgmail.com','pas':123}

mail=input("enter your email id:")
psd=input("enter the password:")

if mail == d1['email'] and psd== d1['pas']:
    print("information is enter is correct")
else:
    print("the information you have enterd wrong")
