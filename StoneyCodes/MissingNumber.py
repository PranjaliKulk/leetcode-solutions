#O(nlogn)
def MissingNumber(nums):
    nums.sort()

    for i, v in enumerate(nums):
        if (i != v):
            return (v - 1)
        
        # edge case for when last number is missing i.e [0, 1] -> 2
        if v == len(nums) - 1: 
            return (v + 1)
        
# O(n):
#return sum(range(nums(len(nums)+1))) - sum(nums)