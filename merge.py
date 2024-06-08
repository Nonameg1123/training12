a=list(map(int,input().split(",")))
b=list(map(int,input().split(",")))
i,j=0,0
c=[]
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
if j!=len(b)-1:
    c.extend(b[j:])
if i!=len(a)-1:
    c.extend(a[i:])
print(c)