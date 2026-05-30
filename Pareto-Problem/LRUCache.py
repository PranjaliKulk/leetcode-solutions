# Use HashMap (Dictionary for key value pairs) to acess in O(1) time.
# Doubly LL for easy insertion and removal of nodes
# get(key) -> return key value else -1
# put (key,value) -> insert: if capacity exceeds, remove LRU. update: add to front as MRU
# head and tail are dummy nodes, real nodes are in between

class Node:
    def __init__(self, key: int, value: int):
        self.key = key                  # store key so we can delete from hashmap during eviction
        self.value = value              # store value for get/put
        self.prev = None                # pointer to previous node in doubly linked list
        self.next = None                # pointer to next node in doubly linked list


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity        # maximum allowed items in cache
        self.cache = {}                 # hashmap: key -> Node (O(1) access to node)

        self.head = Node(0, 0)          # dummy head (MRU side)
        self.tail = Node(0, 0)          # dummy tail (LRU side)

        self.head.next = self.tail      # connect head to tail initially
        self.tail.prev = self.head      # connect tail back to head initially

    def remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node # bypass node from left
        next_node.prev = prev_node # bypass node from right

    def add_to_front(self, node: Node) -> None:
        first_real = self.head.next

        # change both directions by making current node the real head (not dummy one)
        node.prev = self.head
        node.next = first_real

        self.head.next = node
        first_real.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # get the node and add to front as MRU
        node = self.cache[key]
        self.remove(node)
        self.add_to_front(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache: # if key exists, remove old node
            old_node = self.cache[key]
            self.remove(old_node)
            del self.cache[key]

        new_node = Node(key, value) # Create new node and add to front
        self.add_to_front(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity: # remove lru if capacity exceeds
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
    

    