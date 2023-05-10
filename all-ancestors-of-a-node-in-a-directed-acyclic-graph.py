class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> Iterable[List[int]]:
        def dfs(node) -> set:
            if not ancestors[node]:
                for v in graph[node]:
                    if v not in ancestors[node]:
                        ancestors[node].update({v} | dfs(v))
            return ancestors[node]

        graph = defaultdict(set)
        for parent, child in edges:
            graph[child].add(parent)

        ancestors = [set() for _ in range(n)]
        for u in range(n):
            if not ancestors[u]:
                dfs(u)

        return map(sorted, ancestors)