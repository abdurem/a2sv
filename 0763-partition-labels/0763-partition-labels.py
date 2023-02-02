class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l=0
        ans=[]
        
        while len(s) > 0:
            
            for r in range(1,len(s)):
                if s[r] in s[:l+1]:
                    l=r
            ans.append(len(s[:l+1]))
            s=s[l+1:]
            l=0
            
        return ans