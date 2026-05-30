# use BFS and queue to keep current node, swap children
from collections import deque

def invertTree(self, root):

    # check if tree is empty
    if root is None: return None

    queue = deque([root]) # initialise queue with root

    # Process nodes level by level
    while queue:
        node = queue.popleft() # remve node from queue

        node.left, node.right = node.right, node.left # swap children

        # add left node to queue if exists
        if node.left:
            queue.append(node.left)

        # add right node to queue if exists
        if node.right:
            queue.append(node.right)
        
    return root



