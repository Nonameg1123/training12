def fibb(x):
    if x==1:
        return 1
    elif x==2:
        return 1
    return fibb(x-2)+fibb(x-1)
x=3
for i in range(1,x+1):
    print(fibb(i),end="")