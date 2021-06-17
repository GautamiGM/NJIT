z=[[0,2,4],[2,0,3],[4,3,0]]
def analyzetable(matrix):
    totalsum=[]
    for x in range(len(matrix)):
        sum=0
        for y in range(len(matrix[x])):
            if matrix[x][y]%2==0:
                sum=sum+matrix[x][y]
        totalsum.append(sum)
    return totalsum
print(analyzetable(z))
