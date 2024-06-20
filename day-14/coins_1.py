'''ip:[2,3,5,6] coin
11 value
op:yes'''

def fun(l,n):
    l1=[-1]*(n+1)
    l1[0]=1
    for i in l:
        for j in range(1,n+1):
            if(j>=i):
                if l1[j-i]!=-1:
                    if (l1[j]!=-1):
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
                
    print(l1[-1])        
            
l=[2,3,5,6]
n=11
a=fun(l,n)
if a==1:
    print("yes")
else:
    print("no")




