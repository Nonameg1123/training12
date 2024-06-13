d={5:[(7,3),(3,2)],
   7:[(5,3),(4,6),(3,1)],
   4:[(7,6),(8,5),(2,1)],
   3:[(5,2),(7,1),(8,4)],
   8:[(3,4),(4,5),(2,4)],
   2:[(4,1),(8,4)]}

# def spanning_tree(i,v):
#     print(i,end=" ")
#     v.append(i)
#     for j in d[i]:
#         if j not in v:
#             spanning_tree(j,v)

# def all_paths_tree(x,v):
#     v.append(x)
#     if x==2:
#         print(v)
#         v.pop()
#         return
#     for i in d[x]:
#         if i not in v:
#             all_paths_tree(i,v)
#     v.pop()

def cost_spanning_tree(x,v,c):
    v.append(x)
    if x==2:
        print(v,c)
        v.pop()
        return
    for i,j in d[x]:
        if i not in v:
            cost_spanning_tree(i,v,c+j)
    v.pop() 
def min_cost_spanning_tree(x,v,c,m):
    v.append(x)
    if x==2:
        if c<m:
            m=c
        v.pop()
        # print(m)
        return m
    for i,j in d[x]:
        if i not in v:
           m= min_cost_spanning_tree(i,v,c+j,m)
    v.pop()
    return m
# spanning_tree(5,[])
# all_paths_tree(5,[]) 
cost_spanning_tree(5,[],0)  
print(min_cost_spanning_tree(5,[],0,float('inf')))