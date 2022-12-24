class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left=0
        right=0
        ans=0
        
        if len(nums)==1 and nums[0] != val:
            return 1
        
        if val in nums:
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

                print(nums,left,right,ans)
                
        return len(nums)-(right-left)
                