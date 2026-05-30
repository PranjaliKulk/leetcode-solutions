from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertSortedArrayToBST(self, nums):
    # if empty 
    if not nums:
        return None
    
    # initialise n, mid and root node
    n =len(nums)
    mid = n // 2
    root = TreeNode(nums[mid])

    # define queue to keep track of (p, l, r) tuples
    q = deque()
    q.append((root, 0, mid-1))
    q.append((root, mid+1, n-1))

    while q:
        parent , left, right = q.popleft() # Pop values to nodes initialised above 
        if left<=right: #check if valid
            mid = (left + right) // 2 # Mid of subarray
            child = TreeNode(nums[mid]) # actual node to insert
            if nums[mid] < parent.val:
                parent.left = child # insert to left

            else:
                parent.right = child # insert to right
            
            # Queue of subtree
            q.append((child, left, mid -1))
            q.append((child, mid+1, right))
    return root

