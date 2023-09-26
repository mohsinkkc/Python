file = open("myfile.txt", "r")
new = 0


n = file.read()
n1 = n.split("\n")

for i in n1:
	if i:
		new += 1

print(" the number of lines in a file")
print(new)
