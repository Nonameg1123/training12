import math
a=int(input())
# while True:
#     is_p=True
#     if a%2==0:
#         a+=1
#         continue
#     if a%3==0:
#         a+=1
#         continue


#     for i in range(5,int(math.sqrt(a))+1):
#         if a%i==0:
#             is_p=False
#             break
#     if is_p:
#         print(a)
#         break
#     a+=1
while(1):
    c=0
    if a%2==0:
        a+=1
        continue
    if a%3==0:
        a+=1
        continue
    for i in range(5,(a//2)+1):
        if a%i==0:
            c+=1
            break
    if c==0:
        print(a)
        break
    else:
        a+=1