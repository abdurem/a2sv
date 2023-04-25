class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = []
        visited = set()
        direction = [(1,0), (0,1), (-1,0), (0,-1)]

        def bound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        def area(i, j, dir):
            visited.add((i, j))
            ans[-1]+=1
            for dx, dy in dir:
                x = i + dx
                y = j + dy

                if bound(x, y) and grid[x][y] == 1 and (x, y) not in visited:
                    area(x, y, dir)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    ans.append(0)
                    area(i, j, direction)
        
        return max(ans) if len(ans) > 0 else 0