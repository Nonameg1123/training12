from collections import defaultdict
a=input()
c=defaultdict(int)
for i in a:
    c[i]+=1
b=list(c.keys())
d=list(c.values())
for i in range(len(b)):
    print(b[i],"-",d[i])
