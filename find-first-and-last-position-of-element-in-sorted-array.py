class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.search(nums,target,True)
        r = self.search(nums,target,False)

        return [l,r]
    def search(self,nums,target,direction):
        i=-1
        l=0
        r=len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                i=mid
                if direction:
                    r = mid-1
                else:
                    l = mid+1
        return i