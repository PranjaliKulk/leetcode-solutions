from collections import deque
def numberOfIslands(grid):

    if not grid: # Check for empty grid, edge case
        return 0
    
    def bfs(r,c):
        q = deque()
        visit.add((r,c)) #add element to visit set
        q.append((r,c)) #append current element to the dequeue

        while q:
            row,col = q.popleft() #get current element in row and col
            dir = [[1,0], [-1,0],[0,1],[0,-1]] # List of directions i.e. up, down, left, right

            for dr, dc in dir:
                r,c = row+dr, col+dc #Move to current dir from dir list
                if r in range (rows) and c in range(col) and grid[r][c] == '1' and (r,c) not in visit: 
                    #if '1' is present in the current firection add it to visit set
                    q.append((r,c))
                    visit.add((r,c))

    count = 0
    rows = len(grid) #len of rows
    col = len(grid[0]) #len of columns
    visit = set() #empty set initially

    for r in range (rows):
        for c in range (col):
            if [r][c] == '1' and (r,c) not in visit: #check if current element is 1 and is not visited
                bfs(r,c) #goto bfs to find corresponding elements for island
                count +=1 #increment island count by 1
    return count #return final count