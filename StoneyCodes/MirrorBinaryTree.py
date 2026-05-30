
#Define a simple binary tree node
class Node:
    def __init__(self,value):
        self.value = value #Node value
        self.left = None #Left child node
        self.right = None #Right child node

# Function to mirror the binary tree
def mirrorTree(root): 
    # Check for base case; tree is empty -> return none
    if root is None:
        return None
    
    #Recursively call left and right subtree 
    mirrorTree(root.left)
    mirrorTree(root.right)

    # Swap left and right nodes to create mirror image
    root.left, root.right = root.right, root.left

# Print inorder traversal 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# Time complexity : O(n) Visit every node once