# Difference from Combinations -> elements can repeat, no fixed size, stop when sum == target

def combinationSum(nums, target):
    result = []

    def backtrack(start, current, total):
        if total == target: # found a valid combination -> append
            result.append(current[:])
            return
        if total > target: # overshot -> stop
            return
        
        for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, current, total + nums[i]) # Not i+1 because we can now reuse
                current.pop()
    backtrack(0,[], 0)
    return result
