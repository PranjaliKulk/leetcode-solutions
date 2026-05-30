# each pair of lines forms a container; the amount of water it can hold is the area of that container
# area is min of two heights * width, which is distance between them (j-i)
# Approach: use two points, computer area, update max area
# move pointer with smaller height inward

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate area between left and right
        h = min(height[left], height[right])
        w = right - left
        area = h * w
        max_area = max(max_area, area)

        #Move shorter height inwards
        if height[left] < height[right]:
            left += 1
        else: 
            right -= 1
    return max_area