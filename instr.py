nu=int(input())
l=[]
for i in range(nu):
    d=input()
    l.append(list(d))
ch=input()
r=0
no=0
for i in ch:
    if i in l[r]:
        l[r].remove(i)
        r=(r+1)%nu
    else:
        no=1
        break
if no:
    print("NO")
else:
    print("YES")


