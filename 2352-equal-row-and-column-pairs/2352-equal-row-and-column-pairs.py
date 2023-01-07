class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row=[]
        col=[]
        
        for i in range(len(grid)):
            r=[]
            c=[]
            for j in range(len(grid[0])):
                r.append(grid[i][j])
                c.append(grid[j][i])
            row.append(r)
            col.append(c)
        
        ans=0
        for r in row:
            for c in col:
                if r == c:
                    ans+=1
        
        return ans