class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        paths = [i.split() for i in paths]
        content=defaultdict(list)
        stk=[]
        
        for path in paths:
            for p in range(1,len(path)):
                con=''
                fileLen=0
                for j in range(len(path[p])-2,-1,-1):
                    if path[p][j] == '(':
                        content[con].append(path[0]+'/'+path[p][:j])
                        break
                    con=path[p][j]+con
                    fileLen+=1
        
        ans=[]
        for i in content:
            if len(content[i]) > 1:
                ans.append(content[i])
        
        return ans
            
            
                