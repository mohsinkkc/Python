f=open('myfile.txt', 'r')
print(f.readlines())
word=input("Enter word to be searched:")
k = 0

for line in f:
    words = line.split()
    for i in words:
        if(i==word):
            k=k+1
print("the number of the word is:",k)

