class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c=Counter(arr)
        n=0
        N=len(arr)
        ans=0
        for k,v in sorted(c.items(),key=lambda a: -a[1]):
            n+=v
            ans+=1
            if n>=N//2: break
        return ans
            
            
            
            