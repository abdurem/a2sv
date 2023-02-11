class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ans=set()
        for i in range(len(s)):
            if s[i] in ans:
                return s[i]
            ans.add(s[i])
            