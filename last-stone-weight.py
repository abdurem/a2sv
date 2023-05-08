class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        
        stones.sort()
        if stones[-1] == stones[-2]:
            stones = stones[:-2]
        else:
            stones = stones[:-2]+[stones[-1]-stones[-2]]
        
        return self.lastStoneWeight(stones)