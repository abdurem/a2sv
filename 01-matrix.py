class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        def updateDistance(matrix, dist, x, y, q):
            m, n = len(matrix), len(matrix[0])
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == float('inf'):
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        m, n = len(mat), len(mat[0])
        dist = [[float('inf')] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            updateDistance(mat, dist, x, y, q)
        return dist