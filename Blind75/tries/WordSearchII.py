# Uses Tries for multiple word search simultaneously
# Build a Trie
# DFS from every cell
# At each step check if path exists
# if is_end -> mark word found
# backtrack -> unmark cell

# O(m*n*4L) # 4 directions for each word

# Trie node structure
class TrieNode:
    def __init__(self):
        self.children = {} # dict to map next word to each node
        self.is_end = False # marks end of a word

def findWords(board, words):
    # build trie
    root = TrieNode()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.is_end = word # store word itself instead of True
            # stores the word so when you find it, it can be directly added to result instead of rebuilding it from the path

    result = set() # to avoid same word, different paths
    rows, cols = len(board), len(board[0])

    def dfs(r,c,node):
        # base case: out of bounds or wrong char or visited 
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if board[r][c] == "#":
            return
        ch = board[r][c]
        if ch not in node.children:
            return
        
        # move to next node
        next_node = node.children[ch]
        
        if next_node.is_end:
            result.add(next_node.is_end) # is_end stores the word string

        # mark as visited
        board[r][c] = "#"

        # explore all 4 directions
        (dfs(r+1,c,next_node) or dfs(r-1,c,next_node) or dfs(r,c+1, next_node) or dfs(r, c-1, next_node))

        # unmark backtrack - restore original value
        board[r][c] = ch

    for r in range(rows):
        for c in range(cols):
            dfs(r,c,root)

    return list(result)
