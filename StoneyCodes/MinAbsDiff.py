def minAbsDiff(arr):
    arr.sort()

    min_diff = float('inf') #set min diff to a large value of infinity
    for i in range(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i-1]) #calculate min diff of array

    result = [] #array to return all resultamt pairs
    for i in range (1, len(arr)):
        if arr[i] - arr[i-1] == min_diff:
            result.append((arr[i-1], arr[i]))

    return result

arr = [4,2,1,3]
print(minAbsDiff(arr))