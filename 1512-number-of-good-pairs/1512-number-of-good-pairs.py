class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair=0
        count=1
        for i in nums:
            for j in range(len(nums)-1):
                if(j+count>len(nums)-1):
                    break
                if(i==nums[j+count]):
                    pair+=1
            count+=1
        return pair