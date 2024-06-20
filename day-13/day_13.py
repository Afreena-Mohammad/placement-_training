#ip:there are two list [(1,3),(2,5),(4,6),(6,7),(5,8)(7,9)]
# [5,6,5,4,11,2]
# op:17
def fun(l1,l2):
    if len(l1)!=len(l2):
        return []
    wt=[]
    for i in range(len(l1)):
        s,e=l1[i]
        price=p[i]
        wt.append((s,e,price))
    return wt

l1=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
l2=[5,6,5,4,11,2]
print(fun(l1,l2))
    
