# non recursive approach
# use bfs and queue for each level
# increment depth after traversing that level
# keep appending children

from collections import deque

def max_depth(self, root):
    if not root:
        return 0 # depth of an empty tree is 0
    
    depth = 0
    queue = deque([root])
    while queue:
        level_size = len(queue) # keep track of length of that level to iterate only for this level

        for _ in range(level_size):
            node = queue.popleft() # pop current node

            if node.left:
                queue.append(node.left) # append left child

            if node.right:
                queue.append(node.right) # append right child
        depth += 1 # increment depth after completing level traversal

    return depth