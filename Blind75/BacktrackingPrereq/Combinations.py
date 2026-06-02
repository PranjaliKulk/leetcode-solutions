# subsets with len(curr) == k condition
# fixed size + start index

def combinations(n,k):
    result = []
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        for i in range(1, n+1):
            current.append(i)
            backtrack(i+1, current) # needs start index so we dont reuse
            current.pop()
    backtrack(1,[])
    return result