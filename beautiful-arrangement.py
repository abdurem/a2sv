class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(arr, pos):
            nonlocal count
            if pos == n:
                count += 1
                return
            for i in range(1, n+1):
                if i not in arr and (i % (pos+1) == 0 or (pos+1) % i == 0):
                    backtrack(arr+[i], pos+1)
        
        count = 0
        backtrack([], 0)
        return count