#sqaure matrix made a transpose and revised the list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
for i in range(n):
    for j in range(i,n):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp
for i in range(n):
    temp = matrix[i]
    temp.reverse()
    matrix[i] = temp