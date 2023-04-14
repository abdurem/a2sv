class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(limit):
            primes = [True] * (limit + 1)
            primes[0] = False
            primes[1] = False
            for i in range(2, int(limit ** 0.5) + 1):
                if primes[i]:
                    for j in range(i * i, limit + 1, i):
                        primes[j] = False
            return [i for i in range(2, limit + 1) if primes[i] and i >= left]
        
        ans = [-1,-1]
        mn = float('inf')
        s = sieve(right)

        for i in range(len(s)-1):
            if mn > s[i+1] - s[i]:
                ans[0] = s[i]
                ans[1] = s[i+1]
                mn = s[i+1] - s[i]
        
        return ans