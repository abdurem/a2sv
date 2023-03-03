class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        stk=[]

        for i in s:
            while stk and stk[-1] > i and c[stk[-1]] > 1 and i not in stk:
                c[stk[-1]]-=1
                stk.pop()
            if i not in stk:
                stk.append(i)
            else:
                c[i]-=1
        return ''.join(stk)
        #cdadabcc