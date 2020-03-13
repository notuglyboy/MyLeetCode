class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.helper = []
        self.stack =[]

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.helper or self.helper[-1] >= x:
            self.helper.append(x)


    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.helper[-1]:
            self.helper.pop()
        return top

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.helper:
            return None 
        return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
print(minStack.getMin())
print(minStack.pop())

print(minStack.getMin())