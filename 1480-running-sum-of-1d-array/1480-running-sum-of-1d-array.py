class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre=0
        
        for i in range(len(nums)):
            nums[i]+=pre
            pre=nums[i]
        return nums