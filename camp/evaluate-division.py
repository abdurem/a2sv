class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        ans = []

        for i, eq in enumerate(equations):
            graph[eq[0]].append((values[i], eq[1]))
            graph[eq[1]].append((1/values[i], eq[0]))
        
        def bfs(src, dest):
            if src not in graph or dest not in graph:
                return -1
            
            visited = set()
            que = deque([(1, src)])

            while que:
                dis, node = que.popleft()
                if node == dest:
                    return dis
                    
                if node in visited:
                    continue
                
                visited.add(node)

                for d, n in graph[node]:
                    que.append((dis * d, n))
            return -1
        
        return [bfs(src, dest) for src, dest in queries]
