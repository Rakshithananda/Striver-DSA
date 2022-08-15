num = [-2,1,-3,4,-1,2,1,-5,4]
add = 0
max_val = max(num)
for i in range(len(num)):
    add += num[i]
    if add < 0 :
        add = 0
    if add > max_val:
        max_val = add
print(max_val)