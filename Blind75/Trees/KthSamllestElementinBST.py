def kthSmallestElementBST(self, node, k):
    self.k = k
    self.answer = None
    
    def inorder(node):
    
        if node is None:
            return None
        
        inorder(node.left)
        self.k -= 1

        if self.k == 0:
            self.answer = node.val
            return 
        inorder(node.right)
        
    inorder(node)
    return self.answer


# Iterative Cleaner approach without instance variables
def kthSmallestElement(self, root, k):
    stack = []
    curr = root
    
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right
