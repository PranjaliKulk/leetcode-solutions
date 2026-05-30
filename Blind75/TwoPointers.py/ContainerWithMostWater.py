# Good explanation is in pareto problem
# Essentially take area (min of two heights) * width (distsnce between i and j)

def container_with_most_water(heights):
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        # store min height
        height = min(heights[left], heights[right])
        width = right - left
        area = height * width

        max_area = max(area, max_area)
        
        # chose the larget height 
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area