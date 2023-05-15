class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Find the first island and mark it with a unique number
        m, n = len(grid), len(grid[0])
        island = self.findFirstIsland(grid, m, n)
        queue = deque(island)
        seen = set(island)
        steps = 0
        
        # BFS to expand the first island until we reach the second island
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if grid[row][col] == 1:
                    return steps - 1
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = row + dr, col + dc
                    if 0 <= r < m and 0 <= c < n and (r, c) not in seen:
                        seen.add((r, c))
                        queue.append((r, c))
                        if grid[r][c] == 1:
                            return steps
            steps += 1
        
        return -1
    
    def findFirstIsland(self, grid, m, n):
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island = []
                    self.dfs(grid, i, j, island)
                    return island
    
    def dfs(self, grid, i, j, island):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1):
            return
        grid[i][j] = -1
        island.append((i, j))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self.dfs(grid, i + dr, j + dc, island)