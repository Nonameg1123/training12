a=input().split()
fs=0
o=0
e=0
for i in a:\
    if '.' in i:
        i=float(i)
        fs+=i
    else:
        i=int(i)
        if i%2==0:
            e+=i
        else:
            o+=i
print(" fs = ",fs,"\n e = ",e,"\n o = ",o)

