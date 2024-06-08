ip=list(map(int,input().split()))
i=0
j=i+1
buy=0
while j<len(ip):
    if ip[j]<=ip[i]:
        i=j
    else:
        prof=max(prof,ip[j]-ip[i])
    j+=1
print(prof)