class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        memo = {}
        def dp(i):
            if i < 2:
                return cost[i]
            
            if i not in memo:
                memo[i] = min(dp(i-1), dp(i-2))

            return memo[i]+cost[i]

        return dp(len(cost)-1)