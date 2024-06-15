l=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]

def fun(i,j,c):
    if i<0 or j<0 or i>=5 or j>=5 or l[i][j]!=1:
        return c
    l[i][j]=2
    c+=1
    c=fun(i-1,j,c)
    c=fun(i,j-1,c)
    c=fun(i,j+1,c)
    c=fun(i+1,j,c)
    return c
mc=0
for i in range(5):
    for j in range(5):
        if l[i][j]==1:
            cs=fun(i,j,0)
            print(cs)
            mc=max(cs,mc)
            # mc=max(fun(i,j,0),mc)
print(mc)
                    