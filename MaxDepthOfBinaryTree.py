# non recursive approach
# traverse level vise, add nodes to queue for every level
# pop node -> add its children
# increment deapth as we move to next level

from collections import deque

class Solutions:
    def maxDepth(self, root):
        if root is None: return None # if tree is empty return None

        queue = deque([root]) # initialise queue with root

        while queue:
            level_size = len(queue) # length of each level; to know when to stop traversing for that level

            for _ in range (level_size):
                node = queue.popleft() # pop current node

                if node.left:
                    queue.append(node.left) # add left child if exists
                
                if node.right:
                    queue.append(node.right) # add right child if exists
            depth += 1 #increment depth after finishing current level

        return depth
