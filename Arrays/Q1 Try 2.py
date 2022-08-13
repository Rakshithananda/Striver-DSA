matrix = [[1,1,1],[1,0,1],[1,1,1]]
#only for square matrix
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if 0 in matrix[i]:
            if matrix[i][j] == 0 or matrix[j][i] == 0 :
                matrix[i][j] = 0
                matrix[j][i] = 0 
            else:
                matrix[i][j] = -1  
                matrix[j][i] = -1 
print(matrix)