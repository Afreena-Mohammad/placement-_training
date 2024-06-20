#ip: khoor ,3 , hello decode using strings
#testcases 
'''a=input()
shift=int(input())
decoded_text=""
for char in a:
    if char.isalpha():
        shift=shift%26
        mu=ord(char)-shift
        if  mu<ord('a'):
            mu+=26
        decoded_text+=chr(mu)
    else:
        decoded_text+=char
print(decoded_text)'''

#or
'''a='bvec'
b=4
c=b%26
d=''
for i in a:
    if((ord(i)-c)>=97):
        d=d+chr(ord(i)-c)
    else:
        d=d+chr(ord(i)-c+26)
print(d)'''
#ip: "xyzabcdefklmnopqefgh" print the length of logest substring who has the alphabets in sequence
'''a=input()
c=1 #max length
l=1 #current length
for i in range(1,len(a)):
    if ord(a[i])==ord(a[i-1])+1:
        l+=1
    else:
        c=max(c,l)
        l=1
c=max(c,l)
print(c)'''
#ip: 3 ,3X3 matrix  abc pqr abc,string element from each row "yraxpazr" .op:yes
#ip: 4 abcd xyze pqrw stuv  ,"cyptdzsayq", op:no
'''n=int(input())
m=[]
for i in range(n):
    m.append(input())
s=input()
f=0
for i in range(len(s)):
    if(s[i] in m[i%n]):
        continue
    else:
        f=1
        break
if(f==1):
    print("yes")
      
else:
    print("no")
    '''
'''n=int(input())
m=[]
for i in range(n):
    m.append(list(input()))
s=input()
f=0
for i in range(len(s)):
    if(s[i] in m[i%n]):
        print("no")
        f=1
        break
    else:
        m[i].remove(s[i])
if f==0:
    print("yes")'''
#ip: [4,7,1,3,1,3]  first three number of rats 3
# 5 units of food
#op:how many homes are left where rats didnot visit (2)


'''a=[6,5,7,3,2]
a.append([5,8])
a.extend([4,2,1])
print(a)
a.extend('7.8')
a.extend("hi")
print(a)
print(len(a))
'''
'''a={5,1,'5',(5,2),1,(5,2,),'hi',"hi",True,False}
print(a)
print(len(a))'''

#ip:12321 reverse the number using recursion and check whether it is palindrome or not
'''def rev_num(num,rev=0):
    if num==0:
        return rev
    else:
        return rev_num(num//10,rev*10+num%10)
def is_pal(num):
    rev_n=rev_num(num)
    return num==rev_n
num=int(input())
if is_pal(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")'''



'''def fun(x):
    if(x==1):
        return 2
    if(x==2):
        return 3
    if(x==3):
        return 4
    return fun(x-2)+fun(x-1)+fun(x-3)+x
print(fun(8))'''

#ip:5 3 2 7 8 4
#   m t w t f s what could be the max profit made from the give input
'''l1=list(map(int,input().split(",")))
c=0
d=0
for i in range(len(l1)-1):
    for j in range(i+1,len(l1)): 
        d=l1[j]-l1[i]
        c=max(d,c)
print(c)
        '''
#ip: 5  op:* * * * *
#          * 1 2 3 *
#          * 4 5 6 *
#          * 7 8 9 *
#          * * * * *
'''n=int(input())
k=1
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(k,end=' ')
            k=k+1
    print("\n")'''
#ip: 4  1 1 1 1 1 1 1 
#       1 2 2 2 2 2 1
#       1 2 3 3 3 2 1
#       1 2 3 4 3 2 1
#       1 2 3 3 3 2 1
#       1 2 2 2 2 2 1
#       1 1 1 1 1 1 1
n=int(input())
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            



        
        
        
