# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        mid=(l+r)//2

        while l <= r:
            if isBadVersion(mid):
                r=mid-1
            else:
                l=mid+1
            mid=(l+r)//2
        return mid+1