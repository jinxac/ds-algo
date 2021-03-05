class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.aux_stack = []
        self._top = -1
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.aux_stack:
            self.aux_stack.append(x)
        else:
            if self.aux_stack[-1] < x:
                self.aux_stack.append(self.aux_stack[-1])
            else:
                self.aux_stack.append(x)
        
        self._top += 1
        
        

    def pop(self) -> None:
        if self._top == -1:
            return None
        
        self.stack.pop()
        self.aux_stack.pop()
        self._top -= 1
        

    def top(self) -> int:
        if self._top == -1:
            return None
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.top == -1:
            return None
        
        return self.aux_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
