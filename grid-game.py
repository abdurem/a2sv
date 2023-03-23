class Solution:

    def gridGame(self, grid: List[List[int]]) -> int:
        top = sum(grid[0])
        bot= 0
        ans = float('inf')

        for i, j in zip(grid[0], grid[1]):
            top -= i
            ans = min(ans, max(top, bot))
            bot += j
        return ans