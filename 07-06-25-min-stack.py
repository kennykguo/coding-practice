class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        return self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        res = float("infinity")

        for i in range(len(self.stack)):
            if res > self.stack[i]:
                res = self.stack[i]
        
        return res



class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_val = float("infinity")
         
    def push(self, val: int) -> None:
        # if less than current min val, push it onto
        if val < self.min_val:
            self.min_val = val
            self.min_stack.append(self.min_val) # push new lowest value to min stack
        else:
            self.min_stack.append(self.min_stack[-1]) # push most recent value to min stack
        self.stack.append(val) # add to actual stack
        return

    def pop(self) -> None:
        val = self.min_stack.pop() # pop from min stack and get val
        if len(self.min_stack) == 0: # check if stack is empty
            self.min_val = float("infinity")
        else:
            self.min_val = self.min_stack[-1] # if not empty, then replace min_val with newest min_val
        return self.stack.pop() # pop from actual stack

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
