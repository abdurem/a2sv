class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #approch - 
        #count every number in the 3x3, col and row and add to set anc check length
        
        #row
        for row in board:
            count=0
            vals=set()
            for r in row:
                if r.isdigit():
                    count+=1
                    vals.add(r)
            if len(vals) != count:
                return False
        #col
        for col in range(len(board[0])):
            count=0
            vals=set()
            for row in range(len(board)):
                if board[row][col].isdigit():
                    count+=1
                    vals.add(board[row][col])
            if len(vals) != count:
                return False
        
        #3x3
        for bottom in range(2,len(board),3):
            top = bottom-2
            for right in range(2,len(board[0]),3):
                left = right-2
                count=0
                tmp=[board[i][j] for j in range(left,right+1) for i in range(top,bottom+1) if board[i][j].isdigit()]
                vals=set(tmp)
                if len(vals) != len(tmp):
                    return False
        
        return True