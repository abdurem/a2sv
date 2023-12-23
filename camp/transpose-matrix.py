class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                ans[i][j] = matrix[j][i]
        
        return ans
        
            