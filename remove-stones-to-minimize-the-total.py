class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [i * -1 for i in piles]

        heapify(piles)
        
        for i in range(k):
            x = floor(heappop(piles) / 2)
            heappush(piles, x)
        
        return sum(piles)*-1