def isSubTree(self, root, subRoot):
    # if root is empty; return None
    if root is None: return False

    # check if nodes match at this point
    if self.isSameTree(root, subRoot):
        return True
    
    # recursively check for its children
    return isSubTree(root.left, subRoot) or isSubTree(root.right, subRoot)

def isSameTree(self, left, right):
    # if both nodes empty
    if left is None and right is None:
        return True
    
    # if one node is empty
    if left is None or right is None:
        return False
    
    # if values dont match
    if left.val != right.val:
        return False
    
    # recursively call its children
    return isSameTree(left.left, right.left) and isSameTree(left.right, right.right)