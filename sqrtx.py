class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l=0
        r=x//2
        mid = (l+r)//2
        while l <= r:
            if mid**2 > x:
                r=mid-1
            elif mid**2  < x:
                l=mid+1
            else:
                return mid
            mid=(l+r)//2
        return mid