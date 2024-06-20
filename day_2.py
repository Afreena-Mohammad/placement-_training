#problem1 
'''
n=input()
m=sum(list(map(int,n)))
print(m)'''
'''def add(n):
    s=0
    while(n):
        s=s+(n%10)
        n=n//10
    return s
def pnp(x):
    if(n in [2,3,5,7]):
        return m
    else:
        return m+1
    
n=int(input())
m=n
while():
    if n<10:
        if(n in [2,3,5,7]):
            print(pnp(n))
        else:
            print("np")
    else:
        while(1):
            n=add(n)
        if(n<10):
        break
    print(pnp(n))'''
#recurssion
'''def fun(x):
    if(x==6):
        return 500
    print(x)
    t=fun(x+1)
    print(x)
    return t
    
print(fun(1))
print("hi")'''
'''def fun(x):
    return x+10
print(fun(5))'''
'''def fun(x,s):
    if (x==len(a)):
        return s
    s=s+a[x]
    return fun(x+1,s)
    
a=[6,7,2,5]
print(fun(0,0))'''
# using recurssion print sum of even numbers to list a=[ 3,8,5,4,3] b=[5,0,9,3,2] op: add all even in a list and add all odd numbers in 
'''def add(i,se,so):
    if (i==len(a) and a[i]%2==0 ):
        return se,so
    if(a[i]%2==0):
        se=se+a[i]
    if (b[i]%2!=0):
        so=so+b[i]
        return add(i+1,se,so)
        
  

a=[3,8,5,4,3]
b=[5,0,9,3,2]
print(add(0,0,0))'''
#ip:10 sum of all even numbers using recurssion
'''def sum_of(x):
    if(x==0):
        return 0
    return x+sum_of(x-2)
n=int(input())
if(n%2==0):
    print(sum_of(n))
else:
    print(sum_of(n-1))'''
# take list from user print yes if len is even print no if the len odd
'''a=[1,2,3,4,5]
print(type(id(a[0])))'''
#leetcode problem
'''a=[10,4,8,3]
b=[]
for i in range(len(a)):
    b.append(abs(sum(a[:i])-sum(a[i+1:])))
print(b)'''
  #(or)
'''nums=[10,4,8,3]
s=sum(nums)
x=0
r=[]
for i in nums:
    r.append(abs((x)-(s-i-x)))
    x=x+i
print(r)'''
#or
'''def leftRightDifference(self, nums):
    s=sum(nums)
    x=0
    j=0
    for i in nums:
        nums[j]=abs((x)-(s-i-x))
        x=x+i
        j=j+1

    return nums
nums=[10,4,8,3]'''
#ip:take two strings "MMFFMFFMFMMFFMFMMF" IF No of males=female print 0, count of m>f print, m<f print f
'''a="MMFFMMFMFFFMMFFMFFMMM"
c=0
c1=0
for i in range(len(a)):
    if a[i]=='M':
        c=c+1
    if a[i]=='F':
        c1+=1
if c==c1:
    print("0")
elif c>c1:
    print("M")
else:
    print("F")'''
#or
a="MMFFMMFMFFFMMFFMFFMMM"
c=0
for i in a:
    if(i=='M'):
        c=c+1
    else:
        c=c-1
if c>0:
    print("M")
elif c<0:
    print("F")
else:
    print("0")

    

    


    
    


    