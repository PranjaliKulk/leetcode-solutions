# DFS with backtracking
# O(m*n*4L) # 4 directions for each word -> same as word search II because we use tries there

def wordSearch(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r,c,i):
        # Base case: found whole word
        # if i matches the length of word, every character was matched and thus i reached max length
        if i == len(word):
            return True
        # base case: out of bounds or wrong char or visited 
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] == "#":
            return False
        if board[r][c] != word[i]:
            return False
        
        # mark as visited
        board[r][c] = "#"

        # explore all 4 directions
        found = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1, i+1) or dfs(r, c-1, i+1))

        # unmark backtrack - restore original value
        board[r][c] = word[i]

        return found
    for r in range(rows):
        for c in range(cols):
            if dfs(r,c,0):
                return True
            
    return False

