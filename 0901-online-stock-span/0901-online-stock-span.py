class StockSpanner:
    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        if len(self.stk) == 0:
            self.stk.append({price: 1})
            return 1
        count = 1
        while len(self.stk) > 0 and price >= list(self.stk[-1].keys())[0]:
            count += list(self.stk.pop().values())[0]
        self.stk.append({price: count})
        return count