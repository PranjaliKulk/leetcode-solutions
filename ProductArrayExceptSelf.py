# use two passes to calculate product to the left of i and then right of i
# Prefix array to calculate product left of i, use resultant array to calculate product right of i (Suffix)

def productExceptSelf(nums):
    n = len(nums)
    answer = [1]*n

    # Prefix product (left of i)
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Suffix product(right of i)
    suffix = 1
    for i in range(n-1, -1, -1): #reverse traersal; traverse from end to -1 (exclusive so ends at index 0); -1 -> move backwards
        answer[i] *= suffix # because we dont want to erase our prefix product so multiply suffix to prefix
        suffix *= nums[i]

    return answer