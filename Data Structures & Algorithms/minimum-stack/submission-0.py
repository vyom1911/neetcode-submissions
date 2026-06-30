class MinStack:

    def __init__(self):
        self.min_stack=[]
        self.min_stack_val = []

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append(val)
            self.min_stack_val.append(val)
        else:
            self.min_stack.append(val)
            if self.min_stack_val[-1] > val:
                self.min_stack_val.append(val)
            else:
                self.min_stack_val.append(self.min_stack_val[-1])

    def pop(self) -> None:
        self.min_stack.pop() 
        self.min_stack_val.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.min_stack_val[-1]
        
