class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split()
        
        mx=max(len(i) for i in s)
        spaced=[]
        for i in s:
            if len(i) < mx:
                spaced.append(i+' '*mx)
            else:
                spaced.append(i)
        
        ans=[]
        for i in range(mx):
            tmp=''
            for j in spaced:
                tmp+=j[i]
            ans.append(tmp)
        return [i.rstrip() for i in ans]
        
                