class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word):
        def dfs(curr, i):
            # base case - end of word reached
            # check if curr node marks end of valid word
            if i == len(word):
                return curr.is_end
            
            ch = word[i] # current char we are matching
            if ch == ".":
                # wildcard -> try every possible child match
                # if any child leads to a match, return true
                for child in curr.children.values():
                    if dfs(child, i+1): # move to next char with this child
                        return True
                return False
            
            else:
                # normal character -> check if it exists in current node's children
                if ch not in curr.children:
                    return False # char not found
                # char found, move to that child node and next character
                return dfs(curr.children[ch], i+1)
        return dfs(self.root, 0) # start dfs at root at index 0
