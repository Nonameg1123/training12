# l=list(map(int,input().split(",")))
# for i in range(len(l)-1):
#     for j in range(i+1,len(l)-1):
#         for k in range(j+1,len(l)):
#             print(l[i],l[j],l[k])
def comb(l,k):
    def funn(curr,start):
        if(len(curr)==k):
            print(curr)
            return
        for i in range(start,len(l)):
            funn(curr+[l[i]],i+1)
        return
    funn([],0)
l=[2,4,51,5,6,9]
k=3
comb(l,k)