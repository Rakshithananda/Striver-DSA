index_list = []
for i in range(len(matrix)):
    if 0 in matrix[i]:
        for index,value in enumerate(matrix[i]):
            if 0 == matrix[i][index]:
                index_list.append(index)
        for j in range(len(matrix[i])):
            matrix[i][j] = 0
for i in range(len(matrix)):
    for k in index_list:
        matrix[i][k] = 0