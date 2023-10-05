def TOH(n,src,aux,dest):
    if n == 1:
        print("I moved from "+src+" to " + dest)
        return
    TOH( n-1, src, dest, aux)
    print("I moved from "+src+" to " +dest)
    TOH(n-1, aux, src,dest)
n = 3
TOH(n, 'src', 'aux', 'dest')