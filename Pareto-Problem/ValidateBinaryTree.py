# keep track of low and high value to compare each node from, strat with inf
# recursively call left and right subtree 

def validateBinaryTree(root):
    def dfs(node, low, high):
        if node is None:
            return # return if empty
        
        if not (low < node.val < high):
            return False # if node does not lie between low and high values, its not a BST
        
        # recursive call on left and right subtree
        left_bst = dfs(node.left, low, node.val) # direction left, high has to be current node value
        right_bst = dfs(node.right, node.val, high) # direction right, low has to be current node value

        return left_bst and right_bst # return true if both subtrees are true
    return dfs(root, float("-inf"), float("inf")) # initial low and high values are -inf to inf