def qsorting(l,start,end):
    pi=l[end]
    i=start-1
    for j in range(start,end):
        if l[j]<pi:
            i=i+1
            l[j],l[i]=l[i],l[j]
    l[i+1],l[end]=l[end],l[i+1]
    return i+1
def quick(l,start,end):
    if start<end:
        pi=qsorting(l,start,end)
        quick(l,start,pi-1)
        quick(l,pi+1,end)
l=list(map(int,input().split()))
quick(l,0,len(l)-1)
print(l)