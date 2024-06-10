ip=input()
i=0
sol=0
t=[]
j=0
# while j<len(ip):
#     i=j
#     while i<len(ip):
#         if ip[i] not in t:
#             t.append(ip[i])
#         else:
#             sol=max(sol,len(t))
#             break
#         i+=1
#     while j<=i:
#         if ip[j]==ip[i]:
#             j+=1
#             break
#         else:
#             t.remove(ip[j])
#             j+=1
ip=list(ip)
while j<=i and i<len(ip):

    if ip[i] not in t:
        t.append(ip[i])
        print(t)
    else:
        print(t)
        sol=max(sol,len(t))
        j=ip.index(ip[i])
        print(j,i)
        d=t.index(ip[i])
        t=t[d+1:]
        t.append(ip[i])
        print(t)
    i+=1
sol=max(sol,len(t))
print(sol)