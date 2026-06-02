def permutations(nums):
    result = []
    def backtrack(current):
        if len(current) == len(nums): # used all elements, max length should be the len of nums, we stop at that
            result.append(current[:])
            return
        
        for n in nums:
            if n not in current: # element not processed
                current.append(n) # choose
                backtrack(current) # explore
                current.pop() # undo

    backtrack([])
    return result
# O(n! * n) -> n! permutations, each takes O(n) to copy