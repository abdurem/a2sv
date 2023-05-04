class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.tree = {kingName: []}
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.tree:
            self.tree[parentName] = []
        self.tree[parentName].append(childName)
        self.tree[childName] = []

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(node):
            result = []
            if node not in self.dead:
                result.append(node)
            for child in self.tree[node]:
                result.extend(dfs(child))
            return result
        
        return dfs(self.king)