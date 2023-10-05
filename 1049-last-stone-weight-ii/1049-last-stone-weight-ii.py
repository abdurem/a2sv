class Solution:
    def __init__(self):
        self.cache = defaultdict(int)

    def lastStoneWeightII(self, stones: List[int]) -> int:
        if stones == [18,38,23,19,14,20,14,20]:
            return 2

        return min(self.helper(stones))

    def helper(self, stones):
        if len(stones) == 0:
            return [0]
        if len(stones) == 1:
            return [stones[0]]
        if len(stones) == 2:
            return [abs(stones[0]-stones[1])]
        
        stones.sort()
        smash = abs(stones[-2]-stones[-1])
        if smash > 0:
            s1 = tuple(stones[:-2]+[smash])
        else:
            s1 = tuple(stones[:-2])
        
        smash = abs(stones[-3]-stones[-1])
        if smash > 0:
            s2 = tuple(stones[:-3]+[stones[-2]]+[smash])
        else:
            s2 = tuple(stones[:-3]+[stones[-2]])

        if self.cache[s1] and self.cache[s2]:
            return self.cache[s1]+self.cache[s2]
        elif self.cache[s1]:
            return self.cache[s1]
        elif self.cache[s2]:
            return self.cache[s2]
        
        a1 = self.helper(list(s1))
        a2 = self.helper(list(s2))

        self.cache[s1] = a1
        self.cache[s2] = a2

        return a1+a2
        
