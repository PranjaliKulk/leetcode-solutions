# Refer from Blind75 folder

class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # if tree is empty return None
        if root is None: return None

        # if current node is p or q, return node
        if root == p or root == q:
            return root
        
        # recursively call on left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # recursively call on right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # if both returned something; return root
        if left and right:
            return root
        
        # check if left returned a value
        if left: return left

        # check if right returned a value
        if right: return right

        # if neither found anything
        return None