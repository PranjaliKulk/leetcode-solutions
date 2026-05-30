# return intersecting nodes from pacific and antlantic oceans
# water can only flow from greater nodes to smaller or equal nodes
# we start searching from the edges (pacific and atlantic oceana) and move inward
# because we are reversing our search, we also reverse the condition so we move from smaller elements to greater elements
# return elements that intersect (are present in both pacific and atlantic sets)

class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0]) #initialise rows and columns height
        
        # empty sets for pacific and atlantic
        pacific = set()
        atlantic = set()

        def dfs(r,c, visited):
            # add node to visited
            visited.add((r,c))

            # list of all four directions
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc # move to different directions from current row and cols

                if (nr, nc) in visited:
                    continue
                if (nr < 0 or nc < 0 or nr >= rows or nc >= cols):
                    continue

            # reverse condition check
            if heights[nr][nc] >= heights[r][c]:
                dfs(nr, nc, visited)


        # traverse ocean edges
        # top row pacific ocean
        for r in range(rows):
            dfs(r, 0, pacific)
        # left column pacific ocean
        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, cols - 1, atlantic)
        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        
        # return intersection of both oceans
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])

        return result