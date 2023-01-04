class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        sumx=[]
        sumy=[]
        ans=[]
        
        for i in range(len(grid)):
            tx=0
            for j in range(len(grid[0])):
                x=grid[i][j]
                if x == 0:
                    x=-1
                tx+=x
            sumx.append(tx)
            
        for i in range(len(grid[0])):
            ty=0
            for j in range(len(grid)):
                y=grid[j][i]
                if y == 0:
                    y=-1
                ty+=y
                
            sumy.append(ty)
            
        for i in sumx:
            x=[]
            for j in sumy:
                x.append(i+j)
            ans.append(x)
        
        return ans