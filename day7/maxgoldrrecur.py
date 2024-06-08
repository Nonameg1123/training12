def rec(l):
    if len(l)==0:
        return 0
    if len(l)==1:
        return l[0]
    if len(l)==2:
        return max(l[0],l[1])
    ls=l[0]+rec(l[2:])
    rs=l[1]+rec(l[3:])
    return max(ls,rs)
l=[13,9,4,10,5,7]
print(rec(l))
