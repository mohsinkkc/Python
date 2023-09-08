file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]

file1.writelines(L)
file1.close()

file1 = open("myfile.txt","r+")

print("Output of Readlines function is :")
print(file1.readlines())
print()
file1.close()
