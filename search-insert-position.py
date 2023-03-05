class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            l=0
            r=len(nums)-1
            mid=(l+r)//2

            while l <= r:
                if nums[mid] > target:
                    r = mid-1
                elif nums[mid] < target:
                    l = mid+1
                else:
                    return mid
                mid = (l+r)//2
            return r+1