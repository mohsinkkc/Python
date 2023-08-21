a = [10,20,30,20,10,50,60,40,80,50,40]

n = set()
uniqitems = []
for x in a:
    if x not in n:
        uniqitems.append(x)
        n.add(x)

print(n)
