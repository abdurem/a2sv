class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.ans=0
        def inbound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def dfs(i, j, visited, dir):
            visited.add((i,j))

            for dx, dy in dir:
                x = i+dx
                y = j+dy

                if inbound(x,y) and grid[x][y] != 0 :
                    if (x,y) not in visited:
                        dfs(x,y, visited, dir)
                
                else:
                    self.ans+=1


        d = [(-1,0),(1,0),(0,-1),(0,1)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j, set(), d)
                    return self.ans