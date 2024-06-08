
a=input()
cv=[65,69,73,79,85]
lv=[97,101,105,111,117]
c={'lv':0,'uv':0,'lc':0,'uc':0,'d':0,'s':0}
for i in range(len(a)):
    if 47<ord(a[i])<58:
        c['d']+=1
    elif 64<ord(a[i])<91:
        if ord(a[i]) in cv:
            c['uv']+=1
        else:
            c['uc']+=1
    elif 97<ord(a[i])<123:
        if ord(a[i]) in lv:
            c['lv']+=1
        else:
            c['lc']+=1
    else:
        c['s']+=1
for i in c:
    print(i,"-",c[i])

