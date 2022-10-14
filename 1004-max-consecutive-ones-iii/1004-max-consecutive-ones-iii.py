class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lft=0
        
        for rgt in range(len(nums)):
            k-= 1-nums[rgt]
            if k < 0:
                k+= 1-nums[lft]
                lft+=1
        return rgt-lft+1
                