# use BFS and queue, pop node, swap its children and append next nodes to queue

from collections import deque

def invert_binary_tree(self, root):

    # check if tree is empty
    if not root: return None

    # define a queue with root node in it
    queue = deque([root])

    # iterate till queue is empty
    while queue:
        node = queue.popleft() # remove node from queue

        node.left, node.right = node.right, node.left # swap childrem

        # append next children to queue 
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root

# Recursive approach
def invert_recursive(self, root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_recursive(root.left)
    invert_recursive(root.right)
    return root