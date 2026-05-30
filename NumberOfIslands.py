# use DFS, O(n*m)
# check for every "1" -> mark start of an island
# recursively check for all directions 
# mark each "1" to "0" after visiting every node

class NumOfIslands:
    def numOfIsland(self, grid):

        # edge case
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0]) #intialise row and column to start of grid
        count = 0 # to cont no of island

        def dfs(self, r, c):
            # check for out of bounds
            if r < 0 or c < 0 or grid[r][c] == "0" or r >= rows or c >= cols:
                return # element not valid
            grid[r][c] = "0" # mark element visited after verifying its valid

            # call dfs on all four directions
            dfs(r, c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)


        for r in range(rows):
            for c in range(cols):
                if grid [r][c] == "1": # found beginning of the island
                    count += 1 # island found, increment count
                    dfs(r,c) # call dfs on that element


        return count