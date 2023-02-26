class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones=Counter(stones)
        ans=0
        for i in jewels:
            if i in stones:
                ans+=stones[i]
        return ans