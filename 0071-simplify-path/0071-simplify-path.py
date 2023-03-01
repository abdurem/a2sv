class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split('/')
        p=[]
        for i in path:
            if i == '':
                continue
            p.append(i)
        
        ans=[]        
        for i in p:
            if i == '..' and len(ans) > 0:
                ans.pop()
                continue
            elif i == '.' or i == '..':
                continue
            ans.append('/'+i)
        return ''.join(ans) if len(ans) > 0 else '/'
            


