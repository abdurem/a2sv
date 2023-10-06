class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for v, w, t in times:
            graph[v].append((w, t))
        

        priority = [(0, k)]
        visited = set()
        ans = [float('inf')]*n
        ans[k-1] = 0

        while priority:
            dis, node = heapq.heappop(priority)

            if node in visited:
                continue
            visited.add(node)
            
            for nbr, w in graph[node]:
                new_dis = dis + w
                if ans[nbr-1] > new_dis:
                    ans[nbr-1] = new_dis
                    heapq.heappush(priority,(new_dis, nbr))

        return -1 if any(i == float('inf') for i in ans) else max(ans)