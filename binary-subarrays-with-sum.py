class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre=list(accumulate(nums))
        d=defaultdict(int)
        d[0]=1
        ans=0

        for i in pre:
            ans+=d[i-goal]
            d[i]+=1
        return ans