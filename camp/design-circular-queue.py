class MyCircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.arr = [-1]*k
        

    def enQueue(self, value: int) -> bool:
        if self.arr[self.tail] != -1:
            return False
        self.arr[self.tail] = value
        self.tail = (self.tail + 1) % len(self.arr)
        return True

    def deQueue(self) -> bool:
        if self.arr[self.head] == -1:
            return False
        self.arr[self.head] = -1
        self.head = (self.head + 1) % len(self.arr)
        return True

    def Front(self) -> int:
        return self.arr[self.head]

    def Rear(self) -> int:
        return self.arr[(self.tail - 1) % len(self.arr)]
        

    def isEmpty(self) -> bool:
        return self.tail % len(self.arr) == self.head % len(self.arr) and self.arr[self.head] == -1 

    def isFull(self) -> bool:
        return self.tail % len(self.arr) == self.head % len(self.arr) and self.arr[self.head] != -1 


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()