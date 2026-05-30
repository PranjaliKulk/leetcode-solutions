


def lowest_common_ancestorBST(self, root, p,q):
    # if tree is empty, return none
    if root is None:
        return None
    # if current node is p or q, return node
    if root == p or root == q:
        return root
    
    # recursively call on left subtree
    left = self.lowest_common_ancestorBST(root.left, p, q)

    # recursively call on right subtree
    right = self.lowest_common_ancestorBST(root.right, p, q)

    # if left returned something
    if left: return left
    # if right returned something
    if right: return right

    # if both returned something, they have a common root
    if left and right:
        return root
    
    return None

# Use BST property of comapring values and iterating to left or right subtree
# recursive approach
def LCA(self, root, p, q):
    if not root:
        return None
    if p.val < root.val and q.val < root.val:
        return self.LCA(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return self.LCA(root.right, p, q)
    return root # split point, return root

# iterative approach
def LCA(self, root, p, q):
    if not root:
        return None
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr