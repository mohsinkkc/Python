def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
 
 

tups = [("mohsin", 7), ("dhruv", 12), ("dhruvil", 14),
        ("krish", 2), ("heet", 15), ("jigar", 10)]
dict = {}
print(Convert(tups, dict))
