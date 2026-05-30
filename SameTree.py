# recursively check left and right subtree values

class Solution:
    def isSameTree(self, l, r):
        # if both trees are empty; return True
        if l is None and r is None:
            return True
        # if one is empty and other has value
        if l is None or r is None:
            return False # trees differ if either is none
        # if values differ; trees differ
        if l.val != r.val:
            return False
            
        # recursive call on left and right subtree
        left_same = self.isSameTree(self, l.left, r.left)
        right_same = self.isSameTree(self, l.right, r.right)

        return left_same and right_same