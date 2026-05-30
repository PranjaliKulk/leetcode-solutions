def twoSum(nums, target):
    hashMap = {} # Empty hashmap to store values

    for ind, val in enumerate(nums):
        diff = target - val # calculate difference of target and current number
        if diff in hashMap: # if difference is in hasmap; we have found our two numbers
            return(ind, hashMap(diff)) # return two numbers; current and the difference
        hashMap[val] = ind # else append the current number in hashmap

        # O(n) Brute force is O(n^2)