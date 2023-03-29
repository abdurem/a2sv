class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        d = m = -1

        while i < len(nums):
            if nums[i]-1 < i and m != -1:
                m = i
                
            if nums[i]-1 == i:
                i+=1
            
            elif nums[nums[i]-1] == nums[i]:
                d = nums[i]
                m = i
                i+=1
            else:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        return [d,m+1]