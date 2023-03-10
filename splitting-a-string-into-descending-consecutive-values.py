class Solution:
    def splitString(self, s: str, prev=-1) -> bool:
        if len(s) == 0:
            return True
        
        size = len(s)
        if prev == -1:
            size-=1

        for i in range(size):
            p = int(s[:i+1])
            if prev == -1 or prev - 1 == p:
                if self.splitString(s[i+1:], p):
                    return True
                    
        return False