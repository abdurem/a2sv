class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        ans=0
        for bottom in range(2,len(grid)):
            top = bottom-2
            for right in range(2,len(grid[0])):
                left = right-2
                
                elements=[grid[i][j] for i in range(top,bottom+1) for j in range(left,right+1)]
                magic = [[grid[i][j] for j in range(left,right+1)] for i in range(top,bottom+1)]
                template=[i for i in range(1,10)]
                if sorted(elements) == template:
                    sumH = set(sum(row) for row in magic)
                    sumV = set([sum(row[i] for row in magic)for i in range(len(magic))])
                    dig1 = magic[0][0]+magic[1][1]+magic[2][2]
                    dig2 = magic[0][2]+magic[1][1]+magic[2][0]
                    
                    tmp = sumH.union(sumV)
                    tmp.add(dig1)
                    tmp.add(dig2)
                    if len(tmp) == 1:
                        ans+=1
                        
        return ans