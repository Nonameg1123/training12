ip=int(input())
num=1
for i in range(ip):
    for j in range(ip):
        if i==0 or i==ip-1 or j==0 or j==ip-1:
            print("*",end="  ")
        else:
            print(num, end="  ")
            num+=1
    print()
