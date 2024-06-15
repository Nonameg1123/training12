g={5:[(7,3),(3,2)],
   7:[(5,3),(4,6),(3,1)],
   4:[(7,6),(8,5),(2,1)],
   3:[(5,2),(7,1),(8,4)],
   8:[(3,4),(4,5),(2,4)],
   2:[(4,1),(8,4)]}


def fun(x):
    d = {5: float('inf'), 7: float('inf'), 4: float('inf'), 3: float('inf'), 8: float('inf'), 2: float('inf')}
    d[x] = 0
    v = []
    q = [x]
    while q:
        m = float('inf')
        for i in q:
            if m > d[i]:
                m = d[i]
                x = i
        for i in g[x]:
            if i[0] not in v:
                q.append(i[0])
                if d[i[0]] > i[1] + d[x]:
                    d[i[0]] = i[1] + d[x]
        v.append(x)
        q.remove(x)
    print(v)

fun(5)
