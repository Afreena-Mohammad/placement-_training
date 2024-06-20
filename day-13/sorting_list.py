l =[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
sorted_l=sorted(l,key=lambda x:x[0])
l.sort(key=lambda x:x[0])
print(sorted_l)
print(l)
