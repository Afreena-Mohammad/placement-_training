'''ip:6
0 1 1 1 0 1
0 1 0 1 0 0
1 0 1 1 0 0
0 0 0 1 1 1
1 1 0 0 0 1
1 1 1 0 1 0
4 6
op:8
1 -> tree 0->empty lands
fired on pos 4,6
if tree fires and becomes empty ,makes all horizontal ,vertical trees to be fried
for pos 4,6, remaining will be 8
op:8'''
'''def sf(matrix,r,c):
    if r<0 or r>=len(matrix) or c<0 or c>=len(matrix[0])or matrix[r][c]:
        return
    matrix[r][c]=0
    sf(matrix,r-1,c)
    sf(matrix,r+1,c)
    sf(matrix,r,c-1)
    sf(matrix,r,c+1)
def cr(matrix):
    count=0
    for r in matrix:
        count+=r.count(1)
    return count
def main():
    matrix=[
        [0,1,1,1,0,1],
        [0,1,0,1,0,0],
        [1,0,1,1,0,0],
        [0,0,0,1,1,1],
        [1,1,0,0,0,1],
        [1,1,1,0,1,0]
        ]
    ir,ic=4,6
    sf(matrix,ir,ic)
    remaining_trees=cr(matrix)
    print(f"{remaining_trees}")
if __name__=="__main__":
    main()'''


def fun(i,j):
    if i<0 or j<0 or i>=5 or j>=5  or a[i][j]!=1:
        return
    if (a[i][j]==1):
        a[i][j]=2
    fun(i-1,j)
    fun(i,j,-1)
    fun(i+1,j)
    fun(i,j+1)
    return
fun(4,6)
a=[
        [0,1,1,1,0,1],
        [0,1,0,1,0,0],
        [1,0,1,1,0,0],
        [0,0,0,1,1,1],
        [1,1,0,0,0,1],
        [1,1,1,0,1,0]
        ]
c=0
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            c+=1
            
print(c)
    
