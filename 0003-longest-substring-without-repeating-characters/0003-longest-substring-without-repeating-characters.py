class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=0
        ans=0
        window=set()
        while r < len(s):
            if s[r] in window:
                window.remove(s[l])
                l+=1
                continue
            window.add(s[r])
            r+=1
            ans=max(ans,len(window))
        return ans