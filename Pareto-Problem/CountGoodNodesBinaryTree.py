# keep a max_so_far count because a good node has no node greater than itself
# once a geater node than max_so_far is found -> update max_so_far and count variables


    

def countGoodNodes(node, max_so_far):
    if node is None:
        return 0 # return none if node is null

    count = 0 #initialise count to 0

    if node.val >= max_so_far: #found a good node
        max_so_far = node.val #update max_so_far variable to current vaariable
        count += 1 #update count of good nodes

    #call for left and right subtree
    left = countGoodNodes(node.left, max_so_far)
    right = countGoodNodes(node.right, max_so_far)

    return count + left + right # return total count of left subtree and right subtree



