d={5:[7,3],7:[5,3,4],3:[5,8,7],4:[7,8,3],8:[3,4,2],2:[4,8]}

def fun(x,v,q):
    if  x not in v:
        for i in d[x]:
            if i not in v and i not in q:
                q.append(i)
        v.append(x)
        q.remove(x)
    if q:
        v=fun(q[0],v,q)  
    return v
v=fun(5,[],[5])
print(v)

