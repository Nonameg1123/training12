from collections import defaultdict,Counter
p=int(input())
while p:
    ip=input("enter the string to be decoded")
    d=input("enter the cryptographic text")
    n=Counter(ip)
    sol=""
    print(n)
    for i in d:
        if i in ip:
            sol+=i*n[i]
    print(sol)
    print()
    p-=1


