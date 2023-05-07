class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        if len(bombs)==1:
            return 1
        
        arr={i:[] for i in range(len(bombs))}
        
        for i in range(len(bombs)):
            x1,y1,r1=bombs[i]
            for j in range(i+1,len(bombs)):
                x2,y2,r2=bombs[j]
                dist=((x2-x1)**2+(y2-y1)**2)**(1/2)
                if dist<=r1:
                    arr[i].append(j)  
                if dist<=r2:
                    arr[j].append(i)
        
        def dfs(arr,visited,start):
            visited.add(start)
            for i in arr[start]:
                if i not in visited:
                    dfs(arr,visited,i)
        mx=1   
        for v in arr:
            visited=set()
            visited.add(v)
            dfs(arr,visited,v)
            mx=max(mx,len(visited))
        return mx