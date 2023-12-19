class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        h = defaultdict(list)
        freq = defaultdict(int)

        for i in range(len(nums)):
            h[nums[i]].append(i)
            freq[nums[i]]+=1 
        
        f = []
        t = 0
        for i in freq:
            if t == freq[i]:
                f.append(i)
            elif t < freq[i]:
                f = [i]
                t = freq[i]
        
        ans = float('inf')
        for i in f:
            ans = min(ans, h[i][-1]-h[i][0]+1)
        
        return ans