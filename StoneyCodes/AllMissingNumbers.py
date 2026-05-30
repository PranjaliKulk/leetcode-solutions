#[4,3,2,7,8,2,3,1] -> [5,6]
# O(n)
def allMissingNumbers(nums):
    set_nums = set(nums)
    result = []
    for i in range (1, len(nums)+1):
        if i not in set_nums:
            result.append(i)

    return result
        
