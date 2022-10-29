class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i,n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            lft=i+1
            rgt=len(nums)-1
            while lft<rgt:
                if n+nums[lft]+nums[rgt]==0:
                    ans.append([n,nums[lft],nums[rgt]])
                    lft+=1
                    while nums[lft]==nums[lft-1] and lft<rgt:
                        lft+=1
                elif  n+nums[lft]+nums[rgt] > 0:
                    rgt-=1
                else:
                    lft+=1
        return ans