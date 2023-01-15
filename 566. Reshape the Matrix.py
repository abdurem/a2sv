class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        ans=[]
        tmp=[]
        col=0
        for row in mat:
            for cell in row:
                if col == c:
                    ans.append(tmp)
                    tmp=[]
                    col=0
                tmp.append(cell)
                col+=1
        ans.append(tmp)
        return ans
        
