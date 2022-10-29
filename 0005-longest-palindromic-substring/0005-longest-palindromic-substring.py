class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=''
        length=0
        
        for i in range(len(s)):
            lft=rgt=i
            
            while lft >= 0 and rgt < len(s) and s[lft]==s[rgt]:
                if rgt-lft+1 > length:
                    ans=s[lft:rgt+1]
                    length=rgt-lft+1
                lft-=1
                rgt+=1
            
            lft,rgt=i,i+1
            while lft >= 0 and rgt < len(s) and s[lft]==s[rgt]:
                if rgt-lft+1 > length:
                    ans=s[lft:rgt+1]
                    length=rgt-lft+1
                lft-=1
                rgt+=1
        return ans