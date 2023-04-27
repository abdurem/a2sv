class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        grf = {}
        for i in range(len(graph)):
            grf[i] = graph[i]
        
        ans = []
        
        def dfs(node, arr):
            if node == len(graph)-1:
                ans.append(arr[:])
                return

            for n in grf[node]:
                arr.append(n)
                dfs(n, arr)
                arr.pop()
        
        dfs(0, [0])
        return ans