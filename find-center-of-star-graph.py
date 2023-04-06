class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        e = []
        for i in edges:
            e+=i
        
        e = Counter(e)
        
        mx = max(e.values())
        for i in e:
            if e[i] == mx:
                return i