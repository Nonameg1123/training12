m=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]

def fir(i,j,n):
    if m[i][j]==1:
        m[i][j]=0
    else:
        return
    if i>0:
        fir(i-1,j,n)
    if i<n-1:
        fir(i+1,j,n)
    if j>0:
        fir(i,j-1,n)
    if j<n-1:
        fir(i,j+1,n)
    return 

fir(4,5,6)
c=0
for i in range(6):
    for j in range(6):
        if m[i][j]==1:
            c+=1
print(c)
