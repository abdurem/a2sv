class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pChar=[0]*26
        sChar=[0]*26
        ans=[]
        
        for i in p:
            pChar[ord(i)-ord('a')]+=1
        
        for i in s[:len(p)]:
            sChar[ord(i)-ord('a')]+=1
        
        l=0
        r=len(p)
        
        while r < len(s):
            if pChar == sChar:
                ans.append(l)
            sChar[ord(s[l])-ord('a')]-=1
            sChar[ord(s[r])-ord('a')]+=1
            l+=1
            r+=1
        if pChar==sChar:
            ans.append(l)
        return ans
            
        
        
            
            