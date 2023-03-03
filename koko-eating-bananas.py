class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        
        while l <= r:
            time=0
            mid=(l+r)//2
            for i in range(len(piles)):
                time+=ceil(piles[i]/mid)
                
            if time <= h:
                r=mid-1
            else:
                l=mid+1
            
        return l