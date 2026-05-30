#[[1,1], [3,4], [-1,0]]
# Time: O(n) Space: O(1)
def minTimeAllPoints(points):
    res = 0 #time in seconds traversed
    x1, y1 = points.pop()

    while points:
        x2,y2 = points.pop()
        res += abs(y2-y1), abs(x2-x1) #Larger difference of x or y coords is the points traversed i.e. seconds needed

        x1,y1 = x2,y2 #Swap for next points 

    return res
