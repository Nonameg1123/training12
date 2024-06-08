a=input()
def is_prime(a):
    if a==2 or a==3 or a==5 or a==7:
        return True
    return False
p=0
for i in a:
    if is_prime(int(i)):
        p+=1
print(p)
