class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = 0
        for account in accounts:
            mx = max(mx,sum(account))
        
        return mx