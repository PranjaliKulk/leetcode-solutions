def diameter(root):
    best = [0]

    def heights(node):
        if not node: return 0

        left = max(heights(node.left), 0)
        right = max(heights(node.right), 0)

        best[0] = max(best[0], left + right + node.val)
        return node.val + max(left, right)
    
    heights(root)
    return best[0]