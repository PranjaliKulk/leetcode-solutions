class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def are_identical(tree1, tree2):
    # Base case 1 both nodes are null
    if not tree1 and not tree2:
        return True
    # Base case 2 one out of 2 is null
    if not tree1 or not tree2:
        return False
    
    # Recursive call
    return (
        tree1.val == tree2.val and
        are_identical(tree1.left, tree2.left) and
        are_identical(tree1.right, tree2.right)
    )