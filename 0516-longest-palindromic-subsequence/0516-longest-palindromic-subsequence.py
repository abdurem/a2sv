class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubsequence(s, s[::-1])
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1) + 1, len(text2) + 1
        mat = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    mat[i][j] = mat[i-1][j-1] + 1
                else:
                    mat[i][j] = max(mat[i-1][j], mat[i][j-1])
        
        return mat[-1][-1]