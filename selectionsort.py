l=list(map(int,input().split()))
n=len(l)
for i in range(n):
    min = i
    for j in range (i+1,n):
        if l[j]<l[min]:
            min = j
        l[i],l[min]=l[min],l[i]
print(l)
        
