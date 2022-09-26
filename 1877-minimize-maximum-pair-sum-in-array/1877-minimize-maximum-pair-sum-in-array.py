class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        # i=0
        # j=len(nums)-1
        ans=0
        
        for i in range(int(len(nums)/2)):
            j=i+1
            ans=max(ans,nums[i]+nums[-j])
        return ans