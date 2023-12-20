class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        s = set()

        for i in c:
            if c[i] in s:
                return False
            s.add(c[i])
        
        return True