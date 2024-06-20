m=[]
s1=input()
s2=input()
u=len(s1)
v=len(s2)
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])

s=" "
if s1[u-1]==s2[v-1]:
    s=s+s1[u-1]
    u=u-1
    v=v-1
else:
    
    