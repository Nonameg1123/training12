a=input()
sol=[]
def bc(i,s):
    if i==len(a):
        sol.append("".join(s))
        return
    s.append(a[i])
    bc(i+1,s)
    s.pop()
    bc(i+1,s)

bc(0,[])
print(sol)