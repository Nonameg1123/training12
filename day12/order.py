l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
sol=[]
def fun1(e,o,s):
    global sol
    if o!=len(l2):
        if l2[o]%2!=0:
            s=(l1[e]+l2[o]+fun1(e,o+1))
    return s

def fun(e):
    global sol
    if e!=len(l1):
        if l1[e]%2==0:
            sol.append(fun1(e,0,0))
        fun(e+1)

fun(0)
print(sol)
# i=0
# j=0
# while i<len(l1):
#     if l1[i]%2==0:
#         while j<len(l2):
#             if l2[j]%2!=0:
#                 sol.append(l1[i]+l2[j])
#             j+=1
#     i+=1
# print(sol)