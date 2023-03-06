class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=max(nums)
        ans=r

        while l <= r:
            mid=(l+r)//2
            pre=0
            for i in nums:
                pre+=ceil(i/mid)
            
            if pre <= threshold:
                ans=mid
                r=mid-1
            elif pre > threshold:
                l=mid+1

        return ans