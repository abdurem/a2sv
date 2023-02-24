class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans=[]
        for i in logs:
            if i == './':
                continue
            elif i == '../':
                if len(ans) > 0:
                    ans.pop()
            else:
                ans.append('x')
        return len(ans)