class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        d1=0
        d2=0
        
        for i in range(len(mat)):
            d1+=mat[i][i]
            
            if i == len(mat)-1-i and mat[i][i] == mat[len(mat)-1-i][len(mat)-1-i]:
                continue
            d2+=mat[i][len(mat)-1-i]
        return d1+d2
            