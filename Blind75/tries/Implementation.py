# Tries is a tree like data structure that stores characters per node and words are formed traversing the nodes
# Trie is O(m) where m is word length
# Its used for "autocorrect suggestions" or "does any word start with [ap]"

# Trie node structure
class TrieNode:
    def __init__(self):
        self.children = {} # dict to map next word to each node
        self.is_end = False # marks end of a word

# Trie core operations:
# insert(word) -> add new node to trie
# search(word) -> does this word exists
# startswith(prefix) -> does any word start with this prefix

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode() # Add char to Trie
            curr = curr.children[ch] # update current pointer
            curr.is_end = True # mark end after full word

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False # char not found, return False
            curr = curr.children[ch] # update curr pointer
        return curr.is_end # word found, return end of word
        
    def startsWith(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False # char not found, return False
            curr = curr.children[ch] # update current pointer
        return True # prefix found, return true