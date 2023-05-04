class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(N+1)]
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        colors = [0] * (N+1)
        
        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    return False
                if colors[neighbor] == 0 and not dfs(neighbor, -color):
                    return False
            return True
        
        for i in range(1, N+1):
            if colors[i] == 0 and not dfs(i, 1):
                return False
        return True