def minSubarraySum(arr, target):
    l = 0 #left pointer
    total = 0
    result = float('inf')

    for r in range(len(arr)): #right pointer
        total += arr[r] #adding total as we traverse through each element

        while total >= target: #when total reahces target
            res = min(result, r-l+1) #min of curr and prev subarray length

            total -= arr[r] # decrease total to find a smaller subarray
            l +=1 # increase left to shorten subarray
    if res == float('inf'):
        return 0 #return 0 if res was not updated
    else:
        return res