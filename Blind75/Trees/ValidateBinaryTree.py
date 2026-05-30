def validateBinaryTree(root):
    def dfs(node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        
        left_tree = dfs(node.left, low, node.val)
        right_tree = dfs(node.right, node.val, high)

        return left_tree and right_tree
    return dfs(root, float("-inf"), float("inf"))