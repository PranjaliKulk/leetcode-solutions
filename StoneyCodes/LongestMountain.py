#Avg: O(n) Worst: O(n^2)
def largestMountain(arr):
    ret = 0 

    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i] > arr[i+1]: #find peak, set to i
            l=r=i #initialise left and right to peak

            while l>=0 and arr[l] > arr[l-1]: # keep decrementing left 
                l -=1
            while r<= len(arr)-1 and arr[r] > arr[r+1]: # keep incrementing right
                r +=1
            return max(ret, r-l+1) #return maximum subarray sum
    return ret
