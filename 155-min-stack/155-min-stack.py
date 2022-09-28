class MinStack:

    def __init__(self):
        self.ans=[]

    def push(self, val: int) -> None:
        self.ans.append(val)

    def pop(self) -> None:
        self.ans=self.ans[:-1]

    def top(self) -> int:
        return self.ans[-1]

    def getMin(self) -> int:
        return min(self.ans)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()