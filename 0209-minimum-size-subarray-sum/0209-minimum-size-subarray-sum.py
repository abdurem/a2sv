class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lft,rgt=0,0
        tmp=0
        ans=float("inf")
        
        while rgt < len(nums):
            tmp+=nums[rgt]
            while tmp >= target:
                ans=min(ans,rgt-lft+1)
                tmp-=nums[lft]
                lft+=1
            rgt+=1
        if ans == float("inf"):
            return 0
        return ans