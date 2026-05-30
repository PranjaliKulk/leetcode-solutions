class Solution:
    def surroundingRegions(self, board):
        if not board:
            return
        
        rows, cols = len(board), len(board[0])

        def dfs(r,c):
            # check for validity
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            
            board[r][c] == "T" # mark as safe

            # call on all directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        # start from boundaries

        # top and bottom
        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)
        # left and right
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)

        # flip surrounding regions
        for r in range(rows):
            for c in range(cols):

                if board[r][c] == "O": # flip surrounded ones to X
                    board[r][c] == "X"
                elif board [r][c] == "T": # convert safe ones to Os
                    board[r][c] == "O"
