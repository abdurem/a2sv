class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        vis = set()
        self.turn = True

        def bound(x, y):
            return 0 <= x < len(board) and 0 <= y < len(board[0])

        def dfs(x, y):            
            visited.add((x, y))
            vis.add((x, y))
            for dx, dy in direction:
                i = x + dx
                j = y + dy
                if bound(i, j) and board[i][j] == 'O' and (i, j) not in vis:
                    dfs(i, j)
                elif not bound(i, j):
                    self.turn = False
                
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in visited:
                    dfs(i, j)
                    if self.turn:
                        for x, y in vis:
                            board[x][y] = 'X'
                    self.turn = True
                    vis = set()