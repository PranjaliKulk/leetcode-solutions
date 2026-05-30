# similar to number of island, except change counting
# count area after every dfs call on every direction and update max at the end

class Solution:
    def maxAreaIsland(self, grid):
        # edge case
        if not grid:
            return 
        
        rows, cols = len(grid), len(grid[0]) # initialise rows and cols to start of grid
        max_area = 0 # to keep max area value, initally at 0

        def dfs(r, c):
            # check out of bounds
            if r < 0 or c < 0 or r > rows or c> cols or grid[r][c] == "0":
                return # element invalid
            grid[r][c] == "0" # mark element visited
            area = 1 # count curent element which we just marked as visited

            # call dfs on all four directions
            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": # beginning of an island is found
                    area = dfs(r,c) # call dfs on that element
                    max_area = max(max_area, area) # update max area of island we just visited

        return max_area