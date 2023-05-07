class Solution:
    def countSubIslands(self, grid1, grid2) -> int:
        ans = 0
        n, m = len(grid1), len(grid1[0])
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid2[i][j] == 1:
                    queue = [(i, j)]
                    visited[i][j] = True
                    flag = True
                    while queue:
                        x, y = queue.pop(0)
                        if grid1[x][y] != 1:
                            flag = False
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid2[nx][ny] == 1:
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                    if flag:
                        ans += 1
        return ans