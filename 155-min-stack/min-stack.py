class MinStack:

    def __init__(self):
        self.s= []
        self.ms = []

    def push(self, val: int) -> None:
        self.s.append(val)

        if not self.ms or val <= self.ms[-1]:
            self.ms.append(val) 
        

    def pop(self) -> None:
        if self.s:
            val = self.s.pop()
            if val == self.ms[-1]:
                self.ms.pop()
        

    def top(self) -> int:
        if self.s:
            return self.s[-1]

    def getMin(self) -> int:
        if self.ms:
            return self.ms[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()