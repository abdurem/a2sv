class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        preSum=0
        d = defaultdict(int)
        ans=0
        d[0]+=1
        for i in nums:
            preSum+=i
            ans+=d[preSum%k]
            d[preSum%k]+=1

        return ans