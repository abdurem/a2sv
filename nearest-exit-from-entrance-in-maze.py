class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[entrance[0]][entrance[1]] = 0
        q = deque([entrance])
        while q:
            x, y = q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.' and dist[nx][ny] == float('inf'):
                    dist[nx][ny] = dist[x][y] + 1
                    if (nx, ny) != entrance and (nx == 0 or nx == m-1 or ny == 0 or ny == n-1):
                        return dist[nx][ny]
                    q.append((nx, ny))
        return -1