def spiralMatrix(matrix):
    res = []

    while matrix:
        #1 for Beg to End of first row
        res += (matrix.pop(0)) 

        #2 for last elements of all rows
        if matrix and matrix[0]:
            for row in matrix:
                res.append(matrix.pop())
        
        #3 for reverse of last row
        if matrix:
            res += (matrix.pop()[::-1])
        
        #4 for remaining items
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(matrix.pop(0))

    return res
