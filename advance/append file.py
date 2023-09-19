file1=open("mytext.txt",'w')

l=["hi myself mohisn \n","how are you \n","welcome \n"]
file1.writelines(l)
file1.close()

file1=open("mytext.txt",'a')
file1.write("thank for checking")
file1.close()

file1=open("mytext.txt",'r')
print("your file is :")
print(file1.read())
print()
file1.close()
