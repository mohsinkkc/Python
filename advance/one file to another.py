
with open('myfile.txt','r') as firstfile, open('mytext.txt','a') as secondfile:
    for line in firstfile:
        secondfile.write(line)
