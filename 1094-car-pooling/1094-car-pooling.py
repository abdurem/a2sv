class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = defaultdict(int)
        
        for trip in trips:
            d[trip[1]]+=trip[0]
            d[trip[2]]-=trip[0]
        
        preSum=0
        for i in sorted(d):
            preSum+=d[i]
            if preSum > capacity:
                return False
        return True