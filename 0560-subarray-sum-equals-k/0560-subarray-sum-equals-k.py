class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap={0:1}
        curSum=0
        res=0
        
        for i in range(len(nums)):
            curSum+=nums[i]
            if curSum-k in hmap:
                res+=hmap[curSum-k]
            if curSum in hmap:
                hmap[curSum]+=1
            else:
                hmap[curSum]=1
        return res