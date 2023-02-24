class MyStack:

    def __init__(self):
        self.list=[]

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        return self.list.pop()

    def top(self) -> int:
        if self.empty():
            return None
        return self.list[-1]

    def empty(self) -> bool:
        return True if len(self.list) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()