class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0 or rowIndex == 1:
            return [1]*(rowIndex+1)
        
        row=[1]
        mid=self.getRow(rowIndex-1)
        r=1
        while r < len(mid):
            row.append(sum(mid[r-1:r+1]))
            r+=1
        row.append(1)
        
        return row