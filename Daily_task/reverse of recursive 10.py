def rec(x):
    if x<=0:
        return 0
    else:
        return rec(x-1)
    print(rec(10))
