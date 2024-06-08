a=input()
sp=0
s=0
l=0
dif=0
nu=0
ln=len(a)
for i in a :
    if i.isnumeric():
        nu=1
    elif i.isalpha():
        if i.islower():
            s=1
        elif i.isupper():
            l=1
    elif not i.isalnum():
        sp=1
sol=0
if sp==0:
    sol+=1
if s==0:
    sol+=1
if l==0:
    sol+=1
if nu==0:
    sol+=1
if ln==8 and sol==0:
    print(-1)
    exit()
if ln<=8:
    dif=8-ln
if ln>8:
    dif=ln-8

if ln<8:
    
    if dif>=sol:
        print (dif)
    else:
        print(sol)
if ln==8:
    print(sol)
if ln>8:
    
    if dif>=sol:
        print (dif)
    else:
        print(sol)

 