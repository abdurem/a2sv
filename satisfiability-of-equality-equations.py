class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        set1, set2, set3 = set(), set(), set()
        a, b = None, None
        for item in equations:
            if item[1] == "=":
                a, b = item.split("==")
                set2.add((a, b))
            else:
                a, b = item.split("!=")
                set3.add((a, b))
            set1 |= {a, b}
        print(set2)
        
        graph = {char: char for char in set1}
        print(graph)
        def find(char):
            if graph[char] == char:
                return char
            return find(graph[char])
        def union(x, y):
            xrep, yrep = find(x), find(y)
            if xrep != yrep:
                graph[yrep] = xrep
        for x, y in set2:
            union(x, y)
        for x, y in set3:
            r1, r2 = find(x), find(y)
            if r1 == r2:
                return False
        return True