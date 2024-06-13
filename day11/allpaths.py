d={5:[7,3],7:[5,3,4],3:[5,8,7],4:[7,8,3],8:[3,4,2],2:[4,8]}

def fun(x,l,e):
    l.append(x)
    if x==e:
        print(l)
        l.pop()
        return
    for i in d[x]:
        if i not in l:
            fun(i,l,e)
    l.pop()
j=0
for i in d.keys():           
    fun(i,[],2)