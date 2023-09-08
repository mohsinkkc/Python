file1=open("new_file.txt",'w')

L=["new delhi\n","kolkata \n","surat\n"]

print("writing the lines:")
file1.writelines(L)

file1.close()

file1=open("new_file.txt",'r')

print("the o/p of read is:")
print(file1.read())
print()
file1.close()
