# similar to tree level order traversal
# only append the last node

from collections import deque

class Solution:
    def rightSideView(self, root):
        queue = deque([root]) #queue to store current level of tree
        result = [] # result list to store result nodes

        if root is None:
            return #return none if tree is empty
        
        while queue:
            level_size = len(queue) # length of queue at current stage to miss child nodes

            for i in range(level_size): #traverse till current level
                node = queue.popleft() #pop current node 

                #append only if its the last node(right)
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result