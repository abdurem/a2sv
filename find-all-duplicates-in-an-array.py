class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i=0
        ans=set()
        while i < len(nums):
            if nums[i]-1 == i:
                i+=1
            
            elif nums[i]-1 != i and nums[nums[i]-1] == nums[i]:
                ans.add(nums[i])
                i+=1
            if i >= len(nums):
                break
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        return sorted(list(ans))