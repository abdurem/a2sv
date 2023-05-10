class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        inDeg = defaultdict(int)

        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                inDeg[recipes[i]]+=1
        
        que = deque(supplies)
        ans = []

        while que:
            rec = que.popleft()
            for i in graph[rec]:
                inDeg[i] -= 1
                if inDeg[i] == 0:
                    que.append(i)
                    ans.append(i)
        return ans