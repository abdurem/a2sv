class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []

        for i, c in enumerate(s):
            if stk and stk[-1][1] == k:
                for i in range(k):
                    stk.pop()
                
            if stk and stk[-1][0] == c:
                stk.append((c, stk[-1][1]+1)) 
            else:
                stk.append((c, 1))
        
        if stk and stk[-1][1] == k:
            for i in range(k):
                stk.pop()
                
        ans = ''
        for c, i in stk:
            ans += c
        return ans