class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        l=r=0
        sm=0
        ans=0
        mx=0
        while r < len(s):
            sm+=1
            d[s[r]]+=1
            mx=max(d.values())
            
            while sm - mx > k:
                ans = max(ans, sm - 1)
                sm -= 1
                d[s[l]] -= 1
                mx = max(d.values())
                l += 1
            r+=1
        ans=max(ans,sm)
        return ans
                