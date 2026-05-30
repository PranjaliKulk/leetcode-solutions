# append result level by level
# define queue to store current level nodes, traverse only till length of current queue (len(queue), before appending child nodes)
# append child nodes as we reach every new node to the queue

from collections import deque

class Solution:
    def treeLevelTraversal(self, root):
        if root is None: 
            return  # edge case, if tree is empty
        
        result = [] # list to store result
        queue = deque([root]) # queue to store current level nodes OR queue = deque() queue.append(root)

        while queue:
            level_size = len(queue) #length of current level, before appending children
            level = [] #seperate list to store nodes of current level

            for i in range(level_size): # traverse till the end of current level
                node = queue.popleft() # pop current node
                level.append(node.val) # append current node value to level list

                if node.left:
                    queue.append(node.left) # append left children to queue for next iteration
                
                if node.right:
                    queue.append(node.right) # append right children to queue for next iteraation

            result.append(level) #append current level to result list

        return result

