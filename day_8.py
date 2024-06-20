#ip: take list from user that list might have duplicate values [3,2,4,1,3,6,7,2]
#op:[3,2,4,2]
#[6,7,2]
# Example list
'''l=list(map(int,input().split(",")))
for i in range(0,len(l)):
    m=[l[i:i+3]]
    print(m)'''

#l=[1,2,3,4,1,2,3,1,2]   op: [1,2,3,4],[1,2,3] ,[1,2]  and ip:[2,3,1,3,4,3,2] op: [2,3,1] [3,2] [3] and ip:[4,5,2,1] op:[4,5,2,1]

'''def c_l(l):
    l1=[]
    sub=[4,3,2]
    s=0
    for length in sub:
        e=s+length
        sub=l[s:e]
        l1.append(sub)
        s=e
    return l1
l=list(map(int,input().split(",")))
o=c_l(l)
print(o)'''

'''a=[2,3,1,3,4,3,2]
m=[]
c=0
while(c!=len(a)):
    r=[]
    for i in range(len(a)):
        if (not str(a[i]).isalpha()):
            if a[i] not in r:
                c=c+1
                r.append(a[i])
                a[i]='a'
                
    m.append(r)
print(m)'''

#using dictionary
a=[2,3,1,3,4,3,2]
d={}
m=[]
c=0
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
while(c!=len(a)):
    r=[]
    for i in d:
        if(d[i]!=0):
            d[i]=d[i]-1
            c=c+1
            r.append(i)
    m.append(r)
print(m)
            
