class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row=len(mat)
        col=len(mat[0])
        
        cur_r = cur_c = 0
        up=True
        ans=[]
        
        while len(ans) != row*col:
            if up:
                while cur_r >= 0 and cur_c < col:
                    ans.append(mat[cur_r][cur_c])
                    cur_r -= 1
                    cur_c += 1
                
                if cur_c == col:
                    cur_c -= 1
                    cur_r += 2
                else:
                    cur_r += 1
                
                up = False
            else:
                while cur_c >= 0 and cur_r < row:
                    ans.append(mat[cur_r][cur_c])
                    cur_r += 1
                    cur_c -= 1
                
                if cur_r == row:
                    cur_r -= 1
                    cur_c += 2
                else:
                    cur_c += 1
                
                up = True
        return ans
                