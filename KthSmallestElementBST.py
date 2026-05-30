# basic idea is to traverse inorder and store it in a list and return kth element 
# a BST will give inorder traversal as a sorted list
# Optimal approach is to keep a counter to decrement k every time we visit a node, our answer will be at when k is 0


def kthSmallestElement(self, node, k):
    def inorder(node):
        self.k = k # initialise k to the value of k we want are looking for
        self.answer = None # variable to store answer
        if node is None:
            return # if tree is empty return nothing
        
        
        inorder(node.left) # visit left subtree 
        
        self.k -= 1 # decrementing counter
        
        if self.k == 0:
            self.answer = node.val # if k reaches 0, current node is the answer

        inorder(node.right) # visit right subtree

    inorder(self.root) # call inorder fucntion on root
    return self.answer