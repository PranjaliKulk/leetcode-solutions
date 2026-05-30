#Time:O(1) Space:O(n)
def minStack():
    def __init__(self):
        self.stack = []

        def push(self, x):
            if not self.stack:
                current_min = x #If stack is empty, current in is the new element
            else:
                current_min = min(x, current_min) #set current min to minimum of two elements
            self.stack.append(x, current_min) #append element with current min
            #update current min at eevry push so we can return min at getMin()
            #stores -> [x][current_min]-> [0][1]

        def pop(self):
            self.stack.pop()

        def top(self):
            return self.stack[-1][0] #element part from last element i.e. -1
        
        def getMin(self):
            return self.stack[-1][1] #min part from last element i.e. -1