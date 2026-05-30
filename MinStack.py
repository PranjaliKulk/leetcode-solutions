# stack functions with O(1) time
# added function -> getMin -> getMin in brute force gives O(n) complexity and we are going for O(1)

# Min element will be calculated/updated at every push so time complexity will stay O(1)

class MinStack:
    def __init__(self):
        self.stack = [] # each element is stored as (value, min_so_far)

    def push(self, val):
        if not self.stack: #if empty stack, straight append
            self.stack.append((val,val))
        else:
            current_min = self.stack[-1][1] # get the current min from top most element(-1) and min value stored at (1)
            self.stack.append((val, min(val, current_min)))

    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1][0] # return 0th postion where value is
    
    def getMin(self):
        return self.stack[-1][1] # return 1st position which is the min so far