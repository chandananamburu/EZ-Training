def cse(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    return cse(x-1) + cse(x-2)
print(cse(8))
