'''
[1,3,4,5]
17
'''
l=[1,3,4,5]
v=17
a=[0]*(v+1)
a[0]=0
for i in l:
    for j in range(i,v+1):
        if j<i:
            a[j]=j
        elif j>=i:
            k=j-i
            a[j]=min(a[j],a[k]+1)
print(a[v])
        