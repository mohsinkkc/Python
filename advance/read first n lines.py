n = int(input("Enter Lines To Read : "))
file1 = open("mytext.txt","r")
for i in range(n):
	print(file1.readline())
