class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click
        
        def countAdjacentMines(board, row, col):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            count = 0
            
            for d in directions:
                r = row + d[0]
                c = col + d[1]
                if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and board[r][c] == "M":
                    count += 1
            
            return count
            
        def dfs(board, row, col):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != "E":
                return
            
            mines = countAdjacentMines(board, row, col)
            
            if mines > 0:
                board[row][col] = str(mines)
                return
            
            board[row][col] = "B"
            
            for d in directions:
                dfs(board, row + d[0], col + d[1])
    
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        
        dfs(board, row, col)
        
        return board