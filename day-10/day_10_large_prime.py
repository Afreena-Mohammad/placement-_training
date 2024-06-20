#IP: [4,8,14,22,36,68]
'''4to8-------7 largest prime
8to14---------13
14to22-------19
22to36-------31
36to68-------67
sum of all 7+13+19+31+67'''
'''def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

#l=[4,8,14,22,36,68]
l=[14,16,20,22]  
l1=[]
for i in range(len(l)-1):
    s=0
    c=0
    for j in range(l[i],l[i+1]):
        if  prime(j):
            c=j
    s=max(c,s)
    l1.append(c)
print(l1)
print(sum(l1))'''
def is_prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
def lprime(n,m):
    for i in range(m-1,n,-1):
        if is_prime(i):
            return i
            
l=list(map(int,input().split()))
s=0
for  i in range(len(l)-1):
    s=s+lprime(l[i],l[i+1])
print(s)
    