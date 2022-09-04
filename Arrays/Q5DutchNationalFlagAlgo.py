nums = [2,0,1]
low = 0
high = len(nums) - 1
mid = 0
while mid <= high :
    if nums[mid] == 0:
        temp = nums[low]
        nums[low] = nums[mid]
        nums[mid] = temp
        low += 1
        mid += 1
    if mid>high:
        break
    if nums[mid] == 1:
        mid += 1
    if mid>high:
        break
    if nums[mid] == 2:
        temp = nums[high]
        nums[high] = nums[mid]
        nums[mid] = temp
        high -= 1
    print(nums)
    