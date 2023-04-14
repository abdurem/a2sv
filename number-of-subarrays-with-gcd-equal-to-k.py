class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for num in range(len(nums)):
            g = nums[num]

            for i in range(num,len(nums)):    
                g = gcd(g,nums[i])
                if g == k:
                    ans += 1
        return ans