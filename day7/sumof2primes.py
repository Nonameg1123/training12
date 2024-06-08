def isprime(a):
    if a==1 or a==2:
        return True
    for i in range(2,a//2+1):

        if a%i==0:
            return False 
        else:
            return True
a=int(input())
for i in range(1,a//2):
    if isprime(i) and isprime(a-1):
        print("yes")
        break
    else:
        print("no")
        break
