d={5:[7,3],7:[5,3,4],3:[5,8,7],4:[7,8,3],8:[3,4,2],2:[4,8]}
mi=[]

def fun(x,l):
    global mi
    l.append(x)
    if x==2:
        if not mi or  len(l)<len(mi):
            mi=l.copy()
        l.pop()
        return
    for i in d[x]:
        if i not in l:
            fun(i,l)
    l.pop()
            
fun(5,[])
print(mi)