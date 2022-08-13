matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
column_list =list("1" * len(matrix)) 
row_list = list("1" * len(matrix[0]))
#creating dummy column arrary and row array
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            column_list[i]=0
            row_list[j]=0
            #updating dummy column and array
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if column_list[i] == 0 or row_list[j] == 0:
            matrix[i][j] = 0
            #if any of the column or row for the particular index has 0 updating the matrix
print(column_list,row_list,matrix)