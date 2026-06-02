# Generate all possible subsets of a list. General backtracking template
# At every point : include current element or skip current element

def subsets(nums):
    result = []
    def backtrack(start, current):
        result.append(current[:]) # all paths are valid
        for i in range(start, len(nums)):
            current.append(nums[i]) # choose
            backtrack(i+1, current) # explore other paths
            current.pop() # undo
    backtrack(0, [])
    return result

# nums = [1,2,3]
# output = [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]