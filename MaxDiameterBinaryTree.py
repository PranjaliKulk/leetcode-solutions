class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def diameterOfBinaryTree(self,root):
        self.diameter = 0 # initialise diamter to 0; updated later
        def dfs(node):
            # if tree is emmpty; return none    
            if node is None: return None
            # get left subtree heigh
            if node.left:
                left_height = dfs(node.left)
            # get right subtree height
            if node.right:
                right_height = dfs(node.right)
            # calculate current diameter
            current_diameter = left_height + right_height
            # store max diameter 
            self.diameter = max(self.diameter, current_diameter)

            # return max height
            return 1 + max(left_height, right_height) # for parent nodes above where we make recursion call
        
        #call dfs from root
        dfs(root)

        # return diameter
        return self.diameter