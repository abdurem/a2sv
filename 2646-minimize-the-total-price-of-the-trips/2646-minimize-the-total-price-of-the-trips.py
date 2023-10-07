class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        count = [0] * n
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, dest, parent):
            if node == dest:
                count[node] += 1
                return True
        
            for neigh in graph[node]:
                if neigh != parent:
                    res = dfs(neigh, dest, node)
                    if res:
                        count[node] += 1
                        return res
    
        for trip in trips:
            dfs(trip[0], trip[1], -1)
        
        memo = {}
        def dp(node, parent, halved):
            state = (node, parent, halved)

            if state in memo:
                return memo[state]
            
            if halved:
                cost = (price[node] * count[node]) // 2
            else:
                cost = price[node] * count[node]
            
            for neigh in graph[node]:
                if neigh != parent:
                    if halved:
                        cost += dp(neigh, node, False)
                    else:
                        cost += min(dp(neigh, node, False), dp(neigh, node, True))
            
            memo[state] = cost
            return memo[state]

        
        return min(dp(0, -1, True), dp(0, -1, False))