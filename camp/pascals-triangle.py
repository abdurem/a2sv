class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        if numRows > 1:
            ans.append([1,1])
        for i in range(1,numRows-1):
            a = [1]
            for j in range(1,len(ans[-1])):
                a.append(ans[i][j-1]+ans[i][j])
            
            a.append(1)
            ans.append(a)

        return ans