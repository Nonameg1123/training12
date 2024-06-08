ip=int(input())
for i in range(ip):
    c=97
    print("_"*(ip-i),end="")
    for j in range(97,97+i):
        print(chr(c),end="")
        c+=1

    for j in range(c,96,-1):
        print(chr(c),end="")
        c-=1
    print("_"*(ip-i),end="")
    print()