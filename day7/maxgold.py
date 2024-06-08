l=list(map(int,input().split(',')))
d={}
for i,j in enumerate(l):
    d[j]=i
s=sorted(d,reverse=True)
print(s)
sl=0
t=[]
i=0
while i<len(s):
    ad=True
    if not t:
        t.append(s[i])
        sl+=s[i]
        
    else:
        for j in t:
            if abs(d[s[i]]-d[j])==1:
                ad=False
                break
        if ad:
            t.append(s[i])
            sl+=s[i]
    i+=1
print(sl)