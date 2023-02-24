class Solution:
    def removeStars(self, s: str) -> str:
        stk=[]
        
        for i in s:
            if i == '*':
                stk.pop()
                continue
            stk.append(i)
        return ''.join(stk)