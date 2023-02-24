class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        preSum=1
        ans=[1]*len(nums)
        
        for i in range(len(nums)):
            ans[i]*=preSum
            preSum*=nums[i]
        
        preSum=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=preSum
            preSum*=nums[i]
        
        return ans