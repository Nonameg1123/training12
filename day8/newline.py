ip=list(map(int,input().split()))
t=[]
sol=[]
# for i in range(0,len(ip)):
#     if ip[i] not in t:
#         t.append(ip[i])
#     else:
#         sol.append(t)
#         t=[ip[i]]
# sol.append(t)
# print(sol)
while  ip:
    t=[]
    i=0
    while i<len(ip):
        # print(ip[i])
        # print("----------------------------")
        if ip[i] not in t:
            # print(ip[i])
            t.append(ip[i])
            ip.pop(i)
        else:
            i+=1
    sol.append(t)
print(sol)