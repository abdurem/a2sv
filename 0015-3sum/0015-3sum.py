class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        
        for i,n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
                
            lft,rgt=i+1,len(nums)-1
            while lft < rgt:
                tsum=n+nums[lft]+nums[rgt]
                if tsum > 0:
                    rgt-=1
                elif tsum < 0:
                    lft+=1
                else:
                    ans.append([n,nums[lft],nums[rgt]])
                    lft+=1
                    while nums[lft]==nums[lft-1] and lft<rgt:
                        lft+=1
        return ans