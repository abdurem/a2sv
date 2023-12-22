class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            i=0
            j=len(nums)-1 
            while i<=j:
                mid=int((i+j)/2)
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    i=mid+1
                else: 
                    j=mid-1
            return j+1