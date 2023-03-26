class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        
        for i in range(len(haystack)-len(needle)):
            if  haystack[i:i+len(needle)] == needle:
                return i
        
        return 0 if len(haystack) == len(needle) else len(haystack)-len(needle)