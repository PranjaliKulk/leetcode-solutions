def same_tree(self, l, r):
    if l is None and r is None:
        return True
    if l is None or r is None:
        return False
    if l.val != r.val:
        return False
    
    left_same = same_tree(self, l.left, r.left)
    right_same = same_tree(self, l.right, r.right)

    return left_same and right_same

# subtree of another tree builds on isSameTree 
def subtree_another_tree(self, root, subroot):
    if root is None:
        return False
    
    # check if trees are same at this point
    if same_tree(self, root, subroot):
        return True
    
    left_sub = subtree_another_tree(self, root.left, subroot) 
    right_sub = subtree_another_tree(self, root.right, subroot)

    return left_sub or right_sub # or not and, remember