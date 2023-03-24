class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        arr = [0]*k
        self.min = float('inf')
        cookies.sort(reverse=True)

        def backtrack(i, arr):
            if i == len(cookies):
                self.min = min(self.min,max(arr))
                return
            
            if max(arr) >= self.min:
                return
            
            for j in range(k):
                arr[j] += cookies[i]
                backtrack(i+1, arr)
                arr[j] -= cookies[i]
        
        backtrack(0, arr)
        return self.min