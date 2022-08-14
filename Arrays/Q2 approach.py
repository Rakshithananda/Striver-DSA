numRows = int(input())
pascal_triangle = []
pascal_triangle.append([1])
for i in range(2,numRows+1):
    new_list = []
    result = 1
    new_list.append(result)
    for j in range(i-1):
        result = result  * (i - j - 1) 
        result = result // (j +1)
        new_list.append(result)
    pascal_triangle.append(new_list)
print(pascal_triangle)