class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(mid):
            pre=0
            d=0
            for i in weights:
                pre+=i
                if pre > mid:
                    pre=i
                    d+=1
                if i > mid:
                    d=len(weights)
                    break
            if pre >= weights[-1]:
                d+=1
            return d <= days
        l=max(weights)
        r=sum(weights)
        ans = 0

        while l <= r:
            mid = (l+r)//2
            if helper(mid):
                r=mid-1
                ans=mid
            else:
                l=mid+1
        return ans