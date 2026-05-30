# use hashmap to keep track of cloned nodes
# call recursive call on neighbour
# O(V*E)

class Node:
    def __init__(self, val = 0, neighbour = None):
        self.val = val
        self.neighbour = neighbour if neighbour is not None else []

class Solution:
    def cloneGraph(self, node):
        # edge case
        if node is None:
            return # node empty
        
        cloned = {} # hashmap to keep track of cloned nodes to avoid duplication or cycles

        def dfs(curr):
            # if current node is already cloned, return cloned node
            if curr in cloned:
                return cloned(curr)
            
            # if not cloned before, clone it
            copy = Node(curr.val)

            # add newly cloned node to the hashmap
            cloned(curr) = copy

            # call dfs on neighbours to clone all neighbours
            for neighbour in curr.neighbour:
                copy.neighbour.append(dfs(neighbour))

            return copy
        
        return dfs(node)

