class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        ans = 0
        s = 0
        for i in nums:
            s += i

            if s - k in dic:
                ans += dic[s -  k]
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1
        return ans