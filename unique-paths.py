class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for i in range(n)] for j in range(m)]
        directions = [(1, 0), (0, 1)]

        def steps(x, y):
            if x >= m-1 and y >= n-1:
                return 1
            elif x >= m-1:
                return grid[x][y+1]
            elif y >= n-1:
                return grid[x+1][y]
            
            return grid[x+1][y] + grid[x][y+1]
            
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                grid[i][j] += steps(i, j)
        
        return grid[0][0]