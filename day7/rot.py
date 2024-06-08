st=input()
n=int(input())
l=[]
for i in range(n):
    l.append(input())
c=""
for i in l:
    if i[0]=='L':
        c+=st[int(i[1])]
    else:
        c+=st[len(st)-int(i[1])]
print(c)
ss=[]
c=list(c)
c.sort()
print(c)
st=list(st)
for i in range(len(st)-2):
    ss.append(sorted(st[i:i+len(c)]))
print(ss)
if c in ss:
    print("Found")
else:
    print("Not Found")


