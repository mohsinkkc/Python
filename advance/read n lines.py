f=open("mytext.txt",'r')
n=int(input("how many  lines you want to read?:"))
for i in range(n):
    print(f.readline(),end="")
f.close()
