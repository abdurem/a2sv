class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        isSafe = {}

        def dfs(node):
            if len(graph[node]) == 0:
                isSafe[node] = True
                return True
                
            if node in isSafe:
                return isSafe[node]
            
            isSafe[node] = False
            isSafe[node] = all(dfs(nbr) for nbr in graph[node])

            return isSafe[node]

        ans = []          
        for g in range(len(graph)):
            if dfs(g):
                ans.append(g)
                
        return ans