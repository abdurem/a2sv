class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=0
        val=0
        
        while right < len(nums):
            if nums[right] == val and nums[left] != val:
                left=right
                right+=1

            elif nums[right] != val and nums[left] == val:
                tmp=nums[right]
                nums[right]=nums[left]
                nums[left]=tmp
                left+=1
                right+=1
            else:
                right+=1
                