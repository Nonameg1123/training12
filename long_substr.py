s=input()
l=0
i=1
t=1
while i<len(s):
    if ord(s[i])-ord(s[i-1])==1:
        t+=1
    else:
        l=max(l,t)
        t=1
    i+=1
print(max(l,t))