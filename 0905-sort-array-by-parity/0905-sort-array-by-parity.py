class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        left=0
        right=0
        val=0
        
        while right < len(nums):
            if nums[right]%2 != val and nums[left]%2 == val:
                left=right
                right+=1

            elif nums[right]%2 == val and nums[left]%2 != val:
                tmp=nums[right]
                nums[right]=nums[left]
                nums[left]=tmp
                left+=1
                right+=1
            else:
                right+=1
        
        return nums