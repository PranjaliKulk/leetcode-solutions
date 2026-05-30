#Time: O(n) Space: O(1)
def maxPStocks(prices):
    l,r = 0,1 #initialize left and right pointer to first and second position
    maxP = 0 #Max profit is initialised to 0

    while r != len(prices): #while array exists
        if prices[l] < prices[r]: #value of left element should be less than right element
            prof = prices[r] - prices[l] #Calculate difference
            maxP = max(maxP, prof) #store max difference of prev and curr into maxP

        else:
            l = r #increment left pointer
        r +=1    #increment right pointer every time
    return maxP


# prices = [7, 1, 5, 3, 6, 4]
# # Call the function and print result
# result = maxPStocks(prices)
# print("Max Profit:", result)