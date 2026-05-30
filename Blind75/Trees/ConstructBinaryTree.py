class TreeNode:
    def __init__(self, val= 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def constructBinaryTree(self, preorder, inorder):
    if not preorder or not inorder:
        return None
    
    # root is always the first element of preorder
    root = TreeNode(preorder[0])

    # find root in inorder to split left and right subtrees
    mid = inorder.index(preorder[0])

    # recursively build left and right subtrees
    root.left = constructBinaryTree(self, preorder[1:mid], inorder[:mid])
    root.right = constructBinaryTree(self, preorder[mid+1:], inorder[mid+1:])

    return root