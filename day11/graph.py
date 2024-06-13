d={5:[7,3],7:[5,3,4],3:[5,8,7],4:[7,8,3],8:[3,4,2],2:[4,8]}

def fun(x,l):
    print(x)
    l.append(x)
    for i in d[x]:
        if i not in l:
            fun(i,l)
            
fun(5,[])