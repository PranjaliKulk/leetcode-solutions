# Use a stack that keeps track of indices, not temperatures 
# days waited = current_index - previous_index
#brute force O(n^2) optimal O(n)

def dailyTemperatures(temperatures):
    n = len(temperatures) # total number of days
    answer = [0] * n #result array, default 0 for all days
    stack = [] # stack to store indices of days

    for i in range(n): #iterate through each day
        
        #while stack is not empty AND current temp is warmer than temp at top of stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_day = stack.pop() #pop index of colder day
            answer[prev_day] = i - prev_day #days waited for warmer day temp

        stack.append(i) # pushing current day index onto stack

    return answer # return final answer array