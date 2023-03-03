class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.map={value:0}
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.val:
            self.map[self.val]+=1
        else:
            self.map[self.val]=0
        return True if self.map[self.val] >= self.k else False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)