class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        d = []
        for i in range(len(costs)):
            d.append(((costs[i][0]-costs[i][1]), i))
        
        d.sort()
        ans = 0
        l = 0
        r = len(costs)-1
        while l < r:
            ans += costs[d[l][1]][0]+ costs[d[r][1]][1]
            l+=1
            r-=1

        return ans