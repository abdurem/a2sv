class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=defaultdict(list)
        l=0
        r=1
        pre=[0]
        
        for i in nums:
            pre.append(pre[-1]+i)
        
        
        while r < len(pre):
            if pre[r]-pre[l] >= target:
                ans[r-l]=[l,r]
                l+=1
                continue
            r+=1
        return min(ans) if len(ans) > 0 else 0
        
        
