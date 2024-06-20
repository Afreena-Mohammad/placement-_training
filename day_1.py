'''l1=[]
l2=[]

l1=list(map(int,input().split(",")))
l2=list(map(int,input().split(",")))
print(sorted(l1+l2))'''
#problem1
'''l1=[]
l2=[]
l1=list(map(int,input().split(",")))
l2=list(map(int,input().split(",")))
n=len(l1)
m=len(l2)
res= []
i,j =0,0
while i<n and j<m:
    if l1[i]<l2[j]:
        res.append(l2[i])
        i+=1
    else:
        res.append(l2[j])
        j+=1
if(j<len(l2)):
    res.extend(l2[j:])
if(i<len(l1)):
    res.extend(l1[i:])
    
print(res)'''

#problem 2
'''s="aaabbaaaadddb"
c=1
t=''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
        i+=1
    else:
        t=t+s[i]+str(c)
        c=1
t=t+s[-1]+str(c)   # s[i+1], s[i] is also possible
print(t)'''

#problem 3
#ip 3 4 7 9 8 3 8 6 4 3 5
#op 3 - 3 and so on

'''a=list(map(int,input().split( )))
c=1
b=[]
for i in a:
    if(i not in b):
        b.append(i)
for i in b:
    print(i,"-",a.count(i))'''
#p_4
#ip: f46feLK9y56u#@&56hIjbn6KJhA
'''op:
    lowercase -2
    uppercase-2
    lower consonant-
    uc-
    decimal-
    specail-'''
'''s="sfrgRHADBDz$#*%54ejhUb#$^M"
lv=0
uv=0
lc=0
uc=0
d=0
s=0
lv1=""
uv1=""
lc1=""
uc1=""
d1=""
s1=""
for i in s:
    if  i.isalpha and i.islower in "aeiou":
        lv+=1
        lv1+=i
    elif i.isalpha and i.islower not in "aeiou":
        lc+=1
    elif i.isalpha and i.isupper in "aeiou":
        uv+=1
    elif i.isalpha and i.isupper not in "aeiou":
        uc+=1
    elif i.isalnum:
        d+=1
        
    else:
        s+=1
        
print(lv1)'''

'''s="sfrgRHADBDz$#*%54ejhUb#$^M"
uv,uc,lv,lc,d,sp=0,0,0,0,0,0
for i in s:
    if(i.isupper()):
        if(i in'AEIOU'):
            uv=uv+1
        else:
            uc=uc+1
            
    elif(i.islower()):
        if (i in 'aeiou'):
            lv=lv+1
        else:
            lc+=1
    elif(i.isdigit()):
        d=d+1
    elif(not i.isalnum()):
        sp=sp+1
print("uv",uv)
print("uc",uc)
print("lv",lv)
print("lc",lc)
print("d",d)
print("sp",sp)'''

#p_5
'''a=input()# ip:placements op: plAcEmEnts
c=""
for i in a:
    if i in "aeiou":
        i=i.upper()
        c=c+1
    
    else:
        c=c+i
print(c)
'''
#p_6
#ip: "5 3.8  7  5.6  4 2 3"   op: 15 6 9.4
'''a=input()
o,e,de=0,0,0

for i in a:
    if i.isdigit():  #if('.' in a), if(int(a)==a) are  also possible  or print(a%1)
        i=int(i)'''

#p_7
#ip: [300  400] count of numbers which are divisible by 7 between the given range

'''c=0
for i in range(300,400):
    if i%7==0:
        c=c+1
print(c)'''
 # (or)
'''a=300
b=400
print((a/7) -(b/7))'''
#p_8
#input from user if it is prim number print the number if it is not the prime number print the next nearest prime number
'''a=int(input())
while(1):
    c=0
    for i in range(2,(a//2)+1):
        if(a%i==0 ):
            c=c+1
            break
        
    if c==0:
        print(a)
        break
    else: 
        a=a+1'''
#p_9
#ip: 7854 find how many prime digits are present in the given number
'''n=int(input())
c=0
while(n):
    if(n%10 in [2,3,5,7]):
        c=c+1
    n=n//10
print(c)'''
#p_10
#ip: build strong password 8 chars with atleast one uppercase,lowercase,number,specail letter
'''a=input()

if len(a)<8:
    print(8-len(a))
    for i in a:
        if ( i.isalnum()) and (len(a)>=8) and (i.isupper()) and ( i.islower()) and (not i.isalnum()):
            print("-1")'''
n="Afreena@1233"
v,l,s,d=0,0,0,0
for i in n:
    if
            
            
            
    
    

    
        




    

        
    
            

    


    

        

        


    
        
        
        

 
    

    
            


