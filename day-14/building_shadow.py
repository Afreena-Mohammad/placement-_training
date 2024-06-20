'''ip:[3,5,9,6,8,10] list consists of height of the building on how many buildings sunlight fall in the morning and
how many buildings sunlight fall in the evening , [3,4,5,10,4,3]'''
l=list(map(int,input().split()))
c=1
c1=1
for i in range(len(l)):
    if l[i]<l[i+1]:
        c=c+1
    else:
        break
            
for i in range(-1,-len(l)-1,-1):
    if l[i]<l[i-1]:
        c1=c1+1
    else:
        break
print(c)
print(c1)
        
            