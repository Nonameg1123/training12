def rever(a,x):
    if a==0:
        return x
    x=x*10+(a%10)
    return rever(a//10,x)

a=int(input())
x=0
if a==rever(a,x):
    print("palindrome")
else:
    print("not a palindrome")