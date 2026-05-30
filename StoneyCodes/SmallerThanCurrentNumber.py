#[8,1,2,2,3] -> [4,0,1,1,3]
def smallerThanCurrent(nums):
    temp = sorted(nums) #[1,2,2,3,8]
    d = {}

    for i, num in enumerate(temp):
        if num not in d: #Checking for duplicates i.e. 2
            d[num] = i #{1:0, 2:1, 3:3, 8:4}

    res = []

    for i in nums:
        res.append(d[i]) #[4,0,1,1,3]

    return res

