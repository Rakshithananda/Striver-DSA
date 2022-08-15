nums = [2,0,2,1,1,0]
count_0,count_1,count_2 = nums.count(0),nums.count(1),nums.count(2)

index = 0
while count_0 > 0:
    nums[index] = 0
    count_0 -= 1
    index += 1
while count_1 > 0:
    nums[index] = 1
    count_1 -= 1
    index += 1
while count_2 > 0:
    nums[index] = 2
    count_2 -= 1
    index += 1 