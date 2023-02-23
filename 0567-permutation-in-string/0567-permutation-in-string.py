class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) == len(s1) and s1 == s2:
            return True
        
        l=0
        r=len(s1)
        
        S1=sorted(s1)
        S2=sorted(s2[:len(s1)])
        
        while r < len(s2):
            if S1 == S2:
                return True
            l+=1
            r+=1
            S2=sorted(s2[l:r])
        
        if S1 == S2:
            return True
        return False