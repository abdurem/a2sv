class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(n):
            heappush(heap, (matrix[i][0], i, 0))
        for i in range(k):
            val, row, col = heappop(heap)
            if col < n - 1:
                heappush(heap, (matrix[row][col+1], row, col+1))
        return val