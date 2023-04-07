class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = defaultdict(list)
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        
        def path(ver, visited):
            if ver == destination:
                return True

            visited.add(ver)
            
            for i in d[ver]:
                if i in visited:
                    continue
                if path(i, visited):
                    return True

            return False
        
        return path(source, set())