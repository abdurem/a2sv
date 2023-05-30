class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount, idx):
            if amount < 0 or idx >= len(coins):
                return float('inf')
            if amount == 0:
                return 0
            
            state = (amount, idx)
            if state not in memo:
                take = dp(amount-coins[idx], idx)+1
                skip = dp(amount, idx+1)
                memo[state] = min(take, skip)
            return memo[state]
        
        ans = dp(amount, 0)
        return -1 if ans == float('inf') else ans