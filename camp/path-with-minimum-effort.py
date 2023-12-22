class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        direction = [(0,-1),(0,1),(1,0),(-1,0)]
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m
        ans = [float('inf')]
        def dfs(i,j,visited,prev,k):
            if i == n-1 and j == m-1:
                return True
            for x,y in direction:
                newi = x + i
                newj = y + j
                if inbound(newi,newj) and (newi,newj) not in visited and abs(heights[newi][newj]- prev) <= k :
                    visited.add((newi,newj))
                    if dfs(newi,newj,visited,heights[newi][newj],k):
                        return True
            return False
        l = 0
        r = 10**6
        while l < r:
            mid = (l + r) // 2
            if dfs(0,0,set(),heights[0][0],mid):
                r = mid
            else:
                l = mid + 1
        
        return r



            
