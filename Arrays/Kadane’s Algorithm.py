nums = [-2,1,-3,4,-1,2,1,-5,4]
l = len(nums)
if l<2:
    print sum(nums)
else:
    max_value = 10**4
    nums_dict = {}
    for i in range(l):
        for j in range(i+1,l+1):
            if sum(nums[i:j]) < max_value:
                nums_dict[tuple(nums[i:j])] = sum(nums[i:j])
                max_val = sum(nums[i:j])
    max_val = max(nums_dict.values())
    print max_val