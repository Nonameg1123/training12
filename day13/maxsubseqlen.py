s1=input()
s2=input()
m=[]
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i-1][j],m[i][j-1])
print(m[len(s1)][len(s2)])
u=len(s1)
v=len(s2)
s=""
while u>0 and v>0:
    if s1[u-1]==s2[v-1]:
        s+=s1[u-1]
        u-=1
        v-=1
    else:
        if m[u-1][v]==m[u][v]:
            u-=1
        else:
            v-=1
print(s[::-1])
