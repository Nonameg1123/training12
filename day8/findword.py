ip=[['e','r','w','o'],['s','o','p','r'],['r','w','o','d'],['d','r','w','o',]]
f="word"
c=0
def fin(i,j,k,t):
    if(k==len(f)):
        c=1

    if(i<0 or j<0 or i>=len(f) or j>=len(f) or ip[i][j]!=f[k]):
        return
    else:
        return
    if i>0:
        fin(i-1,j,x)
    if i<len(f)-1:
        fin(i+1,j,x)
    if j>0:
        fin(i,j-1,x)
    if j<len(f)-1:
        fin(i,j+1,x)
    return
for i in range(len(f)):
    for j in range(len(f)):
        if ip[i][j]==f[0]:
            fin(i,j,1)
            if c==f:
                print("yes")
                break
            c="w"
print("no")
