new_nums = sorted(nums,reverse=True)
if new_nums == nums:
    nums.sort()
else:
    l = len(nums)
    for i in reversed(range(len(nums))):
        if nums[i] > nums[i - 1]:
            indx1 = i - 1
            break
    for i in reversed(range(len(nums))):
        if nums[indx1] < nums[i]:
            indx2 = i 
            break
    temp = nums[indx1]
    nums[indx1] = nums[indx2]
    nums[indx2] = temp
    start = indx1 + 1
    end = len(nums)
    sublist=nums[start:end]
    sublist.reverse()
    nums[start:end]=sublist



    