class DetectSquares:
    def __init__(self):
        self.counter = Counter()

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x1, y1 = point
        for (x3, y3), count in self.counter.items():
            if abs(x1 - x3) == 0 or abs(x1 - x3) != abs(y1 - y3):
                continue  # Skip empty square or invalid square point!
            ans += count * self.counter[(x1, y3)] * self.counter[(x3, y1)]
        return ans