class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = deque([(0, 0, 1)])
        seen = set()
        while q:
            i, j, dist = q.popleft()
            if (i, j) in seen: 
                continue
            seen.add((i, j))

            if i == j == n-1: 
                return dist

            for x, y in ((i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    q.append((x, y, dist+1))
        return -1