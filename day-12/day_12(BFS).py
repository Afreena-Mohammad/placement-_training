def bfs(d,n):
    vi=[]
    q=[n]
    while(q):
        for i in d[q[0]]:
            if i[0] not in q and i[0] not in vi:
                q.append(i[0])
            vi.append(q.pop(0))
            print(vi[-1])
def fun(d,s,c,e,m,l1): #c=cost, e=end,m=min cost,s=start
    l.append(s)
    if s==e:
        #print(l,c)
        if c<m:
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[s]:
        if i[0] not in l:
            m,l1=fun(d,i[0],c+i[1],e,m,l1)
    l.pop()
    return m,l1
    

            
d={5:[(7,1),(3,11)],
   7:[(5,1),(4,3),(3,12)],4:[(7,3),(8,9),(2,5)],8:[(3,10),(4,9),(2,6)],3:[(5,11),(7,12),(8,10)],2:[(4,5),(8,6)]}

l=[]
c=[]
for i in d.keys():
    print((fun(d,5,0,i,9999,[])))
bfs(d,5)