class Solution:
    def reverseParentheses(self, s: str) -> str:
        s=list(s)
        op=[]
        for i,n in enumerate(s):
            if n == '(':op.append(i)
            elif n == ')': 
                j = op.pop()
                s[j:i] = s[i:j:-1]
            
        return ''.join(st for st in s if st not in ['(',')'])
            