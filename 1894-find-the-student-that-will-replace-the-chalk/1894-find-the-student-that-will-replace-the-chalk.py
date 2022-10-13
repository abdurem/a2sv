class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        p=sum(chalk)        
        k=k%p
        if k == 0:
            return 0
        
        tmp=0
        for i in range(len(chalk)):
            tmp=sum(chalk[:i+1])
            if tmp > k:
                return i