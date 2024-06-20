#ip: take a list which will print all the possible  three three combinations
l=[3,2,5,4,1,6,8]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            print(l[i],l[j],l[k])