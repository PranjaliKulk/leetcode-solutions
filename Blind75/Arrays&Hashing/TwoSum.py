
def two_sum(nums, target):
    # freq = defaultdict(int)

    # for num in freq:
    #     freq[num] += 1

    #     if num - target in freq:
    #         return freq[num]
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i] # return indices
        seen[n] = i # add key-value pair 

nums = [3,4,5,6]
print(two_sum(nums, 7))