class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        ans = 0

        def dp(curSum, idx):
            if curSum == target and idx == len(nums):
                return 1
            if idx == len(nums):
                return 0
            
            # curSum += nums[idx]
            state = (curSum, idx)
            if state not in memo:
                take = dp(curSum + nums[idx], idx+1)
                skip = dp(curSum - nums[idx], idx+1)
                memo[state] = take + skip

            return memo[state]
        
        ans = dp(0, 0)
        
        return ans