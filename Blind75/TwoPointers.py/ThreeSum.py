# good explanation is in pareto problem set
def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        # we are skipping left and right duplicates but we also need to skip i duplicates, i.e. the main pointer apart from left and right
        if i > 0 and nums[i] == nums[i-1]: continue 
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # skip duplicates
                # iterate till two adjecanet elements are equal and increment left/right accordingly
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # move past last duplicate
                left += 1
                right -= 1
            elif total < 0:
                left += 1 # too small, move left
            else:
                right -= 1 # too big, move right
    return result
nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
