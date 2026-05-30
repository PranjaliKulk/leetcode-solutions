class Solution:
    def isBalanced(self, root):
        def dfs(node):
            # if tree is empty; return
            if node is None: return None # height = 0

            left = dfs(node.left) # recursive call on left subtree

            # check if its empty
            if left == -1:
                return -1 #left subtree not balanced
            
            right = dfs(node.right) # recursive call on right subtree

            #check if its empty
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1 # tree not balanced
            
            return 1 + max(left, right) # return height to parent node
        
        return dfs(root) != -1