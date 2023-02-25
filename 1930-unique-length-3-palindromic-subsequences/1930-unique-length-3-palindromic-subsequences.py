class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans=0
        r=len(s)-1
        d = set()
                
        for l in range(len(s)):
            r=len(s)-1
            if s[l] in d:
                continue
            while l < r:
                if s[l] == s[r]:
                    ans+=len(set(s[l+1:r]))
                    d.add(s[l])
                    break
                r-=1
        return ans