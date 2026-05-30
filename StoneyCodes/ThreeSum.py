def threeSum(nums, target):
    # a + b + c = target; b + c = target - a
    for i in range(len(nums)):
        new_target = target - nums[i]
    
    hashMap = {} # Empty hashmap to store values

    for ind, val in enumerate(nums):
        diff = new_target - val # calculate difference of target and current number
        if diff in hashMap: # if difference is in hasmap; we have found our two numbers
            return(nums[i], ind, hashMap(diff)) # return two numbers; current and the difference
        hashMap[val] = ind # else append the current number in hashmap
    return None
