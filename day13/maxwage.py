l1 = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
l2 = [5, 6, 5, 4, 11, 2]
l = l2.copy()
j=1
i=0
while j!=len(l1):
    i=0
    while i<j:
        if l1[j][0]>=l1[i][1]:
            if l2[j]+l[i]>l[j]:
                l[j]=l[i]+l2[j]
        i+=1
    j+=1
print(l)
print(max(l))

