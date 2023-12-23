class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
    
        def robHelp(nums: List[int]) -> int:

            for i in range(len(nums)-3, -1,-1):
                nums[i] += max(nums[i+2:])
            
            return max(nums[:2])
        
        return max(robHelp(nums[:-1]), robHelp(nums[1:]))
