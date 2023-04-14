class Solution:
    def helper(self, currIndex, nums, maxOr, currOr, ans):
        if currIndex == len(nums):
            if currOr == maxOr:
                ans[0] += 1
            return
        
        self.helper(currIndex + 1, nums, maxOr, currOr, ans)
        self.helper(currIndex + 1, nums, maxOr, currOr | nums[currIndex], ans)
        
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        ans = [0]
        
        for a in nums:
            maxOr |= a
        
        self.helper(0, nums, maxOr, 0, ans)
        
        return ans[0]