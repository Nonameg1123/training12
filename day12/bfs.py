# d={5:[7,3],7:[5,3,4],3:[5,8,7],4:[7,8,2],8:[3,4,2],2:[4,8]}
d={5:[7,3],7:[5,3,4],3:[5,8,7],4:[7,8,3],8:[3,4,2,10],2:[4,8,9],9:[2],10:[8,12],12:[10]}


def fun(x):
    v=[]
    q=[x]
    while q:
        if q[0] not in v:
            for i in d[q[0]]:
                if i not in v and i not in q:
                    q.append(i)
            v.append(q.pop(0))
    print(v)         
    
fun(5)


