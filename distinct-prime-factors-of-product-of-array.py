class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ans = set()
        
        for mul in nums:
            d = 2
            while d * d <= mul:
                while mul % d == 0:
                    ans.add(d)
                    mul //= d
                d += 1
            if mul > 1:
                ans.add(mul)

        return len(ans)