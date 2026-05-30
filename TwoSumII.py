# Two sum II has an input array sorted.
# Two pointers staring from two ends
# if diff is too big -> move right pointer to left; if diff is too small -> move left pointer to right
# Time: O(n) Space: O(1)

def twoSumII(nums, target):
    left = 0 #Initialise first pointer at the begginning
    right = len(nums) - 1 #initialise second pointer at the end

    while left<right: # true in loop
        current_sum = nums[left] + nums[right] # current sum

        if current_sum == target: # if match found -> return two values
            return (left + 1,right + 1)
        elif current_sum < target: # too small -> move left towards right
            left += 1
        else: # too big -> move right towards left
            right -= 1