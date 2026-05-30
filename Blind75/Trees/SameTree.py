# reccursive approach call on left and right subtree

def same_tree(self, l, r):

    if l is None and r is None:
        return True # both trees are empty
    if l is None or r is None:
        return False # one tree is empty, other is not
    if l.val != r.val:
        return False # values differ
    
    # recursively call on left and right subtree
    left_same = same_tree(self, l.left, r.left)
    right_same = same_tree(self, l.right, r.right)

    return left_same and right_same