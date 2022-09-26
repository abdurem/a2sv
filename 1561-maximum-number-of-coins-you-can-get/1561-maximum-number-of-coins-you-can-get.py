class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans=0
        coin=0
        for i in range(2,len(piles),2):
            ans+=piles[-i]
            coin+=1
            if(coin == len(piles)/3):
                return ans